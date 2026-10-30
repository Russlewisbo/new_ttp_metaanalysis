"""
Triage the 4,183 NEW rows from Triage_NewSearch_2026-05-22.xlsx into priority
tiers by matching TTP-concept and blood-culture-concept keywords against
title + abstract.

Tiers
-----
TIER_1_HIGH        : explicit TTP phrase + blood-culture concept
TIER_2_MED         : standalone "TTP" abbreviation + blood-culture concept
                     (excludes hematology TTP — thrombotic thrombocytopenic purpura)
TIER_3_BC_ONLY     : blood-culture concept present, no TTP signal
TIER_4_TTP_ONLY    : TTP signal present, no blood-culture concept
TIER_5_OFF_TOPIC   : neither concept

The screener should prioritize TIER_1_HIGH and TIER_2_MED. TIER_3_BC_ONLY is a
large secondary pool; TTP may still be in the full text but not indexed in
title/abstract. TIER_4 and TIER_5 are almost certainly off-topic.
"""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

# Reuse path-resolution from the dedup script
_CANDIDATE_ROOTS = [
    Path("/Users/russelllewis/Desktop/new_ttp_metaanalysis"),
    Path("/sessions/affectionate-keen-franklin/mnt/new_ttp_metaanalysis"),
]
ROOT = next((p for p in _CANDIDATE_ROOTS if p.exists()), _CANDIDATE_ROOTS[0])
IN_XLSX = ROOT / "Triage_NewSearch_2026-05-22.xlsx"
OUT_XLSX = ROOT / "Triage_NewSearch_2026-05-22_tiered.xlsx"
OUT_MD = ROOT / "Triage_NewSearch_2026-05-22_tiered_summary.md"

# ---------------------------------------------------------------------------
# Keyword patterns
# ---------------------------------------------------------------------------

# Explicit TTP-concept phrases. Allow hyphen or space between words.
# The "time to ... positivity" variant tolerates up to 5 intervening words to
# catch "time to blood culture positivity", "time to first positivity", etc.
_TTP_PHRASE_PATTERNS = [
    r"time[\s-]+to(?:[\s-]+\w+){0,5}[\s-]+positiv\w*",
    r"time[\s-]+to(?:[\s-]+\w+){0,5}[\s-]+detection",
    r"time[\s-]+to(?:[\s-]+\w+){0,5}[\s-]+positive",
    r"positivity[\s-]+time",
    r"detection[\s-]+time",
    r"hours?[\s-]+to[\s-]+positiv\w*",
    r"differential[\s-]+time[\s-]+to[\s-]+positiv\w*",
    r"\bDTP\b",   # differential time to positivity (CRBSI literature)
    r"\bgrowth[\s-]+detection\b",   # TTP proxy used in blood-culture systems literature
]
TTP_PHRASE_RE = re.compile("|".join(_TTP_PHRASE_PATTERNS), re.IGNORECASE)

# Standalone TTP abbreviation (without surrounding context) — weaker signal.
TTP_ABBR_RE = re.compile(r"\bTTP\b")

# Homonyms of "TTP" we want to exclude when only the abbreviation hits.
# Hematology: thrombotic thrombocytopenic purpura
# Oncology:   time to progression
# Lab QC:     total testing process
TTP_HOMONYM_RE = re.compile(
    r"thrombotic[\s-]+thrombocytopenic|"
    r"\bTTP[/\s]?HUS\b|"
    r"\bADAMTS13\b|"
    r"thrombocytopenic[\s-]+purpura|"
    r"plasma[\s-]+exchange|"
    r"time[\s-]+to[\s-]+progression|"
    r"total[\s-]+testing[\s-]+process",
    re.IGNORECASE,
)

# Blood-culture-concept terms.
_BC_PATTERNS = [
    r"blood[\s-]+cultur\w*",
    r"bacter[ae]mi\w*",          # bacteremia / bacteraemia / bacteremic
    r"blood[\s-]?stream[\s-]+infection\w*",
    r"\bBSI\b",
    r"\bBSIs\b",
    r"candid[ae]mi\w*",          # candidemia / candidaemia
    r"fung[ae]mi\w*",            # fungemia
    r"septic[ae]mi\w*",          # septicemia / septicaemia
    r"hemoculture\w*",
]
BC_RE = re.compile("|".join(_BC_PATTERNS), re.IGNORECASE)


# ---------------------------------------------------------------------------
# Classification
# ---------------------------------------------------------------------------

def classify(title: str, abstract: str) -> tuple[str, str, str]:
    """Return (tier, ttp_matches, bc_matches) for one record."""
    text = " ".join([str(title or ""), str(abstract or "")])

    ttp_phrase_hits = TTP_PHRASE_RE.findall(text)
    ttp_abbr_hits = TTP_ABBR_RE.findall(text)
    bc_hits = BC_RE.findall(text)
    homonym = TTP_HOMONYM_RE.search(text) is not None

    has_ttp_phrase = bool(ttp_phrase_hits)
    has_ttp_abbr = bool(ttp_abbr_hits) and not homonym
    has_bc = bool(bc_hits)

    if has_ttp_phrase and has_bc:
        tier = "TIER_1_HIGH"
    elif has_ttp_abbr and has_bc:
        tier = "TIER_2_MED"
    elif has_bc:
        tier = "TIER_3_BC_ONLY"
    elif has_ttp_phrase or has_ttp_abbr:
        tier = "TIER_4_TTP_ONLY"
    else:
        tier = "TIER_5_OFF_TOPIC"

    # de-dupe the hit lists for display
    ttp_str = "; ".join(sorted(set(map(str.lower, ttp_phrase_hits + ttp_abbr_hits))))
    bc_str = "; ".join(sorted(set(map(str.lower, bc_hits))))
    return tier, ttp_str, bc_str


