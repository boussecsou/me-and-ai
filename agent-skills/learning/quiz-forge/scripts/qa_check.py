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
LENGTH_RATIO_WARNING = 2.0  # longest option / shortest option


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

    # Length imbalance between options (a classic guessing cue)
    lengths = [len(t) for t in option_texts if t.strip()]
    if lengths and min(lengths) > 0:
        ratio = max(lengths) / min(lengths)
        if ratio > LENGTH_RATIO_WARNING:
            issues.append(
                f"[{item_id}] strong length imbalance between options "
                f"(ratio {ratio:.1f}), check that the correct answer isn't "
                f"mechanically standing out"
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
