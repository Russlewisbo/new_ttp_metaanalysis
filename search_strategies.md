# Search strategies — TTP meta-analysis

**Companion supplementary file to:** *"Time-to-positivity of blood cultures as a predictor of antibiotic failure and mortality in bacteremia: a systematic review and Bayesian meta-analysis"*

**Compliance target:** PRISMA-S checklist (Rethlefsen et al. *Syst Rev* 2021;10:39).

**Status:** TEMPLATE — sections marked `[FILL: …]` need to be completed from the search execution logs before submission. Sections without `[FILL]` are reconstructed from the project's PROSPERO protocol and screening artifacts and should be verified rather than re-written.

---

## 0. Search-date evidence found in the project (read before filling Section 1)

Exact search execution dates are **not recorded anywhere in the project files**, so none of the `[FILL]` cells below could be completed without inventing them. The dates that *can* be supported are listed here. File dates are when a file was created or copied, not when a search was run, so treat them as upper bounds to be replaced with the dates from your database search histories or exported files.

| Evidence | Date | What it supports |
|---|---|---|
| `Elicit_vs_PubMed_triage_report.md` header | 2026-05-12 | Redesigned PubMed strategy compared with the Elicit corpus (V1: 571 records; V3, after fixes: 1,245 records), so PubMed V1/V3 had been run by this date |
| `Elicit - ... Sources (1).ris` (384 records), `TTP_Revised- Sources.ris` | files dated 2026-05-12 to 2026-05-20 | Original Elicit corpus (thesis baseline), run date unknown |
| `Triage_NewSearch_2026-05-22*` | 2026-05-22 | Update search triaged (445-row Elicit export; PubMed record used for triage). Run date inferred as on or before 2026-05-22 |
| `review_22.05.05csv.csv` (4,605 rows) | file dated 2026-05-22 | Covidence export. Provenance of the 4,605 records (which databases, what dates) is **not documented** |
| `Tier3_PubMed_sample_summary.md` | 2026-05-23 | PubMed enrichment of candidate records |
| `TTP_Update_Screening_Pool.*` | 2026-05-25 | 355-record screening pool |

**Search scope (confirmed by the author, 2026-10-30):** the five-database search (PubMed, Embase, Scopus, Cochrane CENTRAL, Web of Science) was executed, and its records are the 4,605 in the Covidence export. CINAHL was **not** searched. Trial registers and preprint servers were **not** searched. No reference-list searching or forward/backward citation tracking was performed. These are deviations from the PROSPERO protocol, which listed CINAHL, trial registers, preprint servers and citation tracking, and they should be reported as such.

Still needed from the author: per-database run dates and record counts (original and update), PubMed run dates, and the role of Elicit. Project files show that the 355-record screening pool was built from an Elicit export plus PubMed enrichment, and that Alvarez 2012 and Peri 2026 are recorded as "handsearch/snowball" in RESUME.md. Both conflict with "no reference-list searching" and need to be reconciled in the Methods and PRISMA flow.

---

## 1. Information sources

### 1.1 Bibliographic databases

| # | Database | Platform / Vendor | Original-search date | Updated-search date |
|---:|---|---|---|---|
| 1 | MEDLINE | PubMed (NLM) | `[FILL: YYYY-MM-DD]` | `2026-05-22` *(inferred from filename `Triage_NewSearch_2026-05-22…`; please confirm)* |
| 2 | Embase | Elsevier (embase.com) | `[FILL: YYYY-MM-DD]` | `[FILL: YYYY-MM-DD]` |
| 3 | Cochrane CENTRAL | Wiley Cochrane Library | `[FILL: YYYY-MM-DD]` | `[FILL: YYYY-MM-DD]` |
| 4 | Web of Science Core Collection | Clarivate | `[FILL: YYYY-MM-DD]` | `[FILL: YYYY-MM-DD]` |
| 5 | Scopus | Elsevier *(added vs thesis)* | n/a | `[FILL: YYYY-MM-DD]` |
| 6 | CINAHL Complete | EBSCOhost | NOT EXECUTED | NOT EXECUTED |

> **Note:** The PROSPERO protocol lists 6 databases. The user-reported total of 4,605 records spans 5 (PubMed, Embase, Scopus, Cochrane, WOS). **Clarify CINAHL's disposition** — either rolled into one of the other counts, dropped at execution, or run separately. This affects the PRISMA figure top-row count.

### 1.2 Trial registers

