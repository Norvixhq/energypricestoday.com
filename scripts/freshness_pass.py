#!/usr/bin/env python3
"""
Add a "Last reviewed: May 15, 2026" indicator to evergreen explainer
articles. These are reference pieces that don't have a single
publication date the way news articles do — adding a "last reviewed"
line signals active maintenance without misleadingly bumping the
original publish date.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "articles"

# Evergreen explainer articles (and explainer-style hub-adjacent pieces)
EVERGREEN = [
    "strait-of-hormuz-explained.html",
    "what-happens-if-strait-of-hormuz-closes.html",
    "what-is-brent-crude-oil-and-why-does-it-matter.html",
    "what-is-opec-plus-how-it-affects-oil-prices.html",
    "what-is-the-rig-count-and-why-does-it-matter-for-oil-prices.html",
    "wti-vs-brent-crude-oil-key-differences-explained.html",
    "oil-price-per-barrel-today-wti-brent-explained.html",
    "strait-of-hormuz.html",
]

LAST_REVIEWED_BADGE = '''<div style="display:inline-flex;align-items:center;gap:8px;font-family:var(--font-body);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-3);padding:6px 12px;background:var(--surface-2);border:1px solid var(--border);border-radius:4px;margin:8px 0 16px"><span style="width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block"></span>Reviewed and current as of May 15, 2026</div>'''


def main():
    touched = 0
    for slug in EVERGREEN:
        path = ARTICLES / slug
        if not path.exists():
            print(f"  ✗ missing: {slug}")
            continue
        txt = path.read_text(encoding="utf-8")
        if "Reviewed and current as of May 15, 2026" in txt:
            print(f"  · {slug}: already has badge, skip")
            continue

        # Try article-meta pattern first
        pattern = re.compile(r'(<div class="article-meta"[^>]*>.*?</div>)', re.DOTALL)
        new_txt, n = pattern.subn(r'\1\n        ' + LAST_REVIEWED_BADGE, txt, count=1)
        if n == 0:
            # Try article-author-row pattern (used by explainer template)
            pattern2 = re.compile(r'(<div class="article-author-row">.*?</div></div></div>)', re.DOTALL)
            new_txt, n = pattern2.subn(r'\1\n        ' + LAST_REVIEWED_BADGE, txt, count=1)
            if n == 0:
                # Last resort: insert after the h1
                pattern3 = re.compile(r'(<h1>[^<]+</h1>)')
                new_txt, n = pattern3.subn(r'\1\n        ' + LAST_REVIEWED_BADGE, txt, count=1)
                if n == 0:
                    print(f"  · {slug}: no insertion point found, skip")
                    continue
        path.write_text(new_txt, encoding="utf-8")
        touched += 1
        print(f"  ✓ {slug}")
    print(f"\n{touched} evergreen articles flagged as reviewed.")


if __name__ == "__main__":
    main()
