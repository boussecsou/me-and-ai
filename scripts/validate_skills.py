#!/usr/bin/env python3
"""Validate packaged skill sources and exercise Quiz Forge's existing checker."""

import json
from pathlib import Path, PurePosixPath
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
