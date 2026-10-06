#!/usr/bin/env python3
"""Validate packaged skill sources and exercise Quiz Forge's existing checker."""

import copy
import json
from pathlib import Path, PurePosixPath
import runpy
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def validate_archive(archive):
    source = archive.with_suffix("")
    expected = set()
    with zipfile.ZipFile(archive) as bundle:
        corrupt = bundle.testzip()
        if corrupt:
            raise ValueError(f"{archive}: corrupt member {corrupt}")
        for member in bundle.infolist():
            path = PurePosixPath(member.filename)
            if path.is_absolute() or ".." in path.parts or not path.parts:
                raise ValueError(f"{archive}: unsafe member {member.filename}")
            if path.parts[0] != source.name:
                raise ValueError(f"{archive}: unexpected archive root {member.filename}")
            if member.is_dir():
                continue
            if member.filename in expected:
                raise ValueError(f"{archive}: duplicate member {member.filename}")
            expected.add(member.filename)
            local = archive.parent.joinpath(*path.parts)
            if not local.is_file() or local.read_bytes() != bundle.read(member):
                raise ValueError(f"{archive}: source mismatch for {member.filename}")
        if f"{source.name}/SKILL.md" not in expected:
            raise ValueError(f"{archive}: missing SKILL.md")
    # README is repository-only documentation; Python caches are generated.
    actual = {
        f"{source.name}/{p.relative_to(source).as_posix()}"
        for p in source.rglob("*")
        if p.is_file()
        and p != source / "README.md"
        and "__pycache__" not in p.relative_to(source).parts
        and p.suffix not in {".pyc", ".pyo"}
    }
    if actual != expected:
        raise ValueError(f"{archive}: source files missing from package: {sorted(actual - expected)}")
    print(f"PASS: {archive.relative_to(ROOT)} ({len(expected)} matching source files)")


def validate_quiz_checker():
    skill = ROOT / "agent-skills/learning/quiz-forge"
    checker = skill / "scripts/qa_check.py"
    example = skill / "assets/example-quiz.json"
    data = json.loads(example.read_text(encoding="utf-8"))
    if not data.get("items"):
        raise ValueError("The sample quiz must exercise at least one item")
    subprocess.run([sys.executable, str(checker), str(example)], check=True)
    print(f"PASS: sample quiz ({len(data['items'])} item(s))")
    data["items"][0]["options"][1]["text"] = data["items"][0]["options"][0]["text"]
    with tempfile.TemporaryDirectory() as temporary:
        invalid = Path(temporary) / "duplicate-options.json"
        invalid.write_text(json.dumps(data), encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(checker), str(invalid)],
            capture_output=True, text=True, check=False,
        )
        if result.returncode != 1 or "identical or near-identical text" not in result.stdout:
            raise ValueError("Checker did not reject duplicate options as expected")
    print("PASS: duplicate options rejected with exit code 1")

    audit = runpy.run_path(str(checker))
    check_item = audit["check_item"]
    check_quiz = audit["check_quiz"]

    def fixture(texts, key="a"):
        item = copy.deepcopy(json.loads(example.read_text(encoding="utf-8"))['items'][0])
        item["options"] = [{"id": label, "text": text}
                           for label, text in zip("abcd", texts)]
        item["correct_option_id"] = key
        item["explanations"] = {label: "Synthetic fixture feedback." for label in "abcd"}
        return item

    def expect(texts, issue=None):
        issues = check_item(fixture(texts), 0)
        if issue is None and issues:
            raise ValueError(f"Balanced fixture rejected: {issues}")
        if issue is not None and not any(issue in message for message in issues):
            raise ValueError(f"Missing expected '{issue}' issue: {issues}")

    # Same word count, dramatically different character counts: should pass.
    expect(["Use AI.", "Choose HTTP.", "Apply electroencephalography."])
    # Equal character counts, dramatically different word counts: should fail.
    texts = ["a b c d e", "abcdefghi", "jklmnopqr"]
    if len({len(text) for text in texts}) != 1:
        raise ValueError("Equal-character fixture is broken")
    expect(texts, "word-count imbalance")
    expect(["Use the cache. Keep it warm.", "Reset the cache before use.",
            "Clear the cache after use."], "sentence-count imbalance")
    expect(["", "Use cache.", "Reset cache."], "has no words")
    expect(["Use cache.", "—", "Reset cache."], "has no words")
    # Apostrophes, hyphens, nonbreaking spaces and punctuation-only tokens.
    if audit["word_count"]("L’API utilise un cache-clé — n8n\u00a0HTTP") != 6:
        raise ValueError("Word tokenizer did not preserve French/technical tokens")
    expect(["M. Ali choisit HTTP 2.0.", "Mme. Sara choisit HTTP 1.1.",
            "Dr. Sami choisit HTTP 3.0."])
    # Exact tolerance boundary at a median of 11: spread 3 passes, 4 fails.
    tokens = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen".split()
    expect([" ".join(tokens[:n]) for n in (10, 11, 13)])
    expect([" ".join(tokens[:n]) for n in (10, 11, 14)], "word-count imbalance")
    # Every item individually passes, but choosing the longest predicts the key.
    items = []
    for index, key in enumerate("abcab"):
        texts = ["Use cache now.", "Reset cache now.", "Clear cache now."]
        # Keep one sentence and a one-word spread.
        texts["abc".index(key)] = texts["abc".index(key)].replace(" now.", " now carefully.")
        item = fixture(texts, key)
        item["id"] = f"synthetic-{index}"
        items.append(item)
    if any(check_item(item, i) for i, item in enumerate(items)):
        raise ValueError("Recurring-cue fixture must pass per-item checks")
    issues = check_quiz({"items": items})
    if not any("uniquely longest" in message for message in issues):
        raise ValueError("Recurring longest-key cue was not detected")
    if check_quiz({"items": items[:4]}):
        raise ValueError("Short quiz unexpectedly triggered the recurring-cue threshold")
    tied = copy.deepcopy(items)
    for item in tied:
        for opt in item["options"]:
            if audit["word_count"](opt["text"]) == 3:
                opt["text"] = opt["text"].replace(" now.", " now carefully.")
    if check_quiz({"items": tied}):
        raise ValueError("Equal-length ties unexpectedly triggered a longest-key cue")
    print("PASS: word/sentence balance, counting conventions, boundaries and recurring cues")


def main():
    archives = sorted((ROOT / "agent-skills").rglob("*.skill"))
    if not archives:
        raise ValueError("No packaged skills found")
    for archive in archives:
        validate_archive(archive)
    validate_quiz_checker()


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, zipfile.BadZipFile, subprocess.CalledProcessError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
