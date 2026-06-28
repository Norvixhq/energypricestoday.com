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
        "context": "Current state (June 28, 2026): The Strait of Hormuz is reopening in force \u2014 Persian Gulf exports are back to roughly 75% of pre-war levels as transits surge and vessels openly navigate with signals on. Crude has settled at pre-war levels (Brent near $72, its lowest since February 27) after an over-10% weekly drop. The 60-day roadmap toward a final deal remains in force, but friction persists: Trump accused Iran of violating the ceasefire by firing drones at ships, and the container ship Ever Lovely was struck off Oman \u2014 yet the strait stayed open and the spike faded. The nuclear and sanctions questions remain open as the supply normalization continues.",
        "lead_articles": [
            ("Hormuz Transits Surge as Gulf Exports Recover to ~75% of Pre-War Levels", "hormuz-transits-surge-gulf-exports-recover-75-percent-pre-war.html", "June 28, 2026",
             "The reopening is now visibly underway: transits have surged, restoring Persian Gulf exports to roughly 75% of pre-war levels, even as residual security risk lingers."),
            ("Container Ship Ever Lovely Struck Off Oman, but the Strait Stays Open", "container-ship-ever-lovely-struck-off-oman-strait-stays-open.html", "June 28, 2026",
             "The Ever Lovely was struck off Oman and Trump accused Iran of firing drones at ships, but the strait stayed open and the price spike quickly faded."),
        ],
    },
    "saudi-arabia.html": {
        "context": "Current state (June 28, 2026): Saudi Arabia is at the center of the supply ramp \u2014 it has begun loading tankers at its Ras Tanura terminal, one of the world\u2019s largest crude-export hubs, signaling a major regional output recovery. Persian Gulf exports are back to roughly 75% of pre-war levels and crude has settled at pre-war prices (Brent near $72) after an over-10% weekly drop. As OPEC\u2019s swing producer, Riyadh now manages a fast recovery in which the binding constraint is tanker availability rather than the conflict; Saudi allocations to Asian refiners and its posture on OPEC+ quotas (with Iraq pushing for more) will shape the second half of 2026.",
        "lead_articles": [
            ("Hormuz Transits Surge as Gulf Exports Recover to ~75% of Pre-War Levels", "hormuz-transits-surge-gulf-exports-recover-75-percent-pre-war.html", "June 28, 2026",
             "Saudi Arabia began loading tankers at Ras Tanura, signaling a major output ramp as Persian Gulf exports recover to roughly 75% of pre-war levels."),
            ("Container Ship Ever Lovely Struck Off Oman, but the Strait Stays Open", "container-ship-ever-lovely-struck-off-oman-strait-stays-open.html", "June 28, 2026",
             "A ship strike off Oman briefly lifted oil, but the strait stayed open and Saudi loadings continued as the regional output ramp proceeds."),
        ],
    },
    "uae.html": {
        "context": "Current state (June 28, 2026): The UAE is part of the accelerating supply recovery, boosting output alongside Saudi Arabia, Kuwait, and Qatar as the Strait of Hormuz reopens and Persian Gulf exports return to roughly 75% of pre-war levels. Crude has settled at pre-war prices (Brent near $72) after an over-10% weekly drop. For the UAE, which formally departed OPEC effective May 1, resumed Hormuz traffic relieves the bypass pressure that had elevated the ADCOP pipeline, and the main constraint on shipping more barrels is now tanker availability. The UAE remains a primary U.S. security partner as the reopening proceeds, tested but not derailed by the Ever Lovely strike off Oman.",
        "lead_articles": [
            ("Hormuz Transits Surge as Gulf Exports Recover to ~75% of Pre-War Levels", "hormuz-transits-surge-gulf-exports-recover-75-percent-pre-war.html", "June 28, 2026",
             "The UAE is boosting supply alongside Saudi Arabia, Kuwait, and Qatar as Persian Gulf exports recover to ~75% of pre-war levels, constrained mainly by tanker availability."),
            ("UAE Nuclear Facility Attacked Over Weekend in Persian Gulf Escalation", "uae-nuclear-facility-attacked-weekend-persian-gulf-escalation.html", "May 18, 2026",
             "Energy infrastructure across the Persian Gulf came under attack, including a nuclear facility in the United Arab Emirates."),
        ],
    },
    "opec-members.html": {
        "context": "Current state (June 28, 2026): With the Gulf reopening, OPEC+ policy has moved to center stage. Iraq is seeking a higher OPEC quota to recoup the oil sales it lost during the war, joining a regional output ramp that includes Saudi loadings at Ras Tanura and increased UAE, Kuwait, and Qatar supply. Persian Gulf exports are back to roughly 75% of pre-war levels and crude has settled at pre-war prices (Brent near $72) after an over-10% weekly drop. Higher OPEC+ export quotas point to refinery inventory rebuilds worldwide \u2014 a bearish backdrop \u2014 while OPEC\u2019s Al Ghais continues to reject forecasts of a near-term demand peak. The binding constraint on the recovery is now tanker availability rather than the conflict.",
        "lead_articles": [
            ("Hormuz Transits Surge as Gulf Exports Recover to ~75% of Pre-War Levels", "hormuz-transits-surge-gulf-exports-recover-75-percent-pre-war.html", "June 28, 2026",
             "Iraq is seeking a higher OPEC quota as Saudi Arabia loads at Ras Tanura and Gulf exports recover to ~75% of pre-war levels, pointing to OPEC+ quota increases."),
            ("UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity.html", "May 13, 2026",
             "The EIA\u2019s May Short-Term Energy Outlook incorporates the UAE\u2019s departure from OPEC, effective May 1, 2026."),
        ],
    },
    "qatar.html": {
        "context": "Current state (June 28, 2026): Qatar is boosting supply alongside Saudi Arabia, the UAE, and Kuwait as the Strait of Hormuz reopens and Persian Gulf exports return to roughly 75% of pre-war levels. LNG and oil tankers are transiting the strait openly with signals on, and global LNG benchmarks have eased as Qatari cargoes resume to Asian and European buyers. Crude has settled at pre-war prices (Brent near $72) after an over-10% weekly drop. The main constraint on shipping additional volume is tanker availability rather than the conflict, though the Ever Lovely strike off Oman is a reminder that residual security risk lingers even as commercial traffic returns in force.",
        "lead_articles": [],
    },
    "russia.html": {
        "context": "Current state (June 28, 2026): Crude has settled at pre-war levels (Brent near $72, its lowest since February 27) after an over-10% weekly drop \u2014 a softer, looser backdrop for Russian Urals differentials as Gulf supply floods back. Persian Gulf exports are at roughly 75% of pre-war levels, Saudi Arabia is loading at Ras Tanura, and Iraq is seeking a higher OPEC quota, all adding competing barrels. Russia remains one of few major producers outside the Gulf disruption zone, but the evaporated war premium erodes the scarcity that had supported its export revenues. The market\u2019s focus has shifted to how fast returning Gulf barrels and higher OPEC+ quotas rebuild global inventories.",
        "lead_articles": [
            ("Hormuz Transits Surge as Gulf Exports Recover to ~75% of Pre-War Levels", "hormuz-transits-surge-gulf-exports-recover-75-percent-pre-war.html", "June 28, 2026",
             "Gulf exports are back to ~75% of pre-war levels and crude has settled at pre-war prices \u2014 a looser backdrop for Urals differentials as competing barrels return."),
        ],
    },
    "brazil.html": {
        "context": "Current state (June 28, 2026): Crude has settled at pre-war levels (Brent near $72) after an over-10% weekly drop as the Gulf reopens and Persian Gulf exports recover to roughly 75% of pre-war levels. Brazilian pre-salt output continues to grow as a non-OPEC source; the IEA cites strong non-OPEC growth \u2014 of which Brazil is a leading contributor \u2014 among factors that could tip the market into a 2027 surplus, though OPEC\u2019s Al Ghais rejects that view. The softer price path tightens pre-salt economics at the margin, a full reversal from the wartime premium. With the war premium gone, the market\u2019s focus has shifted to the demand outlook and the pace of OPEC+ quota increases as Iraq and others push for more.",
        "lead_articles": [],
    },
    "nigeria.html": {
        "context": "Current state (June 28, 2026): Crude has settled at pre-war levels (Brent near $72, its lowest since February 27) after an over-10% weekly drop. Light, sweet Nigerian grades had served as alternatives for refiners losing Middle East crude during the conflict \u2014 a premium that has now faded as Gulf barrels return, Persian Gulf exports recover to roughly 75% of pre-war levels, and Saudi Arabia loads tankers at Ras Tanura. The softer price environment pressures Nigerian fiscal math as the war premium evaporates. With Iraq and others pushing for higher OPEC+ quotas, the market is focused on the demand outlook and the pace of the Gulf supply ramp.",
        "lead_articles": [],
    },
    "venezuela.html": {
        "context": "Current state (June 28, 2026): Crude has settled at pre-war levels (Brent near $72) after an over-10% weekly drop, and Persian Gulf exports have recovered to roughly 75% of pre-war levels. The softer price path reduces the pull on marginal Atlantic Basin barrels that had gained relevance during the wartime disruption, and the returning Gulf supply \u2014 Saudi loadings at Ras Tanura, an Iraqi push for a higher OPEC quota \u2014 adds competing volume. U.S. sanctions policy on Venezuelan crude remains a key variable as the market shifts decisively from scarcity toward a potential 2027 surplus. Venezuelan production capacity stays structurally constrained regardless of the improved geopolitical backdrop.",
        "lead_articles": [],
    },
}

