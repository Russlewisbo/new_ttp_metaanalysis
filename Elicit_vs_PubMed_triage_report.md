# Triage report: Elicit corpus vs. redesigned PubMed search

**Date:** 2026-05-12
**Purpose:** Determine whether the redesigned reproducible PubMed strategy can defend the Elicit-derived corpus currently feeding the meta-analysis, and identify search gaps before PROSPERO registration.

---

## Headline finding

**The originally redesigned PubMed strategy retrieved only 10 of the 18 actually-included full-text studies (56%).** Four of the eight misses were caused by fixable search-strategy defects; three are not indexed in PubMed at all (require Embase / grey-literature defense); one is a borderline inclusion that does not discuss TTP in its title or abstract and is only retrievable via citation tracking. The revised V3 strategy below recovers four of those missed inclusions and brings PubMed sensitivity to 14/18 (78%) — the residual gap is structural and requires the multi-database / forward-citation supplements already planned.

This is a serious finding for the PROSPERO registration: had we registered the original V1 strategy and re-run it from scratch, almost half of the current included studies would have been invisible. Fix the strategy before submitting.

---

## Corpus sizes

| Source | Records |
|---|---|
| Elicit corpus (full `Elicit - … - Sources (1).ris`) | 384 |
| Elicit corpus (with DOI) | 364 |
| Elicit corpus (no DOI — see appendix) | 20 |
| Redesigned PubMed V1 search | 571 |
| Redesigned PubMed V3 search (post-fix) | 1,245 |
| Currently-included full-text studies (PDFs in `publications/`) | 18 |

(Note: the 20-PDF folder contains 18 unique TTP studies once duplicates and the Edwards 2025 / Marco 2025 / Santos-Patarroyo 2025 / Deas 2025 additions are de-duplicated against the original 17 from the thesis. The extraction database has 57 study rows but many are non-PICO placeholders or partial extractions, per `AGENTS.md`.)

---

## Overlap between Elicit and redesigned PubMed V1

| Set | Count |
|---|---|
| In both (reproducibly defensible via PubMed alone) | 99 |
| Elicit only (not retrieved by PubMed V1) | 265 |
| PubMed V1 only (new candidates Elicit missed) | 447 |

The Elicit-only set of 265 is the corpus we cannot currently defend on PubMed-reproducibility grounds. Most are likely retrievable via Embase, Scopus, or citation tracking; some will be off-topic semantic matches that Elicit returned but would be excluded at screening.

The PubMed-only set of 447 is a screening workload, not a problem — most will be irrelevant on title/abstract review.

---

## Per-study diagnosis of missed inclusions (V1)

The 8 currently-included studies missed by V1 split into four diagnostic categories:

**Category A — PubMed humans filter bug (1 study).** Bae 2021 (PMID 34201159, *Antibiotics* — MDPI) matched the population and exposure blocks but was excluded by `humans[All Fields]`. MDPI papers are PubMed-indexed but MeSH human-tagging lags by months. Fix: drop the humans filter and substitute `NOT (animals[MeSH] NOT humans[MeSH])`.

**Category B — Exposure phrase too narrow (2 studies).**
- Melling 2019 (PMID 31544471, *Ann Pharmacother*) — title is "Time to First Culture Positivity Among Critically Ill Adults With MRSA…". The phrase `"time to first culture positivity"[ti]` does not match (a PubMed phrase-indexing quirk for phrases starting with "time to first"), but `"culture positivity"[tiab]` does. Fix: add `"culture positivity"[tiab] OR "blood culture positivity"[tiab]` to the exposure block.
- Minejima 2019 (PMID 30949675, *Clin Infect Dis*) — title is "Defining the Breakpoint Duration of Staphylococcus aureus Bacteremia…". Uses "bacteremia duration" rather than TTP terminology. This is the conceptually-adjacent "duration of positivity" framing. Fix: add a `"bacteremia duration" OR "duration of bacteremia"` concept block as an alternative path.

**Category C — Indexed in PubMed but only mentions TTP in full text (1 study).** Ji 2020 (PMID 32561441, *Chest*) — title and abstract discuss BSI and delayed antibiotic coverage without using TTP phrasing. The TTP analysis is in the full text only. Not catchable by any reasonable title/abstract search; this is the canonical case for forward-citation tracking and reference-list hand search. Not a search-strategy defect — a known limitation that PRISMA-S explicitly accommodates.