| # | Register | URL | Searched? | Execution date |
|---:|---|---|---|---|
| 1 | ClinicalTrials.gov | clinicaltrials.gov | NO | n/a |
| 2 | WHO ICTRP | trialsearch.who.int | NO | n/a |

### 1.3 Preprint servers

| # | Server | URL | Searched? | Execution date |
|---:|---|---|---|---|
| 1 | medRxiv | medrxiv.org | NO | n/a |
| 2 | bioRxiv | biorxiv.org | NO | n/a |

### 1.4 Other methods

| Method | Source paper(s) | Date executed | Records contributed |
|---|---|---|---|
| Forward citation tracking | Hsieh et al. 2022 (*BMC Infect Dis*) | NOT PERFORMED | 0 |
| Forward citation tracking | IJMPR 2026 systematic review | NOT PERFORMED | 0 |
| Reference-list hand-searching | Reference lists of included studies | NOT PERFORMED *(RESUME.md records Álvarez 2012 and Peri 2026 as handsearch/snowball; reconcile)* | 0 |
| Expert contact / direct correspondence | First/senior authors of key studies | `[FILL: YYYY-MM-DD]` | `[FILL: N records]` |

---

## 2. Search strategy — verbatim

The strategy combines **two concept blocks** with `AND`, deliberately omitting an outcome block to maximize sensitivity for prognostic-factor studies whose outcomes may be reported as secondary findings and may not be reliably indexed.

- **Block A — Population**: bloodstream infection / bacteremia / fungemia / blood culture / sepsis
- **Block B — Exposure**: time-to-positivity and its synonyms

No outcome block. No methodological filter. Human studies only.

### 2.1 PubMed (MEDLINE) — verbatim

Strategy version: V3 *(post-defect-fix per `Elicit_vs_PubMed_triage_report.md`)*.

```
[FILL: paste the V3 PubMed strategy here, line-numbered, in this format:

#1   "blood culture"[MeSH Terms] OR "blood cultures"[tiab] OR …
#2   "bacteremia"[MeSH Terms] OR bacteremia[tiab] OR bacteraemia[tiab] OR …
#3   "fungemia"[MeSH Terms] OR fungemia[tiab] OR fungaemia[tiab] OR …
#4   "sepsis"[MeSH Terms] OR sepsis[tiab] OR …
#5   #1 OR #2 OR #3 OR #4
#6   "time to positivity"[tiab] OR "time-to-positivity"[tiab] OR …
#7   "time to detection"[tiab] OR "growth detection time"[tiab] OR …
#8   "differential time to positivity"[tiab] OR DTP[tiab] OR DTTP[tiab] OR …
#9   TTP[tiab] AND ("blood culture"[tiab] OR bacteremia[tiab] OR …)   ← TTP disambiguated from TTP=thrombotic thrombocytopenic purpura / triphosphate
#10  #6 OR #7 OR #8 OR #9
#11  #5 AND #10
#12  #11 NOT (animals[MeSH] NOT humans[MeSH])
]
```

**Date(s) run:** `[FILL: original YYYY-MM-DD / update YYYY-MM-DD]`
**Records retrieved:** `[FILL: N]`

### 2.2 Embase (Elsevier embase.com) — verbatim

```
[FILL: paste the Embase strategy here, line-numbered.
 Use Emtree terms with /exp explosion + free-text :ti,ab with truncation.

 #1   'blood culture'/exp OR 'blood culture':ti,ab,kw
 #2   'bacteremia'/exp OR bacteremia:ti,ab,kw OR bacteraemia:ti,ab,kw
 #3   …
]
```

**Date(s) run:** `[FILL: …]`
**Records retrieved:** `[FILL: N]`

### 2.3 Cochrane CENTRAL — verbatim

```
[FILL: paste the CENTRAL strategy here.

 #1   MeSH descriptor: [Blood Culture] explode all trees
 #2   "blood culture":ti,ab,kw
 #3   …
]
```

**Date(s) run:** `[FILL: …]`
**Records retrieved:** `[FILL: N]`

### 2.4 Web of Science Core Collection (Clarivate) — verbatim

```
[FILL: paste the WOS strategy here.

 #1   TS=("blood culture*" OR bacterem* OR bacteraem* OR fungem* OR fungaem* OR sepsis)
 #2   TS=("time to positivity" OR "time-to-positivity" OR …)
 #3   #1 AND #2
]
```

**Date(s) run:** `[FILL: …]`
**Records retrieved:** `[FILL: N]`
**Indexes searched:** `[FILL: e.g. SCI-EXPANDED, SSCI, ESCI; date range]`

