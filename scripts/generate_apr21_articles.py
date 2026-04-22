#!/usr/bin/env python3
"""
Generate all missing April 21 article HTML files to fix the 404s introduced
when FEATURED_ARTICLES / BREAKING_NEWS / MARKET_DRIVERS / GEO_ITEMS etc. were
updated with today's ceasefire-extension content without creating matching files.

Strategy:
  1. Define the unique stories (normalizing near-duplicate titles)
  2. Build one canonical slug per unique story
  3. Update article-slugs.js ARTICLE_SLUGS map so ALL title variants resolve to
     the right canonical slug
  4. Generate HTML files for each canonical slug using the established template
"""

import re
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"
SLUGS_FILE = ROOT / "js" / "article-slugs.js"

# Canonical stories. Each has:
#   - canonical_slug: the file slug (NO .html)
#   - title_variants: every title variant we use in data.js (map all → this file)
#   - category: display category
#   - category_slug: for breadcrumb link (e.g., 'geopolitics', 'oil-prices', 'gas-prices')
#   - meta_desc: 155-char meta description
#   - h1: article heading
#   - paragraphs: list of HTML-ready paragraph strings
#   - related: list of 2-3 existing slugs to link to

STORIES = [
    {
        "canonical_slug": "trump-extends-iran-ceasefire-indefinitely-citing-fractured-iranian-government",
        "title_variants": [
            "Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Iranian Government",
            "Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Government",
            "Trump Extends Ceasefire Indefinitely, Citing 'Fractured' Iran",
            "Trump Extends Iran Ceasefire Indefinitely on Truth Social",
        ],
        "display_title": "Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Iranian Government",
        "category": "Geopolitics",
        "category_slug": "geopolitics",
        "date": "April 21, 2026",
        "read_time": "7 min",
        "meta_desc": "Trump extended the U.S.-Iran ceasefire indefinitely via Truth Social on April 21, citing a 'seriously fractured' Iranian government at the request of Pakistan.",
        "paragraphs": [
            'In a <a href="https://truthsocial.com/@realDonaldTrump" style="color:var(--blue);text-decoration:none" rel="noopener">Truth Social</a> post Tuesday afternoon, President Donald Trump announced he would extend the U.S.-Iran ceasefire indefinitely until Iran&rsquo;s leadership submits what he called a &ldquo;unified proposal&rdquo; to end the conflict. The decision came hours after Trump had told CNBC that he did not plan to extend the truce.',
            '&ldquo;Based on the fact that the Government of Iran is seriously fractured, not unexpectedly so and, upon the request of Field Marshal Asim Munir, and Prime Minister Shehbaz Sharif, of Pakistan, we have been asked to hold our Attack on the Country of Iran until such time as their leaders and representatives can come up with a unified proposal,&rdquo; Trump wrote. &ldquo;I have therefore directed our Military to continue the Blockade and, in all other respects, remain ready and able, and will therefore extend the Ceasefire until such time as their proposal is submitted, and discussions are concluded, one way or the other.&rdquo;',
            'The extension removes the immediate deadline pressure but also removes Iran&rsquo;s incentive to submit a proposal quickly. The U.S. naval blockade of Iranian ports remains in place, and has forced 28 ships to turn back since it began. Iran&rsquo;s Foreign Minister Seyed Abbas Araghchi has called the blockade &ldquo;an act of war and thus a violation of the ceasefire.&rdquo;',
            'Vice President JD Vance, who had been expected to travel to Islamabad for the next round of talks, remained at the White House Tuesday after Iran failed to confirm it would send a delegation. Pakistan&rsquo;s information minister Attaullah Tarar said a &ldquo;formal response from Iranian side about confirmation of delegation to attend Islamabad Peace Talks is still awaited.&rdquo;',
            'Reports from regional sources suggest an internal split in Tehran. Civilian leadership, including Parliament Speaker Mohammad Bagher Ghalibaf and FM Araghchi, favor continued negotiations. Islamic Revolutionary Guard Corps commanders oppose concessions as long as the U.S. naval blockade continues. This divide is reportedly behind Trump&rsquo;s reference to the &ldquo;seriously fractured&rdquo; Iranian government.',
            'Oil markets reacted sharply to the day&rsquo;s whipsaw. Brent crude futures briefly touched $101.15 intraday on reports that Vance had cancelled his Islamabad trip, then retreated after Trump&rsquo;s extension post. Brent settled +3% at $98.48; WTI settled +3% at $92.13. Monday closes had been +7% and +5%. The Strait of Hormuz remains functionally closed.',
        ],
        "related": [
            ("Hormuz Closed Again: Iran Reverses Course as Trump Refuses to Lift Blockade", "hormuz-closed-again-iran-reverses-course-as-trump-refuses-to-lift-blockade"),
            ("Trump Warns He May Not Extend Ceasefire, Threatens to Resume Bombing Iran", "trump-warns-he-may-not-extend-ceasefire-threatens-to-resume-bombing-iran"),
            ("U.S.-Iran Ceasefire Explained: Timeline, Terms, and Expiration", "us-iran-ceasefire-explained-timeline-terms-expiration"),
        ],
    },
    {
        "canonical_slug": "brent-touches-101-intraday-before-retreating-on-ceasefire-extension",
        "title_variants": [
            "Brent Spikes Above $100 Intraday Before Retreating on Ceasefire Extension News",
            "Brent Touches $101 Intraday Before Retreating on Ceasefire Extension",
            "Brent Touches $101 Intraday Before Retreating on Extension News",
            "WTI Settles +3% at $92.13, Brent +3% at $98.48 on Peace Talk Uncertainty",
        ],
        "display_title": "Brent Touches $101 Intraday Before Retreating on Ceasefire Extension",
        "category": "Oil Markets",
        "category_slug": "oil-prices",
        "date": "April 21, 2026",
        "read_time": "5 min",
        "meta_desc": "Brent briefly broke $100 on Vance-no-travel reports before retreating on Trump's ceasefire extension. WTI +3% at $92.13, Brent +3% at $98.48.",
        "paragraphs": [
            'Crude oil whipsawed through another volatile session Tuesday. Brent crude futures briefly spiked above $100 a barrel, touching an intraday session high of $101.15, when reports emerged that Vice President JD Vance had called off his planned trip to Islamabad for the next round of U.S.-Iran peace talks. Prices then retreated after President Trump&rsquo;s late-afternoon Truth Social post extending the ceasefire indefinitely.',
            'Brent settled +3% at $98.48 per barrel. U.S. benchmark West Texas Intermediate settled +3% at $92.13. Both benchmarks had closed Monday with larger gains &mdash; WTI +7% and Brent +5% &mdash; on the U.S. seizure of an Iranian cargo ship over the weekend.',
            'The intraday swing reflects how tightly oil prices are now tracking every headline out of Washington and Islamabad. &ldquo;This is still the largest oil supply shock in the history of the oil market,&rdquo; said Rory Johnston, founder of Commodity Context. Johnston said a sustained push above $100 Brent could unlock roughly 2.1 million barrels per day of new supply, but that Hormuz disruption continues anchoring prices at elevated levels.',
            'The WTI futures curve remains in steep backwardation through December 2026, signaling tight prompt physical markets. The Brent-WTI spread has widened as maritime risk premiums return, reflecting continued shipping uncertainty through the Strait of Hormuz. The U.S. naval blockade of Iranian ports, which has forced 28 ships to turn back, remains in place despite the ceasefire extension.',
            'OPEC+ is proceeding with its April 206,000 bpd output increase, but Gulf producers are watching IRGC threats against neighboring oil facilities closely. Iran&rsquo;s Revolutionary Guard warned Tuesday it would target oil infrastructure in any neighboring country that allows the U.S. to launch attacks on Iran from its territory, adding tail risk to regional crude flows.',
        ],
        "related": [
            ("Oil Prices Whipsaw on Hormuz Reversal — WTI Recovers From Friday's 11% Plunge", "oil-prices-whipsaw-on-hormuz-reversal-wti-recovers-from-fridays-11-plunge"),
            ("Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Iranian Government", "trump-extends-iran-ceasefire-indefinitely-citing-fractured-iranian-government"),
            ("Hormuz Closed Again: Iran Reverses Course as Trump Refuses to Lift Blockade", "hormuz-closed-again-iran-reverses-course-as-trump-refuses-to-lift-blockade"),
        ],
    },
    {
        "canonical_slug": "us-naval-blockade-of-iranian-ports-remains-in-place-despite-ceasefire-extension",
        "title_variants": [
            "U.S. Naval Blockade of Iranian Ports Remains in Place Despite Ceasefire Extension",
            "U.S. Navy Blockade Has Turned Back 28 Ships Since Beginning",
            "Strait of Hormuz Remains Functionally Closed Despite Extension",
        ],
        "display_title": "U.S. Naval Blockade of Iranian Ports Remains in Place Despite Ceasefire Extension",
        "category": "Geopolitics",
        "category_slug": "geopolitics",
        "date": "April 21, 2026",
        "read_time": "5 min",
        "meta_desc": "Trump's ceasefire extension keeps the U.S. naval blockade of Iranian ports in place. 28 ships have been turned back. Iran calls blockade an 'act of war.'",
        "paragraphs": [
            'President Trump&rsquo;s decision to extend the U.S.-Iran ceasefire indefinitely includes a critical caveat: the U.S. naval blockade of Iranian ports continues. &ldquo;I have therefore directed our Military to continue the Blockade and, in all other respects, remain ready and able,&rdquo; Trump wrote in his Tuesday Truth Social post.',
            'The U.S. military says it has forced 28 ships to turn back since the blockade began earlier this month. The blockade was imposed after an initial round of ceasefire talks in Islamabad ended without agreement. Trump ordered the measure to pressure Iran into reopening the Strait of Hormuz and to apply additional economic leverage.',
            'However, maritime data analysis firm Lloyd&rsquo;s List has tracked &ldquo;shadow fleet&rdquo; vessels continuing to move in and out of Iranian ports despite the blockade, suggesting enforcement is imperfect and Iran retains some export capacity through opaque channels.',
            'Iran&rsquo;s Foreign Minister Seyed Abbas Araghchi has repeatedly denounced the blockade. &ldquo;This constitutes a grave breach of international law, a clear violation of the ceasefire, and an act of aggression marked by the hallmarks of piracy,&rdquo; the Iranian mission to the U.N. wrote in a letter shared on X. The U.S. in turn has accused Iran of violating the ceasefire by firing on vessels in the strait.',
            'The blockade remains a central sticking point in negotiations. Iranian officials have signaled they want an end to the blockade and access to $6 billion in frozen assets before agreeing to broader terms. Trump has said he agreed to the original ceasefire on condition that the Strait of Hormuz be fully reopened &mdash; a condition Iran has not met.',
        ],
        "related": [
            ("Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Iranian Government", "trump-extends-iran-ceasefire-indefinitely-citing-fractured-iranian-government"),
            ("Iran FM Araghchi Calls U.S. Naval Blockade 'An Act of War' and Ceasefire Violation", "iran-fm-araghchi-calls-us-naval-blockade-an-act-of-war-and-ceasefire-violation"),
            ("Hormuz Closed Again: Iran Reverses Course as Trump Refuses to Lift Blockade", "hormuz-closed-again-iran-reverses-course-as-trump-refuses-to-lift-blockade"),
        ],
    },
    {
        "canonical_slug": "vances-islamabad-trip-put-on-hold-as-iran-fails-to-confirm-delegation",
        "title_variants": [
            "Vance's Islamabad Trip Put on Hold as Iran Fails to Confirm Delegation",
            "Vance Holds at White House as Iran Delays Delegation Confirmation",
            "Iran Still Hasn't Confirmed Delegation for Islamabad Talks",
        ],
        "display_title": "Vance's Islamabad Trip Put on Hold as Iran Fails to Confirm Delegation",
        "category": "Geopolitics",
        "category_slug": "geopolitics",
        "date": "April 21, 2026",
        "read_time": "5 min",
        "meta_desc": "VP Vance's planned Islamabad trip for U.S.-Iran peace talks was put on hold Tuesday after Iran failed to confirm a delegation. Talks remain possible at 'a moment's notice.'",
        "paragraphs": [
            'Vice President JD Vance remained at the White House Tuesday afternoon rather than boarding a flight to Islamabad for the anticipated second round of U.S.-Iran peace talks, after Iran failed to respond to American negotiating positions and did not confirm its delegation would attend.',
            'CNN reported Vance arrived at the White House early Tuesday afternoon as questions lingered over whether he would proceed with his planned travel. He was later seen by CNN cameras departing the White House at approximately 6 p.m. ET, having spent roughly five hours inside the West Wing.',
            'A White House official said Vance would not travel to Pakistan Tuesday and that &ldquo;any further updates on in-person meetings will be announced by the White House.&rdquo; A U.S. official with knowledge of the situation told The New York Times that the talks had not been cancelled, and the trip could happen &ldquo;at a moment&rsquo;s notice.&rdquo;',
            'Pakistan, which has been mediating between Washington and Tehran, confirmed it was still waiting on Iran. &ldquo;Formal response from Iranian side about confirmation of delegation to attend Islamabad Peace Talks is still awaited,&rdquo; Pakistan&rsquo;s Information Minister Attaullah Tarar wrote on social media. He said Pakistan as &ldquo;mediator is in constant touch with Iranians and pursuing the path of diplomacy and dialogue.&rdquo;',
            'The earlier round of negotiations, a 21-hour marathon session in Islamabad on April 11, ended without agreement. Vice President Vance blamed Iran for refusing to commit to forgoing a nuclear weapon. &ldquo;We need to see an affirmative commitment that they will not seek a nuclear weapon, and they will not seek the tools that would enable them to quickly achieve a nuclear weapon,&rdquo; Vance said at the time. For Tehran, key demands for extending the ceasefire include ending the U.S. naval blockade of Iranian ports and guarantees that Israel-Hezbollah fighting will not resume.',
        ],
        "related": [
            ("Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Iranian Government", "trump-extends-iran-ceasefire-indefinitely-citing-fractured-iranian-government"),
            ("21-Hour Marathon Talks End Without Deal, Vance Departs Pakistan Blaming Iran", "21-hour-marathon-talks-end-without-deal-vance-departs-pakistan-blaming-iran"),
            ("U.S.-Iran Ceasefire Explained: Timeline, Terms, and Expiration", "us-iran-ceasefire-explained-timeline-terms-expiration"),
        ],
    },
    {
        "canonical_slug": "hezbollah-fires-rockets-at-israeli-troops-in-southern-lebanon-violating-ceasefire",
        "title_variants": [
            "Hezbollah Fires Rockets at Israeli Troops in Southern Lebanon, Violating Ceasefire",
            "Hezbollah Fires Rockets at Israeli Troops in Southern Lebanon",
            "Hezbollah Rocket Fire Breaches 10-Day Ceasefire with Israel",
        ],
        "display_title": "Hezbollah Fires Rockets at Israeli Troops in Southern Lebanon, Violating Ceasefire",
        "category": "Geopolitics",
        "category_slug": "geopolitics",
        "date": "April 21, 2026",
        "read_time": "4 min",
        "meta_desc": "Israeli military says Hezbollah fired rockets at Israeli troops in southern Lebanon Tuesday, breaching the 10-day ceasefire ahead of U.S.-mediated talks.",
        "paragraphs": [
            'The Israeli military said Tuesday that Hezbollah had fired rockets at Israeli troops in southern Lebanon, the first major breach of the 10-day Israel-Lebanon ceasefire that began April 16. The attack came ahead of U.S.-mediated talks between the Israeli and Lebanese governments scheduled for this week.',
            'There was no immediate comment from Hezbollah, though the Iran-backed group has previously said it reserves the right to respond to any Israeli action it perceives as aggressive. The ceasefire terms allow Israel to respond only to &ldquo;imminent threats from Hezbollah,&rdquo; a formulation the group has disputed.',
            'Lebanese Prime Minister Nawaf Salam addressed the situation Tuesday at a joint press conference in Paris with French President Emmanuel Macron. Salam said Lebanon &ldquo;isn&rsquo;t seeking a confrontation with Hezbollah but won&rsquo;t be intimidated&rdquo; by the Iran-backed militia either. Salam&rsquo;s government has struggled to assert authority over Hezbollah-controlled areas of southern Lebanon since the ceasefire took effect.',
            'The breach comes days after a French UN peacekeeper was killed in southern Lebanon on the second day of the ceasefire, an incident France attributed to Hezbollah. The accumulating violations have raised concerns that the 10-day truce will not hold through its scheduled end, and that continued Israel-Lebanon friction will further complicate the parallel U.S.-Iran negotiations &mdash; Iran backs Hezbollah, and regional tensions are deeply interconnected.',
            'The Lebanon front adds a second layer of complication to Trump&rsquo;s Tuesday decision to extend the U.S.-Iran ceasefire indefinitely. Tehran has demanded guarantees that fighting between Israel and Hezbollah will not resume as part of any comprehensive U.S.-Iran deal, making developments in southern Lebanon directly relevant to Hormuz and blockade negotiations.',
        ],
        "related": [
            ("Israel-Lebanon 10-Day Ceasefire Takes Effect, Hezbollah Holds Fire", "israel-lebanon-10-day-ceasefire-takes-effect-hezbollah-holds-fire"),
            ("French UN Peacekeeper Killed in Lebanon Attack, Macron Blames Hezbollah", "french-un-peacekeeper-killed-in-lebanon-attack-macron-blames-hezbollah"),
            ("Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Iranian Government", "trump-extends-iran-ceasefire-indefinitely-citing-fractured-iranian-government"),
        ],
    },
    {
        "canonical_slug": "irgc-threatens-to-target-oil-facilities-in-neighboring-countries-hosting-us-attacks",
        "title_variants": [
            "Iran's IRGC Threatens to Target Oil Facilities in Neighboring Countries Hosting U.S. Attacks",
            "IRGC Threatens to Target Oil Facilities in Neighboring Countries Hosting U.S. Attacks",
            "IRGC Threatens Oil Facilities in Neighboring Countries",
            "IRGC Threatens Oil Facilities in Neighboring Host Countries",
        ],
        "display_title": "IRGC Threatens to Target Oil Facilities in Neighboring Countries Hosting U.S. Attacks",
        "category": "Geopolitics",
        "category_slug": "geopolitics",
        "date": "April 21, 2026",
        "read_time": "5 min",
        "meta_desc": "Iran's Revolutionary Guard warned it would target oil facilities in neighboring countries that allow U.S. attacks from their territory. Gulf producers on high alert.",
        "paragraphs": [
            'Iran&rsquo;s Islamic Revolutionary Guard Corps (IRGC) threatened Tuesday to target oil facilities in neighboring countries if those nations allow the United States to resume launching attacks on Iran from their territory. The warning adds significant tail risk to Gulf oil infrastructure and has put regional producers on heightened alert.',
            'The threat follows ongoing IRGC statements warning against any resumption of direct U.S. military action. The Revolutionary Guard has positioned itself as the primary hawkish voice in Tehran, and according to regional sources, its commanders have opposed concessions to the U.S. as long as the naval blockade of Iranian ports continues.',
            'Gulf Cooperation Council states &mdash; including Saudi Arabia, Kuwait, the UAE, Bahrain, and Qatar &mdash; have hosted U.S. military installations for decades. Any targeting of oil infrastructure in these countries would represent a major escalation and directly threaten global oil supply. Saudi Arabia&rsquo;s Abqaiq facility, which handles 5% of global oil processing, was damaged by drone strikes earlier in the conflict, demonstrating that regional facilities remain vulnerable.',
            'The threat echoes Iran&rsquo;s 2019 strikes on Abqaiq and Khurais facilities, which temporarily removed 5.7 million barrels per day of Saudi production from global markets. Current IRGC posture suggests similar actions are under active consideration should the ceasefire collapse.',
            'The oil market has partly priced this risk, with Brent crude trading above $98 per barrel &mdash; well above pre-conflict levels despite OPEC+ continuing its 206,000 barrel-per-day April output increase. Rystad Energy warned that sustained $100 Brent could unlock additional supply, but the threat to Gulf infrastructure means prices may need to climb further to curb demand if any strikes materialize.',
        ],
        "related": [
            ("Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Iranian Government", "trump-extends-iran-ceasefire-indefinitely-citing-fractured-iranian-government"),
            ("Abqaiq Facility Hit", "abqaiq-facility-hit"),
            ("Hormuz Closed Again: Iran Reverses Course as Trump Refuses to Lift Blockade", "hormuz-closed-again-iran-reverses-course-as-trump-refuses-to-lift-blockade"),
        ],
    },
    {
        "canonical_slug": "iran-fm-araghchi-calls-us-naval-blockade-an-act-of-war-and-ceasefire-violation",
        "title_variants": [
            "Iran FM Araghchi Calls U.S. Naval Blockade 'An Act of War' and Ceasefire Violation",
        ],
        "display_title": "Iran FM Araghchi Calls U.S. Naval Blockade 'An Act of War' and Ceasefire Violation",
        "category": "Geopolitics",
        "category_slug": "geopolitics",
        "date": "April 21, 2026",
        "read_time": "4 min",
        "meta_desc": "Iran's Foreign Minister Seyed Abbas Araghchi denounced the U.S. naval blockade of Iranian ports as 'an act of war' and a clear violation of the ceasefire.",
        "paragraphs": [
            'Iran&rsquo;s Foreign Minister Seyed Abbas Araghchi on Tuesday condemned the U.S. naval blockade of Iranian ports as &ldquo;an act of war and thus a violation of the ceasefire.&rdquo; The denunciation, published on social media and in a letter to the United Nations, came as President Trump extended the ceasefire indefinitely while keeping the blockade in place.',
            '&ldquo;Iran knows how to neutralize restrictions, how to defend its interests, and how to resist bullying,&rdquo; Araghchi wrote in his social media post Tuesday. He called the U.S. seizure of an Iranian cargo ship in the Arabian Sea over the weekend &ldquo;an even greater violation&rdquo; of the ceasefire terms.',
            'The Iranian mission to the United Nations shared a letter on X characterizing the blockade as &ldquo;a grave breach of international law, a clear violation of the ceasefire, and an act of aggression marked by the hallmarks of piracy.&rdquo; The escalating rhetoric comes as Tehran has yet to confirm whether it will send a delegation to the next round of talks in Islamabad.',
            'Araghchi is part of Iran&rsquo;s civilian negotiating team, which reportedly favors continued diplomacy despite hardline opposition from the Islamic Revolutionary Guard Corps. The gap between the civilian diplomatic track and the IRGC military track is believed to be part of what Trump described as Iran&rsquo;s &ldquo;seriously fractured&rdquo; government in announcing the ceasefire extension.',
            'For Tehran, the key demands for any deal include ending the U.S. naval blockade, access to $6 billion in frozen assets, and guarantees that Israel-Hezbollah fighting will not resume. The blockade has forced 28 ships to turn back since it began and remains the most concrete pressure point in U.S. leverage over Iran.',
        ],
        "related": [
            ("U.S. Naval Blockade of Iranian Ports Remains in Place Despite Ceasefire Extension", "us-naval-blockade-of-iranian-ports-remains-in-place-despite-ceasefire-extension"),
            ("Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Iranian Government", "trump-extends-iran-ceasefire-indefinitely-citing-fractured-iranian-government"),
            ("Hormuz Closed Again: Iran Reverses Course as Trump Refuses to Lift Blockade", "hormuz-closed-again-iran-reverses-course-as-trump-refuses-to-lift-blockade"),
        ],
    },
    {
        "canonical_slug": "energy-stocks-mixed-as-ceasefire-extension-eases-but-blockade-stays",
        "title_variants": [
            "Energy Stocks Mixed as Ceasefire Extension Eases but Blockade Stays",
        ],
        "display_title": "Energy Stocks Mixed as Ceasefire Extension Eases but Blockade Stays",
        "category": "Company News",
        "category_slug": "company-news",
        "date": "April 21, 2026",
        "read_time": "4 min",
        "meta_desc": "Energy sector stocks traded mixed Tuesday as Trump's ceasefire extension eased geopolitical tension but the continuing blockade kept supply-disruption premiums elevated.",
        "paragraphs": [
            'Energy sector stocks traded mixed Tuesday afternoon as investors digested President Trump&rsquo;s decision to extend the U.S.-Iran ceasefire indefinitely while maintaining the U.S. naval blockade of Iranian ports. The extension eased some of the day&rsquo;s earlier geopolitical tension but kept the supply-disruption premium embedded in energy equities intact.',
            'Major integrated oil companies tracked crude&rsquo;s intraday volatility. Shares of ExxonMobil, Chevron, ConocoPhillips, and Occidental Petroleum initially jumped with Brent&rsquo;s spike above $100, then pared gains as prices retreated. Refining stocks held a more stable bid as crack spreads remained favorable in the $27-30/bbl range.',
            'LNG-focused names including Cheniere Energy and Venture Global continued to benefit from the ongoing disruption of Qatari liquefied natural gas flows through the Strait of Hormuz. European buyers have returned to premium bidding for U.S. cargoes, and U.S. export terminals are operating near full capacity at roughly 14 Bcf/d.',
            'Shipping stocks moved in the opposite direction. Maersk and Hapag-Lloyd have maintained their Hormuz transit suspensions despite the ceasefire extension, and reshuffled global container schedules continue to pressure freight economics. Marine insurance rates remain elevated, adding $1-2 per barrel to effective Middle East crude costs.',
            'Traders described Tuesday&rsquo;s action as consistent with a market that has moved past the immediate-deadline trade and is now pricing a longer, ambiguous standoff. Options implied volatility across the energy complex remains well above trailing 30-day realized levels, reflecting continued uncertainty over whether the ceasefire will ultimately produce a durable peace or collapse into renewed conflict.',
        ],
        "related": [
            ("Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Iranian Government", "trump-extends-iran-ceasefire-indefinitely-citing-fractured-iranian-government"),
            ("Brent Touches $101 Intraday Before Retreating on Ceasefire Extension", "brent-touches-101-intraday-before-retreating-on-ceasefire-extension"),
            ("Cheniere Energy, Venture Global Ride LNG Premium as Qatar Flows Still Disrupted", "cheniere-energy-venture-global-ride-lng-premium-as-qatar-flows-still-disrupted"),
        ],
    },
    {
        "canonical_slug": "maersk-hapag-lloyd-maintain-hormuz-transit-suspension-amid-continued-uncertainty",
        "title_variants": [
            "Maersk, Hapag-Lloyd Maintain Hormuz Transit Suspension Amid Continued Uncertainty",
        ],
        "display_title": "Maersk, Hapag-Lloyd Maintain Hormuz Transit Suspension Amid Continued Uncertainty",
        "category": "Company News",
        "category_slug": "company-news",
        "date": "April 21, 2026",
        "read_time": "4 min",
        "meta_desc": "Global shipping giants Maersk and Hapag-Lloyd are maintaining their Hormuz transit suspensions despite the ceasefire extension. Vessels continuing to route around Africa.",
        "paragraphs": [
            'Global container shipping giants A.P. Moller-Maersk and Hapag-Lloyd confirmed Tuesday they are maintaining suspensions on Hormuz transits despite President Trump&rsquo;s decision to extend the U.S.-Iran ceasefire indefinitely. The shipping industry&rsquo;s continued caution reflects the underlying reality that the Strait of Hormuz remains functionally closed, and the U.S. naval blockade of Iranian ports remains in place.',
            'Both carriers cited continued threats to commercial shipping, including Iranian Revolutionary Guard warnings that vessels approaching the strait will be &ldquo;treated as cooperating with the enemy.&rdquo; The IRGC&rsquo;s gunboats fired on Indian-flagged tankers Sanmar Herald and MSC Ishyka earlier in the conflict, and a separate container ship was struck by an unknown projectile off the Oman coast.',
            'The suspensions mean Asia-Europe and Middle East-origin container traffic continues to route around the Cape of Good Hope, adding 10-14 days per voyage and significant fuel costs. Industry-wide, the rerouting has removed effective shipping capacity from the market just as global goods trade is entering a seasonal buildup.',
            'Marine insurance premiums for Gulf transits remain at 1-2% of hull value, a level that makes some commercial routes economically unviable without government indemnification. Several shipowners have requested that flag-state insurers or export credit agencies underwrite residual risk, but broad-based solutions have not materialized.',
            'The shipping industry&rsquo;s posture serves as a real-time signal of how credible the ceasefire actually is. When Maersk, Hapag-Lloyd, MSC, and CMA CGM lift their Hormuz suspensions, the market will treat that as a genuine de-escalation signal. Until then, the supply-chain impact of the crisis continues regardless of diplomatic statements.',
        ],
        "related": [
            ("Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Iranian Government", "trump-extends-iran-ceasefire-indefinitely-citing-fractured-iranian-government"),
            ("Hormuz Closed Again: Iran Reverses Course as Trump Refuses to Lift Blockade", "hormuz-closed-again-iran-reverses-course-as-trump-refuses-to-lift-blockade"),
            ("U.S. Naval Blockade of Iranian Ports Remains in Place Despite Ceasefire Extension", "us-naval-blockade-of-iranian-ports-remains-in-place-despite-ceasefire-extension"),
        ],
    },
    {
        "canonical_slug": "saudi-aramco-east-west-pipeline-continues-at-full-capacity-through-blockade",
        "title_variants": [
            "Saudi Aramco East-West Pipeline Continues at Full Capacity Through Blockade",
        ],
        "display_title": "Saudi Aramco East-West Pipeline Continues at Full Capacity Through Blockade",
        "category": "Company News",
        "category_slug": "company-news",
        "date": "April 21, 2026",
        "read_time": "4 min",
        "meta_desc": "Saudi Aramco's East-West Pipeline continues operating at full 5 million bpd capacity, bypassing Hormuz and delivering crude to Red Sea port of Yanbu for export.",
        "paragraphs": [
            'Saudi Aramco&rsquo;s East-West Pipeline continues operating at its full 5 million barrels per day capacity, serving as the kingdom&rsquo;s critical bypass around the Strait of Hormuz chokepoint. The pipeline moves crude from eastern Saudi fields to the Red Sea port of Yanbu, where vessels can load for European and Asian markets without transiting the disputed strait.',
            'The pipeline was damaged by drone strikes on April 8 but was restored to full capacity by April 12. Aramco has since hardened infrastructure protections and coordinated security with Gulf partners, significantly reducing the risk of additional attacks succeeding against hardened facilities.',
            'With Hormuz functionally closed and the U.S. naval blockade of Iranian ports continuing, the East-West Pipeline has become increasingly important to global crude flows. Saudi Arabia has been running the pipeline near its design limit for weeks, and the kingdom has confirmed it is prepared to sustain this posture as long as Hormuz disruption continues.',
            'However, the pipeline cannot fully replace Hormuz flows. At 5 million bpd, it represents roughly a quarter of normal Hormuz-traffic volumes. Other Gulf producers &mdash; Kuwait, the UAE, Qatar, Iraq, and Bahrain &mdash; have limited or no pipeline alternatives to Hormuz, meaning their crude remains stranded or forced to transit via more expensive and slower routes.',
            'Saudi Aramco shares traded modestly higher in Riyadh Tuesday as investors weighed the company&rsquo;s operational resilience against the broader regional risk. The company&rsquo;s Q1 dividend of approximately $25 billion to the Saudi government and international shareholders was affirmed, reflecting confidence in continued production and cash flow through the conflict.',
        ],
        "related": [
            ("Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Iranian Government", "trump-extends-iran-ceasefire-indefinitely-citing-fractured-iranian-government"),
            ("Hormuz Closed Again: Iran Reverses Course as Trump Refuses to Lift Blockade", "hormuz-closed-again-iran-reverses-course-as-trump-refuses-to-lift-blockade"),
            ("Maersk, Hapag-Lloyd Maintain Hormuz Transit Suspension Amid Continued Uncertainty", "maersk-hapag-lloyd-maintain-hormuz-transit-suspension-amid-continued-uncertainty"),
        ],
    },
    {
        "canonical_slug": "cheniere-energy-venture-global-ride-lng-premium-as-qatar-flows-still-disrupted",
        "title_variants": [
            "Cheniere Energy, Venture Global Ride LNG Premium as Qatar Flows Still Disrupted",
        ],
        "display_title": "Cheniere Energy, Venture Global Ride LNG Premium as Qatar Flows Still Disrupted",
        "category": "Company News",
        "category_slug": "company-news",
        "date": "April 21, 2026",
        "read_time": "4 min",
        "meta_desc": "U.S. LNG exporters Cheniere and Venture Global benefit from continued Qatari LNG disruption through Hormuz. Terminals running near 14 Bcf/d capacity.",
        "paragraphs": [
            'U.S. liquefied natural gas exporters Cheniere Energy and Venture Global continue to benefit from the ongoing disruption of Qatari LNG flows through the Strait of Hormuz. Both companies are operating their U.S. Gulf Coast export terminals at near-capacity levels, with combined U.S. LNG exports running close to 14 Bcf/d.',
            'Qatar accounts for roughly 20% of global LNG supply. With Hormuz functionally closed and the U.S. naval blockade of Iranian ports continuing, Qatari loadings remain constrained. European buyers &mdash; who had increasingly relied on Qatari cargoes to diversify away from Russian pipeline gas &mdash; have returned to premium bidding for U.S. volumes, pushing up both JKM (Asian) and TTF (European) benchmark prices.',
            'Cheniere operates the Sabine Pass facility in Louisiana and Corpus Christi in Texas. The company has indicated it can sustain current export rates through the conflict and is evaluating additional capacity expansions as long-term customers lock in higher take-or-pay volumes. Venture Global&rsquo;s Calcasieu Pass and Plaquemines facilities are similarly committed.',
            'The European Union&rsquo;s transport commissioner said Tuesday the bloc is preparing guidance to airlines on handling airport slots, passenger rights, and public service obligations in the event of jet fuel shortages &mdash; a downstream consequence of continued Middle East refinery disruptions. German Economy Minister Katherina Reiche said jet fuel supplies are not yet in danger but that the government is monitoring the situation.',
            'U.S. LNG equities outperformed the broader energy sector Tuesday as investors priced in continued premium pricing. NextDecade and other projects at various stages of development have reported strong interest from European offtakers seeking to secure supply for the 2027-2030 period, when several major new capacity additions are scheduled to come online.',
        ],
        "related": [
            ("Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Iranian Government", "trump-extends-iran-ceasefire-indefinitely-citing-fractured-iranian-government"),
            ("Energy Stocks Mixed as Ceasefire Extension Eases but Blockade Stays", "energy-stocks-mixed-as-ceasefire-extension-eases-but-blockade-stays"),
            ("Hormuz Closed Again: Iran Reverses Course as Trump Refuses to Lift Blockade", "hormuz-closed-again-iran-reverses-course-as-trump-refuses-to-lift-blockade"),
        ],
    },
    {
        "canonical_slug": "opec-april-output-increase-proceeding-despite-market-volatility",
        "title_variants": [
            "OPEC+ April Output Increase Proceeding Despite Market Volatility",
        ],
        "display_title": "OPEC+ April Output Increase Proceeding Despite Market Volatility",
        "category": "Oil Markets",
        "category_slug": "oil-prices",
        "date": "April 21, 2026",
        "read_time": "5 min",
        "meta_desc": "OPEC+ is proceeding with its 206,000 bpd April output increase despite Iran conflict volatility. No emergency meeting called. Gulf producers monitor IRGC threats.",
        "paragraphs": [
            'OPEC+ is proceeding with its previously announced 206,000 barrel-per-day April production increase despite ongoing volatility tied to the U.S.-Iran conflict, the group confirmed Tuesday. No emergency Joint Ministerial Monitoring Committee (JMMC) meeting has been called, and Saudi Arabia continues to balance market-share considerations against price-support concerns in its public positioning.',
            'The April increase reflects the gradual unwinding of earlier voluntary cuts that had removed roughly 1.65 million bpd from global supply during 2025. The pace of restoration has been slowed by the conflict, which has both reduced physical Middle East supply through the Hormuz disruption and elevated prices, creating political pressure for OPEC+ to add barrels.',
            'Saudi Arabia&rsquo;s East-West Pipeline continues to operate at its full 5 million bpd capacity, allowing the kingdom to export despite Hormuz uncertainty. Other Gulf producers &mdash; Kuwait, the UAE, Iraq, and Qatar &mdash; have more limited bypass options, and their output has been effectively constrained by strait access even when their production facilities are physically operational.',
            'The IRGC&rsquo;s Tuesday threat to target oil facilities in neighboring countries that allow U.S. attacks has introduced a new layer of risk. Gulf producers are monitoring the situation closely, and several have quietly stepped up physical security at export terminals, processing facilities, and key pipeline nodes. Saudi Arabia&rsquo;s Abqaiq facility, which handles 5% of global oil processing, was damaged by drone strikes earlier in the conflict.',
            'May production decisions remain in flux. OPEC+ officials have signaled they stand ready to act if Hormuz disruption extends, whether by formally pausing the output increase or by calling an emergency meeting. For now, the group is prioritizing predictability, betting that maintaining the announced path avoids signaling either panic or complacency. The next scheduled ministerial meeting is in early May.',
        ],
        "related": [
            ("Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Iranian Government", "trump-extends-iran-ceasefire-indefinitely-citing-fractured-iranian-government"),
            ("April 206K bpd Increase Proceeds", "april-206k-bpd-increase-proceeds"),
            ("What Is OPEC+ and How Does It Affect Oil Prices?", "what-is-opec-plus-how-it-affects-oil-prices"),
        ],
    },
    {
        "canonical_slug": "us-iran-ceasefire-explained-timeline-terms-and-extension",
        "title_variants": [
            "U.S.-Iran Ceasefire Explained: Timeline, Terms, and Extension",
        ],
        "display_title": "U.S.-Iran Ceasefire Explained: Timeline, Terms, and Extension",
        "category": "Geopolitics",
        "category_slug": "geopolitics",
        "date": "April 21, 2026",
        "read_time": "6 min",
        "meta_desc": "Complete timeline of the U.S.-Iran ceasefire: how it began, the key terms, Trump's April 21 indefinite extension, and what markets expect next.",
        "paragraphs": [
            'The U.S.-Iran ceasefire originated from Pakistan-mediated negotiations in early April 2026, after approximately 50 days of conflict that began on February 28, 2026. The initial two-week ceasefire was intended to create space for a comprehensive peace deal addressing Iran&rsquo;s nuclear program, the Strait of Hormuz, U.S. military deployments, and sanctions relief.',
            '<strong>Initial terms (April 8).</strong> Both sides agreed to halt direct military action. Iran would take steps to reopen the Strait of Hormuz to commercial traffic. The United States would pause planned attacks on Iranian infrastructure and consider easing certain sanctions. A 21-hour marathon negotiating session in Islamabad on April 11 failed to produce a comprehensive agreement, and the U.S. subsequently ordered a naval blockade of Iranian ports.',
            '<strong>The April 17-18 whipsaw.</strong> Iran&rsquo;s Foreign Minister Araghchi declared the Strait of Hormuz &ldquo;completely open&rdquo; on April 17, triggering an 11% single-day crash in WTI crude prices. Within 24 hours, Iran reversed course and reimposed &ldquo;strict control&rdquo; over the strait, citing the continued U.S. blockade as a ceasefire violation. IRGC gunboats fired on Indian-flagged tankers, and a container ship was struck by an unidentified projectile off Oman.',
            '<strong>The April 21 extension.</strong> President Trump extended the ceasefire indefinitely via Truth Social on the afternoon of April 21, citing what he called a &ldquo;seriously fractured&rdquo; Iranian government and a request from Pakistan&rsquo;s Field Marshal Asim Munir and Prime Minister Shehbaz Sharif. Importantly, the U.S. naval blockade remains in place &mdash; it is not being lifted as part of the extension. The blockade has turned back 28 ships since it began.',
            '<strong>Key sticking points.</strong> For Washington, Iran&rsquo;s nuclear program remains the central concern. Vice President Vance has said the U.S. needs &ldquo;an affirmative commitment that they will not seek a nuclear weapon.&rdquo; For Tehran, the key demands are an end to the U.S. naval blockade, access to $6 billion in frozen assets, and guarantees that Israel-Hezbollah fighting will not resume. Reports of a civilian-IRGC split in Tehran complicate efforts to produce a unified Iranian negotiating position.',
            '<strong>Market implications.</strong> An indefinite extension without a deadline removes immediate escalation risk but also removes urgency for a comprehensive agreement. Oil prices remain elevated &mdash; Brent around $98, WTI around $92 &mdash; with the Hormuz risk premium embedded in prices. A collapse would likely send Brent toward the $110-120 range; a genuine breakthrough with Hormuz reopened and blockade lifted could push WTI back toward $70. For now, markets are pricing a protracted, ambiguous standoff.',
        ],
        "related": [
            ("Trump Extends Iran Ceasefire Indefinitely, Citing 'Seriously Fractured' Iranian Government", "trump-extends-iran-ceasefire-indefinitely-citing-fractured-iranian-government"),
            ("Hormuz Closed Again: Iran Reverses Course as Trump Refuses to Lift Blockade", "hormuz-closed-again-iran-reverses-course-as-trump-refuses-to-lift-blockade"),
            ("What Happens If the Strait of Hormuz Closes?", "what-happens-if-the-strait-of-hormuz-closes"),
        ],
    },
]