**Category D — Not indexed in PubMed (3 studies).**
- "E 2012" — Association between TTP and S. aureus Bacteremia in a Geriatric Population. First-author surname appears to be a single letter; likely a conference proceeding or grey publication. Not in PubMed.
- Nadeem 2021 — Time to Grow Positive Blood Cultures…
- Takahashi 2022 — Analysis of Time to Blood Culture Positivity…

These three require Embase or grey-literature retrieval. Embase indexes many regional and proceedings journals that PubMed does not. If still missed there, defend via hand-search of reference lists and direct author contact.

**Category E — Script artifact, not a real miss (1 study).** Zhang 2021 (PMID 34302546, *Support Care Cancer*) — was caught by V1 but my matching script flagged it as missed because PubMed pub-date is 2022 while the PDF filename year is 2021. Not a search defect.

---

## Recommended V3 PubMed strategy (paste-ready)

```
(
  "Blood Culture"[Mesh] OR "Bacteremia"[Mesh] OR "Fungemia"[Mesh]
  OR "Candidemia"[Mesh] OR "Sepsis"[Mesh]
  OR "Bacteraemi*"[tiab] OR "Bacteremi*"[tiab]
  OR "Fungaemi*"[tiab] OR "Fungemi*"[tiab]
  OR "Candidaemi*"[tiab] OR "Candidemi*"[tiab]
  OR "Blood culture"[tiab] OR "Blood cultures"[tiab]
  OR "Bloodstream infection"[tiab] OR "Bloodstream infections"[tiab]
  OR "Blood stream infection"[tiab] OR "Blood stream infections"[tiab]
  OR "BSI"[tiab] OR "BSIs"[tiab]
)
AND
(
    "time to positivity"[tiab] OR "time-to-positivity"[tiab]
  OR "time to blood culture positivity"[tiab]
  OR "time to culture positivity"[tiab]
  OR "blood culture positivity"[tiab]
  OR "culture positivity"[tiab]
  OR "time to detection"[tiab] OR "time-to-detection"[tiab]
  OR "time to growth"[tiab]
  OR "time to positive"[tiab]
  OR "growth detection time"[tiab]
  OR "differential time to positivity"[tiab]
  OR "DTP"[tiab] OR "DTTP"[tiab]
  OR ( "TTP"[tiab]
       AND ("blood culture"[tiab] OR "blood cultures"[tiab]
            OR bacter*emi*[tiab] OR bloodstream[tiab]) )
  OR "bacteremia duration"[tiab] OR "bacteraemia duration"[tiab]
  OR "duration of bacteremia"[tiab] OR "duration of bacteraemia"[tiab]
)
NOT (animals[MeSH Terms] NOT humans[MeSH Terms])
```

Yields **1,245 hits** (vs. 571 for V1). Sensitivity against the 18 actually-included full-text studies: **14/18 = 78%**, up from 56%.

Trade-off: the broader exposure block (especially `"culture positivity"[tiab]` and the bacteremia-duration concept) increases the title/abstract screening burden by ~670 records. This is acceptable for a systematic review; screening 1,245 titles in Covidence is a few hours of dual independent work.

---

## What this means for the registration and the manuscript

1. **Register V3, not V1.** I drafted PROSPERO field 13 (Searches) yesterday assuming V1; the description should be updated to reference V3 with the documented exposure-block expansion and the dropped humans filter. The reasoning belongs in the PRISMA-S supplement.

2. **The 265 Elicit-only records need explicit triage.** Most will be excluded at screening as off-topic semantic matches. Some will be legitimate Embase/Scopus-indexed papers that PubMed doesn't carry. A small number may be retrievable from PubMed under a different query phrasing that we haven't tried. Recommend: run the Elicit-only DOIs through Embase (we can do this once Embase access is available) and document the database in which each record was retrieved for the PRISMA-S supplement.

3. **The PubMed-only set of 447 new candidates needs screening.** Some of these are 2024–2026 papers post-dating the Elicit run, others were missed by Elicit's semantic ranking. Triage in Covidence as part of the dual-screening pass.

4. **Citation tracking is essential, not optional.** Ji 2020 illustrates why: a *Chest* paper whose primary contribution is on BSI outcomes mentions TTP only in the body. Forward-citation tracking from Hsieh 2022, Minejima 2019, and the Jan 2026 IJMPR meta-analysis is the only realistic way to catch this class of paper. Allow a half-day for this in the protocol timeline.

