# Screening-Pool Papers Without Downloaded PDFs

**Status:** RESOLVED — no action needed. Confirmed 2026-05-26.

Of the 355 papers in the screening pool, **307 PDFs were downloaded** (in `new_ttp_pdfs/`). The remaining **57 pool entries lack PDFs by design** — the user pre-screened them out during the download triage as not meeting inclusion criteria (conference abstracts, foreign-language papers, methods-only papers, narrative reviews, etc.) and chose not to download.

In other words: the 307 PDFs in the folder ARE the screening pool the user intended to review. The 57 absent entries are already-excluded items kept in the pool spreadsheet only for audit purposes.

The 302 PDFs we screened (307 minus 5 baseline duplicates) represent the complete set of full-text review papers for this update.

## Reference files

These were generated during the missing-PDF audit but are NOT a backlog:

- `Missing_PDFs.csv` — list of the 57 entries with DOI URLs (for reference only)
- `new_ttp_pdfs/Rogers_1998_FETCHED.pdf` — single OA paper auto-fetched during the audit; can be deleted since it duplicates an existing baseline study

## What this means for the extraction state

| | Count | Status |
|---|---:|---|
| Pool entries | 355 | — |
| Pre-screened out (no PDF download) | 57 | Deliberate; do not pursue |
| PDFs downloaded | 307 | In `new_ttp_pdfs/` |
| Baseline duplicates (skipped) | 5 | Already in 57-study baseline |
| PDFs screened in this run | 302 | All resolved |
| Strict-pool extractions in v3 workbook | 43 | + 57 baseline = 100 |
| Inclusive-pool extractions in v4 workbook | 40 | + 100 = 140 total |

**No outstanding download or screening work remains.**
