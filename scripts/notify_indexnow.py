#!/usr/bin/env python3
"""
notify_indexnow.py — Submit URLs to IndexNow for instant search-engine indexing.

Pushes URLs to Bing's IndexNow endpoint, which is also relayed to Yandex,
Seznam, Naver, and other participating engines. (Google does NOT use
IndexNow — Sitemaps + Google News Publisher cover that side.)

Usage:
  python3 scripts/notify_indexnow.py                    # Submit URLs from news-sitemap.xml (default)
  python3 scripts/notify_indexnow.py --from-sitemap     # Same as default, explicit
  python3 scripts/notify_indexnow.py --homepage         # Submit homepage only
  python3 scripts/notify_indexnow.py --all-major        # Submit homepage + pillar pages
  python3 scripts/notify_indexnow.py --daily            # Submit news-sitemap + major pages (recommended after each refresh)
  python3 scripts/notify_indexnow.py URL [URL ...]      # Submit explicit URLs
       (each URL may be absolute, or a site-relative path like /articles/foo.html)

Rate limit: 10,000 URLs per day. Daily refresh uses ~10. No quota concerns.
Response codes:
  200 OK — submitted
  400 Bad request — payload malformed
  403 Forbidden — key not found at keyLocation (check the .txt is deployed)
  422 Unprocessable — URL doesn't belong to host, or key mismatch
  429 Too many requests — slow down

This script is part of the daily refresh workflow. Call it AFTER:
  - scripts/generate_rss_feed.py
  - scripts/generate_news_sitemap.py
"""

import sys
import json
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from pathlib import Path

# ─── CONFIG ─────────────────────────────────────────────────────────
KEY = "4a82987e5ddb4711928ae0f338dc8898"
HOST = "www.energypricestoday.com"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"

ROOT = Path(__file__).resolve().parent.parent
SITEMAP = ROOT / "news-sitemap.xml"

# Pages we want re-indexed after every daily refresh, since their visible
# content changes (narratives, prices, surfaced articles).
MAJOR_PAGES = [
    "/",
    "/oil-prices.html",
    "/markets.html",
    "/electricity-prices.html",
    "/rig-count.html",
    "/category/gas-prices.html",
    "/category/geopolitics.html",
    "/category/crude-oil.html",
    "/category/natural-gas.html",
]


def urls_from_news_sitemap():
    """Read fresh-article URLs from the news sitemap (last refresh cycle)."""
    if not SITEMAP.exists():
        print(f"[notify_indexnow] news-sitemap.xml not found at {SITEMAP}")
        return []
    try:
        tree = ET.parse(SITEMAP)
        root = tree.getroot()
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        urls = [loc.text for loc in root.findall(".//sm:url/sm:loc", ns) if loc.text]
        return urls
    except Exception as e:
        print(f"[notify_indexnow] failed to parse sitemap: {e}")
        return []


def normalize(arg):
    """Normalize an input — accept absolute URLs or site-relative paths."""
    if arg.startswith("http://") or arg.startswith("https://"):
        return arg
    if not arg.startswith("/"):
        arg = "/" + arg
    return f"https://{HOST}{arg}"


def submit(urls):
    """POST URLs to IndexNow. Returns True on success."""
    if not urls:
        print("[notify_indexnow] nothing to submit")
        return False
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT,
        data=body,
        method="POST",
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            status = resp.status
            reason = resp.reason
            print(f"[notify_indexnow] HTTP {status} {reason} \u2014 submitted {len(urls)} URL(s)")
            return 200 <= status < 300
    except urllib.error.HTTPError as e:
        body_txt = ""
        try:
            body_txt = e.read().decode("utf-8", errors="ignore")[:300]
        except Exception:
            pass
        print(f"[notify_indexnow] HTTP {e.code} {e.reason} \u2014 {body_txt}")
        return False
    except urllib.error.URLError as e:
        print(f"[notify_indexnow] network error \u2014 {e.reason}")
        return False
    except Exception as e:
        print(f"[notify_indexnow] error \u2014 {e}")
        return False


def main(argv):
    args = argv[1:]
    urls = []

    if not args or args == ["--from-sitemap"]:
        urls = urls_from_news_sitemap()
    elif args == ["--homepage"]:
        urls = [f"https://{HOST}/"]
    elif args == ["--all-major"]:
        urls = [f"https://{HOST}{p}" for p in MAJOR_PAGES]
    elif args == ["--daily"]:
        # Daily refresh: fresh articles from news-sitemap + all major pages
        urls = urls_from_news_sitemap()
        urls += [f"https://{HOST}{p}" for p in MAJOR_PAGES]
    else:
        urls = [normalize(a) for a in args]

    if not urls:
        print("[notify_indexnow] no URLs to submit; exiting cleanly")
        return 0

    # Dedupe, preserve order
    urls = list(dict.fromkeys(urls))

    print(f"[notify_indexnow] submitting {len(urls)} URL(s):")
    for u in urls[:20]:
        print(f"  {u}")
    if len(urls) > 20:
        print(f"  \u2026 and {len(urls) - 20} more")

    ok = submit(urls)
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
