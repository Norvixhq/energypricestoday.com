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
        "context": "Current state (May 22, 2026): Baker Hughes reported the U.S. oil rig count rose 10 to 425 \u2014 the largest weekly gain since 2022 \u2014 signaling U.S. shale is finally responding to elevated prices. President Trump threatened renewed military strikes if U.S.-Iran talks fail (Bloomberg). Tehran says the latest U.S. proposal narrows differences, but Supreme Leader Mojtaba Khamenei\u2019s directive that uranium must stay in Iran and the Hormuz tolls dispute (Iran reportedly working with Oman on a permanent framework) continue to cloud the outlook. Rubio: \"slight progress\" in mediated talks. Rapidan Energy warns Brent could surge toward $130 if Hormuz disrupted through August. WTI $94.75-$99.41 Friday; Brent ~$104.",
        "lead_articles": [
            ("Trump Threatens Renewed Iran Strikes if Talks Fail; Markets Swing on Mixed Signals", "trump-threatens-renewed-iran-strikes-talks-fail-markets-swing.html", "May 22, 2026",
             "President Trump threatened renewed military strikes if U.S.-Iran talks fail to produce a deal, Bloomberg reported Friday. Tehran said the latest U.S. proposal narrows differences, but disputes over uranium and Hormuz tolls quickly reignited tensions."),
            ("Trump vs Khamenei: 'We Will Get It' Clashes with Supreme Leader Order Uranium Must Stay in Iran", "trump-khamenei-uranium-standoff-must-stay-iran.html", "May 21, 2026",
             "President Trump declared at the White House the U.S. will eventually recover Iran\u2019s stockpile of highly enriched uranium. Hours earlier, Supreme Leader Mojtaba Khamenei issued a directive the uranium must stay in Iran."),
        ],
    },
    "saudi-arabia.html": {
        "context": "Current state (May 22, 2026): Baker Hughes reported the U.S. oil rig count jumped 10 to 425 \u2014 the biggest weekly gain since 2022 \u2014 partially offsetting structural Persian Gulf shut-ins (~10.5M bpd in April, peaking near 10.8M bpd in May per EIA). Saudi Arabia was among the Gulf states that asked Trump to call off Tuesday\u2019s planned Iran strike. Saudi Aramco CEO Amin Nasser told investors market normalization is pushed to 2027 if Hormuz reopening is delayed past mid-June. Saudi production remains at the lowest level since 1990. Rapidan Energy warns Brent could surge toward $130 if Hormuz disrupted through August.",
        "lead_articles": [
            ("U.S. Oil Rig Count Jumps 10 to 425 \u2014 Biggest Weekly Gain Since 2022", "us-oil-rig-count-jumps-10-to-425-biggest-weekly-gain-since-2022.html", "May 22, 2026",
             "Baker Hughes reported Friday the U.S. oil rig count rose by 10 to 425 in the week ended May 22 \u2014 the largest single-week increase in oil-directed drilling since 2022. The acceleration is concentrated in West Texas (Permian) and South Texas (Eagle Ford)."),
            ("Trump Threatens Renewed Iran Strikes if Talks Fail; Markets Swing on Mixed Signals", "trump-threatens-renewed-iran-strikes-talks-fail-markets-swing.html", "May 22, 2026",
             "President Trump threatened renewed military strikes if U.S.-Iran talks fail. Saudi Arabia, alongside Qatar and the UAE, was among the Gulf states that earlier asked Trump to call off Tuesday\u2019s planned Iran strike."),
        ],
    },
    "uae.html": {
        "context": "Current state (May 22, 2026): The UAE was among the Gulf states (alongside Saudi Arabia and Qatar) that asked Trump to call off Tuesday\u2019s planned Iran strike. The UAE formally departed OPEC effective May 1, 2026. EIA\u2019s May STEO cut OPEC\u2019s 2027 spare capacity forecast to 2.5M bpd from 3.8M prior. A UAE nuclear facility was attacked over the prior weekend (May 17-18). Trump threatened renewed Iran strikes Friday if talks fail. ADCOP pipeline carries available bypass volumes that don\u2019t transit Hormuz. The UAE remains a primary U.S. security partner in the Gulf and attended the G7 Paris meeting (concluded May 19) as an invited guest.",
        "lead_articles": [
            ("Trump Calls Off Planned Iran Strike After Saudi, Qatar, UAE Asked Him to 'Hold Off'", "trump-calls-off-iran-strike-gulf-states-hold-off.html", "May 20, 2026",
             "Gulf states\u2019 coordinated request signals continued regional preference for diplomatic resolution. UAE among states asking Trump to hold off."),
            ("UAE Nuclear Facility Attacked Over Weekend in Persian Gulf Escalation", "uae-nuclear-facility-attacked-weekend-persian-gulf-escalation.html", "May 18, 2026",
             "Energy infrastructure across the Persian Gulf came under attack the prior weekend, including a nuclear facility in the United Arab Emirates."),
        ],
    },
    "opec-members.html": {
        "context": "Current state (May 22, 2026): Saudi Arabia, Qatar, and the UAE (a former OPEC member, departed May 1) asked Trump to call off Tuesday\u2019s planned Iran strike. Baker Hughes May 22: U.S. oil rig count jumped 10 to 425 \u2014 the biggest single-week gain since 2022 \u2014 as non-OPEC supply begins responding. Saudi Aramco CEO Nasser warns market normalization is pushed to 2027 if Hormuz reopening delayed past mid-June. EIA\u2019s May STEO cut OPEC\u2019s 2027 spare capacity forecast to 2.5M bpd from 3.8M prior. EIA: 10.5M bpd Persian Gulf production was shut in during April; expected to peak near 10.8M bpd in May. Rapidan Energy warns Brent could surge toward $130 if Hormuz disrupted through August.",
        "lead_articles": [
            ("U.S. Oil Rig Count Jumps 10 to 425 \u2014 Biggest Weekly Gain Since 2022", "us-oil-rig-count-jumps-10-to-425-biggest-weekly-gain-since-2022.html", "May 22, 2026",
             "Non-OPEC supply begins responding. Baker Hughes reported Friday the U.S. oil rig count rose by 10 to 425 \u2014 the largest single-week increase in oil-directed drilling since 2022."),
            ("UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity.html", "May 13, 2026",
             "The EIA\u2019s May Short-Term Energy Outlook released May 12 incorporates the UAE\u2019s departure from OPEC, effective May 1, 2026."),
        ],
    },
    "qatar.html": {
        "context": "Current state (May 22, 2026): Qatar was among the Gulf states that asked Trump to call off Tuesday\u2019s planned Iran strike. Qatari LNG exports remain disrupted as part of the broader Persian Gulf shutdown that began February 28. EIA\u2019s May STEO notes global LNG prices remain elevated as a result of reduced energy flows through the Strait of Hormuz. Qatar\u2019s economy minister attended the G7 Paris meeting (concluded May 19) as an invited guest. Drones struck Qatari waters in mid-May (UAE and Kuwait intercepted Iranian drones same day). JKM and TTF benchmarks elevated.",
        "lead_articles": [],
    },
    "russia.html": {
        "context": "Current state (May 22, 2026): The U.S. issued a fresh waiver permitting the sale of Russian crude oil already loaded onto tankers, providing a release valve for global supply. Russia\u2019s role in any uranium transfer is in flux after Supreme Leader Mojtaba Khamenei\u2019s directive Thursday that the country\u2019s uranium stockpile must not be sent abroad \u2014 effectively reversing the transfer-to-Russia element of Iran\u2019s revised peace proposal. The Kremlin had previously offered to receive and store the material. Russia remains one of few major producers outside the Persian Gulf disruption zone.",
        "lead_articles": [
            ("Trump vs Khamenei: 'We Will Get It' Clashes with Supreme Leader Order Uranium Must Stay in Iran", "trump-khamenei-uranium-standoff-must-stay-iran.html", "May 21, 2026",
             "Supreme Leader Mojtaba Khamenei\u2019s directive that uranium must stay in Iran effectively reverses the transfer-to-Russia element of the revised peace proposal."),
        ],
    },
    "brazil.html": {
        "context": "Current state (May 22, 2026): Brazilian pre-salt production continues to grow, an increasingly important non-OPEC supply source as Persian Gulf flows remain heavily disrupted. Baker Hughes May 22 reported the U.S. oil rig count jumped 10 to 425 \u2014 a parallel non-OPEC supply signal. With OPEC\u2019s 2027 spare capacity forecast cut to 2.5M bpd from 3.8M prior, Brazil and other non-OPEC producers are receiving heightened market attention. Brazil\u2019s finance minister attended the G7 Paris meeting (concluded May 19) as an invited guest. Petrobras Q1 results and pre-salt output milestones are the key watchpoints.",
        "lead_articles": [],
    },
    "nigeria.html": {
        "context": "Current state (May 22, 2026): Nigerian crude is increasingly important to the non-OPEC supply mix as Persian Gulf production remains heavily disrupted. Light, sweet Nigerian grades serve as alternatives for refiners losing access to Middle East crude. Baker Hughes May 22: U.S. oil rig count jumped 10 to 425 (biggest weekly gain since 2022) \u2014 parallel non-OPEC supply response. Pipeline security, oil-theft enforcement, and African Atlantic Basin flows are the principal watchpoints. The G7 leaders summit June 15-17 in Evian is expected to address rare-earths and supply-chain diversification.",
        "lead_articles": [],
    },
    "venezuela.html": {
        "context": "Current state (May 22, 2026): Venezuelan production capacity remains a structurally relevant question as global spare capacity has tightened sharply. Baker Hughes May 22: U.S. oil rig count jumped 10 to 425 \u2014 the largest weekly gain since 2022 \u2014 as non-OPEC supply finally responds. EIA\u2019s May STEO cut OPEC 2027 spare capacity to 2.5M bpd from 3.8M prior following the UAE\u2019s departure. Rapidan Energy warns Brent could surge toward $130 if Hormuz disrupted through August. U.S. sanctions policy on Venezuelan crude continues as a relevant input to Atlantic Basin supply balance.",
        "lead_articles": [],
    },
}

LAST_REVIEWED_BLOCK = '''<div style="margin-top:8px;display:inline-flex;align-items:center;gap:8px;font-family:var(--font-body);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-3);padding:6px 12px;background:var(--surface-2);border:1px solid var(--border);border-radius:4px"><span style="width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block"></span>Last reviewed: May 22, 2026</div>'''


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
        if "Last reviewed: May 22, 2026" not in txt:
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
