#!/usr/bin/env python3
"""
Generate 3 new article files covering May 10-11, 2026 — the deal-collapse turn.
Same template/style as generate_may9_articles.py.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"

STORIES = [
    {
        "slug": "trump-rejects-iran-counterproposal-as-totally-unacceptable-threatens-bombing",
        "title_variants": [
            "Trump Rejects Iran's Counterproposal as 'Totally Unacceptable'; Threatens to Resume Bombing",
            "Trump Rejects Iran Counteroffer, Threatens Higher-Intensity Bombing",
            "Trump: Iran Counterproposal 'TOTALLY UNACCEPTABLE'; Ceasefire on Life Support",
            "Trump Threatens to Resume Iran Bombing After Counterproposal Rejection",
            "Iran Vows Never to Bow as Trump Rejects Peace Counteroffer",
        ],
        "display_title": "Trump Rejects Iran's Counterproposal as 'Totally Unacceptable'; Threatens to Resume Bombing",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "May 11, 2026",
        "iso_date": "2026-05-11T15:00:00-04:00",
        "section": "Geopolitics",
        "read_time": "7 min",
        "meta_desc": "President Trump on Sunday May 10 publicly rejected Iran's counterproposal to end the 10-week war via Truth Social: 'TOTALLY UNACCEPTABLE.' Trump threatened to resume bombing at 'a much higher level and intensity.' Iran vowed to 'never bow.' Conflict in its twelfth week.",
        "keywords": "Trump rejects Iran counterproposal, Iran totally unacceptable, ceasefire life support, Iran 14-point memorandum, Iran vow never bow, Hormuz deal collapse",
        "paragraphs": [
            "President Donald Trump on Sunday, May 10, 2026, publicly rejected Iran&rsquo;s counterproposal to end the ten-week war in the Middle East, posting on Truth Social: &ldquo;I have just read the response from Iran&rsquo;s so-called &lsquo;Representatives.&rsquo; I don&rsquo;t like it &mdash; TOTALLY UNACCEPTABLE!&rdquo; Iran&rsquo;s counter, delivered through Pakistani mediators, had demanded that the United States lift Office of Foreign Assets Control (OFAC) sanctions on Iranian oil sales for a thirty-day period and end the naval blockade on Iranian ports, according to a report by Iran&rsquo;s semi-official Tasnim news agency.",
            "Trump on Monday May 11 told reporters the state of the ceasefire is &ldquo;unbelievably weak&rdquo; and called Iran&rsquo;s counterproposal &ldquo;garbage.&rdquo; &ldquo;I would say the ceasefire is on massive life support, where the doctor walks in and says, &lsquo;Sir, your loved one has approximately a 1% chance of living,&rsquo;&rdquo; the President said. He went further on Truth Social: &ldquo;If they don&rsquo;t agree, the bombing starts, and it will be, sadly, at a much higher level and intensity than it was before.&rdquo; The threat marks the most explicit U.S. escalation rhetoric since the late February strikes that began the conflict.",
            "Iran&rsquo;s response was equally defiant. Iranian state media framed Tehran&rsquo;s counterproposal as a rejection of the U.S. memorandum, which Iranian officials characterized as a demand for &ldquo;surrender.&rdquo; Iranian Army spokesperson Brig. Gen. Mohammad Akraminia warned of &ldquo;surprising options&rdquo; if adversaries made another &ldquo;miscalculation.&rdquo; A senior Iranian official said: &ldquo;Rather, the goal is to uphold the rights of the Iranian nation and to defend national interests with resolute strength.&rdquo; Tehran vowed not to &ldquo;bow our heads before the enemy.&rdquo;",
            "The Iranian counterproposal contained at least three elements that proved unacceptable to Washington. First, the demand for a thirty-day suspension of OFAC sanctions on Iranian oil sales would have allowed Iran to monetize stockpiled crude, capturing roughly $3&ndash;5 billion in revenue and undermining the leverage the blockade was designed to provide. Second, the demand for an immediate end to the naval blockade would have removed enforcement before any verification mechanism on Iranian nuclear concessions was in place. Third, Iran refused to dismantle nuclear infrastructure outright, offering only to transfer some highly enriched uranium to a third country &mdash; a concession the U.S. has characterized as far short of what its 14-point memorandum required.",
            "Markets responded sharply on Monday. WTI June futures advanced 4.96% to $100.30 per barrel; Brent July futures gained 4.92% to $105.76 per barrel. The rally undoes most of the relief move that followed the May 5 reports that the United States and Iran were close to agreement. The geopolitical risk premium that markets unwound through last week has now re-embedded into futures, with implied volatility on near-dated WTI calls climbing again. Citi maintained that risks to oil prices remain tilted to the upside, with the bank modeling a base case of end-May reopening and downside risk of further pushout.",
            "Multiple Gulf states reported additional weekend hostilities. A drone struck a ship in Qatari waters Sunday. The United Arab Emirates intercepted two drones and openly blamed Tehran. Kuwait intercepted hostile drones. Qatar&rsquo;s Foreign Ministry called the strike &ldquo;a dangerous and unacceptable escalation.&rdquo; The pattern signals that Iran retains both intent and capability to target Gulf infrastructure even during negotiations, undercutting any U.S. argument that the ceasefire is functionally holding.",
            "The collapse hangs over Trump&rsquo;s scheduled visit to Beijing later this week. China has called for the Strait of Hormuz to be reopened given how much of its energy supply transits the waterway. Arriving with the conflict not only unresolved but with the U.S. publicly threatening renewed strikes places Trump in a weaker negotiating posture with Xi Jinping than at any point in recent months. Israeli Prime Minister Benjamin Netanyahu, separately, said the conflict with Iran is &ldquo;not over&rdquo; because &ldquo;more work is to be done&rdquo; &mdash; a position that creates additional pressure for U.S. escalation rather than restraint. For continuing coverage, see our <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a> and <a href=\"strait-of-hormuz-explained.html\" style=\"color:var(--blue);text-decoration:none\">Strait of Hormuz explainer</a>.",
        ],
        "related": [
            ("Oil Rallies 5% as Hormuz Deal Collapses; WTI $100, Brent $106", "oil-rallies-5-percent-as-hormuz-deal-collapses-wti-100-brent-106"),
            ("Drones Strike Qatari Waters; UAE and Kuwait Intercept Iranian Drones", "drones-strike-qatari-waters-uae-and-kuwait-intercept-iranian-drones"),
            ("Aramco CEO: Hormuz Normalization Could Slip Into 2027 as 100M Barrels Lost Weekly", "aramco-ceo-hormuz-normalization-could-slip-into-2027"),
        ],
    },
    {
        "slug": "oil-rallies-5-percent-as-hormuz-deal-collapses-wti-100-brent-106",
        "title_variants": [
            "Oil Rallies 5% as Hormuz Deal Collapses; WTI $100, Brent $106",
            "WTI Jumps Nearly 5% to $100.30, Brent $105.76 on Iran Deal Rejection",
            "Crude Erases Last Week's Losses as Trump Rejects Iran Counterproposal",
            "Oil Rallies After Trump 'Totally Unacceptable' Truth Social Post",
            "Brent Tops $106 on Hormuz Risk Re-Embedding After Deal Collapse",
        ],
        "display_title": "Oil Rallies 5% as Hormuz Deal Collapses; WTI $100, Brent $106",
        "category": "Oil Markets",
        "category_url": "../category/oil-prices.html",
        "date": "May 11, 2026",
        "iso_date": "2026-05-11T17:00:00-04:00",
        "section": "Oil Prices",
        "read_time": "5 min",
        "meta_desc": "Crude futures surged Monday May 11 after Trump's Sunday rejection of Iran's counterproposal. WTI advanced 4.96% to $100.30; Brent gained 4.92% to $105.76. The rally undoes last week's relief move as the geopolitical risk premium re-embeds.",
        "keywords": "WTI crude price May 11, Brent crude $106, oil rally Trump Iran rejection, Hormuz deal collapse oil, crude futures May 11",
        "paragraphs": [
            "Crude oil markets rallied sharply on Monday, May 11, 2026, after President Trump on Sunday publicly rejected Iran&rsquo;s counterproposal to end the war. WTI June futures advanced 4.96% to settle at $100.30 per barrel, crossing back above the psychologically significant $100 mark. Brent July futures gained 4.92% to settle at $105.76 per barrel. The rally erases most of the relief move that followed the May 5 reports that the United States and Iran were close to a 14-point memorandum of understanding, when WTI had crashed as much as 13% intraday to a low of $88.71.",
            "Trump&rsquo;s Truth Social post Sunday rejecting Iran&rsquo;s counterproposal as &ldquo;TOTALLY UNACCEPTABLE&rdquo; was the catalyst. He followed Monday morning with reporters, telling them the ceasefire is &ldquo;on massive life support, where the doctor walks in and says, &lsquo;Sir, your loved one has approximately a 1% chance of living.&rsquo;&rdquo; The same day, Trump threatened on Truth Social: &ldquo;If they don&rsquo;t agree, the bombing starts, and it will be, sadly, at a much higher level and intensity than it was before.&rdquo; The geopolitical risk premium that markets unwound through last week has now re-embedded into futures.",
            "Implied volatility climbed in tandem. Near-dated WTI call options saw the largest daily implied-vol increase since the early April hostilities. Brent futures contracts for delivery in six months posted strong gains as the market priced not just immediate disruption but extended duration. Saudi Aramco CEO Amin Nasser warned on a Monday analyst call that the market is losing roughly 100 million barrels of supply each week and that if reopening of the Strait of Hormuz is &ldquo;delayed by a few more weeks, then normalization will last into 2027.&rdquo;",
            "Citi maintained that risks to oil prices remain tilted to the upside. The bank&rsquo;s base case assumes the Iranian regime makes a deal that reopens the strait around end-May, but the bank flagged downside risk that the timeline is pushed out and/or a partial reopening leaves disruptions in place for longer. Goldman Sachs separately held its previously raised Q4 Brent forecast of $90 per barrel. The structural supply deficit limits any deep crude pullback because GCC production capacity has sustained damage during the conflict and insurers remain reluctant to service tankers crossing the strait.",
            "Refined products tracked crude higher Monday. Gasoline RBOB jumped roughly 4% to $3.42 per gallon. ULSD diesel and heating oil both rose around 4% to $4.12. Jet fuel climbed 4% to $4.49. The strength in refined product cracks reflects continued tight inventory: U.S. gasoline stocks have fallen for 12 consecutive weeks; distillate fuel stocks declined for nine weeks straight. Refiners running flat-out to capture record crack spreads will continue to support input crude demand even as headline crude prices fluctuate on diplomatic headlines.",
            "AAA reported the U.S. national retail gasoline average at $4.520 per gallon Monday May 11, down about 3 cents from the May 8 peak of $4.546. The modest pullback reflects the multi-day lag from last week&rsquo;s crude crash. Monday&rsquo;s rally back above $100 WTI will reverse the retail decline within one to two weeks. California remains the highest-priced state at $6.16 per gallon; Hawaii $5.65. Pump prices are still $1.40 higher than a year ago and at their highest level since 2022.",
            "Prediction-market positioning shifted sharply Monday. Kalshi traders moved odds of WTI reaching $127 at some point in 2026 from roughly 50% on Friday to over 65% Monday afternoon. The shift reflects the market re-pricing not just current spot risk but the option value of further escalation. The next major test will come from Iran&rsquo;s response to Trump&rsquo;s renewed threats and from any U.S. action in the days ahead of the President&rsquo;s scheduled Beijing visit. For continuing coverage, see our <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">live oil prices dashboard</a>.",
        ],
        "related": [
            ("Trump Rejects Iran's Counterproposal as 'Totally Unacceptable'; Threatens to Resume Bombing", "trump-rejects-iran-counterproposal-as-totally-unacceptable-threatens-bombing"),
            ("Aramco CEO: Hormuz Normalization Could Slip Into 2027 as 100M Barrels Lost Weekly", "aramco-ceo-hormuz-normalization-could-slip-into-2027"),
            ("Drones Strike Qatari Waters; UAE and Kuwait Intercept Iranian Drones", "drones-strike-qatari-waters-uae-and-kuwait-intercept-iranian-drones"),
        ],
    },
    {
        "slug": "drones-strike-qatari-waters-uae-and-kuwait-intercept-iranian-drones",
        "title_variants": [
            "Drones Strike Qatari Waters; UAE and Kuwait Intercept Iranian Drones",
            "Gulf Weekend: Drones Hit Qatari Ship, UAE and Kuwait Defend",
            "Qatar Drone Strike Threatens Mediator Role Amid Hormuz Standoff",
            "Drone Hits Ship in Qatari Waters; UAE Openly Blames Iran",
            "Weekend Drone Attacks Across Persian Gulf Underscore Fragility",
        ],
        "display_title": "Drones Strike Qatari Waters; UAE and Kuwait Intercept Iranian Drones",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "May 11, 2026",
        "iso_date": "2026-05-11T13:00:00-04:00",
        "section": "Geopolitics",
        "read_time": "5 min",
        "meta_desc": "Multiple Gulf states reported drone attacks over the weekend May 10. A drone struck a ship in Qatari waters. The UAE intercepted two drones and openly blamed Tehran. Kuwait intercepted hostile drones. Qatar's Foreign Ministry called it 'a dangerous and unacceptable escalation.'",
        "keywords": "Qatar drone strike, UAE intercept Iran drones, Kuwait drones, Gulf weekend attacks, Hormuz Iran escalation, Qatar mediator",
        "paragraphs": [
            "Multiple Gulf states reported drone attacks over the weekend of May 9&ndash;10, 2026, signaling that Iran retains both intent and capability to target regional infrastructure even as Pakistan-mediated negotiations to end the war continue. A drone struck a ship in Qatari waters Sunday May 10, setting it on fire. The United Arab Emirates intercepted two drones over its airspace and openly blamed Tehran for the attack. Kuwait separately intercepted hostile drones over its airspace. No casualties were reported across the three incidents.",
            "Qatar&rsquo;s Foreign Ministry was the most pointed in its response. The ministry called the attack on the ship in Qatari waters &ldquo;a dangerous and unacceptable escalation that threatens the security and safety of maritime trade routes and vital supplies in the region.&rdquo; The condemnation is particularly significant because Qatar has emerged as one of the principal mediators in the conflict, alongside Pakistan, with Doha hosting back-channel contacts between U.S. and Iranian negotiators since late February. Targeting a ship in Qatari waters undermines that mediator role and signals an Iranian willingness to pressure even friendly intermediaries.",
            "The UAE&rsquo;s open attribution to Iran is also notable. Throughout the conflict, the UAE has been careful in its public attributions, often using neutral language even after direct strikes &mdash; including the May 4 Fujairah Oil Industry Zone drone strike that wounded three Indian nationals and the May 8 missile and drone barrage that air defenses engaged. By naming Tehran directly Sunday, the Emirati government appears to be signaling that its tolerance for hostile activity has reached a limit, even within a broader ceasefire framework.",
            "Kuwait&rsquo;s involvement marks an expansion of the geographic footprint. While Iranian drones and missiles have repeatedly targeted the UAE during the conflict, and Qatar has experienced occasional disruption, Kuwait had largely avoided direct attacks until this weekend. The Kuwaiti military said it intercepted hostile drones over its airspace without elaborating on origins or trajectories. Kuwait sits at the head of the Persian Gulf and serves as a major export terminus for both crude oil and refined products, making any escalation against Kuwaiti infrastructure a meaningful supply concern.",
            "Earlier on Sunday, a Qatari liquefied natural gas tanker crossed the Strait of Hormuz for the first time since the war began &mdash; a passage reportedly approved by Iran to build confidence with Qatar and Pakistan as mediators. A Panama-flagged bulk carrier bound for Brazil also transited the strait using a route designated by Iran&rsquo;s armed forces. The juxtaposition of approved symbolic passages and same-day drone strikes captures the paradox of the current moment: Iran is using selective de-escalation to maintain mediator relationships while simultaneously demonstrating coercive capability.",
            "The weekend hostilities came as Iran&rsquo;s counterproposal to the U.S. 14-point memorandum was being reviewed in Washington. President Trump publicly rejected the counterproposal Sunday in a Truth Social post, calling it &ldquo;TOTALLY UNACCEPTABLE&rdquo; and threatening to resume bombing &ldquo;at a much higher level and intensity than it was before.&rdquo; Trump on Monday told reporters the ceasefire is &ldquo;on massive life support.&rdquo; The timing of the drone strikes &mdash; immediately preceding the U.S. rejection &mdash; suggests Iran was signaling its bargaining floor through coercive action even as paper negotiations continued.",
            "The market response was sharp. WTI rallied 4.96% Monday to $100.30 per barrel; Brent jumped 4.92% to $105.76. Insurance markets responded faster: war-risk premiums on hulls transiting the broader Persian Gulf rose 15&ndash;20% on Monday, and several major underwriters quietly tightened coverage windows. For Gulf states that depend on freedom of navigation for their economies, the weekend hostilities reframe the cost-benefit of continued mediator neutrality versus more active alignment with the U.S. position. For continuing coverage, see our <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a> and <a href=\"strait-of-hormuz-explained.html\" style=\"color:var(--blue);text-decoration:none\">Strait of Hormuz explainer</a>.",
        ],
        "related": [
            ("Trump Rejects Iran's Counterproposal as 'Totally Unacceptable'; Threatens to Resume Bombing", "trump-rejects-iran-counterproposal-as-totally-unacceptable-threatens-bombing"),
            ("Oil Rallies 5% as Hormuz Deal Collapses; WTI $100, Brent $106", "oil-rallies-5-percent-as-hormuz-deal-collapses-wti-100-brent-106"),
            ("Aramco CEO: Hormuz Normalization Could Slip Into 2027 as 100M Barrels Lost Weekly", "aramco-ceo-hormuz-normalization-could-slip-into-2027"),
        ],
    },
    {
        "slug": "aramco-ceo-hormuz-normalization-could-slip-into-2027",
        "title_variants": [
            "Aramco CEO: Hormuz Normalization Could Slip Into 2027 as 100M Barrels Lost Weekly",
            "Amin Nasser Warns Hormuz Recovery May Last Into 2027",
            "Saudi Aramco CEO: 100 Million Barrels Lost Each Week",
            "Aramco Flags Multi-Year Recovery as Hormuz Shutdown Drags On",
            "Aramco Nasser Warns of 2027 Normalization Timeline",
        ],
        "display_title": "Aramco CEO: Hormuz Normalization Could Slip Into 2027 as 100M Barrels Lost Weekly",
        "category": "Oil Markets",
        "category_url": "../category/oil-prices.html",
        "date": "May 11, 2026",
        "iso_date": "2026-05-11T16:00:00-04:00",
        "section": "Oil Prices",
        "read_time": "5 min",
        "meta_desc": "Saudi Aramco CEO Amin Nasser warned Monday May 11 that the market is losing roughly 100 million barrels of supply each week and that if Hormuz reopening is 'delayed by a few more weeks, then normalization will last into 2027.' The IEA has called this the largest supply shock on record.",
        "keywords": "Aramco CEO Amin Nasser, Hormuz normalization 2027, 100 million barrels per week, Saudi Aramco supply shock, largest supply shock IEA",
        "paragraphs": [
            "Saudi Aramco Chief Executive Amin Nasser warned analysts on a Monday, May 11, 2026, conference call that the global oil market is losing roughly 100 million barrels of supply each week as the Strait of Hormuz disruption stretches into its twelfth week. Nasser added that if reopening of the strait is &ldquo;delayed by a few more weeks, then normalization will last into 2027.&rdquo; The remarks mark the most explicit timeline guidance from any major producer since the conflict began in late February and align Aramco&rsquo;s public position with the broader industry expectation that post-conflict recovery will be slow.",
            "Aramco&rsquo;s framing is particularly significant because the company is the world&rsquo;s largest crude exporter and one of the principal beneficiaries of the bypass infrastructure that has kept some Saudi crude flowing throughout the conflict. The East-West Pipeline to Yanbu has operated at its full 5 million barrels-per-day capacity since the strait closed, and Saudi Arabia has been the primary supplier of marginal crude to Asian and European buyers cut off from Persian Gulf flows. That Aramco is now publicly modeling a 2027 normalization timeline suggests the company sees structural rather than transitory impairment.",
            "The 100 million barrels per week figure reconciles with the IEA&rsquo;s estimate that the conflict is removing roughly 14 million barrels per day from global supply &mdash; or approximately 98 million barrels per week. The IEA has called the disruption the largest supply shock on record. Goldman Sachs, Barclays, and Citi have all tightened their full-year forecasts during the conflict; Citi&rsquo;s base case currently assumes the regime makes a deal that reopens the strait around end-May, but the bank flags downside risk that the timeline is pushed out and/or a partial reopening leaves disruptions in place for longer.",
            "Three structural factors support the 2027 timeline that Nasser articulated. First, Gulf Cooperation Council production facilities have sustained damage during the conflict &mdash; including the May 4 Iranian drone strike on the Fujairah Oil Industry Zone &mdash; that will require capital investment and time to repair before pre-conflict throughput is restored. Second, insurers have substantially tightened war-risk coverage for tankers transiting the strait, with several major underwriters quietly suspending coverage entirely; restoring full insurance markets will require sustained absence of hostilities rather than just a paper agreement. Third, vessel rescheduling, port slot allocation, and refinery feedstock contracts that were built around Hormuz throughput will take months to renormalize even once shipping resumes.",
            "The Monday warning came on the same day that crude futures rallied roughly 5% after President Trump publicly rejected Iran&rsquo;s counterproposal to end the conflict, calling it &ldquo;TOTALLY UNACCEPTABLE&rdquo; and threatening to resume bombing &ldquo;at a much higher level and intensity than it was before.&rdquo; WTI advanced 4.96% to $100.30 per barrel; Brent gained 4.92% to $105.76. The combination of explicit timeline guidance from the world&rsquo;s largest producer and renewed escalation rhetoric from the U.S. President reframed market expectations for the rest of the year.",
            "For Saudi Arabia, the timeline matters in multiple dimensions. The Kingdom is currently absorbing significant fiscal benefit from elevated crude prices but bearing reputational and security costs from the conflict itself, including increased Iranian harassment of GCC infrastructure. Aramco&rsquo;s Q1 2026 net income reached $26.7 billion, up sharply year-over-year despite production constraints, on the back of higher realized prices. But Aramco has also signaled to investors that the cash-flow tailwind is partially offset by the need for elevated capital expenditure on bypass infrastructure, security spending, and acceleration of upstream projects that were previously phased over multiple years.",
            "Investor reaction to Nasser&rsquo;s warning was modestly positive for oil-leveraged names. Major U.S. supermajors rallied 2&ndash;3% in afternoon trading; European integrateds underperformed slightly on euro-strength concerns. The 2027 normalization framework, if it holds, supports the bullish equity case for upstream producers while raising the cost of capital for downstream and petrochemical operations exposed to high input prices for an extended period. For continuing coverage, see our <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">live oil prices dashboard</a> and <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a>.",
        ],
        "related": [
            ("Trump Rejects Iran's Counterproposal as 'Totally Unacceptable'; Threatens to Resume Bombing", "trump-rejects-iran-counterproposal-as-totally-unacceptable-threatens-bombing"),
            ("Oil Rallies 5% as Hormuz Deal Collapses; WTI $100, Brent $106", "oil-rallies-5-percent-as-hormuz-deal-collapses-wti-100-brent-106"),
            ("Drones Strike Qatari Waters; UAE and Kuwait Intercept Iranian Drones", "drones-strike-qatari-waters-uae-and-kuwait-intercept-iranian-drones"),
        ],
    },
]


def render(s):
    title_safe = s["display_title"].replace('"', '&quot;')
    headline_safe = s["display_title"].replace('"', '\\"').replace("'", "\u2019")
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
  <title>{title_safe} | EnergyPricesToday</title>
  <meta name="description" content="{s['meta_desc']}">
  <link rel="canonical" href="{canonical}">
  <meta name="news_keywords" content="{s['keywords']}">
  <meta name="keywords" content="{s['keywords']}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <meta name="googlebot-news" content="index, follow">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title_safe} | EnergyPricesToday">
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
  <meta name="twitter:title" content="{title_safe[:70]}">
  <meta name="twitter:description" content="{s['meta_desc'][:200]}">
  <meta name="twitter:image" content="https://www.energypricestoday.com/images/og-image.png">
  <link rel="alternate" type="application/rss+xml" title="EnergyPricesToday RSS Feed" href="../feed.xml">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,500&family=Outfit:wght@300;400;500;600;700&display=swap" media="print" onload="this.media='all'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,500&family=Outfit:wght@300;400;500;600;700&display=swap"></noscript>
  <link rel="stylesheet" href="../css/styles.css?v=25">
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
  <script src="../js/data.js?v=25"></script>
  <script src="../js/article-slugs.js?v=25"></script>
  <script src="../js/main.js?v=25"></script>
</body>
</html>
'''


def main():
    for s in STORIES:
        out = ARTICLES_DIR / f"{s['slug']}.html"
        out.write_text(render(s), encoding="utf-8")
        print(f"  wrote {out.name}")
    print(f"\u2713 Generated {len(STORIES)} articles for May 10-11, 2026.")


if __name__ == "__main__":
    main()
