"""Check internal links in the Markdown files of this repository.

- every relative link must point to an existing file;
- links with a #fragment must match a heading in the target (GitHub-style slug);
- en/ and it/ must contain the same set of files.

Exit code 0 if everything is fine, 1 otherwise. Standard library only.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "_site", "vendor", "node_modules", ".jekyll-cache"}

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")


def markdown_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.md")
        if not any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts)
    )


def strip_code(text: str) -> list[str]:
    """Return the lines of text outside fenced code blocks, with inline code removed."""
    lines, in_fence = [], False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            lines.append(re.sub(r"`[^`]*`", "", line))
    return lines


def github_slug(heading: str) -> str:
    heading = re.sub(r"<[^>]+>", "", heading)
    heading = unicodedata.normalize("NFKC", heading).lower()
    heading = re.sub(r"[^\w\- ]", "", heading)
    return heading.replace(" ", "-")


def anchors(path: Path) -> set[str]:
    seen: dict[str, int] = {}
    result = set()
    for line in strip_code(path.read_text(encoding="utf-8")):
        m = HEADING_RE.match(line)
        if not m:
            continue
        slug = github_slug(m.group(2))
        n = seen.get(slug, 0)
        result.add(slug if n == 0 else f"{slug}-{n}")
        seen[slug] = n + 1
    return result


def main() -> int:
    errors: list[str] = []
    files = markdown_files()
    checked = 0

    for md in files:
        for lineno, line in enumerate(strip_code(md.read_text(encoding="utf-8")), 1):
            for target in LINK_RE.findall(line):
                if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                    continue  # http:, https:, mailto: ...
                checked += 1
                path_part, _, fragment = target.partition("#")
                dest = md if not path_part else (md.parent / path_part).resolve()
                if dest.is_dir():
                    dest = dest / "README.md"
                rel = md.relative_to(ROOT)
                if not dest.exists():
                    errors.append(f"{rel}: broken link -> {target}")
                    continue
                if fragment and dest.suffix == ".md" and fragment not in anchors(dest):
                    errors.append(f"{rel}: missing anchor -> {target}")

    en = {p.relative_to(ROOT / "en") for p in (ROOT / "en").rglob("*.md")}
    it = {p.relative_to(ROOT / "it") for p in (ROOT / "it").rglob("*.md")}
    for missing in sorted(en - it):
        errors.append(f"it/{missing.as_posix()} missing (exists in en/)")
    for missing in sorted(it - en):
        errors.append(f"en/{missing.as_posix()} missing (exists in it/)")

    print(f"{len(files)} Markdown files, {checked} internal links checked")
    for e in errors:
        print("ERROR:", e)
    print("OK" if not errors else f"{len(errors)} problem(s) found")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