def main() -> None:
    print(f"Reading {IN_XLSX} (NEW_only sheet) …")
    df = pd.read_excel(IN_XLSX, sheet_name="NEW_only")
    print(f"  {len(df):,} NEW rows")

    tiers, ttp_hits, bc_hits = [], [], []
    for _, row in df.iterrows():
        t, th, bh = classify(row.get("Title", ""), row.get("Abstract", ""))
        tiers.append(t)
        ttp_hits.append(th)
        bc_hits.append(bh)

    df["tier"] = tiers
    df["ttp_keywords_matched"] = ttp_hits
    df["bc_keywords_matched"] = bc_hits

    counts = df["tier"].value_counts().to_dict()
    print("\nTier counts:")
    for k in ["TIER_1_HIGH", "TIER_2_MED", "TIER_3_BC_ONLY", "TIER_4_TTP_ONLY", "TIER_5_OFF_TOPIC"]:
        if k in counts:
            print(f"  {k:>20}: {counts[k]:,}")

    # Reorder columns: tier first
    front = ["tier", "ttp_keywords_matched", "bc_keywords_matched",
             "Title", "Authors", "Published Year", "Journal", "DOI"]
    other = [c for c in df.columns if c not in front]
    df = df[front + other]

    print(f"\nWriting {OUT_XLSX} …")
    with pd.ExcelWriter(OUT_XLSX, engine="openpyxl") as xw:
        df.to_excel(xw, sheet_name="All_NEW", index=False)
        for tier in ["TIER_1_HIGH", "TIER_2_MED", "TIER_3_BC_ONLY",
                     "TIER_4_TTP_ONLY", "TIER_5_OFF_TOPIC"]:
            sub = df[df["tier"] == tier]
            if len(sub) > 0:
                df[df["tier"] == tier].to_excel(xw, sheet_name=tier, index=False)

    # Markdown summary
    summary = [
        "# Tiered triage of the 4,183 NEW records",
        f"_Generated {pd.Timestamp.now():%Y-%m-%d %H:%M}_\n",
        "## Inputs",
        f"- Source: `{IN_XLSX.name}` (sheet `NEW_only`, {len(df):,} rows)",
        f"- Empty abstracts: {(df['Abstract'].fillna('').str.strip()=='').sum():,} "
        f"({(df['Abstract'].fillna('').str.strip()=='').mean():.1%})\n",
        "## Tier definitions",
        "1. **TIER_1_HIGH** — explicit TTP phrase (e.g., \"time to positivity\", \"time to detection\", \"DTP\") + blood-culture concept (blood culture, bacteremia, BSI, candidemia, septicemia…)",
        "2. **TIER_2_MED** — standalone abbreviation \"TTP\" + blood-culture concept, excluding rows where \"TTP\" plausibly means something else: thrombotic thrombocytopenic purpura, time to progression (oncology), total testing process (lab QC)",
        "3. **TIER_3_BC_ONLY** — blood-culture concept but no TTP signal in title/abstract",
        "4. **TIER_4_TTP_ONLY** — TTP signal but no blood-culture concept",
        "5. **TIER_5_OFF_TOPIC** — neither concept matched\n",
        "## Result",
    ]
    for k in ["TIER_1_HIGH", "TIER_2_MED", "TIER_3_BC_ONLY", "TIER_4_TTP_ONLY", "TIER_5_OFF_TOPIC"]:
        if k in counts:
            summary.append(f"- **{k}**: {counts[k]:,}")
    summary += [
        "",
        "## Recommended screening order",
        f"1. **TIER_1_HIGH** ({counts.get('TIER_1_HIGH', 0):,}) — almost certainly relevant; screen everything.",
        f"2. **TIER_2_MED** ({counts.get('TIER_2_MED', 0):,}) — likely relevant; screen everything but expect more borderline.",
        f"3. **TIER_3_BC_ONLY** ({counts.get('TIER_3_BC_ONLY', 0):,}) — bacteremia/BSI papers without an explicit TTP keyword. Many will be off-topic but full-text may still report TTP. Sample-screen first to estimate yield.",
        f"4. **TIER_4_TTP_ONLY** ({counts.get('TIER_4_TTP_ONLY', 0):,}) — TTP signal but no blood-culture term; mostly off-topic. Quick scan.",
        f"5. **TIER_5_OFF_TOPIC** ({counts.get('TIER_5_OFF_TOPIC', 0):,}) — neither concept; skip unless you want to spot-check for missing keywords.",
        "",
        "Each row's `ttp_keywords_matched` and `bc_keywords_matched` columns show the exact phrases that fired, so you can audit the classification.",
    ]
    OUT_MD.write_text("\n".join(summary), encoding="utf-8")
    print(f"Wrote {OUT_MD}")
    print("Done.")


if __name__ == "__main__":
    main()
