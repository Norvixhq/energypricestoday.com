#!/usr/bin/env python3
"""
Generate country and topic hub pages for previously-phantom slugs that
Google was crawling and 404-ing on. Each hub page:
  - Lists every article that meaningfully mentions the country/topic
  - Has its own narrative intro tied to current oil-market relevance
  - Links to live data dashboards (oil prices, geopolitics, etc.)
  - Has full SEO meta tags + NewsArticle CollectionPage schema

This converts wasted Google crawl budget into actual SEO assets.
"""
import re
from pathlib import Path
from datetime import datetime, timezone, timedelta

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"

# Country/topic hubs with intro context and search terms
HUBS = {
    'iran': {
        'title': 'Iran Energy News &amp; Analysis',
        'h1': 'Iran &mdash; Oil, Sanctions & Geopolitics',
        'desc': 'Iran energy news: Strait of Hormuz blockade, U.S. sanctions, IRGC, nuclear program, and how Iran-related events move oil prices. Updated coverage from EnergyPricesToday.',
        'lead': 'Iran is one of the largest oil producers in the world and sits on the Strait of Hormuz &mdash; the chokepoint that moves roughly 20% of global seaborne oil. U.S.-Iran tensions, the active naval blockade, and the diplomatic standoff are the dominant force in oil markets today. This page collects every Iran-related article on EnergyPricesToday, with the most recent at top.',
        'context': 'Current state (April 28, 2026): Iran formally proposed Apr 27 a deal to reopen the Strait of Hormuz if the U.S. lifts its naval blockade and ends military operations &mdash; with nuclear talks deferred. Trump and his security team are reportedly skeptical. WTI rallied to $99.93 and Brent to $111.26 Tuesday on the proposal\'s uncertainty.',
        'terms': ['Iran', 'Iranian', 'Tehran', 'Hormuz', 'IRGC', 'Araghchi', 'Pezeshkian'],
        'keywords': 'Iran oil, Iran sanctions, Strait of Hormuz, Iranian crude exports, IRGC, U.S.-Iran conflict, Iran nuclear program, Iranian oil production',
    },
    'iraq': {
        'title': 'Iraq Energy News &amp; Analysis',
        'h1': 'Iraq &mdash; OPEC Production, Basrah Crude, Pipeline Disputes',
        'desc': 'Iraq energy news: OPEC+ compliance, Basrah Medium and Light crude grades, pipeline disputes with Kurdistan, and Iraqi oil exports.',
        'lead': 'Iraq is OPEC\'s second-largest producer, exporting roughly 3.4 million barrels per day primarily through southern Basrah ports and a smaller volume from Kurdistan via the Ceyhan pipeline. Iraq routinely struggles with OPEC+ quota compliance and has been a focal point in the cartel\'s production discipline disputes.',
        'context': 'Iraqi production has averaged above its OPEC+ quota for most of 2026, with the cartel pressuring Baghdad to compensate via deeper future cuts. Basrah Medium currently trades at a steep discount to Brent due to quality differentials and shipping risk through the Persian Gulf.',
        'terms': ['Iraq', 'Iraqi', 'Baghdad', 'Basrah'],
        'keywords': 'Iraq oil, Iraqi crude, Basrah Medium, OPEC compliance, Iraqi production, Kurdistan oil',
    },
    'saudi-arabia': {
        'title': 'Saudi Arabia Energy News &amp; Analysis',
        'h1': 'Saudi Arabia &mdash; Aramco, OPEC+, East-West Pipeline',
        'desc': 'Saudi Arabia energy news: Saudi Aramco, OPEC+ leadership, the East-West Pipeline as Hormuz bypass, and Riyadh\'s spare capacity decisions.',
        'lead': 'Saudi Arabia is the world\'s largest oil exporter and OPEC+ swing producer. With ~3 million barrels per day of spare capacity and the East-West Pipeline that bypasses the Strait of Hormuz, Saudi decisions are the single biggest variable in global oil supply.',
        'context': 'During the current Hormuz crisis, the East-West Pipeline (5M bpd capacity from eastern fields to the Red Sea port of Yanbu) is operating at full capacity and represents the only meaningful alternative to Persian Gulf shipping. Aramco has held output steady within OPEC+ guidelines despite elevated prices.',
        'terms': ['Saudi Arabia', 'Saudi', 'Riyadh', 'Aramco', 'East-West Pipeline'],
        'keywords': 'Saudi Arabia oil, Saudi Aramco, OPEC+ leadership, East-West Pipeline, Saudi spare capacity',
    },
    'russia': {
        'title': 'Russia Energy News &amp; Analysis',
        'h1': 'Russia &mdash; Urals Crude, Sanctions, Asian Pivot',
        'desc': 'Russia energy news: Urals crude, sanctions impact, redirected exports to India and China, Druzhba pipeline, and Russian energy in the post-Ukraine landscape.',
        'lead': 'Russia is the world\'s second-largest oil exporter and the largest natural gas exporter. Since 2022, sanctions have restructured Russian energy flows: crude oil redirected to Asia at discounted prices, while Europe pivoted away from Russian pipeline gas.',
        'context': 'Urals crude trades at a substantial discount to Brent, with Indian and Chinese refiners absorbing most of the displaced volume. The Druzhba pipeline serves Hungary and Slovakia under sanctions exemptions. Recent ceasefire negotiations have raised the prospect of partial sanctions relief.',
        'terms': ['Russia', 'Russian', 'Moscow', 'Putin', 'Urals', 'Druzhba'],
        'keywords': 'Russia oil, Russian crude, Urals discount, Druzhba pipeline, Russia sanctions, Russian gas exports',
    },
    'mexico': {
        'title': 'Mexico Energy News &amp; Analysis',
        'h1': 'Mexico &mdash; Pemex, Gulf of Mexico, Maya Crude',
        'desc': 'Mexico energy news: Pemex production, Gulf of Mexico drilling, Maya heavy crude exports, and U.S.-Mexico cross-border energy trade.',
        'lead': 'Mexico produces roughly 1.6 million barrels per day, dominated by state-owned Pemex. Maya crude (heavy, sour) is a key feedstock for U.S. Gulf Coast refineries configured for heavy grades. Cross-border energy trade with the U.S. is significant in both directions.',
        'context': 'Mexican production has stabilized after years of decline, with offshore Gulf of Mexico fields offsetting maturing onshore fields. Pemex\'s financial position remains strained but production discipline has improved.',
        'terms': ['Mexico', 'Mexican', 'Pemex'],
        'keywords': 'Mexico oil, Pemex, Maya crude, Gulf of Mexico drilling, Mexican oil exports',
    },
    'canada': {
        'title': 'Canada Energy News &amp; Analysis',
        'h1': 'Canada &mdash; Oil Sands, WCS, Trans Mountain',
        'desc': 'Canada energy news: Western Canadian Select, oil sands production, Trans Mountain Expansion pipeline, and Canada-U.S. energy trade.',
        'lead': 'Canada is the world\'s fourth-largest oil producer and largest exporter to the United States. Western Canadian Select (WCS) heavy crude trades at a discount to WTI reflecting transportation constraints and quality differentials. The Trans Mountain Expansion pipeline opened export capacity to the Pacific Coast in 2024.',
        'context': 'WCS-WTI differentials have narrowed since Trans Mountain came online, but remain elevated during U.S. refinery turnaround season. Canadian oil sands production continues to grow modestly despite policy headwinds. Spring breakup typically reduces rig counts seasonally.',
        'terms': ['Canada', 'Canadian', 'WCS', 'Western Canadian Select', 'Trans Mountain', 'Alberta'],
        'keywords': 'Canada oil, Western Canadian Select, WCS discount, Trans Mountain pipeline, oil sands, Canadian rig count',
    },
    'uae': {
        'title': 'UAE Energy News &amp; Analysis',
        'h1': 'UAE &mdash; ADNOC, Murban Crude, Dubai Benchmark',
        'desc': 'UAE energy news: ADNOC production, Murban and Dubai crude benchmarks, Fujairah port operations, and Emirates energy strategy.',
        'lead': 'The United Arab Emirates produces roughly 3 million barrels per day, primarily through ADNOC. Murban crude and Dubai crude are key Asian benchmarks. Fujairah, on the eastern coast outside the Strait of Hormuz, provides a critical export bypass during Gulf disruptions.',
        'context': 'During the current Hormuz crisis, ADNOC has maximized exports through Fujairah to bypass the strait. Murban has rallied alongside global benchmarks, settling near $112 on April 28.',
        'terms': ['UAE', 'United Arab Emirates', 'Abu Dhabi', 'Dubai Crude', 'Murban', 'ADNOC'],
        'keywords': 'UAE oil, ADNOC, Murban crude, Dubai crude benchmark, Fujairah, UAE production',
    },
    'brazil': {
        'title': 'Brazil Energy News &amp; Analysis',
        'h1': 'Brazil &mdash; Petrobras, Pre-Salt, Offshore Production',
        'desc': 'Brazil energy news: Petrobras production, pre-salt offshore fields, FPSO deployments, and Brazilian crude exports to Asia.',
        'lead': 'Brazil produces roughly 4 million barrels per day, with growth driven by deepwater pre-salt fields off the coast of Rio de Janeiro. Petrobras dominates production but multiple international operators have major stakes in pre-salt blocks.',
        'context': 'Pre-salt output has scaled rapidly as new FPSO (Floating Production, Storage and Offloading) units come online. Brazilian crude is increasingly directed to Asian refiners as China expands its Latin American supply diversity.',
        'terms': ['Brazil', 'Brazilian', 'Petrobras'],
        'keywords': 'Brazil oil, Petrobras, pre-salt production, FPSO deployments, Brazilian crude exports',
    },
    'nigeria': {
        'title': 'Nigeria Energy News &amp; Analysis',
        'h1': 'Nigeria &mdash; Bonny Light, Pipeline Security, OPEC',
        'desc': 'Nigeria energy news: Bonny Light crude, pipeline security improvements, NNPC production, and Nigerian OPEC quota compliance.',
        'lead': 'Nigeria is sub-Saharan Africa\'s largest oil producer, with output historically constrained by pipeline theft and security incidents. Bonny Light is a premium light sweet grade favored by European refiners.',
        'context': 'Pipeline security has improved materially under recent government programs, with sabotage-related production losses down sharply from prior years. Nigerian production remains below OPEC+ quota due to underinvestment rather than the disruptions of past years.',
        'terms': ['Nigeria', 'Nigerian', 'Bonny Light'],
        'keywords': 'Nigeria oil, Bonny Light crude, NNPC, Nigerian production, pipeline security',
    },
    'kazakhstan': {
        'title': 'Kazakhstan Energy News &amp; Analysis',
        'h1': 'Kazakhstan &mdash; CPC Blend, Tengiz, OPEC+',
        'desc': 'Kazakhstan energy news: CPC Blend exports, Tengiz field, the Caspian Pipeline Consortium, and Kazakh OPEC+ production.',
        'lead': 'Kazakhstan produces roughly 1.7 million barrels per day, dominated by the giant Tengiz, Kashagan, and Karachaganak fields. CPC Blend, exported through the Caspian Pipeline Consortium to the Black Sea port of Novorossiysk, is the country\'s primary export grade.',
        'context': 'Kazakhstan has consistently produced above its OPEC+ quota, drawing pressure from the cartel for compensation cuts. CPC pipeline operations face periodic disruption risk from regional conflicts and weather at the Black Sea terminal.',
        'terms': ['Kazakhstan', 'Kazakh', 'CPC Blend', 'Tengiz'],
        'keywords': 'Kazakhstan oil, CPC Blend, Tengiz, Caspian Pipeline, Kazakh OPEC compliance',
    },
    'qatar': {
        'title': 'Qatar Energy News &amp; Analysis',
        'h1': 'Qatar &mdash; LNG, North Field Expansion',
        'desc': 'Qatar energy news: QatarEnergy LNG exports, North Field expansion, Asian premium pricing, and Qatari LNG\'s Hormuz routing dependency.',
        'lead': 'Qatar is one of the world\'s largest LNG exporters, with the North Field development driving capacity expansion. Qatari LNG cargoes ship primarily to Asian buyers via the Strait of Hormuz, making the country highly exposed to Persian Gulf disruption.',
        'context': 'During the current Hormuz crisis, Qatari LNG flows have been intermittently disrupted, driving JKM and Dutch TTF gas prices higher as European and Asian buyers compete for U.S. cargoes to fill the gap.',
        'terms': ['Qatar', 'Qatari'],
        'keywords': 'Qatar LNG, QatarEnergy, North Field expansion, JKM premium, Qatari gas exports',
    },
    'venezuela': {
        'title': 'Venezuela Energy News &amp; Analysis',
        'h1': 'Venezuela &mdash; PDVSA, Sanctions, Heavy Crude',
        'desc': 'Venezuela energy news: PDVSA production, U.S. sanctions, heavy crude exports, and Venezuelan oil\'s constrained recovery.',
        'lead': 'Venezuela holds the world\'s largest proven oil reserves but produces only ~800,000 barrels per day &mdash; well below the 2015 peak of 2.5 million bpd. Years of underinvestment, sanctions, and political instability have eroded production capacity.',
        'context': 'Venezuelan production remains capped by U.S. sanctions and the country\'s limited ability to attract foreign investment. Some specific licenses (Chevron, Repsol) allow narrow operations. Heavy crude remains a niche feedstock for U.S. Gulf Coast refineries.',
        'terms': ['Venezuela', 'Venezuelan', 'PDVSA'],
        'keywords': 'Venezuela oil, PDVSA, Venezuela sanctions, heavy crude, Venezuelan production decline',
    },
    'opec-members': {
        'title': 'OPEC Members &mdash; Production, Quotas, Compliance',
        'h1': 'OPEC+ Member Countries',
        'desc': 'Complete coverage of OPEC and OPEC+ members: production levels, quota compliance, output policies, ministerial meetings, and how OPEC+ decisions shape global oil prices.',
        'lead': 'OPEC+ is a 23-nation alliance led by Saudi Arabia and Russia that controls roughly 40% of global oil production. Their coordinated output decisions &mdash; whether to cut, hold, or increase production &mdash; directly set the floor for global oil prices.',
        'context': 'OPEC+ is currently proceeding with a 206,000 bpd April output increase despite the Hormuz crisis. No emergency JMMC meeting has been called. The cartel is broadly accepting current price levels while preserving Saudi spare capacity.',
        'terms': ['OPEC', 'OPEC+'],
        'keywords': 'OPEC members, OPEC+ countries, OPEC quotas, OPEC compliance, OPEC ministerial meetings, oil supply',
    },
    'suez-canal': {
        'title': 'Suez Canal Energy News &amp; Analysis',
        'h1': 'Suez Canal &mdash; Oil Trade, Bab el-Mandeb, Houthi Risk',
        'desc': 'Suez Canal energy news: oil and LNG transit volumes, Red Sea / Bab el-Mandeb security, Houthi attacks, and shipping route diversions around the Cape of Good Hope.',
        'lead': 'The Suez Canal handles approximately 12% of global trade and ~5.5 million barrels per day of oil equivalents, connecting the Red Sea to the Mediterranean. Combined with the Bab el-Mandeb strait at the Red Sea\'s southern end, the corridor is one of the world\'s most critical energy chokepoints.',
        'context': 'Houthi attacks in the southern Red Sea have diverted most commercial shipping around the Cape of Good Hope, adding 10-14 days per voyage and reducing effective Suez transit. Energy cargoes face the same disruption.',
        'terms': ['Suez Canal', 'Suez', 'Bab el-Mandeb'],
        'keywords': 'Suez Canal oil transit, Bab el-Mandeb, Red Sea shipping, Houthi attacks, Cape of Good Hope rerouting',
    },
}


