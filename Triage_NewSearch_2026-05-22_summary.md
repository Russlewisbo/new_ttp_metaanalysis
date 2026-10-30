# Triage of update search vs prior corpus
_Generated 2026-05-22 15:58_

## Inputs
- New search: `review_22.05.05csv.csv` (4,605 records)
- Prior Elicit RIS: `Elicit - TTP as a Predictor of Antibiotic Failure in Bacter - Sources (1).ris` (384 records)
- Already-included studies: 57 (first-author + year fingerprints from `tbl_study`)
- Prior records dropped from fuzzy index as too-short titles: 5 (DOI still indexed)

## Matching rules (in order)
1. **DOI exact match** → `DUP_DOI`
2. **Fuzzy title match** (rapidfuzz token_set_ratio ≥ 90, or ≥ 95 when the prior title looks truncated) → `DUP_TITLE`
3. **Borderline fuzzy match** against a truncated prior title → `NEEDS_REVIEW`
4. **Author + year fingerprint** matches an included study:
   - also matched on Elicit → `ALREADY_INCLUDED`
   - not matched on Elicit → `AUTHOR_YEAR_HIT` (likely the included paper, confirm by eye)
5. Otherwise → `NEW`

## Result
- **NEW**: 4,183
- **NEEDS_REVIEW**: 28
- **AUTHOR_YEAR_HIT**: 3
- **DUP_DOI**: 194
- **DUP_TITLE**: 108
- **ALREADY_INCLUDED**: 89

## How to screen
Open **`Triage_NewSearch_2026-05-22.xlsx`** and work the sheets in this order:
1. **`NEW_only`** — primary screening target.
2. **`NEEDS_REVIEW`** — borderline fuzzy matches; ~1 minute each to adjudicate.
3. **`AUTHOR_YEAR_HIT`** — confirm these really are the included studies, then ignore.
4. **`DUP_DOI`** / **`DUP_TITLE`** / **`ALREADY_INCLUDED`** — already screened in the prior review, no action needed unless you want to spot-check.