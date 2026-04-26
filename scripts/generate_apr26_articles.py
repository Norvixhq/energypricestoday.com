#!/usr/bin/env python3
"""
Generate 6 new article files covering April 22-26, 2026 developments.
Matches the existing template format used by April 21 articles.
"""

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"

STORIES = [
    {
        "slug": "trump-orders-navy-shoot-and-kill-iranian-mine-laying-vessels-in-strait",
        "title_variants": [
            "Trump Orders Navy to 'Shoot and Kill' Iranian Mine-Laying Vessels in Strait",
            "Trump Orders Navy to 'Shoot and Kill' Iranian Boats Laying Mines in Hormuz",
            "Trump Escalates: 'Shoot and Kill' Order Against Iranian Mine-Laying Boats",
        ],
        "display_title": "Trump Orders Navy to 'Shoot and Kill' Iranian Mine-Laying Vessels in Strait",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "April 22, 2026",
        "read_time": "6 min",
        "meta_desc": "President Trump ordered the U.S. Navy to 'shoot and kill' Iranian small boats laying mines in the Strait of Hormuz, marking a sharp escalation in U.S. enforcement posture.",
        "paragraphs": [
            "President Donald Trump on Thursday, April 22, 2026, ordered the U.S. Navy to &ldquo;shoot and kill&rdquo; Iranian small boats observed laying mines in the Strait of Hormuz, marking the sharpest escalation in U.S. enforcement posture since the naval blockade of Iranian ports began on April 13. The order, announced via Truth Social, applies specifically to vessels actively engaged in mine-laying operations in international waters of the strait.",
            "Trump&rsquo;s post described the U.S. naval blockade as &ldquo;unbelievably effective&rdquo; and said that Iran&rsquo;s economic situation was being severely degraded by the loss of oil export revenue. &ldquo;When you have lines of vast amounts of oil pouring through your system, if for any reason that line is closed because you can&rsquo;t continue to put it into containers or ships, which has happened to them, they have no ships because of the blockade, what happens is that line explodes from within,&rdquo; he said.",
            "The order escalates the rules of engagement that had previously governed U.S. Navy operations in the strait. Earlier in April, U.S. Navy destroyers had conducted &ldquo;mine clearance operations&rdquo; described by U.S. Central Command as freedom-of-navigation transits. Today&rsquo;s order moves from defensive clearance to active interdiction with lethal force authorized.",
            "Iran responded sharply through state media. Iranian officials disputed Trump&rsquo;s characterization of a leadership rift in the Islamic Republic and called the &ldquo;shoot and kill&rdquo; order a violation of international law. According to one earlier report, Iran has lost track of mines it planted in the Strait of Hormuz, which is part of why the strait has not fully reopened despite earlier diplomatic announcements.",
            "The U.S. military also boarded a supertanker carrying Iranian oil in the Indian Ocean, far from the Strait itself. The boarding signals that the U.S. interdiction net extends well beyond the Persian Gulf, and that any vessel suspected of carrying sanctioned Iranian crude could face boarding and seizure on global shipping routes.",
            "Oil markets responded with renewed volatility. WTI crude was up sharply in afternoon trading following the order, and Brent extended its weekly gains. The escalation reinforces the geopolitical risk premium that has held crude prices above $90 per barrel for weeks. For live market tracking, see <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">our oil price dashboard</a> and the <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics risk dashboard</a>.",
        ],
        "related": [
            ("U.S. Naval Blockade of Iranian Ports Remains in Place Despite Ceasefire Extension", "us-naval-blockade-of-iranian-ports-remains-in-place-despite-ceasefire-extension"),
            ("Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Iranian Government", "trump-extends-iran-ceasefire-indefinitely-citing-fractured-iranian-government"),
            ("Hormuz Closed Again: Iran Reverses Course as Trump Refuses to Lift Blockade", "hormuz-closed-again-iran-reverses-course-as-trump-refuses-to-lift-blockade"),
        ],
    },
    {
        "slug": "wti-surges-13-percent-on-week-as-hormuz-stays-closed-and-talks-stall",
        "title_variants": [
            "WTI Surges 13% on Week as Hormuz Stays Closed and Talks Stall",
            "WTI Posts 13% Weekly Gain on Stalled Diplomacy and Hormuz Closure",
            "Brent Up 18% on Week as Iran Talks Deadlock, Hormuz Remains Shut",
            "Crude Oil Posts Biggest Weekly Gain Since March on Iran Standoff",
        ],
        "display_title": "WTI Surges 13% on Week as Hormuz Stays Closed and Talks Stall",
        "category": "Oil Markets",
        "category_url": "../oil-prices.html",
        "date": "April 24, 2026",
        "read_time": "6 min",
        "meta_desc": "WTI crude rose 13% on the week and Brent rose 18%, the biggest weekly gains since early March, as Hormuz stayed closed and U.S.-Iran diplomacy deadlocked. WTI settled at $94.7, Brent at $104.4.",
        "paragraphs": [
            "U.S. crude oil benchmarks posted their biggest weekly gain since early March, with West Texas Intermediate up 13% and Brent up roughly 18% on the week ending Friday, April 24, 2026. The rally was driven by the persistent closure of the Strait of Hormuz, the continuing U.S. naval blockade of Iranian ports, and growing recognition that diplomatic resolution remains weeks or months away.",
            "Friday&rsquo;s session ended with WTI settling at $94.70 per barrel after slipping 1.51% on news that the White House would send envoys Steve Witkoff and Jared Kushner to Pakistan for second-round talks with Iran. Brent crude futures slipped to $104.40 per barrel, reversing earlier gains and snapping a four-session winning streak as hopes of diplomatic progress briefly improved sentiment. By Saturday those hopes had collapsed when Trump cancelled the U.S. envoys&rsquo; trip.",
            "The week&rsquo;s 13% WTI gain reflects how thoroughly geopolitical risk has come to dominate fundamental supply-demand factors in oil pricing. Analysts at Goldman Sachs, Morgan Stanley, and Citigroup have all noted that the typical correlation between U.S. inventory data and crude prices has weakened significantly since the conflict began, with each Hormuz development moving prices by margins that dwarf weekly stockpile reports.",
            "&ldquo;Oil markets have entered a geopolitically driven regime where supply disruption fears, particularly around the Strait of Hormuz, are overriding traditional fundamentals and fueling volatility,&rdquo; one major investment bank wrote in a note to clients this week. Options markets reflect this view: implied volatility on near-term WTI contracts is at multi-year highs, and the skew on out-of-the-money calls remains pronounced.",
            "OPEC+ has continued its planned April production increase of approximately 206,000 barrels per day despite the volatile environment. Saudi Arabia&rsquo;s East-West Pipeline is operating at its full 5 million bpd capacity, providing the primary bypass around the Hormuz chokepoint. Other Gulf producers have effectively idled production that cannot reach export terminals.",
            "Looking ahead to next week, traders are watching for any restart of formal U.S.-Iran talks, the next weekly EIA inventory report on Wednesday, and any Israeli or Iranian action that could expand the conflict. The most probable scenario remains continued elevated prices &mdash; analysts widely expect WTI to stay above $90 until diplomatic resolution becomes credible. For continuous market tracking, see <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">our oil price dashboard</a>.",
        ],
        "related": [
            ("Brent Touches $101 Intraday Before Retreating on Ceasefire Extension", "brent-touches-101-intraday-before-retreating-on-ceasefire-extension"),
            ("Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Iranian Government", "trump-extends-iran-ceasefire-indefinitely-citing-fractured-iranian-government"),
            ("OPEC+ April Output Increase Proceeding Despite Market Volatility", "opec-april-output-increase-proceeding-despite-market-volatility"),
        ],
    },
    {
        "slug": "trump-cancels-witkoff-kushner-pakistan-trip-as-iran-talks-stall",
        "title_variants": [
            "Trump Cancels Witkoff-Kushner Pakistan Trip as Iran Talks Stall",
            "U.S. Envoys' Pakistan Trip Cancelled as Talks With Iran Break Down Again",
            "Trump Halts Talks: Witkoff and Kushner Trip to Islamabad Cancelled",
        ],
        "display_title": "Trump Cancels Witkoff-Kushner Pakistan Trip as Iran Talks Stall",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "April 25, 2026",
        "read_time": "6 min",
        "meta_desc": "Trump cancelled the planned trip of U.S. envoys Witkoff and Kushner to Islamabad on Saturday April 25, halting the second round of U.S.-Iran peace talks before it could begin.",
        "paragraphs": [
            "President Donald Trump cancelled the planned trip of U.S. envoys Steve Witkoff and Jared Kushner to Islamabad on Saturday, April 25, 2026, halting what was expected to be the second formal round of U.S.-Iran peace talks before it could begin. The cancellation came less than 24 hours after the White House had announced the envoys would travel to Pakistan for direct discussions with the Iranian delegation.",
            "The cancellation followed mixed signals from Tehran about whether Iranian officials were prepared to engage substantively with U.S. demands. Iranian Foreign Minister Abbas Araghchi had arrived in Islamabad on Friday night and met with Pakistan&rsquo;s Field Marshal Asim Munir on Saturday, but Iran did not confirm any direct meeting with U.S. officials would take place.",
            "Pakistani Prime Minister Shehbaz Sharif spoke with Iranian President Masoud Pezeshkian by phone on Saturday night for approximately 50 minutes. According to Sharif&rsquo;s office, the two leaders had a &ldquo;detailed exchange of views on the current regional situation and ongoing efforts to promote peace and stability in the region,&rdquo; though no specific terms were disclosed.",
            "The cancellation marks the second time in two weeks that direct U.S.-Iran talks have failed to materialize. The first round, conducted between Vice President JD Vance and Iran&rsquo;s parliament speaker Mohammad Bagher Ghalibaf in mid-April, ran for 21 hours but ended without agreement. The U.S. naval blockade of Iranian ports was imposed shortly afterward, and remains in place.",
            "Pakistan&rsquo;s mediating role has continued through the cancellation. Sharif and Munir have remained in continuous contact with both Tehran and Washington, and Pakistan&rsquo;s information ministry confirmed that the country remains prepared to host talks &ldquo;at a moment&rsquo;s notice&rdquo; if both sides agree to engage. The phone call between Sharif and Pezeshkian suggests the back-channel mediation effort is ongoing despite the formal trip cancellation.",
            "Markets are expected to react sharply to the failed weekend diplomacy when trading resumes Monday. Friday&rsquo;s closes &mdash; WTI at $94.70 and Brent at $104.40 &mdash; were already higher on the week despite Friday&rsquo;s pullback on initial trip announcements. With the trip now cancelled, analysts expect the geopolitical risk premium to reassert itself in early-week trading. For live market tracking, see <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">our oil price dashboard</a> and the <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics risk dashboard</a>.",
        ],
        "related": [
            ("Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Iranian Government", "trump-extends-iran-ceasefire-indefinitely-citing-fractured-iranian-government"),
            ("Vance's Islamabad Trip Put on Hold as Iran Fails to Confirm Delegation", "vances-islamabad-trip-put-on-hold-as-iran-fails-to-confirm-delegation"),
            ("Iran FM Araghchi Calls U.S. Naval Blockade 'An Act of War' and Ceasefire Violation", "iran-fm-araghchi-calls-us-naval-blockade-an-act-of-war-and-ceasefire-violation"),
        ],
    },
    {
        "slug": "araghchi-leaves-pakistan-without-meeting-us-officials-as-talks-collapse",
        "title_variants": [
            "Araghchi Leaves Pakistan Without Meeting U.S. Officials as Talks Collapse",
            "Iran's FM Araghchi Departs Islamabad Without U.S. Meeting",
            "Araghchi Returns to Tehran After Talks With Pakistani Mediators Only",
        ],
        "display_title": "Araghchi Leaves Pakistan Without Meeting U.S. Officials as Talks Collapse",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "April 26, 2026",
        "read_time": "5 min",
        "meta_desc": "Iran's Foreign Minister Araghchi left Islamabad Sunday April 26 without meeting any U.S. officials, after Trump cancelled the Witkoff-Kushner trip. Pakistani mediation continues but direct talks remain stalled.",
        "paragraphs": [
            "Iran&rsquo;s Foreign Minister Seyed Abbas Araghchi left Islamabad on Sunday, April 26, 2026, without meeting any U.S. officials, ending what had been billed as a potential second round of U.S.-Iran peace talks. Araghchi&rsquo;s departure follows President Trump&rsquo;s Saturday cancellation of the planned trip by U.S. envoys Steve Witkoff and Jared Kushner.",
            "Araghchi met with Pakistan&rsquo;s Field Marshal Asim Munir and Prime Minister Shehbaz Sharif during his weekend visit but had no direct contact with American counterparts. Pakistani state media reported that discussions focused on Iran&rsquo;s conditions for a lasting peace agreement, including an end to the U.S. naval blockade, the release of approximately $6 billion in frozen Iranian assets, and security guarantees regarding the Israel-Hezbollah conflict.",
            "The collapse of the second round of talks confirms what regional analysts had been warning for over a week: that the gap between U.S. and Iranian negotiating positions remains too wide to bridge in short-format diplomacy. The U.S. has prioritized Iran&rsquo;s nuclear commitments and verifiable enrichment limits; Iran has prioritized economic relief and reciprocal U.S. concessions on the blockade.",
            "Pakistan&rsquo;s mediating role appears to be continuing despite the failed direct meetings. The Sharif-Pezeshkian phone call on Saturday evening, lasting approximately 50 minutes, suggests that back-channel diplomacy is still active. However, the inability to bring American and Iranian officials into the same room represents a significant setback for the diplomatic track.",
            "The U.S. naval blockade of Iranian ports remains in place, and the Strait of Hormuz remains essentially closed. The dual blockade &mdash; with the U.S. preventing ships from accessing Iranian ports and Iran preventing commercial transit through the strait &mdash; continues to disrupt approximately 20% of seaborne global oil and a comparable share of LNG shipments.",
            "Markets enter Monday&rsquo;s trading session with the geopolitical risk premium fully embedded in prices. Analysts expect WTI to push back above $95 and potentially toward $100 in early-week trading absent fresh diplomatic developments. The next significant catalysts will be Wednesday&rsquo;s EIA petroleum inventory report and any signs of renewed direct U.S.-Iran communication. For continuous tracking of these developments, see <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">our geopolitics risk dashboard</a>.",
        ],
        "related": [
            ("Trump Cancels Witkoff-Kushner Pakistan Trip as Iran Talks Stall", "trump-cancels-witkoff-kushner-pakistan-trip-as-iran-talks-stall"),
            ("Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Iranian Government", "trump-extends-iran-ceasefire-indefinitely-citing-fractured-iranian-government"),
            ("U.S. Naval Blockade of Iranian Ports Remains in Place Despite Ceasefire Extension", "us-naval-blockade-of-iranian-ports-remains-in-place-despite-ceasefire-extension"),
        ],
    },
    {
        "slug": "israeli-strikes-kill-lebanese-journalist-amal-khalil-during-extended-ceasefire",
        "title_variants": [
            "Israeli Strikes Kill Lebanese Journalist Amal Khalil During Extended Ceasefire",
            "Lebanese Journalist Killed in Israeli Strike, Heavy Bombing Continues Despite Truce",
            "Israeli Strikes on Lebanon Kill 6 Including Journalist as Ceasefire Strains",
        ],
        "display_title": "Israeli Strikes Kill Lebanese Journalist Amal Khalil During Extended Ceasefire",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "April 23, 2026",
        "read_time": "5 min",
        "meta_desc": "Lebanese journalist Amal Khalil was killed and others wounded in an Israeli strike April 22, sharply straining the extended Israel-Lebanon ceasefire. Multiple new strikes followed across south Lebanon.",
        "paragraphs": [
            "Lebanese journalist Amal Khalil was killed in an Israeli strike on April 22, 2026, sharply straining the extended Israel-Lebanon ceasefire and prompting widespread condemnation from press freedom organizations. Two other journalists were wounded in the same incident, which Khalil&rsquo;s newspaper and rights groups called a targeted attack.",
            "Israel&rsquo;s military said it was reviewing the incident in which Khalil was killed but stated that it does not target journalists. The killing occurred during what Wednesday became one of the bloodiest days since the Israel-Lebanon ceasefire came into effect. Khalil&rsquo;s funeral procession in Baisariyeh on April 23 drew large crowds of mourners and fellow journalists.",
            "The strike came despite the formal extension of the Israel-Lebanon ceasefire that had originally been set to expire approximately on April 25-26. The ceasefire had been extended by three weeks earlier in the month, but multiple violations from both sides have steadily eroded its credibility. Hezbollah has been accused of breaching the truce with rocket fire on Israeli troops in southern Lebanon; Israel has been accused of disproportionate retaliation including strikes that have killed civilians and journalists.",
            "On Saturday, April 25, Israeli strikes killed an additional six people in south Lebanon. Lebanon&rsquo;s health ministry reported that strikes on a truck and motorbike in Yohmor al-Shaqeef killed four people, and an attack on Safad al-Battikh killed two more and injured 17. Israel&rsquo;s military said it had &ldquo;eliminated&rdquo; three Hezbollah operatives driving a vehicle &ldquo;loaded with weapons,&rdquo; one on a motorcycle, and two more armed members elsewhere.",
            "Israeli Prime Minister Benjamin Netanyahu earlier ordered the military to &ldquo;forcefully attack Hezbollah targets&rdquo; after the army accused the group of breaching the truce. The escalation cycle &mdash; Hezbollah action, Israeli reprisal, Hezbollah counter-action &mdash; has been the defining pattern of the so-called ceasefire period and threatens to collapse the agreement entirely in coming weeks.",
            "The Lebanon front remains directly relevant to the parallel U.S.-Iran negotiations. Iran has consistently demanded that any comprehensive U.S.-Iran agreement include guarantees against renewed Israeli action in Lebanon, since Hezbollah is an Iranian proxy. The continued Israeli strikes therefore complicate Tehran&rsquo;s ability to commit to any U.S.-Iran deal, even as Pakistani mediators attempt to broker further talks.",
        ],
        "related": [
            ("Hezbollah Fires Rockets at Israeli Troops in Southern Lebanon, Violating Ceasefire", "hezbollah-fires-rockets-at-israeli-troops-in-southern-lebanon-violating-ceasefire"),
            ("Israel-Lebanon 10-Day Ceasefire Takes Effect, Hezbollah Holds Fire", "israel-lebanon-10-day-ceasefire-takes-effect-hezbollah-holds-fire"),
            ("French UN Peacekeeper Killed in Lebanon Attack, Macron Blames Hezbollah", "french-un-peacekeeper-killed-in-lebanon-attack-macron-blames-hezbollah"),
        ],
    },
    {
        "slug": "us-boards-supertanker-carrying-iranian-oil-in-indian-ocean",
        "title_variants": [
            "U.S. Boards Supertanker Carrying Iranian Oil in Indian Ocean",
            "U.S. Forces Board Iranian-Oil Supertanker in Indian Ocean Interdiction",
            "Sanctioned Tanker Boarded as U.S. Extends Iran Interdiction Globally",
        ],
        "display_title": "U.S. Boards Supertanker Carrying Iranian Oil in Indian Ocean",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "April 22, 2026",
        "read_time": "5 min",
        "meta_desc": "U.S. forces boarded a supertanker carrying Iranian oil in the Indian Ocean April 22, signaling that interdiction operations now extend well beyond the Persian Gulf and naval blockade zone.",
        "paragraphs": [
            "U.S. forces boarded a supertanker carrying Iranian oil in the Indian Ocean on April 22, 2026, marking a significant geographic expansion of U.S. interdiction operations beyond the immediate naval blockade zone in the Persian Gulf. The boarding signals that any vessel suspected of carrying sanctioned Iranian crude could face interception on global shipping routes.",
            "The boarding came on the same day President Trump ordered the U.S. Navy to &ldquo;shoot and kill&rdquo; Iranian small boats observed laying mines in the Strait of Hormuz. Together, the two announcements represent the sharpest escalation in U.S. enforcement posture since the formal naval blockade began on April 13, and they demonstrate the breadth of operational reach the U.S. military has chosen to project.",
            "Iran&rsquo;s &ldquo;shadow fleet&rdquo; of tankers operating with disabled transponders, flags of convenience, and ship-to-ship transfers has been the primary mechanism by which Iranian crude has reached Asian buyers throughout the conflict. Maritime tracking services including Lloyd&rsquo;s List and Windward have observed continued shadow fleet activity even after the blockade began, but the latest U.S. boarding suggests this workaround is now also under direct pressure.",
            "Industry estimates of Iranian crude exports under blockade have varied widely. Pre-conflict baseline Iranian exports were approximately 1.5 million barrels per day, primarily to Chinese refiners via intermediaries. The blockade is believed to have reduced this to approximately 600,000-900,000 barrels per day. The Indian Ocean boarding suggests the true figure may be lower still, depending on how aggressively the U.S. extends interdiction beyond the Persian Gulf.",
            "China has not publicly responded to the boarding, but the political calculus for Beijing is increasingly difficult. Chinese refiners have purchased the bulk of Iranian crude during the conflict period at discounted prices. Each U.S. interdiction action raises the implicit cost of these purchases and increases the risk of broader U.S.-China energy frictions just as both governments are attempting to manage their own bilateral tensions.",
            "The interdiction also raises legal questions under international maritime law. The U.S. has not formally claimed expanded authorities to interdict third-flag vessels in international waters, and Iranian officials have called the boarding &ldquo;piracy.&rdquo; However, U.S. authorities point to existing UN Security Council resolutions on Iranian proliferation as providing legal cover. The legal disputes are unlikely to be resolved formally during the active conflict.",
        ],
        "related": [
            ("Trump Orders Navy to 'Shoot and Kill' Iranian Mine-Laying Vessels in Strait", "trump-orders-navy-shoot-and-kill-iranian-mine-laying-vessels-in-strait"),
            ("U.S. Naval Blockade of Iranian Ports Remains in Place Despite Ceasefire Extension", "us-naval-blockade-of-iranian-ports-remains-in-place-despite-ceasefire-extension"),
            ("Iran FM Araghchi Calls U.S. Naval Blockade 'An Act of War' and Ceasefire Violation", "iran-fm-araghchi-calls-us-naval-blockade-an-act-of-war-and-ceasefire-violation"),
        ],
    },
]


