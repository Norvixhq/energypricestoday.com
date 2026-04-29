#!/usr/bin/env python3
"""
Pre-deploy guard: validate every inline <script> block in every HTML page.

This catches the recurring bug pattern where a single typo in JS-string-quoted
prose (especially apostrophes) makes a whole page's inline script fail to parse,
which silently nukes JS-rendered content like the geopolitics breaking ticker
and risk cards. The page renders but is missing all dynamic content.

Run before every deploy. Exits non-zero if any script fails to parse.

Usage:
    python3 scripts/validate_inline_js.py

Excludes:
    - <script src="...">  (loaded externally, validated separately)
    - <script type="application/ld+json">  (structured data, not JS)
    - FB pixel snippets (self-contained, parser confused by !function)
    - Google Analytics stubs (window.dataLayer pattern)
"""
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
broken = []
total_blocks = 0

def scan_file(f):
    global total_blocks
    txt = f.read_text(encoding='utf-8', errors='ignore')
    for m in re.finditer(r'<script(?![^>]*\bsrc=)(?![^>]*\btype="application)[^>]*>(.*?)</script>', txt, re.DOTALL):
        code = m.group(1)
        if len(code) < 100: continue
        stripped = code.strip()
        if stripped.startswith('!function(f,b,e,v,n,t,s)'): continue  # FB Pixel
        if 'window.dataLayer' in code and len(code) < 300: continue  # GA stub
        total_blocks += 1
        with open('/tmp/_inline_validate.js', 'w') as fp: fp.write(code)
        r = subprocess.run(['node', '--check', '/tmp/_inline_validate.js'],
                           capture_output=True, text=True, timeout=10)
        if r.returncode != 0:
            err_line = ''
            for line in r.stderr.split('\n'):
                if 'SyntaxError' in line or 'Error:' in line:
                    err_line = line.strip()[:200]
                    break
            broken.append((str(f.relative_to(ROOT)), err_line))

# Top-level + category pages first (most edited, highest risk)
for f in ROOT.glob('*.html'):
    scan_file(f)
for f in (ROOT/'category').glob('*.html'):
    scan_file(f)
# Article pages last (programmatically generated, lower risk but still scan)
for f in (ROOT/'articles').glob('*.html'):
    scan_file(f)

if broken:
    print(f"✗ FAIL: {len(broken)} broken inline scripts in {total_blocks} scanned blocks")
    for f, e in broken:
        print(f"  {f}")
        print(f"    {e}")
    print("\nFix these before deploying. The page will render but JS-injected")
    print("content (breaking ticker, risk cards, charts, etc.) will be missing.")
    sys.exit(1)

print(f"✓ PASS: {total_blocks} inline JS blocks validated, 0 broken")
sys.exit(0)
