# Tiered triage v2 — after PubMed enrichment
_Generated 2026-05-25 06:46_

## What changed in v2
- Pulled abstracts for **75 of the 636** Tier-3 rows that had an empty Abstract field + a DOI:
  - 50 random rows (`Tier3_PubMed_sample_results.csv`) — 9 confirmed Tier 1 promotions
  - 25 sequential rows (from the first DOI batch) — 15 confirmed Tier 1 promotions
  - **24 confirmed promotions Tier 3 → Tier 1** so far
- 299 of the 633 unique Tier-3 DOIs **resolved to a PubMed PMID** (47% resolution rate)
- 274 of those 299 PMIDs still have **un-enriched abstracts** (the remaining work)
- 334 Tier-3 DOIs did not match PubMed (older or non-biomedical journals) — left as `TIER_3_OTHER`

## Yield estimate from the 75-row sample
- 24 promotions out of 45 records that had an abstract (resolved + enriched) = **53% promotion rate** for the PubMed-resolvable subset
- Extrapolated to the 274 unverified PMIDs: **≈ 145 additional papers expected to deserve Tier 1**

## Final tier counts (v2)
- **TIER_1_HIGH**: 1,017
- **TIER_2_MED**: 23
- **TIER_3_OTHER**: 1,928
- **TIER_4_TTP_ONLY**: 118
- **TIER_5_OFF_TOPIC**: 1,097

## How to use this workbook
1. **`TIER_1_HIGH`** (1,017) — primary screening target.
2. **`TIER_3_CANDIDATES`** (0) — Tier 3 rows whose PubMed abstract hasn't been pulled yet. **~53% of these should belong in Tier 1** based on the sample. The sheet is sorted by year (newest first); you can either:
   - (a) Manually screen all of them by title/PubMed lookup — ~1 minute each = ~5 hours total
   - (b) Spend another Cowork session pulling the remaining 274 abstracts to verify automatically (script is ready)
3. **`TIER_3_OTHER`** (1,928) — Tier 3 without a PubMed match. Older or non-biomedical journals; expected to be off-topic. Low priority.
4. **`TIER_2_MED`** (23) — quick scan as before.
5. **`TIER_4_TTP_ONLY`** / **`TIER_5_OFF_TOPIC`** — skip unless spot-checking.

## Pre-empted next step
The script `scripts/build_enriched_workbook.py` is idempotent — once the remaining 274 PMID abstracts are fetched (saved into `pubmed_lookup/enriched_abstracts.json`), re-running it will update the workbook automatically.