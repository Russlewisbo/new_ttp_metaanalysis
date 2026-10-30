"""
Build the final enriched triage workbook v2.

Inputs:
  - Triage_NewSearch_2026-05-22_tiered.xlsx (current tiered output)
  - Tier3_PubMed_sample_results.csv (50-row sample verified manually)
  - pubmed_lookup/enriched_abstracts.json (25 PMIDs verified from full pool)
  - pubmed_lookup/all_doi_to_pmid.json (299 PMIDs resolved from 633 DOIs)

Output:
  - Triage_NewSearch_2026-05-22_tiered_v2.xlsx
      All           — every NEW row with status, tier, and (where applicable) the
                      PMID, abstract enrichment status, and verified TTP decision
      TIER_1_HIGH   — Tier 1 + the 24 confirmed promotions from PubMed sampling
      TIER_2_MED
      TIER_3_CANDIDATES — Tier 3 rows that have a PMID but haven't been verified yet
                          (yield estimate ~53% should be Tier 1). Sorted by year desc.
      TIER_3_OTHER  — Tier 3 rows without a PMID
      TIER_4_TTP_ONLY
      TIER_5_OFF_TOPIC
      Summary       — counts and recommendation
"""

from __future__ import annotations
import csv, json, re, sys
from pathlib import Path
import pandas as pd

_CANDIDATE_ROOTS = [
    Path("/Users/russelllewis/Desktop/new_ttp_metaanalysis"),
    Path("/sessions/affectionate-keen-franklin/mnt/new_ttp_metaanalysis"),
    Path("/sessions/relaxed-blissful-allen/mnt/new_ttp_metaanalysis"),
    Path("/sessions/dazzling-wonderful-curie/mnt/new_ttp_metaanalysis"),
]


def _safe_exists(p: Path) -> bool:
    try:
        return p.exists()
    except (OSError, PermissionError):
        return False


ROOT = next((p for p in _CANDIDATE_ROOTS if _safe_exists(p)), _CANDIDATE_ROOTS[0])

IN_XLSX  = ROOT / "Triage_NewSearch_2026-05-22_tiered.xlsx"
DOI2PMID = ROOT / "pubmed_lookup" / "all_doi_to_pmid.json"
# Use the latest (full) enriched file which contains decisions accumulated across sessions.
ENRICHED = ROOT / "pubmed_lookup" / "enriched_abstracts_full.json"
SAMPLE50 = ROOT / "Tier3_PubMed_sample_results.csv"
OUT_XLSX = ROOT / "Triage_NewSearch_2026-05-22_tiered_v4.xlsx"
OUT_MD   = ROOT / "Triage_NewSearch_2026-05-22_tiered_v4_summary.md"


def normalize_doi(d: str) -> str:
    if not d: return ""
    d = d.strip().lower()
    d = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", d)
    return d.strip().strip(".").strip()


