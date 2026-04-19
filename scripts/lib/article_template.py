"""
article_template.py — Generate a new article HTML file from a title,
body paragraphs, and metadata. Uses the site's established template
(FB Pixel + GA4 + OG + canonical + category nav).
"""

from pathlib import Path
from datetime import date
import html

ARTICLES_DIR = Path(__file__).resolve().parent.parent.parent / "articles"

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','957762016897581');fbq('track','PageView');</script><noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=957762016897581&ev=PageView&noscript=1"/></noscript>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>{meta_title} — EnergyPricesToday.com</title>
  <meta name="description" content="{meta_desc}">
  <link rel="canonical" href="https://www.energypricestoday.com/articles/{slug}.html">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{meta_title}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:url" content="https://www.energypricestoday.com/articles/{slug}.html">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{meta_title}">
  <meta name="twitter:description" content="{meta_desc}">
  <link rel="stylesheet" href="../css/styles.css">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-FXGF8HZFWL"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","G-FXGF8HZFWL");</script>
  <link rel="icon" type="image/svg+xml" href="../images/favicon.svg">
  <link rel="apple-touch-icon" sizes="180x180" href="../images/apple-touch-icon.png">
</head>
<body>
  <header class="site-header" id="site-header"></header>
  <main>
    <article class="article-page">
      <div class="container" style="max-width:780px">
        <nav class="breadcrumbs"><a href="../index.html">Home</a> &rsaquo; <a href="../category/{primary_cat}.html">{cat_label}</a> &rsaquo; <span>Article</span></nav>
        <h1>{title}</h1>
        <div class="article-meta" style="margin:14px 0 24px">
          <span>Staff</span>
          <span>{date_label}</span>
          <span>{read_time} min read</span>
        </div>
        <div class="article-body">
{body_html}
        </div>
        <div style="margin-top:32px;padding-top:20px;border-top:1px solid var(--border);display:flex;gap:12px;flex-wrap:wrap">
          <a href="../oil-prices.html" class="btn-secondary">Oil Prices</a>
          <a href="../category/gas-prices.html" class="btn-secondary">Gas Prices</a>
          <a href="../category/geopolitics.html" class="btn-secondary">Geopolitics</a>
          <a href="../index.html" class="btn-secondary">Home</a>
        </div>
      </div>
    </article>
  </main>
  <footer class="site-footer" id="site-footer"></footer>
  <script src="../js/data.js"></script>
  <script src="../js/article-slugs.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
"""


CAT_LABELS = {
    "geopolitics": "Geopolitics",
    "gas-prices": "Gas Prices",
    "oil-prices": "Oil Prices",
    "markets": "Markets",
    "company-news": "Company News",
    "crude-oil": "Crude Oil",
    "natural-gas": "Natural Gas",
    "heating-oil": "Heating Oil",
    "oil-futures": "Oil Futures",
    "rig-count": "Rig Count",
    "nuclear": "Nuclear",
    "solar": "Solar",
    "wind": "Wind",
    "renewable-energy": "Renewable Energy",
    "alternative-energy": "Alternative Energy",
}


def infer_category(title: str) -> str:
    """Pick the best-fitting category slug for an article based on title keywords."""
    t = title.lower()
    # Priority order matters — most specific first
    rules = [
        (["hormuz", "iran", "ceasefire", "opec", "sanction", "israel", "lebanon",
          "pakistan", "russia", "saudi", "middle east", "geopolit", "blockade",
          "strait", "trump", "macron", "summit"], "geopolitics"),
        (["gas price", "pump price", "gasoline", "aaa"], "gas-prices"),
        (["rig count", "baker hughes"], "rig-count"),
        (["natural gas", "lng", "henry hub"], "natural-gas"),
        (["heating oil", "distillate"], "heating-oil"),
        (["oil futur", "curve", "backwardation", "contango"], "oil-futures"),
        (["wti", "brent", "crude oil", "crude", "oil price", "barrel"], "oil-prices"),
        (["nuclear"], "nuclear"),
        (["solar"], "solar"),
        (["wind"], "wind"),
        (["renewable"], "renewable-energy"),
        (["exxon", "chevron", "conoco", "shell", "bp", "cheniere", "aramco",
          "earnings", "dividend", "shares"], "company-news"),
        (["market", "stock", "s&p", "nasdaq", "dow"], "markets"),
    ]
    for keywords, cat in rules:
        if any(k in t for k in keywords):
            return cat
    return "geopolitics"  # default fallback


def write_article(
    title: str,
    body_paragraphs: list[str],
    slug: str | None = None,
    category: str | None = None,
    date_str: str | None = None,
    read_time: int = 5,
    overwrite: bool = False,
) -> Path:
    """
    Create or overwrite an article file.

    Returns the path to the created file.
    Raises FileExistsError if overwrite=False and the file exists.
    """
    from .data_js import slugify

    if slug is None:
        slug = slugify(title)
    if category is None:
        category = infer_category(title)
    if date_str is None:
        today = date.today()
        date_str = today.strftime("%b %-d, %Y")

    path = ARTICLES_DIR / f"{slug}.html"
    if path.exists() and not overwrite:
        raise FileExistsError(f"{path} already exists")

    # HTML-escape title for meta, but NOT for display (preserves entities like em-dash)
    meta_title = html.escape(title, quote=True)
    meta_desc_raw = (body_paragraphs[0] if body_paragraphs else title)[:160]
    # Strip HTML entities from meta desc
    import re as _re
    meta_desc_raw = _re.sub(r"<[^>]+>", "", meta_desc_raw)
    meta_desc_raw = meta_desc_raw.replace("&rsquo;", "'").replace("&ldquo;", '"').replace("&rdquo;", '"').replace("&mdash;", "-")
    meta_desc = html.escape(meta_desc_raw, quote=True)

    body_html = "\n".join(f"          <p>{p}</p>" for p in body_paragraphs)

    cat_label = CAT_LABELS.get(category, category.replace("-", " ").title())

    content = TEMPLATE.format(
        title=title,
        meta_title=meta_title,
        meta_desc=meta_desc,
        slug=slug,
        date_label=date_str,
        read_time=read_time,
        body_html=body_html,
        primary_cat=category,
        cat_label=cat_label,
    )

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return path


def write_stub_article(title: str, headline_summary: str = "") -> Path:
    """
    Write a minimal placeholder article for a breaking headline when we
    don't yet have full content (e.g., RSS-only fetch, no AI available).

    The stub is still a real, readable article — just shorter.
    """
    body = []
    if headline_summary:
        body.append(headline_summary)
    body.append(
        f"This is a developing story. For the latest updates on {title.lower()}, "
        "see our <a href=\"../category/geopolitics.html\">Geopolitics</a>, "
        "<a href=\"../oil-prices.html\">Oil Prices</a>, and "
        "<a href=\"../category/gas-prices.html\">Gas Prices</a> pages."
    )
    body.append(
        "EnergyPricesToday.com provides live oil prices, state-by-state U.S. gas "
        "prices, real-time geopolitical risk analysis, and corporate intelligence "
        "on the world's largest energy companies. All commodity prices marked LIVE "
        "update every 5 minutes via real exchange data."
    )
    return write_article(title, body, read_time=3)