LAST_REVIEWED_BLOCK = '''<div style="margin-top:8px;display:inline-flex;align-items:center;gap:8px;font-family:var(--font-body);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-3);padding:6px 12px;background:var(--surface-2);border:1px solid var(--border);border-radius:4px"><span style="width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block"></span>Last reviewed: June 28, 2026</div>'''


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
        if "Last reviewed: June 28, 2026" not in txt:
            # Find the close of the lead p tag inside .article-body
            lead_pattern = re.compile(
                r'(<p style="font-size:16\.5px;line-height:1\.7;color:var\(--text-2\)">[^<]*?</p>)',
                re.DOTALL
            )
            new_txt, n = lead_pattern.subn(r'\1\n          ' + LAST_REVIEWED_BLOCK, txt, count=1)
            if n > 0:
                txt = new_txt

        # 3) Daily lead articles REPLACE prior daily leads (no accumulation).
        #    Prior prepends are wrapped in <!--DAILY_LEADS_START-->...<!--DAILY_LEADS_END-->.
        #    Strip any existing marked block first, then inject today's (also marked).
        LEAD_START = "<!--DAILY_LEADS_START-->"
        LEAD_END = "<!--DAILY_LEADS_END-->"

        # Count how many rows are currently inside an existing marker block (to decrement the count)
        prior_block = re.search(re.escape(LEAD_START) + r'(.*?)' + re.escape(LEAD_END), txt, re.DOTALL)
        prior_lead_count = 0
        if prior_block:
            prior_lead_count = prior_block.group(1).count('<article class="hub-article-row">')
            # Remove the entire prior marked block (and trailing whitespace)
            txt = re.sub(re.escape(LEAD_START) + r'.*?' + re.escape(LEAD_END) + r'\s*', '', txt, flags=re.DOTALL)
        # Defensively strip any ORPHANED markers left by past manual edits (prevents
        # mismatched START/END counts from corrupting future strip passes).
        txt = txt.replace(LEAD_START, '').replace(LEAD_END, '')

        added = 0
        if data["lead_articles"]:
            new_articles_html = "\n            ".join(
                render_article_row(t, s, d, e) for t, s, d, e in data["lead_articles"]
            )
            block = LEAD_START + "\n            " + new_articles_html + "\n            " + LEAD_END + "\n            "
            list_open_pattern = re.compile(
                r'(<p style="color:var\(--text-3\);font-size:13px;margin:0 0 20px">[^<]*</p>\s*<div>\s*)',
                re.DOTALL
            )
            new_txt, n = list_open_pattern.subn(r'\1' + block, txt, count=1)
            if n > 0:
                txt = new_txt
                added = len(data["lead_articles"])

        # 4) Reconcile the displayed article count: subtract prior leads, add today's.
        count_pattern = re.compile(r'<p style="color:var\(--text-3\);font-size:13px;margin:0 0 20px">(\d+) articles, most recent first\.')
        m = count_pattern.search(txt)
        if m:
            new_count = int(m.group(1)) - prior_lead_count + added
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