def get_canonical_section(slug):
    if slug in ['iran', 'iraq', 'saudi-arabia', 'russia', 'venezuela', 'qatar', 'suez-canal']: return 'Geopolitics'
    if slug == 'opec-members': return 'OPEC'
    return 'Energy'


def collect_articles_for_hub(hub_slug, hub_def):
    """Find articles that mention the hub's terms enough to be relevant."""
    terms = hub_def['terms']
    candidates = []
    for f in ARTICLES_DIR.glob('*.html'):
        if f.stem == hub_slug: continue  # skip self
        txt = f.read_text(encoding='utf-8', errors='ignore')

        # Get title
        title_m = re.search(r'<title>([^<]+)</title>', txt)
        title = (title_m.group(1) if title_m else f.stem).split(' | ')[0].split(' — EnergyPricesToday')[0].strip()

        # Get description
        desc_m = re.search(r'<meta name="description" content="([^"]+)"', txt)
        excerpt = desc_m.group(1)[:220] + '…' if desc_m else ''

        # Get publish date
        pub_m = re.search(r'article:published_time"\s+content="(\d{4}-\d{2}-\d{2})', txt)
        pub_date = pub_m.group(1) if pub_m else '2026-04-01'

        # Score: how many term mentions in body
        body = re.sub(r'<[^>]+>', ' ', txt)
        score = sum(body.lower().count(t.lower()) for t in terms)

        if score >= 3:
            candidates.append({
                'slug': f.stem,
                'title': title,
                'excerpt': excerpt,
                'date': pub_date,
                'score': score,
            })

    # Sort by date desc (most recent first), then score desc
    candidates.sort(key=lambda x: (x['date'], x['score']), reverse=True)
    return candidates[:30]  # cap at 30 most relevant articles


