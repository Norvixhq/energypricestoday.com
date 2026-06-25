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
        "context": "Current state (June 24, 2026): Crude has round-tripped to pre-war levels \u2014 WTI below $70, Brent below $74, down ~40% from the wartime peak \u2014 as Gulf supply returns under the interim deal. But the Strait of Hormuz is a half-open puzzle: Iran signaled a renewed closure over the weekend, and Windward said transits briefly fell to 12 vessels from more than 21, with traffic dark and sanctioned. The 60-day roadmap toward a final deal remains in force, with technical talks continuing, but the strike threat and Lebanon ceasefire dispute are unresolved. A U.S. waiver now permits purchases of already-loaded Iranian oil, adding supply even as the nuclear and sanctions questions stay open.",
        "lead_articles": [
            ("Hormuz Baffles Markets: Half-Open, Half-Closed After Iran\u2019s Renewed Closure Signal", "hormuz-half-open-half-closed-iran-renewed-closure-signal.html", "June 24, 2026",
             "Iran signaled a renewed closure over the weekend even as overall supply returns; transits briefly fell to 12 vessels with traffic dark and sanctioned. Insurers still treat the region as a war zone."),
            ("Crude Sinks to Pre-War Levels as Gulf Supply Returns: WTI Below $70, Brent Below $74", "crude-sinks-pre-war-levels-gulf-supply-returns-wti-below-70-brent-below-74.html", "June 24, 2026",
             "Oil round-tripped to pre-war levels, down ~40% from the peak, as tankers resume Hormuz transits and the IEA estimates the UAE is exporting at ~85% of pre-war levels."),
        ],
    },
    "saudi-arabia.html": {
        "context": "Current state (June 24, 2026): Crude has round-tripped to pre-war levels (Brent below $74, down ~40% from the peak) as Gulf supply returns. Brent\u2019s prompt spread flipped into bearish contango for the first time since the conflict, a structural signal of ample near-term supply. The IEA estimates the UAE \u2014 a key Gulf exporter alongside Saudi Arabia \u2014 is shipping at ~85% of pre-war levels. As the cartel\u2019s swing producer, Riyadh now faces the familiar tension of accommodating Iranian volume recovery without deepening a price collapse; Saudi allocations to Chinese refiners in 2H26 will be the key leading indicator. A renewed Hormuz closure signal from Iran keeps a risk premium flickering.",
        "lead_articles": [
            ("Crude Sinks to Pre-War Levels as Gulf Supply Returns: WTI Below $70, Brent Below $74", "crude-sinks-pre-war-levels-gulf-supply-returns-wti-below-70-brent-below-74.html", "June 24, 2026",
             "Brent\u2019s curve flipped into contango as Gulf supply returns; Riyadh faces the tension of accommodating Iranian volume recovery without deepening the price collapse."),
            ("Hormuz Baffles Markets: Half-Open, Half-Closed After Iran\u2019s Renewed Closure Signal", "hormuz-half-open-half-closed-iran-renewed-closure-signal.html", "June 24, 2026",
             "A renewed closure signal from Tehran keeps a risk premium flickering even as overall Gulf volumes, including Saudi barrels, improve."),
        ],
    },
    "uae.html": {
        "context": "Current state (June 24, 2026): The UAE is at the center of the supply recovery \u2014 the IEA estimates it is exporting oil at nearly 85% of pre-war levels, having sold roughly 60 million barrels from the Persian Gulf recently. Crude has round-tripped to pre-war levels (Brent below $74) and Brent\u2019s curve flipped into contango. For the UAE, which formally departed OPEC effective May 1, resumed Hormuz traffic relieves the bypass pressure that had elevated the ADCOP pipeline. But the strait is a half-open puzzle after Iran\u2019s renewed closure signal, and insurers still treat the region as a war zone. The UAE remains a primary U.S. security partner as attention shifts to the durability of the 60-day roadmap.",
        "lead_articles": [
            ("Crude Sinks to Pre-War Levels as Gulf Supply Returns: WTI Below $70, Brent Below $74", "crude-sinks-pre-war-levels-gulf-supply-returns-wti-below-70-brent-below-74.html", "June 24, 2026",
             "The IEA estimates the UAE is exporting at ~85% of pre-war levels, having sold ~60M barrels recently \u2014 a centerpiece of the supply recovery that has pushed crude to pre-war lows."),
            ("UAE Nuclear Facility Attacked Over Weekend in Persian Gulf Escalation", "uae-nuclear-facility-attacked-weekend-persian-gulf-escalation.html", "May 18, 2026",
             "Energy infrastructure across the Persian Gulf came under attack, including a nuclear facility in the United Arab Emirates."),
        ],
    },
    "opec-members.html": {
        "context": "Current state (June 24, 2026): Crude has round-tripped to pre-war levels (Brent below $74, down ~40% from the peak), and Brent\u2019s prompt spread flipped into bearish contango for the first time since the conflict \u2014 a structural signal of ample near-term supply. OPEC Secretary General Al Ghais continues to reject forecasts of a near-term demand peak and IEA glut projections, citing fundamentals, but the war premium has now evaporated. The IEA estimates the UAE is exporting at ~85% of pre-war levels, and a U.S. waiver on already-loaded Iranian oil adds supply. The bloc faces decisions on restoring shut-in capacity without accelerating a 2027 surplus, with Saudi allocations to Asian refiners the key indicator.",
        "lead_articles": [
            ("Brent\u2019s Prompt Spread Flips Into Contango for the First Time Since the Conflict", "crude-sinks-pre-war-levels-gulf-supply-returns-wti-below-70-brent-below-74.html", "June 24, 2026",
             "Brent\u2019s curve flipped into bearish contango, signaling ample near-term supply; OPEC\u2019s Al Ghais still rejects glut forecasts as the bloc weighs restoring shut-in capacity."),
            ("UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity.html", "May 13, 2026",
             "The EIA\u2019s May Short-Term Energy Outlook incorporates the UAE\u2019s departure from OPEC, effective May 1, 2026."),
        ],
    },
    "qatar.html": {
        "context": "Current state (June 24, 2026): Qatar, a lead mediator alongside Pakistan, helped broker the 60-day roadmap toward a final U.S.-Iran deal that remains in force. Crude has round-tripped to pre-war levels and LNG tankers are transiting Hormuz again, though the strait is a half-open puzzle after Iran signaled a renewed closure over the weekend \u2014 transits briefly fell to 12 vessels. Global LNG benchmarks should ease as Qatari cargoes resume to Asian and European buyers, but insurers still treat the region as a war zone and a full recovery in flows appears weeks away. Qatar\u2019s diplomatic role and its commercial stake in a durable reopening now run in parallel.",
        "lead_articles": [],
    },
    "russia.html": {
        "context": "Current state (June 24, 2026): Crude has round-tripped to pre-war levels (Brent below $74, down ~40% from the peak) and Brent\u2019s curve flipped into bearish contango \u2014 a softer, looser backdrop for Russian Urals differentials. A U.S. waiver permitting purchases of already-loaded Iranian oil adds a competing barrel, and the IEA estimates the UAE is exporting at ~85% of pre-war levels. Russia remains one of few major producers outside the Gulf disruption zone, but the evaporating war premium erodes the scarcity that had supported its export revenues. A renewed Hormuz closure signal from Iran keeps a risk premium flickering even as the dominant trend is normalization.",
        "lead_articles": [
            ("Crude Sinks to Pre-War Levels as Gulf Supply Returns: WTI Below $70, Brent Below $74", "crude-sinks-pre-war-levels-gulf-supply-returns-wti-below-70-brent-below-74.html", "June 24, 2026",
             "Crude round-tripped to pre-war levels and Brent\u2019s curve flipped into contango \u2014 a looser backdrop for Urals differentials as competing barrels return."),
        ],
    },
    "brazil.html": {
        "context": "Current state (June 24, 2026): Crude has round-tripped to pre-war levels (Brent below $74) and Brent\u2019s prompt spread flipped into bearish contango. Brazilian pre-salt output continues to grow as a non-OPEC source; the IEA cites strong non-OPEC growth \u2014 of which Brazil is a leading contributor \u2014 among factors that could tip the market into a 2027 surplus, though OPEC\u2019s Al Ghais rejects that view. The softer price path tightens pre-salt economics at the margin, a full reversal from the wartime premium. With the war premium gone, the market\u2019s focus has shifted to the demand outlook and the pace of Gulf normalization, complicated by Iran\u2019s renewed Hormuz closure signal.",
        "lead_articles": [],
    },
    "nigeria.html": {
        "context": "Current state (June 24, 2026): Crude has round-tripped to pre-war levels (Brent below $74, down ~40% from the peak). Light, sweet Nigerian grades had served as alternatives for refiners losing Middle East crude during the conflict \u2014 a premium that has now faded as Gulf barrels return, the IEA estimates the UAE is exporting at ~85% of pre-war levels, and a U.S. waiver adds already-loaded Iranian oil. The softer price environment pressures Nigerian fiscal math as the war premium evaporates. Brent\u2019s flip into contango underscores ample near-term supply, leaving the market focused on demand and the pace of Gulf normalization.",
        "lead_articles": [],
    },
    "venezuela.html": {
        "context": "Current state (June 24, 2026): Crude has round-tripped to pre-war levels (Brent below $74, down ~40% from the peak), and Brent\u2019s curve flipped into bearish contango. The softer price path reduces the pull on marginal Atlantic Basin barrels that had gained relevance during the wartime disruption, and a U.S. waiver permitting purchases of already-loaded Iranian oil adds competing supply. U.S. sanctions policy on Venezuelan crude remains a key variable as the market shifts decisively from scarcity to a potential 2027 surplus \u2014 a view OPEC\u2019s Al Ghais disputes. Venezuelan production capacity stays structurally constrained regardless of the improved geopolitical backdrop.",
        "lead_articles": [],
    },
}

LAST_REVIEWED_BLOCK = '''<div style="margin-top:8px;display:inline-flex;align-items:center;gap:8px;font-family:var(--font-body);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-3);padding:6px 12px;background:var(--surface-2);border:1px solid var(--border);border-radius:4px"><span style="width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block"></span>Last reviewed: June 24, 2026</div>'''


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
        if "Last reviewed: June 24, 2026" not in txt:
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
