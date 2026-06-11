#!/usr/bin/env python3
"""Check whether a lesson follows the repository lesson template."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "학습 목표",
    "왜 이 개념이 임베디드 제어 SW에서 중요한가",
    "기초 개념",
    "공식 또는 이론의 유도/직관",
    "간단한 예시",
    "실무형 예시",
    "직접 구현 실습",
    "디버깅 포인트",
    "방산/로봇 SW 관점에서의 주의점",
    "확인 문제",
    "심화 과제",
    "포트폴리오 연결 아이디어",
]

FORBIDDEN_PATTERNS = [
    "weapon targeting",
    "target acquisition",
    "evasion algorithm",
    "offensive military",
]


def normalize_heading(line: str) -> str | None:
    """Return heading text without markdown hashes and numeric prefixes."""
    match = re.match(r"^#{2,6}\s+(.+?)\s*$", line)
    if not match:
        return None
    text = match.group(1).strip()
    text = re.sub(r"^\d+\.\s*", "", text)
    return text


def check_lesson(path: Path) -> list[str]:
    errors: list[str] = []

    if not path.exists():
        return [f"file does not exist: {path}"]
    if path.suffix != ".md":
        errors.append("lesson file should use .md extension")

    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    headings = [heading for line in lines if (heading := normalize_heading(line))]

    missing = [section for section in REQUIRED_SECTIONS if section not in headings]
    if missing:
        errors.append("missing required sections: " + ", ".join(missing))

    positions = [headings.index(section) for section in REQUIRED_SECTIONS if section in headings]
    if positions != sorted(positions):
        errors.append("required sections are not in the expected order")

    if len(content) < 2000:
        errors.append("lesson appears too short for a high-quality study-book chapter")

    lower_content = content.lower()
    for pattern in FORBIDDEN_PATTERNS:
        if pattern in lower_content:
            errors.append(f"forbidden safety-boundary phrase found: {pattern}")

    korean_chars = len(re.findall(r"[가-힣]", content))
    latin_chars = len(re.findall(r"[A-Za-z]", content))
    if korean_chars <= latin_chars:
        errors.append("lesson should primarily be written in Korean")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("lesson", type=Path, help="Path to a markdown lesson file")
    args = parser.parse_args()

    errors = check_lesson(args.lesson)
    if errors:
        print(f"FAIL: {args.lesson}")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PASS: {args.lesson}")
    print(f"Required sections: {len(REQUIRED_SECTIONS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
