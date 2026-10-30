# TTP Meta-analysis — Project Resume Notes

**Status:** Tier-3 enrichment complete · screening pool prepared · awaiting full-text PDFs · ready to extend extraction database
**Last updated:** 2026-05-25 by Cowork session `local_d6d15fff`

---

## Where the project stands right now

The Tier-3 PubMed enrichment work is done (all 215 unique PMIDs reviewed). The next-search candidate pool has been deduplicated and triaged against the existing 57 extracted studies. The user is now **downloading full-text PDFs for the 355 papers in the screening pool**; once those arrive the next session will extract data into `TTP_MetaAnalysis_Extraction_Complete.xlsx`.

### Headline numbers

| | |
|---|---|
| Studies already extracted (thesis baseline) | 57 |
| Tier-3 PubMed enrichment decisions | 299 (146 with TTP signal = TRUE) |
| Tier 1 candidates after enrichment (v4 workbook) | 1,017 |
| Papers prioritized as on-topic for "TTP as predictor of antibiotic failure" | 45 (31 Priority A + 14 Priority B) |
| New Elicit search results uploaded by user | 445 rows (348 unique DOIs) |
| **Screening pool to update the thesis database** | **355 papers** |
| Combined Elicit search coverage of the 57 thesis studies | 55/57 = 96% (Alvarez2012 and Peri2026 came from handsearch/snowball) |

---

## What's next (immediate work)

1. **User is downloading full-text PDFs** for the 355 screening-pool papers. Likely workflow: open `TTP_Update_Screening_Pool.xlsx` → use the DOI URL column to fetch each PDF → save into a folder (probably `pdfs/` or similar inside the workspace folder).

2. **Next Cowork session will perform data extraction** from those PDFs into `TTP_MetaAnalysis_Extraction_Complete.xlsx`. The user wants to add new studies to the existing 57-study database — same schema, same study_id format (`AuthorYear`).

3. **Extraction workbook schema** (already in use for the 57 baseline studies):
   - `tbl_study` (19 cols) — study_id, first_author, pub_year, country, study_design, enrollment dates, single/multi-center, funding, risk-of-bias (QUIPS) ratings
   - `tbl_population` (23 cols) — n_total, age, sex, pathogen class/species, %MRSA, infection source, source control, %ICU, severity score, %appropriate empiric, BC system
   - `tbl_ttp` (21 cols) — ttp_reporting (continuous/dichotomized/categorical), unit, mean/median/IQR, cutpoint(s), n_short/n_long, category labels
   - `tbl_outcomes` (23 cols) — outcome_type (mortality/clinical failure/persistence/etc.), definition, timepoint, events_short_ttp, n_short_ttp, events_long_ttp, n_long_ttp, effect_measure, estimate, CI, p, adjusted, beta_per_hour
   - `tbl_es` (17 cols) — auto-populated in R via `metafor::escalc()`; **do not edit manually**
   - `Codebook` — field-by-field descriptions and permitted values (read this before extracting)

