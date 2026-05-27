#!/usr/bin/env python3
"""
Hub refresh — update country/topic hubs with current verified context.

For each hub, replaces the "Current Context" box content with current
(May 22, 2026) framing, and adds a "Last reviewed" indicator.

All content is grounded in real, verified May 21-22 reporting.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "articles"

# ─── Per-hub current context (verified May 17, 2026) ──────────────────
HUBS = {
    "iran.html": {
        "context": "Current state (May 26, 2026): The diplomatic track has shifted decisively. President Trump said Saturday on Truth Social that a U.S.-Iran agreement has been \u201Clargely negotiated\u201D and that the Strait of Hormuz will be reopened. The framework under discussion is a 60-day ceasefire-extension MOU during which Iran clears the naval mines it deployed, the U.S. lifts its blockade, and the strait operates with no tolls; parallel negotiations begin on Iran\u2019s uranium stockpile and frozen Iranian assets. U.S. CENTCOM conducted defensive strikes in southern Iran Tuesday targeting missile sites and mine-laying boats; IRGC claimed F-35 engagement. Iran\u2019s foreign ministry Tuesday: navigation \u201Cwill have costs.\u201D Iran\u2019s 87-day internet blackout partially lifted today. Rubio: deal could take \u201Cseveral more days.\u201D",
        "lead_articles": [
            ("Trump: U.S.-Iran Agreement \u2018Largely Negotiated\u2019; Strait of Hormuz to Reopen Under 60-Day Framework", "trump-iran-agreement-largely-negotiated-60-day-hormuz-framework.html", "May 26, 2026",
             "Trump said Saturday on Truth Social that an agreement involving the U.S., Iran, and several regional countries had been \u201Clargely negotiated.\u201D The framework: 60-day ceasefire extension during which Iran clears mines, U.S. lifts blockade, and Hormuz operates with no tolls."),
            ("U.S. CENTCOM Conducts Defensive Strikes in Southern Iran; IRGC Claims F-35 Engagement", "us-centcom-defensive-strikes-southern-iran-irgc-f35-claim.html", "May 26, 2026",
             "U.S. Central Command said Tuesday it conducted \u201Cself-defense strikes\u201D in southern Iran, targeting missile launch sites and Iranian boats attempting to emplace mines. Iran\u2019s IRGC claimed it engaged an F-35 in Iranian airspace."),
        ],
    },
    "saudi-arabia.html": {
        "context": "Current state (May 26, 2026): Saudi Arabia is among the regional partners (alongside Pakistan, Qatar, UAE, Turkey, Egypt, Jordan, Bahrain) pressing Washington to accept the U.S.-Iran 60-day MOU framework. Trump (May 24): agreement \u201Clargely negotiated\u201D; Strait of Hormuz will reopen. Saudi Aramco CEO Amin Nasser previously warned market normalization is pushed to 2027 if Hormuz reopening is delayed past mid-June; the proposed framework just barely meets that timing if signed quickly. Saudi production remains at the lowest level since 1990. Brent traded around $98-$99 Tuesday near five-week lows on deal-progression news.",
        "lead_articles": [
            ("Trump: U.S.-Iran Agreement \u2018Largely Negotiated\u2019; Strait of Hormuz to Reopen Under 60-Day Framework", "trump-iran-agreement-largely-negotiated-60-day-hormuz-framework.html", "May 26, 2026",
             "Saudi Arabia is among the regional partners pressing Washington to accept the 60-day MOU framework. Trump cited the regional diplomacy in his \u201Clargely negotiated\u201D Truth Social statement."),
            ("U.S. Oil Rig Count Jumps 10 to 425 \u2014 Biggest Weekly Gain Since 2022", "us-oil-rig-count-jumps-10-to-425-biggest-weekly-gain-since-2022.html", "May 22, 2026",
             "Non-OPEC supply begins responding. Baker Hughes reported May 22 the U.S. oil rig count rose by 10 to 425 \u2014 the largest single-week increase in oil-directed drilling since 2022."),
        ],
    },
    "uae.html": {
        "context": "Current state (May 26, 2026): The UAE is among the Gulf states pressing Washington to accept the U.S.-Iran 60-day MOU framework. The UAE formally departed OPEC effective May 1, 2026. Trump (May 24): U.S.-Iran agreement \u201Clargely negotiated\u201D; Strait of Hormuz will reopen. A UAE nuclear facility was attacked over the May 17-18 weekend (now nearly two weeks ago). U.S. CENTCOM conducted defensive strikes in southern Iran Tuesday; IRGC claimed F-35 engagement. ADCOP pipeline continues to carry available bypass volumes that don\u2019t transit Hormuz. The UAE remains a primary U.S. security partner in the Gulf.",
        "lead_articles": [
            ("Trump: U.S.-Iran Agreement \u2018Largely Negotiated\u2019; Strait of Hormuz to Reopen Under 60-Day Framework", "trump-iran-agreement-largely-negotiated-60-day-hormuz-framework.html", "May 26, 2026",
             "The UAE, alongside Saudi Arabia and Qatar, has been pressing Washington to accept the deal. Trump credited regional partners for facilitating the framework."),
            ("UAE Nuclear Facility Attacked Over Weekend in Persian Gulf Escalation", "uae-nuclear-facility-attacked-weekend-persian-gulf-escalation.html", "May 18, 2026",
             "Energy infrastructure across the Persian Gulf came under attack the prior weekend, including a nuclear facility in the United Arab Emirates."),
        ],
    },
    "opec-members.html": {
        "context": "Current state (May 26, 2026): The diplomatic track has shifted decisively. Trump (May 24): U.S.-Iran agreement \u201Clargely negotiated\u201D; Strait of Hormuz will reopen under a 60-day MOU framework. Saudi Arabia, Qatar, and the UAE (former member, departed May 1) are among the regional partners pressing acceptance. The proposed framework would allow Iran to freely sell oil during the 60-day window in exchange for mine-clearing and unrestricted Hormuz passage. EIA assessed 10.5M bpd of Persian Gulf production shut in during April; energy executives via MUFG still warn full normalization may not occur until 2027 due to the scale of disruption. Brent ~$98-99 Tuesday near five-week lows.",
        "lead_articles": [
            ("Trump: U.S.-Iran Agreement \u2018Largely Negotiated\u2019; Strait of Hormuz to Reopen Under 60-Day Framework", "trump-iran-agreement-largely-negotiated-60-day-hormuz-framework.html", "May 26, 2026",
             "Saudi Arabia, Qatar, and the UAE are among the regional partners pressing acceptance of the 60-day MOU framework. The proposed deal would allow Iran to freely sell oil during the window."),
            ("UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity.html", "May 13, 2026",
             "The EIA\u2019s May Short-Term Energy Outlook incorporates the UAE\u2019s departure from OPEC, effective May 1, 2026."),
        ],
    },
    "qatar.html": {
        "context": "Current state (May 26, 2026): Qatar is one of the principal mediators of the U.S.-Iran framework alongside Pakistan, with Pakistani and Qatari negotiators holding talks with Iranian counterparts Thursday and Friday while staying in regular contact with U.S. envoy Steve Witkoff. Trump (May 24): agreement \u201Clargely negotiated\u201D; Strait of Hormuz will reopen. The 60-day MOU framework would allow Qatari LNG exports to resume as the strait reopens with no tolls during the window. Qatar\u2019s economy minister attended the G7 Paris meeting (concluded May 19) as an invited guest. JKM and TTF benchmarks remain elevated.",
        "lead_articles": [],
    },
    "russia.html": {
        "context": "Current state (May 26, 2026): Russia\u2019s role in any uranium transfer is no longer the focus, with the proposed U.S.-Iran 60-day MOU framework setting nuclear-program negotiations as a parallel track rather than a precondition. Iran\u2019s foreign ministry spokesperson Baghaei confirmed nuclear issues are not part of current negotiations. The U.S. previously issued a waiver permitting the sale of Russian crude already loaded onto tankers, providing a release valve for global supply. Russia remains one of few major producers outside the Persian Gulf disruption zone, and Brent pulling back toward $98 has implications for Urals discount dynamics.",
        "lead_articles": [
            ("Trump: U.S.-Iran Agreement \u2018Largely Negotiated\u2019; Strait of Hormuz to Reopen Under 60-Day Framework", "trump-iran-agreement-largely-negotiated-60-day-hormuz-framework.html", "May 26, 2026",
             "The 60-day MOU framework moves nuclear negotiations to a parallel track. Iran\u2019s foreign ministry confirmed nuclear issues are not part of current negotiations; uranium transfer to Russia element of earlier proposals is deprioritized."),
        ],
    },
    "brazil.html": {
        "context": "Current state (May 26, 2026): Brazilian pre-salt production continues to grow as an increasingly important non-OPEC supply source even as the U.S.-Iran 60-day MOU framework offers near-term resolution of the Persian Gulf disruption. Trump (May 24): U.S.-Iran agreement \u201Clargely negotiated\u201D; Strait of Hormuz will reopen. Brazil\u2019s finance minister attended the G7 Paris meeting (concluded May 19) as an invited guest. Petrobras Q1 results and pre-salt output milestones remain key watchpoints; Brent pulling back toward $98 affects pre-salt project economics at the margin.",
        "lead_articles": [],
    },
    "nigeria.html": {
        "context": "Current state (May 26, 2026): Nigerian crude remains important to the non-OPEC supply mix even as the U.S.-Iran 60-day MOU framework offers near-term resolution of the Persian Gulf disruption. Trump (May 24): agreement \u201Clargely negotiated\u201D; Strait of Hormuz will reopen with no tolls during the 60-day window. Light, sweet Nigerian grades have served as alternatives for refiners losing access to Middle East crude through the conflict. The G7 leaders summit June 15-17 in Evian is expected to address rare-earths and supply-chain diversification.",
        "lead_articles": [],
    },
    "venezuela.html": {
        "context": "Current state (May 26, 2026): Venezuelan production capacity remains a structurally relevant question as the U.S.-Iran 60-day MOU framework approaches finalization. Trump (May 24): agreement \u201Clargely negotiated\u201D; Strait of Hormuz will reopen. EIA\u2019s May STEO cut OPEC 2027 spare capacity to 2.5M bpd from 3.8M prior following the UAE\u2019s departure, keeping non-OPEC supply quality in focus. U.S. sanctions policy on Venezuelan crude continues as a relevant input to Atlantic Basin supply balance. Brent ~$98-99 near five-week lows.",
        "lead_articles": [],
    },
}

LAST_REVIEWED_BLOCK = '''<div style="margin-top:8px;display:inline-flex;align-items:center;gap:8px;font-family:var(--font-body);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-3);padding:6px 12px;background:var(--surface-2);border:1px solid var(--border);border-radius:4px"><span style="width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block"></span>Last reviewed: May 26, 2026</div>'''


def render_article_row(title, slug, date, excerpt):
    return (f'<article class="hub-article-row"><a href="{slug}" class="hub-article-title">{title}</a>'
            f'<div class="hub-article-meta"><span>{date}</span></div>'
            f'<p class="hub-article-excerpt">{excerpt}…</p></article>')


def main():
    touched = 0
    for slug, data in HUBS.items():
        path = ARTICLES / slug
        if not path.exists():
            print(f"  ✗ missing: {slug}")
            continue
        txt = path.read_text(encoding="utf-8")
        orig = txt

        # 1) Replace the Current Context paragraph
        ctx_pattern = re.compile(
            r'(<h3 style="margin:0 0 8px;font-size:13px;text-transform:uppercase;letter-spacing:0\.06em;color:var\(--blue\)">Current Context</h3>\s*)'
            r'<p style="margin:0;font-size:14\.5px;line-height:1\.6;color:var\(--text-2\)">[^<]*</p>',
            re.DOTALL
        )
        replacement_ctx = (r'\1<p style="margin:0;font-size:14.5px;line-height:1.6;color:var(--text-2)">'
                           + data["context"] + '</p>')
        new_txt, ctx_n = ctx_pattern.subn(replacement_ctx, txt, count=1)
        if ctx_n == 0:
            print(f"  · {slug}: context not matched, skipping context update")
        txt = new_txt

        # 2) Add Last reviewed badge after the lead intro paragraph
        if "Last reviewed: May 26, 2026" not in txt:
            # Find the close of the lead p tag inside .article-body
            lead_pattern = re.compile(
                r'(<p style="font-size:16\.5px;line-height:1\.7;color:var\(--text-2\)">[^<]*?</p>)',
                re.DOTALL
            )
            new_txt, n = lead_pattern.subn(r'\1\n          ' + LAST_REVIEWED_BLOCK, txt, count=1)
            if n > 0:
                txt = new_txt

        # 3) Prepend lead_articles to the article list, if any
        if data["lead_articles"]:
            # Find the start of <article class="hub-article-row"> and inject before
            new_articles_html = "\n            ".join(
                render_article_row(t, s, d, e) for t, s, d, e in data["lead_articles"]
            )
            # Avoid duplicate prepends — check if first lead article slug already appears as first row
            first_slug = data["lead_articles"][0][1]
            # The pattern: <div>\n<article ... href="<first_slug>"... only count one match
            already = f'<article class="hub-article-row"><a href="{first_slug}"' in txt
            # Check if it's the FIRST article in the list (not just present)
            list_open_match = re.search(r'<p[^>]*>30 articles[^<]*</p>\s*<div>\s*(.+?)(?:<article|</div>)', txt, re.DOTALL)
            already_first = False
            if list_open_match:
                already_first = f'href="{first_slug}"' in list_open_match.group(1)[:200]

            if not already_first:
                # Insert right after the opening <div> of the list, before the first <article>
                list_open_pattern = re.compile(
                    r'(<p style="color:var\(--text-3\);font-size:13px;margin:0 0 20px">[^<]*</p>\s*<div>\s*)',
                    re.DOTALL
                )
                injection = r'\1' + new_articles_html + '\n            '
                new_txt, n = list_open_pattern.subn(injection, txt, count=1)
                if n > 0:
                    txt = new_txt

        # 4) Update the article count if we added articles
        added = len(data["lead_articles"]) if data["lead_articles"] else 0
        if added > 0:
            count_pattern = re.compile(r'<p style="color:var\(--text-3\);font-size:13px;margin:0 0 20px">(\d+) articles, most recent first\.')
            m = count_pattern.search(txt)
            if m:
                new_count = int(m.group(1)) + added
                txt = count_pattern.sub(
                    f'<p style="color:var(--text-3);font-size:13px;margin:0 0 20px">{new_count} articles, most recent first.',
                    txt, count=1
                )

        if txt != orig:
            path.write_text(txt, encoding="utf-8")
            touched += 1
            print(f"  ✓ {slug}")

    print(f"\n{touched} hubs refreshed.")


if __name__ == "__main__":
    main()