def render_hub(slug, hub_def):
    articles = collect_articles_for_hub(slug, hub_def)
    section = get_canonical_section(slug)

    # Format date for display
    def pretty_date(iso):
        try:
            d = datetime.strptime(iso, '%Y-%m-%d')
            return d.strftime('%b %d, %Y')
        except: return iso

    # Build the article list HTML
    if articles:
        items = []
        for a in articles:
            items.append(
                f'<article class="hub-article-row">'
                f'<a href="{a["slug"]}.html" class="hub-article-title">{a["title"]}</a>'
                f'<div class="hub-article-meta"><span>{pretty_date(a["date"])}</span></div>'
                f'<p class="hub-article-excerpt">{a["excerpt"]}</p>'
                f'</article>'
            )
        articles_html = '\n            '.join(items)
    else:
        articles_html = '<p style="color:var(--text-3);font-size:14px">No articles available yet. Check back soon.</p>'

    canonical = f'https://www.energypricestoday.com/articles/{slug}.html'
    iso_now = datetime.now(timezone(timedelta(hours=-4))).isoformat()
    keywords = hub_def['keywords']

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','957762016897581');fbq('track','PageView');</script><noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=957762016897581&ev=PageView&noscript=1"/></noscript>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>{hub_def['title']} | EnergyPricesToday</title>
  <meta name="description" content="{hub_def['desc']}">
  <link rel="canonical" href="{canonical}">
  <meta name="news_keywords" content="{keywords}">
  <meta name="keywords" content="{keywords}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <meta name="googlebot-news" content="index, follow">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{hub_def['title']} | EnergyPricesToday">
  <meta property="og:description" content="{hub_def['desc']}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="EnergyPricesToday.com">
  <meta property="og:image" content="https://www.energypricestoday.com/images/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{hub_def['title']}">
  <meta name="twitter:description" content="{hub_def['desc']}">
  <meta name="twitter:image" content="https://www.energypricestoday.com/images/og-image.png">
  <link rel="alternate" type="application/rss+xml" title="EnergyPricesToday RSS Feed" href="../feed.xml">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,500&family=Outfit:wght@300;400;500;600;700&display=swap" media="print" onload="this.media='all'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,500&family=Outfit:wght@300;400;500;600;700&display=swap"></noscript>
  <link rel="stylesheet" href="../css/styles.css?v=15">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-FXGF8HZFWL"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","G-FXGF8HZFWL");</script>
  <link rel="icon" type="image/x-icon" href="../images/favicon.ico?v=2">
  <link rel="icon" type="image/svg+xml" href="../images/favicon.svg?v=2">
  <link rel="icon" type="image/png" sizes="16x16" href="../images/favicon-16x16.png?v=2">
  <link rel="icon" type="image/png" sizes="32x32" href="../images/favicon-32x32.png?v=2">
  <link rel="icon" type="image/png" sizes="48x48" href="../images/favicon-48x48.png?v=2">
  <link rel="apple-touch-icon" sizes="180x180" href="../images/apple-touch-icon.png?v=2">
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"CollectionPage","name":"{hub_def['title'].replace('&amp;','and').replace('&mdash;','-')}","description":"{hub_def['desc']}","url":"{canonical}","isPartOf":{{"@type":"WebSite","name":"EnergyPricesToday.com","url":"https://www.energypricestoday.com"}},"about":{{"@type":"Thing","name":"{hub_def['h1'].split(' &mdash;')[0].replace('&amp;','and')}"}},"publisher":{{"@type":"NewsMediaOrganization","name":"EnergyPricesToday.com","url":"https://www.energypricestoday.com","logo":{{"@type":"ImageObject","url":"https://www.energypricestoday.com/images/logo.png","width":674,"height":130}}}}}}</script>
  <style>
    .hub-article-row{{padding:18px 0;border-bottom:1px solid var(--border)}}
    .hub-article-row:last-child{{border-bottom:none}}
    .hub-article-title{{display:block;color:var(--text-1);font-size:17px;font-weight:600;text-decoration:none;line-height:1.35;margin-bottom:4px}}
    .hub-article-title:hover{{color:var(--blue)}}
    .hub-article-meta{{color:var(--text-3);font-size:11.5px;font-weight:600;letter-spacing:0.04em;text-transform:uppercase;margin-bottom:8px}}
    .hub-article-excerpt{{color:var(--text-2);font-size:14px;line-height:1.55;margin:0}}
  </style>