4. **Extraction workflow guidance** (from the workbook's `Instructions` sheet — verify in the workbook itself before extracting):
   - One row per study in `tbl_study`, `tbl_population`, `tbl_ttp`
   - Multiple rows allowed in `tbl_outcomes` (one per outcome per arm)
   - `arm_id = 'all'` for whole-cohort estimates; subgroup arms get their own IDs
   - Risk-of-bias uses QUIPS domains, scored 1 (low) / 2 (moderate) / 3 (high)

---

## Key files in the workspace folder

```
new_ttp_metaanalysis/
  RESUME.md                                          ← this file
  TTP_MetaAnalysis_Extraction_Complete.xlsx          ← 57-study baseline (the target to extend)
  Elicit - New_screen-results.xlsx                   ← 445-row new Elicit search (user-uploaded, in /uploads/)
  Elicit - extract.xlsx                              ← 384-row original Elicit search (thesis baseline)

  ── Deliverables produced in this session ─────────
  TTP_Update_Screening_Pool.xlsx                     ← 355 papers to full-text screen → extract
  TTP_Update_Screening_Pool.ris                      ← same 355 records as RIS (import to Zotero/EndNote/Covidence)
  Search_Comparison_New_vs_Old.xlsx                  ← NEW vs OLD Elicit set overlap + 57-thesis coverage
  TTP_Prioritized_Review_List.xlsx                   ← 45 PMIDs (31 A + 14 B) from PubMed enrichment, prioritized
  PRISMA_TIER1_to_Priority_filter.svg                ← flow diagram: how 1,017 → 45 priority papers

  ── Tier-3 enrichment artifacts ───────────────────
  Triage_NewSearch_2026-05-22_tiered_v4.xlsx         ← post-enrichment workbook (TIER_1_HIGH=1,017, TIER_3_CANDIDATES=0)
  Triage_NewSearch_2026-05-22_tiered_v3.xlsx         ← previous checkpoint, preserved
  scripts/
    build_enriched_workbook.py                       ← idempotent rebuild script
  pubmed_lookup/
    enriched_abstracts_full.json                     ← 299 enrichment decisions (FINAL)
    batch_07_decisions.json … batch_27_decisions.json (21 per-batch checkpoints)
    remaining_batch_07.json … remaining_batch_27.json (input files)
    all_doi_to_pmid.json
```

---

## Screening pool composition (the 355 papers)

| Source | Count | Notes |
|---|---:|---|
| `NEW_search` only | 311 | Elicit pre-screened as `Include`; sort by Elicit screening score |
| `NEW_search + PRIORITY_A` | 11 | Highest signal: both Elicit and PubMed enrichment surfaced these |
| `PRIORITY_A` only | 19 | High alignment with "TTP as predictor of antibiotic failure" |
| `NEW_search + PRIORITY_B` | 1 | |
| `PRIORITY_B` only | 13 | TTP measured as outcome in workflow/pre-analytical context |

Already-extracted exclusions: 57 studies matched by first-author surname + year (±1 yr tolerance).

Deliberately deferred (not in this pool):
- **272 "OLD only" DOIs** from the original Elicit search that the new search dropped. These were available during the original thesis and presumably already screened out. Listed in `Search_Comparison_New_vs_Old.xlsx → OLD_only_DOIs` if revisiting needed.
- **~972 BC-system/media comparison papers** in TIER_1_HIGH that don't address the meta-analysis question (Bactec vs BacT/Alert, antimicrobial neutralization, fungal media). See `TTP_Prioritized_Review_List.xlsx` README for rationale.

---

## How the screening pool was derived (audit trail)

1. **Tier 3 PubMed enrichment** (this session + 2 prior sessions): 215 unique Tier-3 PMIDs → 299 abstract-level decisions in `enriched_abstracts_full.json` → 146 flagged as TTP-signal=TRUE → workbook rebuilt with TIER_1_HIGH at 1,017.
2. **Relevance triage of the 146 TTP-signal PMIDs**: keyword filter + manual inspection of "neither" group → **45 priority papers** (31 Priority A clinical-aligned + 14 Priority B workflow-context). Documented in `PRISMA_TIER1_to_Priority_filter.svg`.
3. **User uploaded new Elicit search** (445 papers, all `Include` per Elicit auto-screen).
4. **Cross-check of new search vs the 57-thesis baseline** by first-author surname + year (±1 yr): new search recovers 48/57 thesis studies = 84% (vs 51/57 = 89% for original); combined Elicit coverage is 55/57 = 96%. Full breakdown in `Search_Comparison_New_vs_Old.xlsx`.
5. **Build screening pool**: union of (445 new Elicit) ∪ (45 priority list) − (57 already-extracted, matched by author+year ±1) = **355 unique candidates**.

---

## Per-batch TTP signal hit rates (this session, 17–27)

| Batch | PMIDs | TTP signals | %    |
|------:|------:|------------:|-----:|
| 17    | 10    | 2           | 20%  |
| 18    | 10    | 2           | 20%  |
| 19    | 10    | 4           | 40%  |
| 20    | 10    | 6           | 60%  |
| 21    | 10    | 6           | 60%  |
| 22    | 10    | 8           | 80%  |
| 23    | 10    | 8           | 80%  |
| 24    | 10    | 9           | 90%  |
| 25    | 10    | 10          | 100% |
| 26    | 10    | 9           | 90%  |
| 27    | 10    | 8           | 80%  |
| **Total** | **110** | **72** | **65%** |

Hit rate climbed across older year ranges (1980s–2000s) because those batches were dominated by BC-system comparison studies measuring TTD/LTD as the primary endpoint — promoted by the keyword screen but later filtered out at the Priority A/B step because they don't address the meta-analysis question.

---

## Final tier counts in v4 workbook

- **TIER_1_HIGH**: 1,017 — primary screening pool from the broader Triage workbook
- **TIER_2_MED**: 23
- **TIER_3_OTHER**: 1,928 — no PubMed match (older/non-biomedical journals)
- **TIER_4_TTP_ONLY**: 118
- **TIER_5_OFF_TOPIC**: 1,097

(`TIER_3_CANDIDATES` sheet is gone — all candidates classified.)

---

## Coverage gaps to be aware of

**Missing from BOTH Elicit searches (handsearch/snowball sourced):**
- `Alvarez2012` — *[Prognostic factors of bacteremia: prospective study]* — Spanish
- `Peri2026` — most recent paper, may post-date both Elicit searches

**Missing from the NEW Elicit search but in the OLD search** (and already extracted):
Deas2025, Kassis2009, Maillart2012, Melling2019, Osaki2020, SantosPatarroyo2025, Takahashi2022 — 7 studies. Worth verifying the new Elicit search string didn't unintentionally exclude these (e.g., language filter, date range).

**Newly recovered by the NEW Elicit search** (missed by the OLD search):
Blackberg2022, Blackberg2023, Cilloniz2017, Simeon2019 — 4 studies, validates that the new search is catching some real signal.

---

## Next-session bootstrap prompt (copy/paste)

> Continue the TTP meta-analysis update. Read `RESUME.md` in the project root first. The user has been downloading full-text PDFs for the 355 papers in `TTP_Update_Screening_Pool.xlsx`. The task now is to extract data from those PDFs into `TTP_MetaAnalysis_Extraction_Complete.xlsx`, appending new rows to `tbl_study`, `tbl_population`, `tbl_ttp`, and `tbl_outcomes` using the schema documented in the workbook's Instructions and Codebook sheets. Use the same `AuthorYear` study_id format as the existing 57 rows. Confirm the PDF folder location with the user before starting. After each batch of extractions, save the workbook and report which study_ids were added.

---

## Known issues / gotchas (carried forward)

1. **`Triage_NewSearch_2026-05-22_tiered_v4_summary.md`** is auto-generated by `build_enriched_workbook.py` but the human-readable text still says "v2" with "274 unverified PMIDs" — the numbers are current but the prose is stale. Treat this `RESUME.md` as the source of truth.

2. **`build_enriched_workbook.py`** has session-specific paths in `_CANDIDATE_ROOTS`. Add the next session's `/sessions/<name>/mnt/new_ttp_metaanalysis` path before re-running the script.

3. **Elicit RIS duplicates** — both the old and new Elicit exports produce ~1.4 rows per unique PMID/DOI. Always dedupe by DOI before counting.

4. **Author-name parsing** — old Elicit uses `F. Last, F. Last` format; new Elicit uses `Last, F.; Last, F.` format. Any cross-search join by author must handle both. The parser in `scripts/` was updated this session to handle both.

5. **PubMed legal-attribution** — any user-facing text that cites specific papers must include the DOI link and attribute to PubMed. The deliverables in this session that reference specific papers (e.g., Priority A/B Excel) include DOI URLs per row.
