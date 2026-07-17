"""Validate repository Markdown without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAGES = (
    "concept",
    "development",
    "production",
    "utilization",
    "support",
    "retirement",
)
INLINE_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
BASELINE = "Status: **baseline 0.2**"


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts
    )


def validate_whitespace(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.endswith((" ", "\t")):
            errors.append(f"{path.relative_to(ROOT)}:{line_number}: trailing whitespace")
    if text and not text.endswith("\n"):
        errors.append(f"{path.relative_to(ROOT)}: missing final newline")
    return errors


def validate_links(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    for target in INLINE_LINK.findall(text):
        if target.startswith(("https://", "http://", "mailto:", "#")):
            continue
        local_target = target.split("#", 1)[0]
        if not local_target:
            continue
        resolved = (path.parent / local_target).resolve()
        if not resolved.exists():
            errors.append(
                f"{path.relative_to(ROOT)}: missing local link target {target!r}"
            )
    return errors


def validate_stages() -> list[str]:
    errors: list[str] = []
    stage_dir = ROOT / "docs" / "stages"
    for index, stage in enumerate(STAGES):
        path = stage_dir / f"{stage}.md"
        if not path.is_file():
            errors.append(f"missing stage document: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        if BASELINE not in text.splitlines()[:6]:
            errors.append(f"{path.relative_to(ROOT)}: expected {BASELINE}")
        if index > 0:
            previous = STAGES[index - 1]
            expected = rf"Previous:\s*\[{previous.title()}\]\({previous}\.md\)"
            if not re.search(expected, text):
                errors.append(f"{path.relative_to(ROOT)}: missing navigation {expected!r}")
        if index < len(STAGES) - 1:
            following = STAGES[index + 1]
            expected = rf"Next:\s*\[{following.title()}\]\({following}\.md\)"
            if not re.search(expected, text):
                errors.append(f"{path.relative_to(ROOT)}: missing navigation {expected!r}")
    return errors


def main() -> int:
    files = markdown_files()
    errors: list[str] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        errors.extend(validate_whitespace(path, text))
        errors.extend(validate_links(path, text))
    errors.extend(validate_stages())

    if errors:
        print("documentation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"documentation validation passed ({len(files)} Markdown files, 6 stages)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