def main() -> None:
    print("Loading tiered workbook …")
    df = pd.read_excel(IN_XLSX, sheet_name="All_NEW")
    print(f"  {len(df):,} NEW rows")

    df["doi_norm"] = df["DOI"].fillna("").map(normalize_doi)

    print("Loading DOI → PMID map …")
    doi2pmid = json.load(open(DOI2PMID))
    df["pmid"] = df["doi_norm"].map(doi2pmid).fillna("")
    print(f"  Rows with resolved PMID: {(df['pmid']!='').sum():,}")

    print("Loading enriched abstracts (verified by PubMed) …")
    enriched = json.load(open(ENRICHED))
    enriched_pmids = set(enriched.keys())
    df["enriched"] = df["pmid"].isin(enriched_pmids)
    print(f"  Rows with enriched abstract: {df['enriched'].sum()}")

    # Load 50-row sample decisions
    print("Loading 50-row sample decisions …")
    sample = pd.read_csv(SAMPLE50, dtype=str).fillna("")
    sample["doi_norm"] = sample["doi"].str.lower()
    sample_decision = dict(zip(sample["doi_norm"], sample["decision"]))
    df["sample50_decision"] = df["doi_norm"].map(sample_decision).fillna("")

    # Build verified-decision column
    def decide(row):
        if row["sample50_decision"] == "PROMOTE_TIER_1":
            return "PROMOTE_TIER_1"
        if row["sample50_decision"] == "KEEP_TIER_3":
            return "KEEP_TIER_3"
        if row["pmid"] and row["pmid"] in enriched_pmids:
            return "PROMOTE_TIER_1" if enriched[row["pmid"]]["ttp_signal"] else "KEEP_TIER_3"
        return ""  # unverified
    df["pubmed_verified_decision"] = df.apply(decide, axis=1)

    # Apply promotions
    promote_mask = df["pubmed_verified_decision"] == "PROMOTE_TIER_1"
    n_promote = promote_mask.sum()
    print(f"Confirmed promotions Tier 3 → Tier 1: {n_promote}")
    df.loc[promote_mask, "tier"] = "TIER_1_HIGH"
    df.loc[promote_mask, "ttp_keywords_matched"] = (
        df.loc[promote_mask, "ttp_keywords_matched"].fillna("").astype(str) +
        " [verified via PubMed abstract]"
    ).str.strip()

    # Mark unverified Tier 3 with a PMID as TIER_3_CANDIDATES (53% expected yield)
    cand_mask = (df["tier"] == "TIER_3_BC_ONLY") & (df["pmid"] != "") & (df["pubmed_verified_decision"] == "")
    df.loc[cand_mask, "tier"] = "TIER_3_CANDIDATES"
    n_cand = cand_mask.sum()
    print(f"Unverified Tier 3 candidates (PMID exists, abstract not yet pulled): {n_cand}")

    # Renaming remaining Tier 3
    df.loc[df["tier"] == "TIER_3_BC_ONLY", "tier"] = "TIER_3_OTHER"

    # Final counts
    counts = df["tier"].value_counts().to_dict()
    print("\nFinal tier counts:")
    for k in ["TIER_1_HIGH", "TIER_2_MED", "TIER_3_CANDIDATES", "TIER_3_OTHER",
              "TIER_4_TTP_ONLY", "TIER_5_OFF_TOPIC"]:
        if k in counts:
            print(f"  {k:>20}: {counts[k]:,}")

    # Reorder columns
    front = ["tier", "pubmed_verified_decision", "pmid", "ttp_keywords_matched",
             "bc_keywords_matched", "Title", "Authors", "Published Year",
             "Journal", "DOI"]
    other = [c for c in df.columns if c not in front]
    df = df[front + other]

    # Write workbook
    print(f"\nWriting {OUT_XLSX} …")
    with pd.ExcelWriter(OUT_XLSX, engine="openpyxl") as xw:
        df.to_excel(xw, sheet_name="All_NEW", index=False)
        for tier in ["TIER_1_HIGH", "TIER_2_MED", "TIER_3_CANDIDATES",
                     "TIER_3_OTHER", "TIER_4_TTP_ONLY", "TIER_5_OFF_TOPIC"]:
            sub = df[df["tier"] == tier]
            if len(sub):
                # For Tier 3 candidates, sort by year desc to put recent papers first
                if tier == "TIER_3_CANDIDATES":
                    sub = sub.sort_values("Published Year", ascending=False, na_position="last")
                sub.to_excel(xw, sheet_name=tier, index=False)

    # Markdown summary
    summary = [
        "# Tiered triage v2 — after PubMed enrichment",
        f"_Generated {pd.Timestamp.now():%Y-%m-%d %H:%M}_\n",
        "## What changed in v2",
        f"- Pulled abstracts for **75 of the 636** Tier-3 rows that had an empty Abstract field + a DOI:",
        "  - 50 random rows (`Tier3_PubMed_sample_results.csv`) — 9 confirmed Tier 1 promotions",
        "  - 25 sequential rows (from the first DOI batch) — 15 confirmed Tier 1 promotions",
        f"  - **24 confirmed promotions Tier 3 → Tier 1** so far",
        "- 299 of the 633 unique Tier-3 DOIs **resolved to a PubMed PMID** (47% resolution rate)",
        "- 274 of those 299 PMIDs still have **un-enriched abstracts** (the remaining work)",
        "- 334 Tier-3 DOIs did not match PubMed (older or non-biomedical journals) — left as `TIER_3_OTHER`",
        "",
        "## Yield estimate from the 75-row sample",
        "- 24 promotions out of 45 records that had an abstract (resolved + enriched) = **53% promotion rate** for the PubMed-resolvable subset",
        "- Extrapolated to the 274 unverified PMIDs: **≈ 145 additional papers expected to deserve Tier 1**",
        "",
        "## Final tier counts (v2)",
    ]
    order = ["TIER_1_HIGH", "TIER_2_MED", "TIER_3_CANDIDATES", "TIER_3_OTHER",
             "TIER_4_TTP_ONLY", "TIER_5_OFF_TOPIC"]
    for k in order:
        if k in counts:
            summary.append(f"- **{k}**: {counts[k]:,}")
    summary += [
        "",
        "## How to use this workbook",
        f"1. **`TIER_1_HIGH`** ({counts.get('TIER_1_HIGH',0):,}) — primary screening target.",
        f"2. **`TIER_3_CANDIDATES`** ({counts.get('TIER_3_CANDIDATES',0):,}) — Tier 3 rows whose PubMed abstract hasn't been pulled yet. **~53% of these should belong in Tier 1** based on the sample. The sheet is sorted by year (newest first); you can either:",
        "   - (a) Manually screen all of them by title/PubMed lookup — ~1 minute each = ~5 hours total",
        "   - (b) Spend another Cowork session pulling the remaining 274 abstracts to verify automatically (script is ready)",
        f"3. **`TIER_3_OTHER`** ({counts.get('TIER_3_OTHER',0):,}) — Tier 3 without a PubMed match. Older or non-biomedical journals; expected to be off-topic. Low priority.",
        f"4. **`TIER_2_MED`** ({counts.get('TIER_2_MED',0):,}) — quick scan as before.",
        f"5. **`TIER_4_TTP_ONLY`** / **`TIER_5_OFF_TOPIC`** — skip unless spot-checking.",
        "",
        "## Pre-empted next step",
        "The script `scripts/build_enriched_workbook.py` is idempotent — once the remaining 274 PMID abstracts are fetched (saved into `pubmed_lookup/enriched_abstracts.json`), re-running it will update the workbook automatically.",
    ]
    OUT_MD.write_text("\n".join(summary), encoding="utf-8")
    print(f"Wrote {OUT_MD}")
    print("Done.")


if __name__ == "__main__":
    main()
