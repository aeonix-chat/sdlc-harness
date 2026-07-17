"""Reject common local-path, PII, and secret leakage before publication."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIPPED_PARTS = {".git", ".venv", "__pycache__"}
SKIPPED_SUFFIXES = {
    ".gif", ".ico", ".jpeg", ".jpg", ".pdf", ".png", ".pyc", ".webp", ".zip"
}
EXAMPLE_EMAIL_DOMAINS = {"example.com", "example.net", "example.org"}
LOCAL_PATH_PATTERN = (
    r"(?<![A-Za-z0-9])(?:file:"
    + r"//|/"
    + r"Users/|/"
    + r"home/|/"
    + r"root/|[A-Za-z]:[\\/]"
    + r"Users[\\/])"
)
PRIVATE_KEY_PATTERN = (
    r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE " + r"KEY-----"
)


@dataclass(frozen=True)
class Rule:
    name: str
    pattern: re.Pattern[str]


RULES = (
    Rule(
        "absolute local filesystem path",
        re.compile(LOCAL_PATH_PATTERN),
    ),
    Rule(
        "private key material",
        re.compile(PRIVATE_KEY_PATTERN),
    ),
    Rule("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    Rule("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b")),
    Rule("OpenAI-style secret key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    Rule(
        "generic assigned secret",
        re.compile(
            r"(?i)\b(?:api[_-]?key|client[_-]?secret|access[_-]?token|password)"
            r"\s*[:=]\s*['\"][^'\"\s]{8,}['\"]"
        ),
    ),
    Rule(
        "phone number",
        re.compile(r"(?<!\w)\+[1-9][0-9 .()\-]{7,}[0-9](?!\w)"),
    ),
)
EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})\b")


def publication_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and not SKIPPED_PARTS.intersection(path.relative_to(ROOT).parts)
        and path.suffix.lower() not in SKIPPED_SUFFIXES
    )


def scan(path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []

    relative = path.relative_to(ROOT)
    errors: list[str] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        for rule in RULES:
            if rule.pattern.search(line):
                errors.append(f"{relative}:{line_number}: {rule.name}")
        for match in EMAIL.finditer(line):
            if match.group(1).lower() not in EXAMPLE_EMAIL_DOMAINS:
                errors.append(f"{relative}:{line_number}: non-example email address")
    return errors


def main() -> int:
    files = publication_files()
    errors = [error for path in files for error in scan(path)]
    if errors:
        print("publication safety validation failed:")
        for error in errors:
            print(f"- {error}")
        print("Review each finding; do not suppress real credentials or personal data.")
        return 1

    print(f"publication safety validation passed ({len(files)} text candidates)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
