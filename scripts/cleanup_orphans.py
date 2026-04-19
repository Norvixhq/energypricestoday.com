#!/usr/bin/env python3
"""
cleanup_orphans.py — Remove article files that are no longer referenced
by any visible content block or any other article.

Safety: only removes articles that are truly unreferenced. Runs as part
of the nightly audit, never during high-frequency jobs.

Exit codes:
  0 — Cleanup ran (may or may not have removed files)
  2 — Error
"""

import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib import data_js  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"

# Some article slugs are deliberately kept even if unreferenced
# (e.g., legacy SEO URLs). Add to this set to protect.
PROTECTED_SLUGS: set[str] = set()


def collect_referenced_slugs() -> set[str]:
    """Every slug referenced by (a) visible titles in data.js or (b) any HTML file."""
    referenced = set()

    # From visible titles
    for title in data_js.extract_all_visible_titles():
        referenced.add(data_js.slugify(title))

    # From any HTML file link
    for root, _, files in os.walk(ROOT):
        for f in files:
            if not f.endswith(".html"):
                continue
            path = Path(root) / f
            try:
                with open(path, encoding="utf-8") as fp:
                    content = fp.read()
            except Exception:
                continue
            for m in re.finditer(
                r'(?:\.\./)?articles/([a-z0-9\-]+)\.html', content
            ):
                referenced.add(m.group(1))

    # From article-slugs.js (slugs that are actively mapped)
    slugs_js = ROOT / "js" / "article-slugs.js"
    if slugs_js.exists():
        with open(slugs_js, encoding="utf-8") as f:
            content = f.read()
        for m in re.finditer(r':\s*"([a-z0-9\-]+)"', content):
            referenced.add(m.group(1))

    return referenced


def on_disk_slugs() -> set[str]:
    return {
        f.replace(".html", "")
        for f in os.listdir(ARTICLES_DIR)
        if f.endswith(".html")
    }


def main() -> int:
    # Max we'll remove in one run — safety cap
    MAX_REMOVE = 30

    referenced = collect_referenced_slugs()
    on_disk = on_disk_slugs()
    orphans = on_disk - referenced - PROTECTED_SLUGS

    if not orphans:
        print("[cleanup_orphans] No orphans found")
        return 0

    if len(orphans) > MAX_REMOVE:
        print(f"[cleanup_orphans] WARNING: {len(orphans)} orphans detected — "
              f"exceeds MAX_REMOVE={MAX_REMOVE}. Aborting to prevent accidental mass deletion.")
        print("  Sample orphans:")
        for s in sorted(orphans)[:10]:
            print(f"    - {s}")
        return 2

    print(f"[cleanup_orphans] Removing {len(orphans)} orphan articles:")
    for slug in sorted(orphans):
        path = ARTICLES_DIR / f"{slug}.html"
        if path.exists():
            path.unlink()
            print(f"  - deleted {slug}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