# ─── Template ──────────────────────────────────────────────────────
def render_article(story):
    slug = story["canonical_slug"]
    title = story["display_title"]
    # Escape single quotes in title for HTML title attribute
    title_safe = title.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    meta_desc = story["meta_desc"].replace('"', '&quot;')
    category = story["category"]
    cat_slug = story["category_slug"]
    # Determine category link URL
    if cat_slug in ("oil-prices", "rig-count", "oil-futures", "markets"):
        cat_url = f"../{cat_slug}.html"
    else:
        cat_url = f"../category/{cat_slug}.html"

    paragraphs_html = "\n          ".join(f"<p>{p}</p>" for p in story["paragraphs"])
    related_html = ""
    if story.get("related"):
        items = []
        for rel_title, rel_slug in story["related"]:
            items.append(f'<li><a href="{rel_slug}.html" style="color:var(--blue);text-decoration:none">{rel_title}</a></li>')
        related_html = (
            '<div style="margin-top:40px;padding:24px;background:var(--surface-2);border-radius:10px;border-left:3px solid var(--blue)">\n'
            '          <h3 style="margin:0 0 12px 0;font-size:14px;text-transform:uppercase;letter-spacing:0.06em;color:var(--text-2)">Related Coverage</h3>\n'
            '          <ul style="margin:0;padding-left:20px;line-height:1.8">\n            '
            + '\n            '.join(items)
            + '\n          </ul>\n        </div>'
        )

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','957762016897581');fbq('track','PageView');</script><noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=957762016897581&ev=PageView&noscript=1"/></noscript>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>{title_safe} | EnergyPricesToday</title>
  <meta name="description" content="{meta_desc}">
  <link rel="canonical" href="https://www.energypricestoday.com/articles/{slug}.html">
  <meta property="og:type" content="article"><meta property="og:title" content="{title_safe} | EnergyPricesToday">
  <meta property="og:description" content="{meta_desc}">
  <link rel="stylesheet" href="../css/styles.css">
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
          <a href="{cat_url}" style="color:var(--text-2);text-decoration:none">{category}</a>
          <span style="color:var(--text-3)">&rsaquo;</span>
          <span style="color:var(--text-2)">Article</span>
        </nav>
        <h1>{title_safe}</h1>
        <div class="article-meta" style="margin:14px 0 24px"><span>Staff</span><span>{story["date"]}</span><span>{story["read_time"]} read</span></div>
        <div class="article-body">
          {paragraphs_html}
        </div>

        {related_html}

        <div style="margin-top:32px;padding-top:20px;border-top:1px solid var(--border);display:flex;gap:12px;flex-wrap:wrap">
          <a href="../oil-prices.html" class="btn-secondary">Oil Prices</a>
          <a href="../category/gas-prices.html" class="btn-secondary">Gas Prices</a>
          <a href="../electricity-prices.html" class="btn-secondary">Electricity Rates</a>
          <a href="../category/geopolitics.html" class="btn-secondary">Geopolitics</a>
          <a href="../markets.html" class="btn-secondary">Markets</a>
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
'''


# ─── Slug map update ──────────────────────────────────────────────
def update_slug_map():
    """Inject every title_variant → canonical_slug mapping into ARTICLE_SLUGS."""
    current = SLUGS_FILE.read_text(encoding="utf-8")

    # Build the new entries. We'll insert them just before the closing `};`
    # of ARTICLE_SLUGS. Use double-backslashes for apostrophes in JS string keys.
    new_entries = []
    for story in STORIES:
        canonical = story["canonical_slug"]
        for variant in story["title_variants"]:
            # Escape the title for a JS string literal: double-quote safe
            escaped = variant.replace("\\", "\\\\").replace('"', '\\"')
            new_entries.append(f'  "{escaped}": "{canonical}"')

    # Dedupe — keep first occurrence
    seen = set()
    deduped = []
    for entry in new_entries:
        key = entry.split('":')[0]
        if key in seen:
            continue
        seen.add(key)
        deduped.append(entry)

    # Find ARTICLE_SLUGS = {...}; and insert before the closing
    # Look for the last entry line before `};`
    match = re.search(r'(const ARTICLE_SLUGS\s*=\s*\{)(.+?)(\n\};)', current, re.DOTALL)
    if not match:
        print("ERROR: couldn't find ARTICLE_SLUGS block")
        return False

    header = match.group(1)
    body = match.group(2)
    footer = match.group(3)

    # Remove any existing entries with the same keys (to avoid duplicates across re-runs)
    for entry in deduped:
        key = entry.split('":')[0] + '":'
        # Remove lines that start with this exact key
        body = re.sub(r'^\s*' + re.escape(key) + r'[^\n]*\n', '', body, flags=re.MULTILINE)

    # Append new entries
    new_block = header + body.rstrip() + ',\n' + ',\n'.join(deduped) + '\n' + footer
    # Replace in the file
    updated = current[:match.start()] + new_block + current[match.end():]
    SLUGS_FILE.write_text(updated, encoding="utf-8")
    print(f"✓ Updated ARTICLE_SLUGS with {len(deduped)} title → slug mappings")
    return True


# ─── Main ─────────────────────────────────────────────────────────
def main():
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)

    # Generate article files
    created = 0
    skipped = 0
    for story in STORIES:
        slug = story["canonical_slug"]
        path = ARTICLES_DIR / f"{slug}.html"
        if path.exists():
            print(f"SKIP (exists): {slug}.html")
            skipped += 1
            continue
        html = render_article(story)
        path.write_text(html, encoding="utf-8")
        print(f"✓ Created: {slug}.html ({len(html)} bytes)")
        created += 1

    print(f"\n{created} articles created, {skipped} skipped")

    # Update slug map
    update_slug_map()


if __name__ == "__main__":
    main()