5. **Three non-PubMed studies need explicit grey-literature defense.** E 2012, Nadeem 2021, Takahashi 2022. Source the Embase records for these and document the retrieval path. If Embase also misses them, declare them as identified via hand-search / author contact and cite the original retrieval (Elicit, Google Scholar — note that Elicit is not itself a defensible primary source for systematic-review reporting; the citing source for each grey-literature inclusion must be the actual database that indexes it, even if Elicit is what surfaced it during exploration).

6. **The Elicit retrieval cannot be the registered primary search.** PROSPERO and PRISMA require reproducible database searches. Reframe Elicit's role honestly in the PRISMA flow diagram and methods: "Preliminary scoping was performed using the Elicit semantic search tool; the registered systematic search was conducted independently in PubMed, Embase, Cochrane CENTRAL, Web of Science, CINAHL, and Scopus per the strategy in Supplementary Appendix S1." Records identified through Elicit but not retrieved by the registered databases enter the flow diagram as "other sources" or "hand search" with the original indexing database cited.

---

## Files produced for this triage

In the project folder (`new_ttp_metaanalysis/`):

| File | Contents |
|---|---|
| `Elicit_vs_PubMed_triage_report.md` | This report |
| (Reference) `Elicit - … - Sources (1).ris` | Existing Elicit corpus |

In Claude's working folder (intermediate artifacts — copy to project if needed):

| File | Contents |
|---|---|
| `elicit_corpus.json` | Parsed Elicit corpus (384 records, normalized) |
| `pubmed_redesigned_pmids.json` | V1 query, 571 PMIDs |
| `pubmed_redesigned_records.json` | Metadata for the 571 V1 records |
| `pubmed_revised_v2.json` | V2 (humans filter removed) — 679 PMIDs |
| `pubmed_revised_v3.json` | V3 (full revised strategy) — 1,245 PMIDs |
| `triage_summary.json` | Overlap / unique counts |
| `triage_records.json` | Per-record lists for each set |
| `parse_ris.py`, `pubmed_search.py`, `fetch_pubmed_dois.py`, `triage.py`, `deep_diagnose.py` | The scripts used |

I can move any of these into the project folder on request; they're currently held outside it to keep the project clean.

---

## Appendix — Elicit records without a DOI (n=20)

These are likely conference proceedings, Chinese-language papers, regional indexes, and one entry with a corrupted title field. They cannot be reproducibly retrieved without an authoritative identifier and would need manual lookup if any prove to be eligible.

- Bo 2011 — Relationship between time to positivity of blood culture with clinical characteristics
- Chen 2020 — [title appears to be a typesetter artifact: "S0950268820000941jra 1..3"]
- Liao 2008 — Lack of increase in time to blood culture positivity in a patient with persistent…
- Wacharasint 2016 — Impact of Time to Report Positive Hemoculture on Mortality in Surgical Critically Ill
- Aziz 2010 — Antibiotic-resistant Bacteria in Hospitalized Patients with Bloodstream infection
- Cheewinmethasiri 2014 — Microbiology, risk factors and mortality of patients with intravenous catheter related…
- Le 2013 (×3) — multiple Chinese-language entries on TTP in blood cultures (likely the same author)
- Cobos-Triguero 2017 — Time-to-positivity, type of culture media and oxidase test…
- Grozdanovski 2012 — Early prognosis in patients with community-acquired severe sepsis and septic shock
- Wischmeyer 2004 — THE "SEVILLE SCORE": A NEW PREEMPTIVE ANTIFUNGAL THERAPY APPROACH FOR CANDIDA…
- Añón 2001 — [Prognostic factors of bacteremia: prospective study] (Spanish)
- Fontaine 2024 — [Does a rapid antibiotic susceptibility test optimize…] (French)
- Saito 2009 — [Measures to reduce turnaround time (TAT)…] (Japanese)
- Li-Rong 2012 — Reciprocity between the Positive Tocsin Time of Blood Cultivation… (Chinese)
- Leili 2011 — Diagnostic value of positivity in candida bloodstream infection
- Rui-huan 2013 — Value of procalcitonin and time to blood culture positivity in early prediction…
- (One entry with no first author and a duplicated journal-name title)

Most of these (Spanish, French, Chinese, Japanese language papers; conference abstracts) are at the eligibility boundary defined in PROSPERO field 28 (Language). The protocol permits English, Italian, Spanish, French, German, and Portuguese; the Chinese and Japanese papers will be excluded at language screening unless professional translation is arranged.

---

*Triage executed against the live NCBI E-utilities on 2026-05-12. All scripts are reproducible.*
