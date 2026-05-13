#!/usr/bin/env python3
"""Generate 3 article files covering May 13, 2026 — data-heavy day."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"

STORIES = [
    {
        "slug": "iea-global-oil-inventories-record-4m-bpd-pace-undersupply-through-october",
        "title_variants": [
            "IEA: Global Oil Inventories Drawing at Record 4M bpd Pace; Severe Undersupply Through October",
            "IEA Warns Record 4M bpd Inventory Draws; Undersupply Through October",
            "IEA Oil Market Report Flags Record Inventory Draws as Hormuz Stays Closed",
            "IEA: Severe Oil Undersupply Likely Through October Even If Conflict Ends",
        ],
        "display_title_html": "IEA: Global Oil Inventories Drawing at Record 4M bpd Pace; Severe Undersupply Through October",
        "seo_title": "IEA: Record 4M bpd Oil Draws; Undersupply Through October",
        "category": "Oil Markets",
        "category_url": "../category/oil-prices.html",
        "date": "May 13, 2026",
        "iso_date": "2026-05-13T10:00:00-04:00",
        "section": "Oil Markets",
        "read_time": "6 min",
        "meta_desc": "The IEA's Oil Market Report Wednesday warned that global oil inventories fell at a record pace of around 4 million bpd in March and April, and that the market could remain severely undersupplied through October even if the conflict ends sooner.",
        "keywords": "IEA Oil Market Report May 2026, global oil inventories 4M bpd, Hormuz undersupply, oil market report Asian refiners, Persian Gulf alternatives",
        "paragraphs": [
            "The International Energy Agency warned in its monthly Oil Market Report released Wednesday, May 13, 2026, that global observed oil inventories fell at a record pace of around 4 million barrels per day in March and April &mdash; the steepest sustained draw in the agency&rsquo;s tracking history. The IEA said in the report that with inventories already drawing sharply, further volatility is likely ahead of the peak summer demand season, and the market could remain severely undersupplied until October even if the conflict ends sooner.",
            "The 4 million barrel per day inventory draw rate is structurally important. Roughly 9 to 10 million barrels per day of crude that would normally transit the Strait of Hormuz are not reaching global markets. With production cuts among Persian Gulf producers compounding the disruption, even substantial draws from commercial and strategic stocks have failed to bridge the supply gap. Cushing stocks remain below the five-year average; OECD commercial inventories have fallen for nine consecutive months.",
            "The IEA&rsquo;s warning about persistence is the most consequential element. By framing undersupply as &ldquo;severe&rdquo; through October even in a fast-resolution scenario, the agency is implicitly forecasting that the structural damage from the conflict will outlast the political settlement by months. Refinery turnaround scheduling, sourcing relationships, and trade flows are reconfiguring around the new reality faster than they could revert if a deal were reached tomorrow.",
            "Asian refiners are leading the sourcing pivot. Reports Wednesday confirmed that Japanese, South Korean, and increasingly Chinese refiners are actively seeking alternatives to Persian Gulf crude &mdash; turning to West African grades, Latin American heavy sour streams, and U.S. WTI for replacement barrels. The shift is not just a temporary substitution: long-term contracts with Persian Gulf producers are being renegotiated or paused, and refiner-level configuration shifts to handle different crude slates take months once initiated.",
            "The IEA also flagged the macro pass-through visible in April U.S. CPI data, which accelerated more than anticipated as surging energy prices linked to the Middle East crisis added meaningfully to price pressures. The report suggested that prolonged elevated crude prices through the summer would test central bank tolerance: Fed easing expectations could shift if the inflation pass-through proves persistent rather than transient.",
            "Market reaction Wednesday was measured. WTI June futures slipped 0.3% to $101.85; Brent July futures eased 0.7% to $107.05 after a 7.6% three-day rally. The pullback suggests traders are now pricing the IEA framework as their base case rather than treating it as a downside scenario. Citi maintained its assessment that prices can rise further if dealmaking remains thorny. Kalshi prediction-market odds of WTI reaching $127 in 2026 held above 70%.",
            "The next data point worth watching is the EIA&rsquo;s Weekly Petroleum Status Report due later Wednesday, which has confirmed a 4.3 million barrel crude draw &mdash; nearly double consensus expectations. The combined IEA + EIA data drop tightens the supply-side narrative materially. For continuing coverage, see our <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">live oil prices dashboard</a> and <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics page</a>.",
        ],
        "related": [
            ("EIA Crude Stocks Drop 4.3M Barrels — Nearly Double Expectations", "eia-crude-stocks-drop-4-3-million-barrels-nearly-double-expectations"),
            ("UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity"),
            ("Iranian Oil Export Shipments Stall — First Sustained Interruption Since Conflict Began", "iranian-oil-export-shipments-stall-first-sustained-interruption"),
        ],
    },
    {
        "slug": "eia-crude-stocks-drop-4-3-million-barrels-nearly-double-expectations",
        "title_variants": [
            "EIA Crude Stocks Drop 4.3M Barrels — Nearly Double Expectations",
            "EIA: U.S. Crude Inventories Fall 4.3M Barrels; Distillates Up First Time Since March",
            "Weekly Petroleum Status Report: Crude -4.3M, Distillate +190K",
            "U.S. Crude Inventories Fall Sharply on EIA Wednesday Report",
        ],
        "display_title_html": "EIA Crude Stocks Drop 4.3M Barrels — Nearly Double Expectations",
        "seo_title": "EIA Crude Stocks -4.3M Barrels; Nearly Double Expectations",
        "category": "Oil Markets",
        "category_url": "../category/oil-prices.html",
        "date": "May 13, 2026",
        "iso_date": "2026-05-13T11:00:00-04:00",
        "section": "Oil Markets",
        "read_time": "5 min",
        "meta_desc": "EIA's Weekly Petroleum Status Report Wednesday showed U.S. commercial crude oil inventories fell 4.3 million barrels last week — nearly double the 2.2 million expected. Distillate stocks rose 190,000 barrels, the first increase since March.",
        "keywords": "EIA crude inventory May 13, weekly petroleum status report, crude oil draw 4.3 million, distillate inventory March, U.S. oil stocks decline",
        "paragraphs": [
            "U.S. commercial crude oil inventories fell by 4.3 million barrels for the week ending May 8, 2026, according to the Energy Information Administration&rsquo;s Weekly Petroleum Status Report released Wednesday, May 13. The draw was nearly double the consensus expectation of a 2.2 million barrel decline and confirms the IEA&rsquo;s broader assessment Wednesday that global oil markets are severely undersupplied.",
            "The data set was bullish across most line items. Total U.S. commercial crude inventories now sit roughly 23 million barrels below the five-year seasonal average. Cushing stocks fell 1.1 million barrels to their lowest level since November 2024. U.S. crude oil imports averaged 6.2 million barrels per day, down 340,000 bpd from the prior week as Persian Gulf-origin cargoes continued to be redirected or delayed.",
            "Distillate inventories rose by 190,000 barrels &mdash; the first weekly increase since March 6 &mdash; easing some refined product supply concerns. The build reflects gradually rising refinery throughput as spring maintenance season winds down. Refinery utilization climbed to 89.4%, up from 87.2% the prior week, supporting product output even as input crude costs sit at multi-year highs.",
            "Gasoline inventories continued their multi-week decline, falling 1.8 million barrels. The 12-week consecutive draw streak is the longest sustained gasoline destocking pattern since 2022. Summer driving season demand combined with the May 1 transition to summer-grade fuel is depleting tank levels faster than refiners can replenish them. Implied gasoline demand averaged 9.4 million bpd, the highest since Labor Day weekend.",
            "Crude oil exports surged to 4.7 million barrels per day, near a record high, as global buyers continued to bid aggressively for U.S. barrels to backfill Persian Gulf shortfalls. Strategic Petroleum Reserve stocks held steady at 402.1 million barrels, reflecting administration restraint on releases despite the elevated price environment. The reserve has not been drawn on since the conflict began in late February.",
            "Market reaction was modest. WTI June futures held near $101.85 in the immediate aftermath; Brent July eased to $107.05. The data was directionally bullish but largely confirmed what the IEA Oil Market Report had already framed Wednesday morning. Citi and Goldman analysts maintained their existing forecasts. The combined IEA + EIA data drop reinforces the supply-side narrative but does not, by itself, alter the resolution timeline for the conflict.",
            "The next EIA inventory report is scheduled for Wednesday May 20. Goldman Sachs analysts suggested that if distillate stocks fail to maintain the modest build trajectory through the summer, refined product cracks could widen further from already multi-year-high levels. For continuing coverage, see our <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">live oil prices dashboard</a>.",
        ],
        "related": [
            ("IEA: Global Oil Inventories Drawing at Record 4M bpd Pace; Severe Undersupply Through October", "iea-global-oil-inventories-record-4m-bpd-pace-undersupply-through-october"),
            ("UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity"),
            ("WTI Tops $102, Brent $108 as Hormuz Stalemate Deepens", "wti-tops-102-brent-108-as-hormuz-stalemate-deepens"),
        ],
    },
    {
        "slug": "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity",
        "title_variants": [
            "UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast",
            "UAE Leaves OPEC May 1; Spare Capacity Forecast Reduced",
            "OPEC Loses UAE: 2027 Spare Capacity Now 2.5M bpd vs 3.8M Prior",
            "EIA May STEO Incorporates UAE Departure From OPEC",
        ],
        "display_title_html": "UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast",
        "seo_title": "UAE Departs OPEC May 1; EIA Cuts 2027 Spare Capacity",
        "category": "Oil Markets",
        "category_url": "../category/oil-prices.html",
        "date": "May 13, 2026",
        "iso_date": "2026-05-13T13:00:00-04:00",
        "section": "Oil Markets",
        "read_time": "6 min",
        "meta_desc": "The EIA's May Short-Term Energy Outlook released Tuesday incorporates the UAE's departure from OPEC, effective May 1, 2026. EIA now expects OPEC's 2027 spare capacity to average 2.5 million bpd, down from a 3.8 million prior forecast.",
        "keywords": "UAE leaves OPEC May 2026, EIA STEO May 2026, OPEC spare capacity 2027, UAE departure OPEC announcement, OPEC structure",
        "paragraphs": [
            "The Energy Information Administration&rsquo;s May Short-Term Energy Outlook, released Tuesday, May 12, 2026, formally incorporates the UAE&rsquo;s departure from OPEC, effective May 1, 2026. OPEC production numbers in the outlook now exclude data from the UAE, both for historical and forecast periods. The structural shift is one of the most consequential changes to OPEC&rsquo;s composition since Ecuador&rsquo;s 2020 departure and arguably more important: the UAE accounted for roughly 11% of OPEC production and was the second-largest holder of spare capacity within the group.",
            "The mechanical impact on spare capacity is meaningful. Because the UAE held substantial spare crude oil production capacity, the EIA now expects OPEC&rsquo;s spare capacity to average 2.5 million barrels per day in 2027, compared with a previous forecast of 3.8 million bpd. The 1.3 million bpd downward revision is roughly equivalent to two years of typical OPEC production growth. The reduced buffer matters most for OPEC&rsquo;s ability to respond to future supply disruptions or demand spikes.",
            "The UAE&rsquo;s departure has been telegraphed for more than a year. Disputes with the OPEC+ secretariat over baseline production quotas escalated in late 2024 as the UAE sought recognition for its post-2020 capacity expansion to roughly 4.85 million bpd. The current Hormuz crisis has accelerated the formal split: with the UAE already operating its ADCOP bypass pipeline at full capacity to compensate for Hormuz disruption, the constraint of OPEC quota discipline has become harder to justify to domestic stakeholders.",
            "The geographic implications are significant. The UAE remains a member of the Organization of Arab Petroleum Exporting Countries (OAPEC) and continues to coordinate informally with Saudi Arabia, the de facto OPEC leader. The Gulf Cooperation Council mechanism remains intact. Bilateral Saudi-Emirati production coordination is likely to continue, but the public, multilateral forcing function of OPEC quotas no longer applies to UAE output.",
            "For prices, the UAE departure removes a stabilizing buffer that previously dampened both upside and downside moves. With the global market already stretched by the Hormuz disruption, less spare capacity means less ability to respond to additional shocks. Citi analysts noted in a Wednesday client note that the reduced spare capacity is one of the structural reasons their upside risk distribution skews further from the base case. Goldman Sachs flagged spare capacity reduction as a key reason for elevated tail risk through 2027.",
            "OPEC itself has remained quiet on the departure publicly. The May ministerial meeting, scheduled for mid-month, is now functionally the first to operate under the new composition. Saudi Arabia&rsquo;s Energy Minister Abdulaziz bin Salman has emphasized the group&rsquo;s remaining cohesion among the 11 continuing members. The structural concern is whether other producers &mdash; particularly Kuwait or Iraq under different economic pressures &mdash; might follow over the next 12 to 24 months.",
            "For market participants, the UAE departure is primarily a long-term structural story rather than a near-term price catalyst. The price-relevant data continues to be the IEA Oil Market Report and EIA Weekly Petroleum Status Report, both released Wednesday and both confirming severe near-term undersupply. For continuing coverage, see our <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">live oil prices dashboard</a> and <a href=\"what-is-opec-plus-how-it-affects-oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">OPEC+ explainer</a>.",
        ],
        "related": [
            ("IEA: Global Oil Inventories Drawing at Record 4M bpd Pace; Severe Undersupply Through October", "iea-global-oil-inventories-record-4m-bpd-pace-undersupply-through-october"),
            ("EIA Crude Stocks Drop 4.3M Barrels — Nearly Double Expectations", "eia-crude-stocks-drop-4-3-million-barrels-nearly-double-expectations"),
            ("Aramco CEO: Hormuz Normalization Could Slip Into 2027 as 100M Barrels Lost Weekly", "aramco-ceo-hormuz-normalization-could-slip-into-2027"),
        ],
    },
    {
        "slug": "iranian-oil-export-shipments-stall-first-sustained-interruption",
        "title_variants": [
            "Iranian Oil Export Shipments Stall — First Sustained Interruption Since Conflict Began",
            "Iranian Crude Exports Halt for First Sustained Period Since Feb 28",
            "Iran Export Shipments Stall as Trump Heads to Beijing",
        ],
        "display_title_html": "Iranian Oil Export Shipments Stall — First Sustained Interruption Since Conflict Began",
        "seo_title": "Iranian Oil Exports Stall — First Sustained Interruption",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "May 13, 2026",
        "iso_date": "2026-05-13T15:00:00-04:00",
        "section": "Geopolitics",
        "read_time": "5 min",
        "meta_desc": "Reports Wednesday indicated Iranian oil export shipments have recently stalled, marking the first sustained interruption since the conflict started February 28. Iranian crude had been one of the few continuing supply paths from the Persian Gulf.",
        "keywords": "Iran oil exports stall, Iranian crude shipments halt, US Iran interdiction May 2026, Iran sanctions tankers, Persian Gulf supply",
        "paragraphs": [
            "Reports Wednesday, May 13, 2026, indicated Iranian oil export shipments have recently stalled, marking the first sustained interruption since the conflict between the United States, Israel, and Iran began on February 28. The development matters because Iranian crude has been one of the few continuing supply paths from the Persian Gulf despite the broader Hormuz disruption. With Iranian flows now interrupted, the supply picture from the region is materially tighter than it was a week ago.",
            "The cause of the stall is unclear but multiple potential drivers are at play. U.S. Navy interdiction activity has intensified following the May 9 incident in which U.S. forces disabled two Iranian tankers attempting to evade the broader blockade. President Trump characterized that incident as a &ldquo;love tap.&rdquo; A more aggressive interdiction posture combined with Iranian operational disruption from sanctions tightening and shipping insurance pullback could collectively be cutting off the export channel.",
            "Iranian crude has flowed primarily to China throughout the conflict, with Chinese teapot refiners using ship-to-ship transfers in the Strait of Malacca to receive cargoes that started under Iranian flag and ended under Indonesian or Marshall Islands papers. The volumes were estimated at roughly 1.4 million barrels per day before the recent disruption &mdash; a meaningful contribution to global supply at the margin even though it was not visible in official OPEC production data.",
            "President Trump told reporters Wednesday that the situation remains under control, downplaying concerns about the Iranian export stall ahead of his Beijing summit with Xi Jinping later this week. Trump indicated that trade negotiations would take precedence over Iran-related developments during the talks &mdash; a framing that suggests the administration views the Iran file as separable from the U.S.-China relationship rather than as leverage to apply through Beijing.",
            "The market implications are bullish but bounded. With Iranian flows already at risk and now interrupted, the upside risk to crude prices is more about pace than direction. WTI eased 0.3% Wednesday to $101.85 and Brent fell 0.7% to $107.05 in muted trading, as markets had already largely priced both the IEA undersupply assessment and the assumption that Iranian flows would eventually be curtailed under sustained sanctions enforcement.",
            "Iran has options to respond. The Iranian Army spokesperson&rsquo;s prior warnings about &ldquo;surprising options&rdquo; in the event of further escalation remain on the table. Asymmetric responses including additional drone attacks against Gulf infrastructure, a maritime kinetic event in the Strait of Hormuz, or a cyber action against U.S. or Israeli targets are within the range of plausible Iranian moves if the export interruption persists. The next 7 to 10 days are likely to be the critical window.",
            "For continuing coverage, see our <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a>, the <a href=\"trump-heads-to-beijing-set-to-press-xi-to-lean-on-iran.html\" style=\"color:var(--blue);text-decoration:none\">Trump-Xi summit preview</a>, and the <a href=\"strait-of-hormuz-explained.html\" style=\"color:var(--blue);text-decoration:none\">Strait of Hormuz explainer</a>.",
        ],
        "related": [
            ("IEA: Global Oil Inventories Drawing at Record 4M bpd Pace; Severe Undersupply Through October", "iea-global-oil-inventories-record-4m-bpd-pace-undersupply-through-october"),
            ("Trump Heads to Beijing This Week; Set to Press Xi to Lean on Iran", "trump-heads-to-beijing-set-to-press-xi-to-lean-on-iran"),
            ("Trump Weighs Return to Military Action; National Security Team Meeting on Hormuz", "trump-weighs-return-to-military-action-national-security-team-hormuz"),
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
  <link rel="stylesheet" href="../css/styles.css?v=28">
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
  <script src="../js/data.js?v=28"></script>
  <script src="../js/article-slugs.js?v=28"></script>
  <script src="../js/main.js?v=28"></script>
</body>
</html>
'''


def main():
    for s in STORIES:
        out = ARTICLES_DIR / f"{s['slug']}.html"
        out.write_text(render(s), encoding="utf-8")
        print(f"  wrote {out.name}")
    print(f"\u2713 Generated {len(STORIES)} articles for May 13, 2026.")


if __name__ == "__main__":
    main()