### 2.5 Scopus (Elsevier) — verbatim

```
[FILL: paste the Scopus strategy here.

 TITLE-ABS-KEY( ("blood culture*" OR bacterem* OR bacteraem* OR fungem* OR fungaem* OR sepsis)
                AND
                ("time to positivity" OR "time-to-positivity" OR "time to detection" OR …) )
 AND PUBYEAR > [lower-bound] AND PUBYEAR < [upper-bound]
 AND DOCTYPE(ar OR re OR cp)
]
```

**Date(s) run:** `[FILL: …]`
**Records retrieved:** `[FILL: N]`

### 2.6 CINAHL Complete (EBSCOhost) — verbatim *(if executed)*

```
[FILL: paste the CINAHL strategy here OR mark "NOT EXECUTED — substituted by Scopus per …"]
```

**Date(s) run:** `[FILL: …]`
**Records retrieved:** `[FILL: N]`

---

## 3. Per-database results summary (feeds the PRISMA figure)

| Source | Records identified | Search date |
|---|---:|---|
| MEDLINE (PubMed) | `[FILL: N]` | `[FILL: date]` |
| Embase | `[FILL: N]` | `[FILL: date]` |
| Cochrane CENTRAL | `[FILL: N]` | `[FILL: date]` |
| Web of Science | `[FILL: N]` | `[FILL: date]` |
| Scopus | `[FILL: N]` | `[FILL: date]` |
| CINAHL | not executed | n/a |
| **Subtotal from databases** | **`[FILL: sum] = 4,605`** *(per user)* | — |
| Hand-search of reference lists | not performed *(reconcile with Álvarez 2012, Peri 2026)* | n/a |
| Forward citation tracking | not performed | n/a |
| Trial registers (CT.gov, ICTRP) | not searched | n/a |
| Preprint servers (medRxiv, bioRxiv) | not searched | n/a |
| Expert correspondence | `[FILL: N or '0']` | `[FILL: date]` |
| **Subtotal from other methods** | **`[FILL: sum]`** | — |
| **Grand total identified** | **`[FILL: sum]`** | — |

---

## 4. Deduplication

| Field | Value |
|---|---|
| Tool / software used | `[FILL: e.g. Rayyan / EndNote 21 / Covidence / R script (provide version)]` |
| Match keys | `[FILL: e.g. DOI exact + (first-author surname + year ±1) fuzzy match]` |
| Manual verification of probable duplicates | `[FILL: YES / NO]` |
| Records removed as duplicates | **1,409** *(per user)* |
| Records after deduplication | **3,196** |

---

## 5. Screening process

### 5.1 Title / abstract screening

| Field | Value |
|---|---|
| Records screened | **3,196** |
| Software used | `[FILL: e.g. Rayyan / Covidence / Elicit / custom script]` |
| Reviewers | `[FILL: e.g. "Two independent reviewers (initials), discrepancies resolved by third reviewer (initials)" OR "Single reviewer (initials), LLM-assisted with structured-prompt second-pass QC"]` |
| Records excluded | **2,841** *(derived = 3,196 − 355)* |
| Records sought for retrieval | **355** |

### 5.2 Retrieval

| Field | Value |
|---|---|
| Reports sought | **355** |
| Reports not retrieved | **53** *(deliberately not downloaded at retrieval triage — pre-screened as ineligible: predominantly conference abstracts, non-English-language papers, methods-only papers)* |
| Reports assessed for eligibility | **302** *(307 PDFs in `new_ttp_pdfs/` minus 5 baseline duplicates already in the thesis database)* |

### 5.3 Full-text eligibility (strict criterion)

| Field | Value |
|---|---|
| Reports assessed | **302** |
| Reviewers | `[FILL: per above. The 2026 update was assisted by an LLM agent with independent second-pass QC verification — see `QC_Verification_Report.md`. Update wording to your preference.]` |
| **Excluded** | **259** *(see `PDF_Extraction_Inclusion_Exclusion_Report.md` for full audit trail)* |
| └ wrong_design (review, abstract, case report n<10, study protocol, correspondence) | **104** |
| └ no_ttp (TTP not measured — confused with duration-of-bacteremia, time-to-antibiotic, etc.) | **65** |
| └ no_assoc (TTP and outcome both reported but no quantitative TTP↔outcome model) | **54** |
| └ no_outcome (methods/microbiology paper only) | **29** |
| └ duplicate (filename or republication duplicate) | **5** |
| └ not_bsi (population not bloodstream infection) | **2** |
| **Included (strict)** | **43** *(new in v4 update)* |
| **Plus baseline (already in database from thesis)** | **57** |
| **TOTAL in primary analysis pool** | **100** |

