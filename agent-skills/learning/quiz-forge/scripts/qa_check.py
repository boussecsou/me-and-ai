#!/usr/bin/env python3
"""
qa_check.py - Mechanical audit of a quiz generated as JSON (see assets/example-quiz.json)

This script does not replace human review or the checklist in
references/qa-checklist.md: it only catches defects that are detectable
mechanically (forbidden option phrasing, length imbalance, missing fields,
duplicates). Everything else (distractor plausibility, real grounding in
the source, correct Bloom level) remains a judgment call made while
writing the item.

The quiz's actual content can be in any language (see the Language
section of SKILL.md); this script's own messages are in English since
it's an internal tooling script, not user-facing content.

Usage:
    python qa_check.py path/to/quiz.json
"""

import json
import math
import re
from statistics import median
import sys

# Non-exhaustive: "all/none of the above" equivalents in a few common
# languages. Extend this list if you regularly generate quizzes in other
# languages; this check can't catch a phrase it doesn't know.
FORBIDDEN_PATTERNS = [
    "all of the above",
    "none of the above",
    "both of the above",
    "toutes les réponses ci-dessus",
    "aucune des réponses ci-dessus",
    "aucune de ces réponses",
    "les deux ci-dessus",
    "todas las anteriores",
    "ninguna de las anteriores",
]

MIN_OPTIONS = 3
MAX_OPTIONS = 4
WORD_SPREAD_FRACTION = 0.20
MIN_WORD_SPREAD = 2


def word_count(text):
    """Count whitespace-separated tokens containing a letter or number.

    Apostrophes, hyphens and technical tokens stay intact; punctuation-only
    tokens do not count. Languages without word spaces need manual review.
    """
    return sum(any(char.isalnum() for char in token) for token in text.split())


def sentence_count(text):
    """Approximate sentence units, treating an unpunctuated fragment as one.

    Ignore common French/English abbreviations and decimal points. This is
    a heuristic, not a multilingual sentence parser; review code/math manually.
    """
    text = re.sub(
        r"\b(?:e\.g\.|i\.e\.|etc\.|M\.|Mme\.|Dr\.|Mr\.|Mrs\.|Ms\.|vs\.)",
        lambda match: match.group().replace(".", ""), text, flags=re.IGNORECASE,
    )
    parts = re.split(r'[.!?]+["”»\')\]]*(?:\s+|$)', text.strip())
    return sum(word_count(part) > 0 for part in parts)


def check_item(item, index):
    issues = []
    item_id = item.get("id", f"item#{index}")

    stem = item.get("stem", "")
    if not stem.strip():
        issues.append(f"[{item_id}] empty stem")

    options = item.get("options", [])
    if not (MIN_OPTIONS <= len(options) <= MAX_OPTIONS):
        issues.append(
            f"[{item_id}] {len(options)} option(s), expected between "
            f"{MIN_OPTIONS} and {MAX_OPTIONS}"
        )

    option_texts = [opt.get("text", "") for opt in options]
    option_ids = [opt.get("id", "") for opt in options]

    # Duplicate/near-identical option text
    seen = {}
    for opt in options:
        normalized = opt.get("text", "").strip().lower()
        if normalized in seen:
            issues.append(
                f"[{item_id}] options '{seen[normalized]}' and "
                f"'{opt.get('id')}' have identical or near-identical text"
            )
        seen[normalized] = opt.get("id")

    # Forbidden phrasing
    for text in option_texts:
        lowered = text.lower()
        for pattern in FORBIDDEN_PATTERNS:
            if pattern in lowered:
                issues.append(
                    f"[{item_id}] forbidden phrasing detected: \"{pattern}\""
                )

    # Compare words, never characters; apply the same rule to every option.
    lengths = [word_count(text) for text in option_texts]
    for opt, count in zip(options, lengths):
        if count == 0:
            issues.append(f"[{item_id}] option '{opt.get('id')}' has no words")
    if lengths and min(lengths) > 0:
        allowed = max(MIN_WORD_SPREAD, math.ceil(WORD_SPREAD_FRACTION * median(lengths)))
        if max(lengths) - min(lengths) > allowed:
            issues.append(
                f"[{item_id}] word-count imbalance: "
                f"{dict(zip(option_ids, lengths))}; maximum spread {allowed} words. "
                f"Rewrite options without padding or removing essential qualifications"
            )
    sentences = [sentence_count(text) for text in option_texts]
    if sentences and len(set(sentences)) > 1:
        issues.append(
            f"[{item_id}] sentence-count imbalance: {dict(zip(option_ids, sentences))}; "
            f"use the same sentence structure and review segmentation manually"
        )

    # Valid correct-answer key
    correct_id = item.get("correct_option_id")
    if correct_id not in option_ids:
        issues.append(
            f"[{item_id}] correct_option_id '{correct_id}' doesn't match "
            f"any listed option"
        )

    # Explanation present for every option
    explanations = item.get("explanations", {})
    for opt_id in option_ids:
        if not explanations.get(opt_id, "").strip():
            issues.append(f"[{item_id}] option '{opt_id}' has no explanation")

    # Source grounding
    if not item.get("source_ref", "").strip():
        issues.append(f"[{item_id}] missing or empty 'source_ref' field (no documented grounding)")

    # Bloom level present
    if not item.get("bloom_level", "").strip():
        issues.append(f"[{item_id}] missing 'bloom_level' field")

    return issues


def check_quiz(data):
    all_issues = []
    items = data.get("items", [])
    if not items:
        return ["Quiz has no items ('items' is empty or missing)"]

    for i, item in enumerate(items):
        all_issues.extend(check_item(item, i))

    # Detect a recurrent cue even when individual word counts are close.
    eligible = 0
    longest_keys = 0
    for item in items:
        options = item.get("options", [])
        lengths = [word_count(opt.get("text", "")) for opt in options]
        keys = [i for i, opt in enumerate(options)
                if opt.get("id") == item.get("correct_option_id")]
        if not MIN_OPTIONS <= len(lengths) <= MAX_OPTIONS or not all(lengths) or len(keys) != 1:
            continue
        eligible += 1
        if lengths[keys[0]] == max(lengths) and lengths.count(max(lengths)) == 1:
            longest_keys += 1
    if eligible >= 5 and longest_keys / eligible > 0.6:
        all_issues.append(
            f"The correct answer is uniquely longest by word count in "
            f"{longest_keys}/{eligible} questions (over 60%); revise wording "
            f"to remove the recurring length cue, not just shuffle options"
        )

    # Distribution of correct-answer positions (detects an overly regular pattern)
    positions = [item.get("correct_option_id") for item in items]
    if len(positions) >= 4:
        from collections import Counter

        counts = Counter(positions)
        most_common_id, most_common_count = counts.most_common(1)[0]
        if most_common_count / len(positions) > 0.6:
            all_issues.append(
                f"The correct answer is in position '{most_common_id}' in "
                f"over 60% of questions ({most_common_count}/{len(positions)}); "
                f"vary the position more to avoid a guessable pattern"
            )

    return all_issues


def main():
    if len(sys.argv) != 2:
        print("Usage: python qa_check.py path/to/quiz.json")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    issues = check_quiz(data)

    if not issues:
        print("OK: no mechanical defect detected.")
        sys.exit(0)

    print(f"{len(issues)} issue(s) detected:\n")
    for issue in issues:
        print(f"  - {issue}")
    sys.exit(1)


if __name__ == "__main__":
    main()
