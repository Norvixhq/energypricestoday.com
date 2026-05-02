#!/usr/bin/env python3
"""
Bulk byline + schema author standardization.

For each article:
  HTML byline:  <span>Staff</span>  -->  <span>EnergyPricesToday Editorial</span>
  meta tag:     article:author Staff -->  article:author EnergyPricesToday Editorial
  JSON-LD author:
    "author":[{"@type":"Organization","name":"EnergyPricesToday Staff", ...}]
    -->
    "author":{"@type":"NewsMediaOrganization","name":"EnergyPricesToday","url":"https://www.energypricestoday.com"}

Idempotent: articles already at the target standard are left untouched.
Hub pages (CollectionPage schema, no byline) are skipped automatically — they
have neither <span>Staff</span> nor an Organization Staff author tag.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"

NEW_AUTHOR_LD = '"author":{"@type":"NewsMediaOrganization","name":"EnergyPricesToday","url":"https://www.energypricestoday.com"}'

# Old author shape we want to rewrite. Multiple variants exist in the corpus.
OLD_AUTHOR_PATTERNS = [
    # Array form with Organization
    re.compile(
        r'"author":\[{"@type":"Organization","name":"EnergyPricesToday Staff","url":"https://www\.energypricestoday\.com/about\.html"}\]'
    ),
    re.compile(
        r'"author":\[{"@type":"Organization","name":"EnergyPricesToday Staff"}\]'
    ),
    # Bare object form
    re.compile(
        r'"author":{"@type":"Organization","name":"EnergyPricesToday Staff","url":"https://www\.energypricestoday\.com/about\.html"}'
    ),
    re.compile(
        r'"author":{"@type":"Organization","name":"EnergyPricesToday Staff"}'
    ),
    # Person form (defensive — none expected, but safe)
    re.compile(
        r'"author":{"@type":"Person","name":"Staff"[^}]*}'
    ),
    re.compile(
        r'"author":\[{"@type":"Person","name":"Staff"[^}]*}\]'
    ),
]


def upgrade(path):
    txt = path.read_text(encoding="utf-8", errors="ignore")
    original = txt
    changes = []

    # 1. HTML byline: <span>Staff</span> -> <span>EnergyPricesToday Editorial</span>
    new_txt, n = re.subn(
        r'<span>Staff</span>',
        '<span>EnergyPricesToday Editorial</span>',
        txt,
    )
    if n:
        changes.append(f"byline×{n}")
        txt = new_txt

    # 2. article:author meta tag
    new_txt, n = re.subn(
        r'<meta property="article:author" content="Staff">',
        '<meta property="article:author" content="EnergyPricesToday Editorial">',
        txt,
    )
    if n:
        changes.append(f"meta×{n}")
        txt = new_txt

    # 3. JSON-LD author
    for pat in OLD_AUTHOR_PATTERNS:
        new_txt, n = pat.subn(NEW_AUTHOR_LD, txt)
        if n:
            changes.append(f"schema×{n}")
            txt = new_txt
            break  # Only one author shape per file

    if txt == original:
        return False, "already-standard"

    path.write_text(txt, encoding="utf-8")
    return True, ",".join(changes)


def main():
    upgraded = 0
    skipped = 0
    failed = 0
    for f in sorted(ARTICLES_DIR.glob("*.html")):
        try:
            ok, info = upgrade(f)
            if ok:
                upgraded += 1
            else:
                skipped += 1
        except Exception as e:
            failed += 1
            print(f"  FAIL {f.name}: {e}")
    print(f"Upgraded: {upgraded}")
    print(f"Skipped (already standard): {skipped}")
    print(f"Failed: {failed}")


if __name__ == "__main__":
    main()
