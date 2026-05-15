#!/usr/bin/env python3
"""Generate 2 articles covering verified May 14-15, 2026 events.

All quotes are real and attributed to real, published sources.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"

STORIES = [
    {
        "slug": "trump-xi-summit-beijing-iran-hormuz-deal",
        "title_variants": [
            "Trump-Xi Summit in Beijing: Both Sides Agree Strait of Hormuz Must Remain Open",
            "Trump-Xi Beijing Summit Concludes With Hormuz, Iran Nuclear Agreement",
            "Xi Offers to Help Broker Iran Peace Deal at Trump Beijing Summit",
        ],
        "display_title_html": "Trump-Xi Summit in Beijing: Both Sides Agree Strait of Hormuz Must Remain Open",
        "seo_title": "Trump-Xi Beijing Summit: Hormuz Must Remain Open",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "May 15, 2026",
        "iso_date": "2026-05-15T09:00:00-04:00",
        "section": "Geopolitics",
        "read_time": "6 min",
        "meta_desc": "President Trump and President Xi held a two-day summit in Beijing concluding May 14. The White House readout said both leaders agreed the Strait of Hormuz must remain open and that Iran cannot have a nuclear weapon.",
        "keywords": "Trump Xi summit Beijing May 2026, Strait of Hormuz reopening, Iran nuclear deal China, US China oil purchases, Bessent China Hormuz",
        "paragraphs": [
            "President Donald Trump and Chinese President Xi Jinping concluded a two-day summit in Beijing on Thursday, May 14, 2026, with both sides agreeing that the Strait of Hormuz must remain open to support the free flow of energy and that Iran cannot have a nuclear weapon. The agreement, according to a White House readout, marked the clearest signal yet that the world&rsquo;s two largest economies are aligned on the central question driving the eleven-week energy shock that has lifted Brent above $100 per barrel.",
            "Trump told Fox News that Xi offered to help broker peace with Iran. &ldquo;He said, &lsquo;I would love to be a help, if I can be of any help whatsoever,&rsquo;&rdquo; Trump said of Xi. Trump added that Xi assured him China would not provide military equipment to Iran: &ldquo;He said he&rsquo;s not going to give military equipment. That&rsquo;s a big statement.&rdquo; The assurance, however, stopped short of addressing broader questions about Chinese support for Iran including intelligence sharing or electronics exports.",
            "The White House readout said Xi reiterated Beijing&rsquo;s opposition to the militarization of the Strait of Hormuz and to any effort to charge a toll for its use &mdash; both elements of the standoff that have emerged as central obstacles to ending the conflict. Iran has reportedly sought to implement a transit toll system, which the U.S. has rejected as a precondition. Xi also expressed interest in purchasing more American crude oil to reduce China&rsquo;s dependence on Persian Gulf supply over time.",
            "On the U.S. side, Treasury Secretary Scott Bessent framed the summit&rsquo;s significance bluntly in a Thursday CNBC interview. &ldquo;It&rsquo;s very much in their interest to get the strait reopened,&rdquo; Bessent told CNBC&rsquo;s Joe Kernen. &ldquo;I think they will be working behind the scenes to the extent anyone has any say over the Iranian leadership. China has a much bigger interest in reopening the strait than the U.S. does.&rdquo; China is the largest crude oil importer in the world and a major buyer of Iranian crude.",
            "Secretary of State Marco Rubio had framed the U.S. position similarly in a pre-summit Fox News interview that aired before the bilateral meeting. &ldquo;It&rsquo;s in their interest to resolve this,&rdquo; Rubio said of Beijing. &ldquo;We hope to convince them to play a more active role in getting Iran to walk away from what they&rsquo;re doing now and trying to do now in the Persian Gulf.&rdquo;",
            "The Chinese readout of the meeting was notably more restrained on Iran. State news agency Xinhua said only that the two leaders &ldquo;exchanged views on major international and regional issues, such as the Middle East situation,&rdquo; without mentioning Iran&rsquo;s nuclear program or the Strait of Hormuz by name. The asymmetry between the two readouts is consistent with prior expert assessments that Beijing wants to avoid being pulled too deeply into the conflict and continues to view its resolution as primarily America&rsquo;s problem to solve.",
            "Following the summit, Trump indicated he was running out of patience with Iran and warned Tehran to reach a deal or face &ldquo;annihilation.&rdquo; Trump told reporters: &ldquo;We may have to do a little cleanup work because we had a month-long ceasefire.&rdquo; The administration has reportedly proposed a 20-year verified moratorium on Iran&rsquo;s nuclear program and the surrender of all highly enriched uranium as conditions to end hostilities, with Pakistan acting as an intermediary.",
            "Market reaction to the summit was muted. WTI crude traded near $103.50 Friday morning, on track for a roughly 10% weekly gain. Brent traded near $106.90. Both benchmarks remain elevated reflecting persistent uncertainty over the timing and conditions of a Hormuz reopening. For continuing coverage, see our <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a> and <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">live oil prices</a>.",
        ],
        "related": [
            ("Trump Warns Iran to Reach a Deal or Face 'Annihilation'", "trump-warns-iran-annihilation-20-year-nuclear-moratorium"),
            ("UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity"),
            ("IEA: Global Oil Inventories Drawing at Record 4M bpd Pace; Severe Undersupply Through October", "iea-global-oil-inventories-record-4m-bpd-pace-undersupply-through-october"),
        ],
    },
    {
        "slug": "trump-warns-iran-annihilation-20-year-nuclear-moratorium",
        "title_variants": [
            "Trump Warns Iran to Reach a Deal or Face 'Annihilation'",
            "Trump's 20-Year Nuclear Moratorium Offer for Iran",
            "Trump to Iran: Reach Deal or Face Annihilation",
        ],
        "display_title_html": "Trump Warns Iran to Reach a Deal or Face &lsquo;Annihilation&rsquo;",
        "seo_title": "Trump Warns Iran: Reach Deal or Face Annihilation",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "May 15, 2026",
        "iso_date": "2026-05-15T11:00:00-04:00",
        "section": "Geopolitics",
        "read_time": "5 min",
        "meta_desc": "Speaking after the Beijing summit, President Trump warned Iran to reach a deal or face annihilation. The administration has reportedly proposed a 20-year verified nuclear moratorium and surrender of highly enriched uranium as conditions.",
        "keywords": "Trump Iran annihilation warning, 20 year nuclear moratorium Iran, Trump Iran deal HEU, Pakistan intermediary Iran talks, Hormuz reopening conditions",
        "paragraphs": [
            "President Donald Trump warned Iran on Thursday, May 14, 2026, to reach a deal or face &ldquo;annihilation,&rdquo; saying his patience with Tehran was running out and that the United States may have to resume military operations against the Islamic Republic if a negotiated settlement remains out of reach. The warning came as Trump concluded his two-day summit with Chinese President Xi Jinping in Beijing and as the U.S.-led blockade of the Strait of Hormuz entered its eleventh week.",
            "Trump made the &ldquo;annihilation&rdquo; remark in remarks to reporters, telling Fox News that &ldquo;we may have to do a little cleanup work because we had a month-long ceasefire.&rdquo; The comment reflects a return to the harder posture Trump took before the April 7 emergency ceasefire that he announced less than two hours before his deadline for Iran to reopen the strait. That earlier deadline came with Trump warning a &ldquo;civilization will die tonight&rdquo; if no deal was reached.",
            "Politico has reported that the administration is offering Iran a 20-year verified moratorium on its nuclear program and the surrender of all highly enriched uranium (HEU), along with free commercial traffic through the Strait of Hormuz, as the conditions under which the United States would consider hostilities ended. The 20-year moratorium represents a notable shift for Trump, who had previously insisted Iran never be allowed to enrich uranium under any timeline.",
            "Pakistan has emerged as the principal intermediary in the talks. Prime Minister Shehbaz Sharif worked with U.S. officials before the April ceasefire to construct a framework that both Tehran and Washington could publicly accept. Reporting from Trump and from outlets including Hot Air indicates the 20-year framework may have originated as a Pakistani-backed proposal designed to bring Iran&rsquo;s Islamic Revolutionary Guard Corps to the negotiating table on the nuclear-weapons question at all.",
            "China&rsquo;s role at the summit was carefully calibrated. According to Trump, Xi told him China would help diplomatically &mdash; or directly with its own personnel &mdash; in extracting any agreed-upon highly enriched uranium from Iranian territory. But Beijing&rsquo;s public readout of the summit did not mention Iran by name, signaling China&rsquo;s preference to support the process without becoming visibly entangled in U.S. enforcement against a major Chinese trading partner.",
            "The market backdrop is unforgiving. The EIA&rsquo;s May Short-Term Energy Outlook released May 12 assesses that Iraq, Saudi Arabia, Kuwait, the UAE, Qatar, and Bahrain collectively shut in 10.5 million barrels per day of crude oil production in April, with shut-ins expected to peak near 10.8 million bpd in May as storage limits force additional producer cutbacks. Saudi Arabia informed OPEC that its output had fallen to the lowest level since 1990.",
            "Whether Iran will accept the 20-year framework remains the central question of the next several weeks. Reports of approximately 30 vessels transiting Hormuz in recent days, including transit allowances for some Chinese ships, suggest Iran is calibrating rather than completely closing the strait. Whether that calibration leads to a settlement, or to renewed U.S. military action, will be visible in the days ahead. For continuing coverage, see our <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a>.",
        ],
        "related": [
            ("Trump-Xi Summit in Beijing: Both Sides Agree Strait of Hormuz Must Remain Open", "trump-xi-summit-beijing-iran-hormuz-deal"),
            ("UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity"),
            ("Strait of Hormuz Explained", "strait-of-hormuz-explained"),
        ],
    },
]


def render(s):
    title_safe = s["display_title_html"].replace('"', '&quot;')
    seo_title = s["seo_title"].replace('"', '&quot;')
    headline_safe = s["display_title_html"].replace('"', '\\"').replace("'", "\u2019")
    desc_safe = s["meta_desc"].replace('"', '\\"').replace("'", "\u2019")
    canonical = f"https://www.energypricestoday.com/articles/{s['slug']}.html"
    cat_label = s["category"]
    word_count = sum(len(p.split()) for p in s["paragraphs"])
    paragraphs = "\n          ".join(f"<p>{p}</p>" for p in s["paragraphs"])
    related_items = "\n            ".join(
        f'<li><a href="{slug}.html" style="color:var(--text-1);text-decoration:none">{title}</a></li>'
        for title, slug in s["related"]
    )

    news_schema = (
        '<script type="application/ld+json">'
        '{"@context":"https://schema.org","@type":"NewsArticle",'
        f'"headline":"{headline_safe}",'
        f'"description":"{desc_safe}",'
        f'"datePublished":"{s["iso_date"]}",'
        f'"dateModified":"{s["iso_date"]}",'
        '"author":{"@type":"NewsMediaOrganization","name":"EnergyPricesToday","url":"https://www.energypricestoday.com"},'
        '"image":["https://www.energypricestoday.com/images/og-image.png"],'
        f'"articleSection":"{s["section"]}",'
        f'"wordCount":{word_count},'
        f'"mainEntityOfPage":{{"@type":"WebPage","@id":"{canonical}"}},'
        '"isAccessibleForFree":true,'
        '"publisher":{"@type":"NewsMediaOrganization","name":"EnergyPricesToday.com","url":"https://www.energypricestoday.com","logo":{"@type":"ImageObject","url":"https://www.energypricestoday.com/images/logo.png","width":674,"height":130}}}'
        '</script>'
    )

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','957762016897581');fbq('track','PageView');</script><noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=957762016897581&ev=PageView&noscript=1"/></noscript>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>{seo_title}</title>
  <meta name="description" content="{s['meta_desc']}">
  <link rel="canonical" href="{canonical}">
  <meta name="news_keywords" content="{s['keywords']}">
  <meta name="keywords" content="{s['keywords']}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <meta name="googlebot-news" content="index, follow">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{seo_title}">
  <meta property="og:description" content="{s['meta_desc']}">
  <meta property="article:published_time" content="{s['iso_date']}">
  <meta property="article:modified_time" content="{s['iso_date']}">
  <meta property="article:author" content="EnergyPricesToday Editorial">
  <meta property="article:section" content="{s['section']}">
  <meta property="article:tag" content="{s['section']}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="EnergyPricesToday.com">
  <meta property="og:image" content="https://www.energypricestoday.com/images/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@energypricestoday">
  <meta name="twitter:title" content="{seo_title}">
  <meta name="twitter:description" content="{s['meta_desc'][:200]}">
  <meta name="twitter:image" content="https://www.energypricestoday.com/images/og-image.png">
  <link rel="alternate" type="application/rss+xml" title="EnergyPricesToday RSS Feed" href="../feed.xml">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,500&family=Outfit:wght@300;400;500;600;700&display=swap" media="print" onload="this.media='all'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,500&family=Outfit:wght@300;400;500;600;700&display=swap"></noscript>
  <link rel="stylesheet" href="../css/styles.css?v=29">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-FXGF8HZFWL"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","G-FXGF8HZFWL");</script>
  <link rel="icon" type="image/x-icon" href="../images/favicon.ico?v=2">
  <link rel="icon" type="image/svg+xml" href="../images/favicon.svg?v=2">
  <link rel="icon" type="image/png" sizes="16x16" href="../images/favicon-16x16.png?v=2">
  <link rel="icon" type="image/png" sizes="32x32" href="../images/favicon-32x32.png?v=2">
  <link rel="icon" type="image/png" sizes="48x48" href="../images/favicon-48x48.png?v=2">
  <link rel="apple-touch-icon" sizes="180x180" href="../images/apple-touch-icon.png?v=2">
  {news_schema}
</head>
<body>
  <header class="site-header" id="site-header"></header>
  <main>
    <article class="article-page">
      <div class="container" style="max-width:780px">
        <nav aria-label="Breadcrumb" style="margin:24px 0 16px;font-size:12px;color:var(--text-3);display:flex;flex-wrap:wrap;gap:6px;align-items:center">
          <a href="../index.html" style="color:var(--text-2);text-decoration:none">Home</a>
          <span style="color:var(--text-3)">&rsaquo;</span>
          <a href="{s['category_url']}" style="color:var(--text-2);text-decoration:none">{cat_label}</a>
          <span style="color:var(--text-3)">&rsaquo;</span>
          <span style="color:var(--text-2)">Article</span>
        </nav>
        <h1>{title_safe}</h1>
        <div class="article-meta" style="margin:14px 0 24px"><span>EnergyPricesToday Editorial</span><span>{s['date']}</span><span>{s['read_time']} read</span></div>
        <div class="article-body">
          {paragraphs}
        </div>

        <div style="margin-top:40px;padding:24px;background:var(--surface-2);border-radius:10px;border-left:3px solid var(--blue)">
          <h3 style="margin:0 0 12px 0;font-size:14px;text-transform:uppercase;letter-spacing:0.06em;color:var(--text-2)">Related Coverage</h3>
          <ul style="margin:0;padding-left:20px;line-height:1.8">
            {related_items}
          </ul>
        </div>

        <div style="margin-top:32px;padding-top:20px;border-top:1px solid var(--border);display:flex;gap:12px;flex-wrap:wrap">
          <a href="../oil-prices.html" class="btn-secondary">Oil Prices</a>
          <a href="../category/gas-prices.html" class="btn-secondary">Gas Prices</a>
          <a href="../electricity-prices.html" class="btn-secondary">Electricity</a>
          <a href="../category/geopolitics.html" class="btn-secondary">Geopolitics</a>
          <a href="../markets.html" class="btn-secondary">Markets</a>
          <a href="strait-of-hormuz-explained.html" class="btn-secondary">Hormuz Explainer</a>
        </div>
      </div>
    </article>
  </main>
  <footer class="site-footer" id="site-footer"></footer>
  <script src="../js/data.js?v=29"></script>
  <script src="../js/article-slugs.js?v=29"></script>
  <script src="../js/main.js?v=29"></script>
</body>
</html>
'''


def main():
    for s in STORIES:
        out = ARTICLES_DIR / f"{s['slug']}.html"
        out.write_text(render(s), encoding="utf-8")
        print(f"  wrote {out.name}")
    print(f"\u2713 Generated {len(STORIES)} articles for May 15, 2026.")


if __name__ == "__main__":
    main()