### 5.4 Inclusive re-screen (sensitivity-pool addendum)

`See Inclusive_Rescreen_Addendum.md.` 54 papers previously excluded as `no_assoc` were re-assessed under inclusive criteria (TTP + outcome both present in cohort, even without quantitative model). **40 flipped to include** for the sensitivity pool; **14 stayed excluded** (7 no_outcome, 4 no_ttp, 2 wrong_design, 1 ttp_is_outcome_not_exposure).

| Pool | N studies |
|---|---:|
| Primary (strict): 57 baseline + 43 new strict | **100** |
| Sensitivity (strict + inclusive): + 40 inclusive | **140** |

---

## 6. Limits and filters

| Element | Setting |
|---|---|
| Date range | No lower bound (inception); upper bound = search-execution date |
| Language | No language restriction at search level |
| Language eligibility | English, Italian, Spanish, French, German, Portuguese (translation capability in review team) |
| Publication type | Excluded: editorials, commentaries, narrative reviews, case reports / series n<10, conference abstracts without sufficient quantitative data, existing systematic reviews / meta-analyses (used only as sources for citation tracking) |
| Human filter | Applied as `NOT (animals[MeSH] NOT humans[MeSH])` in PubMed *(V3 fix per `Elicit_vs_PubMed_triage_report.md` — the original `humans[All Fields]` filter caused false-negatives for MDPI papers with MeSH-tagging lag, including Bae 2021)* |
| Study design | Observational: prospective and retrospective cohort, case-control, registry-based, RCT cohort phases. Excluded: pure case series |

---

## 7. Search strategy peer review (PRESS)

| Element | Status |
|---|---|
| PRESS-checklist review performed? | `[FILL: YES — by [reviewer] on [date] / NO — note plan]` |
| Reviewer credentials | `[FILL: e.g. medical librarian, MLS]` |
| Key recommendations and responses | `[FILL: bullet-point summary OR 'see attached PRESS form']` |

---

## 8. Search strategy iteration history

Per `Elicit_vs_PubMed_triage_report.md` (2026-05-12):

- **V1 PubMed strategy** retrieved 10/18 (56%) of currently-included full-text studies. Diagnosed defects:
  - **Humans-filter bug** — `humans[All Fields]` excluded Bae 2021 (MDPI, MeSH-lag). Fixed in V3 by switching to `NOT (animals[MeSH] NOT humans[MeSH])`.
  - **British/American spelling gap** — missing `bacteraemia`, `fungaemia` variants in some blocks.
  - **TTP disambiguation insufficient** — bare `TTP[tiab]` returned excess noise from thrombotic thrombocytopenic purpura papers.
  - `[FILL: any other documented V1→V3 fixes]`
- **V3 PubMed strategy** brought PubMed sensitivity to **14/18 (78%)**. Residual 4-paper gap is structural (not PubMed-indexed); recovered via Embase + Scopus + forward-citation tracking.

---

## 9. Reproducibility

| Element | Status / link |
|---|---|
| OSF deposit DOI for search-execution exports | `[FILL: 10.17605/OSF.IO/XXXXX]` |
| Raw `.ris` exports | Included in OSF deposit: `[FILL: file list]` |
| PRISMA-S checklist completed | `[FILL: YES — attached / NO]` |
| All search strings re-runnable as documented above | Yes — line-numbered |

---

## 10. Items still to decide / verify before figure finalization

- [ ] **Per-database counts** (Section 3) — pull from each database's search export
- [ ] **CINAHL disposition** (Section 1.1) — was it actually run?
- [ ] **Search execution dates** for original and update runs (Section 1.1, 2.x)
- [ ] **Whether trial registers / preprint servers were actually queried**, and if so the counts (Section 1.2, 1.3)
- [ ] **Reviewer roster** (Section 5.x) — single-reviewer + LLM with QC, or dual independent?
- [ ] **Deduplication tool/method** (Section 4)
- [ ] **PRESS review status** (Section 7)

Once Sections 1.1, 3, and 4 are filled, the publication PRISMA figure can be generated with full per-database counts and exact dates. Update `PRISMA_v4_update.svg` to a `PRISMA_v4_publication.svg` (and PDF/PNG/PPTX) once these are in.
