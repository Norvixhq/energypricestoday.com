#!/usr/bin/env python3
"""
Generate 5 new article files covering May 5-9, 2026 — the diplomacy turn.
Same template/style as generate_may4_articles.py.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"

STORIES = [
    {
        "slug": "us-iran-near-14-point-memorandum-to-end-hormuz-war",
        "title_variants": [
            "U.S. Awaits Iran Response to 14-Point Memorandum to End Hormuz War",
            "U.S. and Iran Near 14-Point Memorandum to End Hormuz War",
            "Axios: U.S.-Iran 14-Point MOU Would End War, Reopen Hormuz",
            "Trump Awaits Iran Response on 14-Point Hormuz Deal",
            "14-Point Memorandum Could End U.S.-Iran War; Iran Response Awaited",
        ],
        "display_title": "U.S. Awaits Iran Response to 14-Point Memorandum to End Hormuz War",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "May 8, 2026",
        "iso_date": "2026-05-08T17:00:00-04:00",
        "section": "Geopolitics",
        "read_time": "7 min",
        "meta_desc": "U.S. and Iran are reportedly close to a 14-point memorandum of understanding that would end the war and reopen the Strait of Hormuz. Iran would commit to a uranium enrichment moratorium; the U.S. would lift sanctions and release frozen funds. Iran's formal response expected through Pakistan.",
        "keywords": "US Iran memorandum, 14-point MOU, Hormuz reopening deal, Iran enrichment moratorium, Rubio Iran response, Axios Iran deal, Pakistan mediator",
        "paragraphs": [
            "U.S. officials told Axios on Wednesday, May 6, 2026, that Washington and Tehran were close to a one-page, 14-point memorandum of understanding that would end the war and establish a framework for further negotiations. The deal &mdash; if accepted by Iran &mdash; would lift restrictions in the Strait of Hormuz, with Iran committing to a moratorium on uranium enrichment in exchange for the United States lifting sanctions and releasing frozen Iranian funds.",
            "By Friday, May 8, Secretary of State Marco Rubio said the United States expected Iran&rsquo;s formal response that day. Reports indicate that Iran will deliver its response through Pakistan within two days. Pakistan has emerged as the primary back-channel mediator throughout the conflict, with PM Sharif and Field Marshal Munir maintaining open lines to both Washington and Tehran. Iranian Foreign Minister Abbas Araghchi traveled to Beijing on Tuesday May 5 as China continues to mediate U.S.-Iran negotiations in parallel.",
            "Markets responded with the largest single-day move in years. Tuesday May 5, WTI crude crashed as much as 13.2% intraday to a low of $88.71 per barrel &mdash; the first sub-$90 print since April 21. Brent plummeted as much as 12% to a low of $96.77. Both benchmarks recovered partially through the rest of the week, with Friday closes of $95.42 (WTI) and $101.29 (Brent), but still finished the week down more than 6%. Traders now refer to the move as a &ldquo;panic premium unwind.&rdquo;",
            "Defense Sec. Pete Hegseth said earlier in the week that the ceasefire is &ldquo;currently effective.&rdquo; Rubio said the offensive phase of military operations against Iran has &ldquo;ended.&rdquo; President Trump on Tuesday paused Project Freedom shipping operations to allow space for an agreement to be reached and signed, citing &ldquo;significant progress&rdquo; with Iranian representatives. The pause held until Friday, when U.S. forces disabled two Iranian oil tankers that attempted to evade the naval blockade &mdash; an action Trump described as &ldquo;just a love tap&rdquo; while reaffirming that the ceasefire remained in effect.",
            "Not everyone in Tehran is on board. On Thursday, Mohsen Rezaei, a member of Iran&rsquo;s Expediency Council, said via state news agency PressTV that the United States must pay reparations for damage done to Iran before any settlement. Tehran, Rezaei said, will not allow the U.S. to dictate terms unilaterally. The hardline framing has not derailed the technical talks but signals that any final deal will face internal Iranian political resistance similar to the friction within the U.S. side over War Powers compliance and sanction relief sequencing.",
            "Wall Street has begun adjusting forecasts to a softer-but-not-soft trajectory. Goldman Sachs raised its Q4 2026 Brent forecast to $90 per barrel and WTI to $83. Barclays sees Brent holding near $100 even after a deal. The structural supply deficit limits any deeper pullback because GCC production capacity has sustained damage during the conflict, insurers remain reluctant to service tankers crossing the strait, and U.S. gasoline inventories have fallen for 12 consecutive weeks. A peace deal, when it arrives, will not flood markets with supply.",
            "President Trump&rsquo;s scheduled Beijing visit, originally delayed from April, hangs over the timeline. China has called for the Strait of Hormuz to be reopened given how much of its energy supply transits the waterway. Arriving in Beijing with the conflict resolved &mdash; or at minimum with a credible framework &mdash; would substantially strengthen Trump&rsquo;s negotiating position with Xi Jinping. The next 72 hours will determine whether that timeline holds. For continuing coverage, see our <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a> and <a href=\"strait-of-hormuz-explained.html\" style=\"color:var(--blue);text-decoration:none\">Strait of Hormuz explainer</a>.",
        ],
        "related": [
            ("Oil Crashes 13% Intraday as U.S.-Iran MOU Talks Emerge", "oil-crashes-13-percent-intraday-as-us-iran-mou-talks-emerge"),
            ("U.S. Navy Disables Two Iranian Tankers; Trump Calls Strike a 'Love Tap'", "us-navy-disables-two-iranian-tankers-trump-calls-strike-a-love-tap"),
            ("Iran's Mohsen Rezaei Demands U.S. Reparations Before Any Deal", "iran-mohsen-rezaei-demands-us-reparations-before-any-deal"),
        ],
    },
    {
        "slug": "oil-crashes-13-percent-intraday-as-us-iran-mou-talks-emerge",
        "title_variants": [
            "Oil Crashes 13% Intraday as U.S.-Iran MOU Talks Emerge",
            "WTI Plunges to $88.71 Low as 14-Point Memorandum News Breaks",
            "Crude Tumbles 13% on Hormuz Deal Hopes; Brent Hits $96.77 Low",
            "Oil Markets Crash on U.S.-Iran Deal Talks; WTI Below $90",
            "WTI Crashes 13.2% to $88.71 — Lowest Since April 21",
        ],
        "display_title": "Oil Crashes 13% Intraday as U.S.-Iran MOU Talks Emerge",
        "category": "Oil Markets",
        "category_url": "../category/oil-prices.html",
        "date": "May 5, 2026",
        "iso_date": "2026-05-05T17:00:00-04:00",
        "section": "Oil Prices",
        "read_time": "6 min",
        "meta_desc": "WTI crude crashed as much as 13.2% intraday Tuesday May 5 to a low of $88.71 — first sub-$90 print since April 21. Brent plummeted as much as 12% to $96.77 low. The crash followed news that U.S. and Iran were close to a 14-point memorandum of understanding to end the war.",
        "keywords": "WTI crude crash May 5, oil crash 13 percent, Brent below $100, 14-point MOU oil, Iran deal oil price, panic premium unwind",
        "paragraphs": [
            "Crude oil markets suffered the largest single-day decline in years on Tuesday, May 5, 2026, with WTI crude futures crashing as much as 13.2% intraday to a low of $88.71 per barrel &mdash; the first sub-$90 print since April 21. Brent crude plummeted as much as 12% to an intraday low of $96.77. The crash followed reports that the United States and Iran were close to a one-page, 14-point memorandum of understanding that would end the war, reopen the Strait of Hormuz, and establish a framework for further negotiations.",
            "The selloff began before the U.S. cash open and accelerated through the morning as confirmation arrived that Defense Sec. Pete Hegseth had described the ceasefire as &ldquo;currently effective&rdquo; and Sec. of State Marco Rubio had said the &ldquo;offensive phase&rdquo; of military operations against Iran had &ldquo;ended.&rdquo; President Trump on Tuesday night announced he was pausing Project Freedom shipping operations to allow space for the deal to be reached and signed, citing &ldquo;significant progress&rdquo; with Iranian representatives.",
            "Iranian Foreign Minister Abbas Araghchi departed Tuesday for Beijing as China continues to mediate U.S.-Iran negotiations in parallel with the Pakistan back channel. The combination of three concurrent diplomatic tracks &mdash; bilateral memorandum drafting, Pakistani mediation, and Chinese facilitation &mdash; appears to have given markets enough confidence to unwind the &ldquo;panic premium&rdquo; that had built into crude during the previous week&rsquo;s Hormuz exchange of fire.",
            "The intraday recovery was partial. Both benchmarks closed Tuesday well off their lows, with WTI settling around $93 and Brent around $103. Traders described the move as a &ldquo;panic premium unwind&rdquo; rather than a fundamental reset. The structural supply deficit driving the rally remains in place: the IEA estimates the war is removing roughly 14 million barrels per day from global supply, GCC production capacity has sustained damage, and U.S. gasoline inventories have fallen for 12 consecutive weeks.",
            "Wall Street responded by adjusting forecasts. Goldman Sachs raised its Q4 2026 Brent forecast to $90 per barrel and WTI to $83. Barclays now sees Brent holding near $100 even after a peace deal. Both desks emphasized that any post-conflict production recovery would be slow: insurers remain reluctant to service tankers crossing the strait, and resumption of GCC capacity is expected to take months rather than weeks. Goldman noted total global oil stocks at roughly 101 days of demand currently, falling to 98 days by end of May.",
            "Refined products tracked crude lower but with less violence. Gasoline RBOB fell to roughly $3.30 per gallon by week&rsquo;s end. ULSD diesel and jet fuel both pulled back from May 4 highs. Despite the sharp move down, the AAA national gasoline retail average actually continued climbing through the week to reach $4.546 by Friday May 8 &mdash; up 25 cents on the week and at the highest level since 2022. The retail-to-spot lag means consumers will not see Tuesday&rsquo;s crash at the pump for another 1&ndash;2 weeks.",
            "Prediction markets remained bullish on continued strength. Kalshi traders currently assign greater than 50% probability that WTI will reach $127 per barrel at some point this year, well above the current trading range. The market consensus is now that crude trades in a $95&ndash;$105 range on WTI through the summer, with directional moves determined almost entirely by diplomatic headlines out of Washington, Tehran, Islamabad, and Beijing. For continuing coverage, see our <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">live oil prices dashboard</a>.",
        ],
        "related": [
            ("U.S. Awaits Iran Response to 14-Point Memorandum to End Hormuz War", "us-iran-near-14-point-memorandum-to-end-hormuz-war"),
            ("U.S. Navy Disables Two Iranian Tankers; Trump Calls Strike a 'Love Tap'", "us-navy-disables-two-iranian-tankers-trump-calls-strike-a-love-tap"),
            ("AAA Gas Average Hits $4.55, Up 25 Cents for Second Straight Week", "aaa-gas-average-hits-455-up-25-cents-for-second-straight-week"),
        ],
    },
    {
        "slug": "us-navy-disables-two-iranian-tankers-trump-calls-strike-a-love-tap",
        "title_variants": [
            "U.S. Navy Disables Two Iranian Tankers; Trump Calls Strike a 'Love Tap'",
            "CENTCOM: Navy Warplane Disables Two Iranian Tankers Friday",
            "M/T Sea Star III, M/T Sevda Disabled by U.S. Navy Strike",
            "Trump: Iran Tanker Strikes Just a 'Love Tap'; Ceasefire Holds",
            "U.S. Disables Two Iranian Tankers Evading Blockade Friday",
        ],
        "display_title": "U.S. Navy Disables Two Iranian Tankers; Trump Calls Strike a 'Love Tap'",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "May 8, 2026",
        "iso_date": "2026-05-08T18:00:00-04:00",
        "section": "Geopolitics",
        "read_time": "5 min",
        "meta_desc": "U.S. forces fired Friday May 8 on two empty Iranian oil tankers (M/T Sea Star III and M/T Sevda) that attempted to evade the naval blockade. CENTCOM said a Navy warplane fired into the smokestacks and disabled both vessels. Trump called the strikes 'just a love tap' and insisted the ceasefire remains in effect.",
        "keywords": "US Navy Iran tankers, M/T Sea Star III, M/T Sevda, love tap Trump, CENTCOM tanker strike, Iran blockade evasion",
        "paragraphs": [
            "U.S. forces on Friday, May 8, 2026, fired on two empty Iranian oil tankers that attempted to evade the U.S. naval blockade of Iranian ports. According to U.S. Central Command, a Navy warplane fired into the smokestacks of the vessels &mdash; identified as M/T Sea Star III and M/T Sevda &mdash; disabling both ships. The strike represents the first significant U.S. kinetic action against Iranian assets since President Trump on Tuesday paused Project Freedom shipping operations to create space for memorandum talks.",
            "President Trump told ABC News later Thursday that the strikes were &ldquo;just a love tap.&rdquo; The President insisted the U.S.-Iran ceasefire remained in effect during a phone call with the network. The framing &mdash; describing acts of war as a &ldquo;love tap&rdquo; while insisting hostilities have not resumed &mdash; reflects the administration&rsquo;s effort to thread the needle between enforcing the blockade and preserving the diplomatic opening represented by the 14-point memorandum currently under Iranian review.",
            "The same day, the United Arab Emirates reported additional Iranian attacks. The UAE Defense Ministry said its air defenses engaged two ballistic missiles and three drones launched from Iran &mdash; at least the second time this week that Iran fired projectiles at the UAE. The UAE, which sustained the largest single direct attack of the conflict on Monday May 4 with 19 missiles and drones, has now experienced repeated waves of incoming fire even with diplomatic talks underway.",
            "Iran has not officially responded to either incident, though state media has pushed back on Trump&rsquo;s framing. The strikes raise difficult questions for the diplomatic track. If &ldquo;defensive&rdquo; U.S. operations continue while the memorandum is being finalized, Iran has plausible grounds to argue that the U.S. has not honored the spirit of the ceasefire framework. If the U.S. ceases blockade enforcement entirely, Iranian tankers will resume open evasion and the leverage the blockade provides will erode.",
            "Sec. of State Rubio on Friday told reporters the U.S. expected Iran&rsquo;s formal response to the 14-point memorandum that day. Reports indicate the response will travel through Pakistan within two days. ANZ Research wrote in a note: &ldquo;The risk of a proposed U.S. peace deal breaking down will likely keep oil markets volatile.&rdquo; Citi analysts said they expect broader financial markets to stabilize despite recent volatility but warned that the path toward normalization is unlikely to be smooth.",
            "Markets digested the day&rsquo;s events with relative calm given the friction. WTI crude settled marginally higher at $95.42 per barrel (+0.6%). Brent crude added approximately 1% to close at $101.29 per barrel. Both contracts posted weekly losses of more than 6% as the broader market continued to price in deal optimism over Friday&rsquo;s tactical incidents. The continuing enforcement of the blockade &mdash; even via &ldquo;love taps&rdquo; &mdash; signals that the U.S. has not yet ceded its leverage.",
            "The disabled tankers will not constitute a meaningful supply event. Both vessels were empty at the time of the strikes, consistent with the broader pattern of Iranian shadow-fleet movements during the blockade. The strategic significance is symbolic: U.S. willingness to engage Iranian assets even during deal negotiations underlines that the conflict is not over until both sides commit in writing. For continuing coverage, see our <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a>.",
        ],
        "related": [
            ("U.S. Awaits Iran Response to 14-Point Memorandum to End Hormuz War", "us-iran-near-14-point-memorandum-to-end-hormuz-war"),
            ("Oil Crashes 13% Intraday as U.S.-Iran MOU Talks Emerge", "oil-crashes-13-percent-intraday-as-us-iran-mou-talks-emerge"),
            ("Iran's Mohsen Rezaei Demands U.S. Reparations Before Any Deal", "iran-mohsen-rezaei-demands-us-reparations-before-any-deal"),
        ],
    },
    {
        "slug": "aaa-gas-average-hits-455-up-25-cents-for-second-straight-week",
        "title_variants": [
            "AAA Gas Average Hits $4.55, Up 25 Cents for Second Straight Week",
            "U.S. Gas Average Reaches $4.546 — Highest Since 2022",
            "Pump Prices $1.40 Higher Than Year Ago as National Average Hits $4.55",
            "AAA: National Gas Average Up 25 Cents for Second Consecutive Week",
            "Gas Prices Climb to $4.55 Despite Crude Below $100",
        ],
        "display_title": "AAA Gas Average Hits $4.55, Up 25 Cents for Second Straight Week",
        "category": "Gas Prices",
        "category_url": "../category/gas-prices.html",
        "date": "May 8, 2026",
        "iso_date": "2026-05-08T14:00:00-04:00",
        "section": "Gas Prices",
        "read_time": "5 min",
        "meta_desc": "AAA reported the U.S. national average for regular gasoline reached $4.546 per gallon Friday May 8 — up 25 cents for the second straight week. Pump prices are now $1.40 higher than a year ago and at their highest level since 2022. Despite crude pulling back below $100, retail prices continue to climb on multi-day pass-through lag.",
        "keywords": "AAA gas $4.55, US gas average May 8, gas prices highest since 2022, pump prices Iran conflict, gasoline inventory drawdown",
        "paragraphs": [
            "AAA reported Friday, May 8, 2026, that the U.S. national average for a gallon of regular unleaded gasoline reached $4.546 &mdash; up roughly 25 cents from $4.30 a week earlier and from $4.05 two weeks ago. The reading caps the second consecutive week with a 25-cent national gain &mdash; the kind of pace last seen in the immediate aftermath of major refinery disruptions. Pump prices are now $1.40 higher than at the same time a year ago, and at their highest level since 2022, when the national average peaked at $5.01 per gallon.",
            "The continued retail climb is happening even as crude oil prices have pulled back sharply. WTI closed Friday at $95.42 and Brent at $101.29 &mdash; both down more than 6% on the week as markets priced in the U.S.-Iran 14-point memorandum talks. The disconnect reflects the multi-day lag between wholesale crude pricing and retail pump prices. Refiners are working through inventory acquired at the May 4 highs of $105 WTI / $114 Brent; that crude shows up at the pump 1&ndash;2 weeks later. Friday&rsquo;s settle of $95 WTI will not show at retail until late next week at the earliest.",
            "Regional variation continues to widen. California is averaging above $6.16 per gallon, the highest in the nation. The District of Columbia sits at $4.63, Connecticut $4.62, and Hawaii $5.65. The lowest-priced states &mdash; Mississippi, Oklahoma, Louisiana &mdash; remain below $4.20 but are climbing fast. Tennessee crossed $4 last week for the first time since July 2022 and continues to climb. The Midwest spike that began with the Indiana refinery issue continues to ripple: Michigan $4.86, Illinois (anchored by Chicago) near $5.10, Ohio above $4.40.",
            "The structural backdrop is more concerning than the headline number. U.S. gasoline inventories have fallen for 12 consecutive weeks. Distillate fuel stocks have declined for nine weeks straight. EIA reports crude inventories fell another 2.3 million barrels last week to 457.2 million barrels &mdash; about 1% above the five-year average. Refiners are running flat-out to capture record gasoline crack spreads, but rising gasoline demand combined with a 12-week inventory drawdown means the supply cushion is approaching critical levels in some regions.",
            "Diesel and middle distillates are even tighter. The U.S. diesel average sits at $6.24 per gallon. Heating oil futures fell to $3.96 with crude, but distillate stocks remain near multi-year lows. Rural agricultural states &mdash; whose economies depend heavily on diesel for trucking, farming, and rail &mdash; remain particularly exposed. The diesel-to-gasoline price differential is among the widest since 2022, signaling tight middle distillate supply globally even as gasoline cracks widen.",
            "AAA spokeswoman Megan Cooper said the 25-cent weekly jumps reflect &ldquo;the lagged pass-through from earlier crude price surges combined with strong spring travel demand.&rdquo; AAA is forecasting continued price pressure into the Memorial Day weekend regardless of how the U.S.-Iran memorandum talks proceed in the next two weeks, because the inventory cushion is too thin to absorb expected demand growth.",
            "The political pressure is rising in tandem. Several state-level proposals to suspend gasoline taxes are in active discussion. The Trump administration has not yet announced any Strategic Petroleum Reserve releases beyond what was authorized earlier in the conflict. The next AAA reading is expected Monday May 11. The next EIA weekly inventory report is due Wednesday May 13. For continuing coverage, see our <a href=\"../category/gas-prices.html\" style=\"color:var(--blue);text-decoration:none\">U.S. gas prices dashboard</a> and <a href=\"../oil-prices.html\" style=\"color:var(--blue);text-decoration:none\">live oil prices</a>.",
        ],
        "related": [
            ("Oil Crashes 13% Intraday as U.S.-Iran MOU Talks Emerge", "oil-crashes-13-percent-intraday-as-us-iran-mou-talks-emerge"),
            ("U.S. Awaits Iran Response to 14-Point Memorandum to End Hormuz War", "us-iran-near-14-point-memorandum-to-end-hormuz-war"),
            ("U.S. Gas Average Climbs to $4.46, Up Another 6 Cents Over Weekend", "us-gas-average-climbs-to-446-up-another-6-cents-over-weekend"),
        ],
    },
    {
        "slug": "iran-mohsen-rezaei-demands-us-reparations-before-any-deal",
        "title_variants": [
            "Iran's Mohsen Rezaei Demands U.S. Reparations Before Any Deal",
            "Mohsen Rezaei: U.S. Must Pay Reparations Before Settlement",
            "Iran Expediency Council Member Demands Reparations from U.S.",
            "Tehran Hardliner Rezaei Pushes Back on 14-Point Memorandum Terms",
            "PressTV: Iran's Rezaei Says U.S. Must Pay Reparations First",
        ],
        "display_title": "Iran's Mohsen Rezaei Demands U.S. Reparations Before Any Deal",
        "category": "Geopolitics",
        "category_url": "../category/geopolitics.html",
        "date": "May 7, 2026",
        "iso_date": "2026-05-07T16:00:00-04:00",
        "section": "Geopolitics",
        "read_time": "5 min",
        "meta_desc": "Mohsen Rezaei, member of Iran's Expediency Council, said via state news agency PressTV that the U.S. must pay reparations for damage done to Iran before any settlement. The hardline framing complicates the 14-point memorandum even as Iranian negotiators continue Pakistan-mediated talks.",
        "keywords": "Mohsen Rezaei reparations, Iran Expediency Council, PressTV Iran demands, 14-point MOU resistance, Iran hardliner U.S. deal",
        "paragraphs": [
            "Mohsen Rezaei, a member of Iran&rsquo;s Expediency Council and one of the regime&rsquo;s most prominent hardline voices, said Thursday, May 7, 2026, via the state news agency PressTV that the United States must pay reparations for damage done to Iran before any settlement of the conflict can proceed. Rezaei said Tehran will not allow the United States to dictate terms unilaterally and that the Iranian people will not accept a deal that does not address what he called &ldquo;the criminal damages&rdquo; inflicted by U.S. and Israeli operations.",
            "The remarks complicate &mdash; though they have not derailed &mdash; the 14-point memorandum of understanding currently being finalized between U.S. negotiators and the Iranian Foreign Ministry. Sec. of State Marco Rubio has said the U.S. expects Iran&rsquo;s formal response to the memorandum within days. Iranian Foreign Minister Abbas Araghchi traveled to Beijing on Tuesday May 5 as China continues to mediate U.S.-Iran negotiations in parallel with the Pakistan back channel.",
            "Rezaei&rsquo;s position is significant for institutional reasons. The Expediency Council is a constitutional body that arbitrates between the Iranian Parliament and the Guardian Council and provides advice to the Supreme Leader. Its members do not have direct executive power, but they shape the regime&rsquo;s acceptable range of policy outcomes. A vocal demand for reparations from a senior Expediency Council member functions as a public floor on Iranian negotiating concessions: any deal that emerges must be politically defensible against the &ldquo;reparations first&rdquo; framing now circulating in Tehran.",
            "The U.S. position has been that the memorandum already addresses Iranian economic damage indirectly through sanctions relief and the release of frozen Iranian funds &mdash; estimated at upwards of $80 billion across U.S., U.K., and South Korean banks. The Iranian counter-position, articulated by Rezaei, is that frozen funds belong to Iran by definition and that returning them does not constitute compensation for war damages. Whether this distinction blocks the deal will depend on how Iranian Supreme Leader Mojtaba Khamenei chooses to handle it in the formal response.",
            "Markets have priced in the possibility of friction without panicking. Brent crude pulled back slightly on Thursday to close at $100.06 per barrel after the Rezaei remarks were translated and circulated, though both crude benchmarks remained well below their May 4 highs of $105 WTI and $114 Brent. ANZ Research noted in a Friday client note: &ldquo;The risk of a proposed U.S. peace deal breaking down will likely keep oil markets volatile.&rdquo; Goldman Sachs and Barclays both kept their reduced Q4 Brent forecasts ($90 and $100 respectively) despite the hardline pushback.",
            "Iran&rsquo;s domestic political calculus is more complex than it appears from Washington. The conflict has imposed enormous costs on the Iranian economy and population: shortages, inflation, blackouts, and the loss of Supreme Leader Ali Khamenei in the late February strikes. A deal that lifts sanctions and reopens commerce serves an immediate Iranian interest. But signing under U.S. terms without a face-saving frame risks destabilizing the regime at a moment when its grip on internal politics is already tested.",
            "The next 72 hours are decisive. If Iran accepts the memorandum substantially as drafted, the conflict ends and Hormuz reopens within weeks. If Iran returns with reparations demands as a precondition, the U.S. likely walks; the blockade continues; and crude moves sharply higher again. Markets are pricing roughly 60&ndash;70% probability of a deal on Kalshi-style prediction markets. President Trump&rsquo;s Beijing visit, scheduled for next week, will function as a hard deadline either way. For continuing coverage, see our <a href=\"../category/geopolitics.html\" style=\"color:var(--blue);text-decoration:none\">geopolitics dashboard</a>.",
        ],
        "related": [
            ("U.S. Awaits Iran Response to 14-Point Memorandum to End Hormuz War", "us-iran-near-14-point-memorandum-to-end-hormuz-war"),
            ("Oil Crashes 13% Intraday as U.S.-Iran MOU Talks Emerge", "oil-crashes-13-percent-intraday-as-us-iran-mou-talks-emerge"),
            ("U.S. Navy Disables Two Iranian Tankers; Trump Calls Strike a 'Love Tap'", "us-navy-disables-two-iranian-tankers-trump-calls-strike-a-love-tap"),
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
  <link rel="stylesheet" href="../css/styles.css?v=24">
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
  <script src="../js/data.js?v=24"></script>
  <script src="../js/article-slugs.js?v=24"></script>
  <script src="../js/main.js?v=24"></script>
</body>
</html>
'''


def main():
    for s in STORIES:
        out = ARTICLES_DIR / f"{s['slug']}.html"
        out.write_text(render(s), encoding="utf-8")
        print(f"  wrote {out.name}")
    print(f"\u2713 Generated {len(STORIES)} articles for May 5-9, 2026.")


if __name__ == "__main__":
    main()
