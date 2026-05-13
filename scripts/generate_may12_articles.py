#!/usr/bin/env python3
"""
Generate 3 new article files covering May 12, 2026 — military-return / frozen-conflict turn.
Same template as generate_may11_articles.py.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"

STORIES = [
    {
        "slug": "trump-weighs-return-to-military-action-national-security-team-hormuz",
        "title_variants": [
            "Trump Weighs Return to Military Action; National Security Team Meeting on Hormuz",
            "Trump Considers Restart of Military Operations Against Iran",
            "U.S. Considers Restart of Commercial Vessel Escorts Through Strait of Hormuz",
            "National Security Team to Meet as Trump Weighs Iran Action",
            "Trump Mulls Project Freedom Restart as Hormuz Stalemate Deepens",
        ],
        "display_title_html": "Trump Weighs Return to Military Action; National Security Team Meeting on Hormuz",
        "seo_title": "Trump Weighs Return to Military Action; Vessel Escorts Eyed",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "May 12, 2026",
        "iso_date": "2026-05-12T15:00:00-04:00",
        "section": "Geopolitics",
        "read_time": "7 min",
        "meta_desc": "Reports Tuesday May 12 indicated President Trump is preparing to meet with his national security team to weigh a potential return to military operations against Iran, alongside renewed discussions about restarting commercial vessel escorts through the Strait of Hormuz.",
        "keywords": "Trump military action Iran, vessel escorts Hormuz, Project Freedom restart, US Iran stalemate, national security team Hormuz",
        "paragraphs": [
            "Reports Tuesday, May 12, 2026, indicated that President Trump is preparing to meet with his national security team to weigh a potential return to military operations against Iran, alongside renewed discussions about restarting commercial vessel escorts through the Strait of Hormuz. The escalation in posture follows Trump&rsquo;s Sunday rejection of Iran&rsquo;s counterproposal as &ldquo;TOTALLY UNACCEPTABLE&rdquo; and his Monday characterization of the ceasefire as &ldquo;on massive life support… 1% chance of living.&rdquo;",
            "A restart of vessel escorts would mark an explicit operational signal that the diplomatic track has run out. The original Project Freedom initiative, launched in early May, was paused on Tuesday May 5 to give space for the 14-point memorandum talks. The pause held until Friday, when U.S. forces disabled two Iranian tankers attempting to evade the blockade in what President Trump characterized as a &ldquo;love tap.&rdquo; Restarting full escorts would shift U.S. activity from enforcement on the margins back to scheduled convoy operations through the strait &mdash; a posture closer to active wartime operations than to a ceasefire.",
            "Markets read the signals clearly. WTI June futures advanced 4.2% Tuesday to settle at $102.18 per barrel; Brent July futures gained 3.4% to $107.77. Both benchmarks are now up more than 45% since the U.S.-Israeli war against Iran began February 28. Implied volatility climbed across the curve. Kalshi traders moved odds of WTI reaching $127 at some point in 2026 above 70%. Citi wrote in a note Tuesday: &ldquo;Oil prices have been volatile and can rise further if US-Iran dealmaking remains thorny.&rdquo;",
            "The military-posture review comes as Trump prepares to travel to Beijing later this week for talks with President Xi Jinping. According to Henry Wilkinson, chief intelligence officer at geopolitical risk firm Dragonfly, Trump may use the Xi meeting to press China to lean on Iran to accept U.S. terms. China has called repeatedly for the Strait of Hormuz to reopen given how much of its energy supply transits the waterway. A diplomatic breakthrough this week is unlikely, however, with the Trump-Xi summit serving more as a forcing function for the next phase of the negotiation than as a venue for an actual deal.",
            "Iran&rsquo;s position has hardened. Iranian state media continues to frame Tehran&rsquo;s counterproposal as a rejection of what it characterizes as a U.S. demand for &ldquo;surrender.&rdquo; Iranian Army spokesperson Brig. Gen. Mohammad Akraminia has warned of &ldquo;surprising options&rdquo; if adversaries made another &ldquo;miscalculation.&rdquo; The Iranian counter demanded a 30-day suspension of OFAC sanctions on Iranian oil sales and an end to the naval blockade &mdash; conditions the U.S. has consistently rejected as unacceptable preconditions to substantive nuclear concessions.",
            "Amos Hochstein, former senior energy advisor to President Biden, captured the mood on CNBC&rsquo;s &ldquo;Squawk Box&rdquo; Tuesday: &ldquo;We&rsquo;re in a stalemate, a frozen conflict. In the meantime, the straits are closed so we&rsquo;re in a no war, no oil, no straits condition.&rdquo; Hochstein said oil is likely to remain in a $90-100 range through the rest of 2026 and into 2027 even if Hormuz reopens in early June &mdash; an indication that even producers and former officials see no quick path back to pre-conflict normalcy.",
            "The combination of a hardening military posture and the looming Beijing summit creates a narrow window. If Trump&rsquo;s national security team converges on a recommendation to restart Project Freedom and authorize tighter enforcement before he departs for China, the market will price further escalation. If the team holds off pending the Xi meeting, the next 72 hours will be quieter, but the underlying stalemate persists. Either path produces structurally higher crude. For continuing coverage, see our <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a> and <a href=\"strait-of-hormuz-explained.html\" style=\"color:var(--blue);text-decoration:none\">Strait of Hormuz explainer</a>.",
        ],
        "related": [
            ("WTI Tops $102, Brent $108 as Hormuz Stalemate Deepens", "wti-tops-102-brent-108-as-hormuz-stalemate-deepens"),
            ("Hochstein: 'Frozen Conflict, No War, No Oil, No Straits'; Sees $90-100 Through 2027", "hochstein-frozen-conflict-no-war-no-oil-no-straits-90-100-through-2027"),
            ("Trump Heads to Beijing This Week; Set to Press Xi to Lean on Iran", "trump-heads-to-beijing-set-to-press-xi-to-lean-on-iran"),
        ],
    },
    {
        "slug": "wti-tops-102-brent-108-as-hormuz-stalemate-deepens",
        "title_variants": [
            "WTI Tops $102, Brent $108 as Hormuz Stalemate Deepens",
            "Oil Rally Extends: WTI Up 4.2%, Brent 3.4% on Tuesday",
            "Crude Up 45% Since Conflict Began Feb 28 as Hormuz Stays Closed",
            "WTI Settles $102.18, Brent $107.77 as Markets Price Frozen Conflict",
        ],
        "display_title_html": "WTI Tops $102, Brent $108 as Hormuz Stalemate Deepens",
        "seo_title": "WTI Tops $102, Brent $108 as Hormuz Stalemate Deepens",
        "category": "Oil Markets",
        "category_url": "../category/oil-prices.html",
        "date": "May 12, 2026",
        "iso_date": "2026-05-12T17:00:00-04:00",
        "section": "Oil Prices",
        "read_time": "5 min",
        "meta_desc": "WTI June futures advanced 4.2% Tuesday to settle at $102.18; Brent July futures gained 3.4% to $107.77. Both benchmarks are now up more than 45% since the U.S.-Israeli war against Iran began Feb 28. Citi sees prices rising further if dealmaking remains thorny.",
        "keywords": "WTI Brent price May 12, oil rally Hormuz stalemate, WTI $102, Brent $108, crude up 45 percent, Iran oil disruption",
        "paragraphs": [
            "Crude oil markets extended Monday&rsquo;s rally into Tuesday, May 12, 2026, as the Hormuz stalemate deepened with no signs of a diplomatic breakthrough. WTI June futures advanced 4.2% to settle at $102.18 per barrel; Brent July futures gained 3.4% to $107.77. WTI is now $3 higher than its Friday close of $95.42 and $13 above its May 5 intraday low of $88.71. Brent is $7 above its Friday close and $11 above its May 5 low of $96.77.",
            "Since the U.S.-Israeli war against Iran began February 28, both benchmarks are up more than 45%. The structural shift in pricing reflects the IEA&rsquo;s assessment that the conflict is removing roughly 14 million barrels per day from global supply &mdash; the largest supply shock on record. Saudi Aramco CEO Amin Nasser reinforced the framing Monday on an analyst call, warning that the oil market will take until 2027 to normalize if the Strait of Hormuz remains blocked beyond mid-June.",
            "Tuesday&rsquo;s rally was catalyzed by reports that President Trump is preparing to meet with his national security team to weigh a potential return to military operations against Iran, alongside renewed discussions about restarting commercial vessel escorts through Hormuz. Trump told reporters Monday the ceasefire is &ldquo;on massive life support&rdquo; and called Iran&rsquo;s counterproposal &ldquo;garbage.&rdquo; The combination of escalation rhetoric and the prospect of military posture changes drove the geopolitical risk premium back to roughly $25-30 per barrel by Citi&rsquo;s estimate.",
            "Wall Street&rsquo;s posture has firmed in tandem. Citi wrote in a note: &ldquo;Oil prices have been volatile and can rise further if US-Iran dealmaking remains thorny.&rdquo; Amos Hochstein, former senior energy advisor to President Biden, told CNBC&rsquo;s &ldquo;Squawk Box&rdquo; Tuesday that oil will likely remain in a $90-100 range through the rest of 2026 and into 2027 even if Hormuz reopens in early June. The forecast implies that any post-deal pullback would be limited, and crude could remain structurally above pre-conflict levels for 18-24 months.",
            "Refined products tracked crude higher. Gasoline RBOB jumped to $3.53 per gallon Tuesday from $3.42 Monday. ULSD diesel and heating oil rose to $4.25. Jet fuel climbed to $4.63. Crack spreads &mdash; the refiner margin over crude &mdash; remain near multi-year highs, supporting input demand even as headline prices rise. The strong product crack environment is helping insulate refiner margins and keeping refineries running flat-out, which in turn maintains crude demand and contributes to the tight supply picture.",
            "Implied volatility climbed across the curve. Near-dated WTI call options saw their largest daily implied-vol increase since early April. Kalshi traders moved odds of WTI reaching $127 at some point in 2026 above 70% &mdash; up from roughly 50% a week ago and 65% Monday. Prediction-market positioning reflects expectations that the conflict either escalates further or settles at structurally higher equilibrium prices, not a return to pre-conflict $60-70 WTI.",
            "AAA reported the U.S. national retail gasoline average at $4.504 per gallon Tuesday, down 1.6 cents from Monday. The brief retail pullback reflects multi-day pass-through lag from the May 5-9 crude crash. Tuesday&rsquo;s WTI rally back above $100 will reverse the retail easing within one to two weeks. California remains highest at $6.16; Hawaii $5.65. Diesel averages $6.18. For continuing coverage, see our <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">live oil prices dashboard</a>.",
        ],
        "related": [
            ("Trump Weighs Return to Military Action; National Security Team Meeting on Hormuz", "trump-weighs-return-to-military-action-national-security-team-hormuz"),
            ("Hochstein: 'Frozen Conflict, No War, No Oil, No Straits'; Sees $90-100 Through 2027", "hochstein-frozen-conflict-no-war-no-oil-no-straits-90-100-through-2027"),
            ("Aramco CEO: Hormuz Normalization Could Slip Into 2027 as 100M Barrels Lost Weekly", "aramco-ceo-hormuz-normalization-could-slip-into-2027"),
        ],
    },
    {
        "slug": "hochstein-frozen-conflict-no-war-no-oil-no-straits-90-100-through-2027",
        "title_variants": [
            "Hochstein: 'Frozen Conflict, No War, No Oil, No Straits'; Sees $90-100 Through 2027",
            "Hochstein Calls Hormuz a 'Frozen Conflict'; Forecasts $90-100 Oil",
            "Former Biden Energy Advisor: Oil Stays $90-100 Through 2027",
            "Hochstein: 'No War, No Oil, No Straits' as Stalemate Hardens",
        ],
        "display_title_html": "Hochstein: 'Frozen Conflict, No War, No Oil, No Straits'; Sees $90-100 Through 2027",
        "seo_title": "Hochstein: 'Frozen Conflict' Holds Oil at $90-100 Into 2027",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "May 12, 2026",
        "iso_date": "2026-05-12T11:00:00-04:00",
        "section": "Geopolitics",
        "read_time": "6 min",
        "meta_desc": "Amos Hochstein, former senior energy advisor to President Biden, told CNBC Tuesday: 'We're in a stalemate, a frozen conflict… no war, no oil, no straits.' He sees oil remaining in a $90-100 range through 2026 and into 2027 even if Hormuz reopens in early June.",
        "keywords": "Amos Hochstein frozen conflict, oil forecast 2027, Hormuz stalemate, no war no oil no straits, Biden energy advisor Iran",
        "paragraphs": [
            "Amos Hochstein, former senior energy advisor to President Biden, characterized the U.S.-Iran standoff Tuesday, May 12, 2026, as a &ldquo;frozen conflict&rdquo; that will keep oil prices elevated for the foreseeable future. Speaking on CNBC&rsquo;s &ldquo;Squawk Box,&rdquo; Hochstein said: &ldquo;We&rsquo;re in a stalemate, a frozen conflict. In the meantime, the straits are closed so we&rsquo;re in a no war, no oil, no straits condition.&rdquo;",
            "Hochstein&rsquo;s framing matters because it comes from a senior practitioner who handled Middle East energy diplomacy through the previous administration. His core forecast: oil prices will likely remain in a $90-100 per barrel range through the rest of 2026 and into 2027 even if the Strait of Hormuz reopens in early June. The implication is that even a successful diplomatic resolution would not produce a near-term return to pre-conflict pricing &mdash; the structural damage and supply chain reconfiguration are too significant.",
            "The &ldquo;no war, no oil, no straits&rdquo; formulation captures the paradox of the current moment. There is no active hot war between U.S. and Iranian forces. There are no significant oil flows from the Persian Gulf to global markets through the strait. There is no functioning shipping corridor. And yet there is also no formal escalation of hostilities and no formal closure of the strait by Iran &mdash; only practical impossibility for most commercial vessels. The conflict has settled into a steady-state disruption that markets must price as durable rather than transient.",
            "Hochstein expects no breakthrough this week. With Trump scheduled to head to Beijing for talks with President Xi Jinping, the U.S. diplomatic apparatus is focused on whether China can apply useful pressure on Tehran. Hochstein said the conflict is now better understood as a multi-party problem requiring Chinese, Pakistani, and Qatari mediation in addition to the bilateral U.S.-Iran channel. The structure of negotiations has therefore become more complex, not simpler, even as the underlying terms have not changed.",
            "The Hochstein framework aligns with Wall Street&rsquo;s firming bearish view of any near-term resolution. Saudi Aramco CEO Amin Nasser warned Monday that the oil market will take until 2027 to normalize if Hormuz remains blocked beyond mid-June. Citi has kept risks tilted to the upside on its base case. Goldman Sachs has held its Q4 2026 Brent forecast at $90. Barclays sees Brent at $100. The forecaster consensus has shifted to assume the conflict resolves over months rather than weeks, with limited near-term price relief.",
            "Felipe Elink Schuurman, CEO and co-founder of Sparta Commodities, told CNBC that the COVID-19 pandemic is a useful analogy for understanding what comes next. &ldquo;Now the question is where is that demand destruction going to come from? Unfortunately, it&rsquo;s going to be a situation where the richer countries are going to pay up. Maybe you don&rsquo;t see $200 on crude, but you will see that on a regular basis on products, which is what people consume.&rdquo; The implication is that wealthier importing economies will absorb the shock while poorer countries face humanitarian and economic pressure.",
            "For investors, the Hochstein and Schuurman frameworks together suggest a barbell strategy: long upstream crude producers benefiting from sustained $90-100 pricing, but caution on downstream refiners and consumer-facing energy users that will eventually face margin compression as input costs cement above pre-conflict levels for an extended period. The next data point worth watching is whether Trump&rsquo;s national security meeting this week produces a decision on restarting vessel escorts through Hormuz. For continuing coverage, see our <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a> and <a href=\"strait-of-hormuz-explained.html\" style=\"color:var(--blue);text-decoration:none\">Strait of Hormuz explainer</a>.",
        ],
        "related": [
            ("Trump Weighs Return to Military Action; National Security Team Meeting on Hormuz", "trump-weighs-return-to-military-action-national-security-team-hormuz"),
            ("WTI Tops $102, Brent $108 as Hormuz Stalemate Deepens", "wti-tops-102-brent-108-as-hormuz-stalemate-deepens"),
            ("Aramco CEO: Hormuz Normalization Could Slip Into 2027 as 100M Barrels Lost Weekly", "aramco-ceo-hormuz-normalization-could-slip-into-2027"),
        ],
    },
    {
        "slug": "trump-heads-to-beijing-set-to-press-xi-to-lean-on-iran",
        "title_variants": [
            "Trump Heads to Beijing This Week; Set to Press Xi to Lean on Iran",
            "Trump-Xi Summit This Week as Iran Stalemate Becomes Test of Influence",
            "Trump to Ask Xi to Press Tehran During Beijing Visit",
            "Dragonfly: Trump May Use Xi Meeting to Pressure Iran",
        ],
        "display_title_html": "Trump Heads to Beijing This Week; Set to Press Xi to Lean on Iran",
        "seo_title": "Trump Heads to Beijing; Set to Press Xi on Iran",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "May 12, 2026",
        "iso_date": "2026-05-12T13:00:00-04:00",
        "section": "Geopolitics",
        "read_time": "5 min",
        "meta_desc": "President Trump is scheduled to travel to Beijing later this week to meet with President Xi Jinping. Trump may ask Xi to press Iran to accept U.S. terms during their talks, according to Dragonfly's Henry Wilkinson. China has called repeatedly for the Strait of Hormuz to reopen.",
        "keywords": "Trump Beijing visit, Trump Xi meeting Iran, China pressure Tehran, Hormuz Xi diplomacy, Dragonfly Iran forecast",
        "paragraphs": [
            "President Donald Trump is scheduled to travel to Beijing later this week for talks with President Xi Jinping &mdash; a summit that has taken on substantially more significance with the U.S.-Iran standoff stuck in stalemate. According to Henry Wilkinson, chief intelligence officer at geopolitical risk firm Dragonfly, Trump may use the Xi meeting to press China to lean on Iran to accept U.S. terms. Wilkinson made the assessment on CNBC&rsquo;s &ldquo;Squawk Box Asia&rdquo; Tuesday.",
            "China&rsquo;s alignment matters because roughly half of all crude exiting the Persian Gulf in pre-conflict times was destined for Chinese refineries. The closure of the Strait of Hormuz has therefore hit China&rsquo;s energy supply harder than any other single country. Beijing has publicly called for the strait to reopen multiple times during the conflict. Iranian Foreign Minister Abbas Araghchi traveled to Beijing on May 5 as China continued to mediate, alongside Pakistan and Qatar, in parallel with the bilateral U.S.-Iran channel.",
            "The structure of the Trump-Xi meeting limits what can be agreed publicly. Trump cannot extract concessions from Iran through China alone &mdash; Tehran retains its own decision-making authority and is constrained by domestic politics that demand visible resistance to U.S. terms. What China can do is signal back-channel preferences to Tehran that affect Iranian calculations on timing and on which red lines are firm versus negotiable. That kind of pressure is invisible from outside but historically effective in similar standoffs.",
            "The summit is also a domestic test for Trump. Arriving in Beijing with the conflict unresolved &mdash; or with the U.S. publicly threatening renewed strikes after rejecting Iran&rsquo;s counterproposal Sunday &mdash; places Trump in a weaker negotiating posture than at any point in recent months. China negotiates from strength when its counterpart is constrained. The Iranian standoff has become a constraint that Beijing can exploit on adjacent issues including trade, Taiwan, and rare-earth supply chains.",
            "Markets are watching the summit timeline as a hard deadline. If Trump returns from Beijing with even a framework of Chinese pressure on Iran &mdash; quiet, off-the-record, but credible to U.S. and Iranian audiences &mdash; the panic premium could compress meaningfully. If Trump returns without anything substantive, markets are likely to price the stalemate as durable through the summer, with WTI in the $100-110 range and Brent $105-115 as the new normal. Crude futures Tuesday already reflected the latter scenario: WTI $102.18, Brent $107.77, both up more than 45% YTD.",
            "There is a parallel diplomatic risk if China publicly aligns with Iranian positions during the summit. Beijing has been careful throughout the conflict to maintain official neutrality while pressing privately for reopening. A public Chinese statement that explicitly endorses Iran&rsquo;s 30-day OFAC sanctions suspension demand or end-the-blockade demand would mark a meaningful diplomatic loss for the U.S. and would likely accelerate any Trump decision on restarting Project Freedom escorts through Hormuz.",
            "The most likely outcome from the summit, in Wilkinson&rsquo;s framing and that of other geopolitical analysts, is process commitments rather than substantive movement. Trump and Xi may agree on continued mediation, on shared interest in reopening Hormuz, and on bilateral talks at the foreign-minister level over the coming weeks. None of that would resolve the stalemate, but all of it would buy time and tamp down the most extreme escalation scenarios in the near term. For continuing coverage, see our <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a>.",
        ],
        "related": [
            ("Trump Weighs Return to Military Action; National Security Team Meeting on Hormuz", "trump-weighs-return-to-military-action-national-security-team-hormuz"),
            ("Hochstein: 'Frozen Conflict, No War, No Oil, No Straits'; Sees $90-100 Through 2027", "hochstein-frozen-conflict-no-war-no-oil-no-straits-90-100-through-2027"),
            ("WTI Tops $102, Brent $108 as Hormuz Stalemate Deepens", "wti-tops-102-brent-108-as-hormuz-stalemate-deepens"),
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
  <link rel="stylesheet" href="../css/styles.css?v=27">
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
  <script src="../js/data.js?v=27"></script>
  <script src="../js/article-slugs.js?v=27"></script>
  <script src="../js/main.js?v=27"></script>
</body>
</html>
'''


def main():
    for s in STORIES:
        out = ARTICLES_DIR / f"{s['slug']}.html"
        out.write_text(render(s), encoding="utf-8")
        print(f"  wrote {out.name}")
    print(f"\u2713 Generated {len(STORIES)} articles for May 12, 2026.")


if __name__ == "__main__":
    main()
