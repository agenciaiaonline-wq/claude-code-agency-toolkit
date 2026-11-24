"""Pre-commit hook blocking accidental secret tokens from entering git history."""

from pathlib import Path
import re
import sys

SECRET_PATTERNS = [
    ("Stripe Live Key", re.compile(r"sk_live_[A-Za-z0-9]{12,}")),
    ("GitHub Token", re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}")),
    ("OpenAI Style Key", re.compile(r"sk-[A-Za-z0-9_-]{24,}")),
    ("Private Key Header", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
]

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}


def scan_paths(root: Path) -> list[str]:
    hits: list[str] = []
    for file_path in sorted(root.rglob("*")):
        if not file_path.is_file() or any(p in SKIP_DIRS for p in file_path.parts):
            continue
        text = file_path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in SECRET_PATTERNS:
            if pattern.search(text):
                hits.append(f"{label} detected in {file_path.relative_to(root).as_posix()}")
    return hits


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    findings = scan_paths(target.resolve())
    if findings:
        for item in findings:
            print(f"[BLOCKED] {item}", file=sys.stderr)
        raise SystemExit(1)
    print("[PASS] Pre-commit secret check passed.")