def render_article(s):
    title_safe = s["display_title"].replace('&', '&amp;')
    paragraphs = "\n          ".join(f"<p>{p}</p>" for p in s["paragraphs"])
    related_items = "\n            ".join(
        f'<li><a href="{slug}.html" style="color:var(--blue);text-decoration:none">{title}</a></li>'
        for title, slug in s["related"]
    )
    cat_label = s["category"]

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','957762016897581');fbq('track','PageView');</script><noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=957762016897581&ev=PageView&noscript=1"/></noscript>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>{title_safe} | EnergyPricesToday</title>
  <meta name="description" content="{s['meta_desc']}">
  <link rel="canonical" href="https://www.energypricestoday.com/articles/{s['slug']}.html">
  <meta property="og:type" content="article"><meta property="og:title" content="{title_safe} | EnergyPricesToday">
  <meta property="og:description" content="{s['meta_desc']}">
  <link rel="stylesheet" href="../css/styles.css?v=5">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-FXGF8HZFWL"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","G-FXGF8HZFWL");</script>
  <link rel="icon" type="image/x-icon" href="../images/favicon.ico?v=2">
  <link rel="icon" type="image/svg+xml" href="../images/favicon.svg?v=2">
  <link rel="icon" type="image/png" sizes="16x16" href="../images/favicon-16x16.png?v=2">
  <link rel="icon" type="image/png" sizes="32x32" href="../images/favicon-32x32.png?v=2">
  <link rel="icon" type="image/png" sizes="48x48" href="../images/favicon-48x48.png?v=2">
  <link rel="apple-touch-icon" sizes="180x180" href="../images/apple-touch-icon.png?v=2">
  <link rel="shortcut icon" href="../images/favicon.ico?v=2">
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
        <div class="article-meta" style="margin:14px 0 24px"><span>Staff</span><span>{s['date']}</span><span>{s['read_time']} read</span></div>
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
        </div>
      </div>
    </article>
  </main>
  <footer class="site-footer" id="site-footer"></footer>
  <script src="../js/data.js?v=5"></script>
  <script src="../js/article-slugs.js?v=5"></script>
  <script src="../js/main.js?v=5"></script>
</body>
</html>
'''


def main():
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    created = 0
    for s in STORIES:
        path = ARTICLES_DIR / f"{s['slug']}.html"
        if path.exists():
            print(f"SKIP (exists): {s['slug']}.html")
            continue
        path.write_text(render_article(s), encoding="utf-8")
        print(f"✓ {s['slug']}.html")
        created += 1
    print(f"\n{created} new articles created")


if __name__ == "__main__":
    main()