</head>
<body>
  <header class="site-header" id="site-header"></header>
  <main>
    <article class="article-page">
      <div class="container" style="max-width:880px">
        <nav aria-label="Breadcrumb" style="margin:24px 0 16px;font-size:12px;color:var(--text-3);display:flex;flex-wrap:wrap;gap:6px;align-items:center">
          <a href="../index.html" style="color:var(--text-2);text-decoration:none">Home</a>
          <span style="color:var(--text-3)">&rsaquo;</span>
          <a href="../category/geopolitics.html" style="color:var(--text-2);text-decoration:none">{section}</a>
          <span style="color:var(--text-3)">&rsaquo;</span>
          <span style="color:var(--text-2)">{hub_def['h1'].split(' &mdash;')[0].replace('&amp;','and')}</span>
        </nav>
        <h1>{hub_def['h1']}</h1>
        <div class="article-body" style="margin-top:24px">
          <p style="font-size:16.5px;line-height:1.7;color:var(--text-2)">{hub_def['lead']}</p>
          <div style="margin-top:18px;padding:18px 22px;background:var(--surface-2);border-radius:10px;border-left:3px solid var(--blue)">
            <h3 style="margin:0 0 8px;font-size:13px;text-transform:uppercase;letter-spacing:0.06em;color:var(--blue)">Current Context</h3>
            <p style="margin:0;font-size:14.5px;line-height:1.6;color:var(--text-2)">{hub_def['context']}</p>
          </div>
        </div>

        <section style="margin-top:40px">
          <h2 style="font-size:20px;font-weight:600;letter-spacing:-0.01em;color:var(--text-1);margin:0 0 8px">All Coverage</h2>
          <p style="color:var(--text-3);font-size:13px;margin:0 0 20px">{len(articles)} articles, most recent first.</p>
          <div>
            {articles_html}
          </div>
        </section>

        <div style="margin-top:48px;padding:24px;background:var(--surface-2);border-radius:10px;border-left:3px solid var(--blue)">
          <h3 style="margin:0 0 12px;font-size:14px;text-transform:uppercase;letter-spacing:0.06em;color:var(--text-2)">Related Dashboards</h3>
          <div style="display:flex;gap:10px;flex-wrap:wrap">
            <a href="../oil-prices.html" class="btn-secondary">Oil Prices</a>
            <a href="../category/geopolitics.html" class="btn-secondary">Geopolitics</a>
            <a href="../markets.html" class="btn-secondary">Markets</a>
            <a href="../category/gas-prices.html" class="btn-secondary">Gas Prices</a>
            <a href="../electricity-prices.html" class="btn-secondary">Electricity</a>
          </div>
        </div>
      </div>
    </article>
  </main>
  <footer class="site-footer" id="site-footer"></footer>
  <script src="../js/data.js?v=15"></script>
  <script src="../js/article-slugs.js?v=15"></script>
  <script src="../js/main.js?v=15"></script>
</body>
</html>
'''


def main():
    created = 0
    for slug, hub_def in HUBS.items():
        path = ARTICLES_DIR / f"{slug}.html"
        path.write_text(render_hub(slug, hub_def), encoding='utf-8')
        print(f"  ✓ {slug}.html")
        created += 1
    print(f"\nGenerated {created} hub pages")


if __name__ == '__main__':
    main()
