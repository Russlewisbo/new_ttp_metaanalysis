# TTP meta-analysis: project checklist to submission

**Owner:** Russ Lewis
**Updated:** 2026-05-12
**Target journal (primary):** Clinical Microbiology and Infection
**Estimated time to submission:** 10–12 weeks with focused effort

This is a working checklist. Tick boxes as completed; items marked **(blocker)** stop downstream work. Items marked **(can run parallel)** don't.

---

## Phase 0 — Pre-flight (this week)

- [ ] **(blocker)** Recruit a second reviewer for dual screening and dual QUIPS rating. Required for any defensible PROSPERO registration. Options: a fellow at Padova, a colleague from another institution, or a senior infectious diseases trainee. Without this person, every downstream step has a methodological hole.
- [ ] **(blocker)** Decide whether to add a methodologist/statistician as co-author. The Bayesian analysis is sophisticated; a named statistician on the byline reduces reviewer pushback at CMI or CID.
- [ ] Finalize the authorship list (Francesco first, you senior, the second reviewer, statistician if added). Get email confirmations from each co-author that they accept ICMJE authorship criteria. Store the email chain.
- [ ] Confirm no industry funding to declare. Confirm your JAC editorial conflict is the only relevant disclosure.

---

## Phase 1 — Register the protocol (week 1)

- [ ] Update the PROSPERO draft (`PROSPERO_registration_draft.md`) to reference the V3 search strategy from the triage report, not V1. Field 13 (Searches) needs the corrected exposure block. I can do this in 10 minutes if you ask.
- [ ] Add the second reviewer's name and affiliation to field 9.
- [ ] Add the methodologist (if recruited) to field 9.
- [ ] Confirm or revise the start date (field 3) and anticipated completion date (field 4).
- [ ] Read fields 5, 34, 35, 36 (the honest-disclosure paragraphs) one more time. If you want to soften any wording, do it now — but soft-pedalling post-hoc registration is the most common reason PROSPERO rejects or asks for revisions.
- [ ] Submit at https://www.crd.york.ac.uk/prospero/. Save the confirmation email and the assigned registration number (CRD420260XXXXX) into the project folder.
- [ ] Add the PROSPERO number to a banner at the top of `AGENTS.md` so it appears in every future session.

---

## Phase 2 — Reproducible systematic search (weeks 1–2)

- [ ] Translate the V3 PubMed strategy from the triage report into Embase syntax. Run on embase.com, set the date to today, capture the yield count and the date-stamped query history.
- [ ] Translate to Cochrane CENTRAL syntax (Wiley Cochrane Library). Run, archive yield and date.
- [ ] Translate to Web of Science Core Collection (using `?` single-character wildcard and the TS= field). Run, archive yield and date.
- [ ] Translate to CINAHL Complete (EBSCOhost). Run, archive yield and date.
- [ ] Translate to Scopus (Elsevier). Run, archive yield and date.
- [ ] **(can run parallel)** Search ClinicalTrials.gov and WHO ICTRP for "time to positivity" + "blood culture" or "bloodstream infection". Capture any prospective trials that might have completed and reported.
- [ ] **(can run parallel)** Search medRxiv and bioRxiv. Capture preprints; note that PROSPERO permits inclusion of preprints if methods are sufficient.
- [ ] **(can run parallel)** Forward citation tracking in Web of Science and in Scopus from three seed papers: Hsieh 2022 (BMC Infect Dis), the January 2026 IJMPR meta-analysis, and Minejima 2019 (CID).
- [ ] Export all database results in RIS or similar format. Import to Covidence. Deduplicate via Covidence's built-in algorithm and document the dedup yield.
- [ ] Take a screenshot or PDF export of every database search history page. PRISMA-S requires this. Store in a `search_archive/` subfolder.

---

## Phase 3 — Screening (weeks 2–4)

- [ ] Create the Covidence project. Configure eligibility criteria from the PROSPERO field 16–22 wording verbatim.
- [ ] Pilot screening on the first 50 deduplicated records (you + second reviewer, independent). Compare decisions. Calibrate any disagreement before scaling. Document the calibration discussion.
- [ ] Dual independent title/abstract screening on the full corpus. Resolve disagreements by discussion; third-arbiter (you) for unresolved. Calculate Cohen's kappa and record it.
- [ ] Retrieve full text for all included-after-T/A studies. Note: some 2026 papers may not yet have full text — request via author email if needed.
- [ ] Dual independent full-text screening. Resolve as above. Calculate kappa.
- [ ] **(can run parallel with above)** Hand-search reference lists of every included study and every recent narrative review on TTP. Add candidates to Covidence as "other source".
- [ ] **(can run parallel with above)** Email Hsieh, Minejima, Martín-Gutiérrez, and the senior author of the IJMPR 2026 paper for unpublished or in-press TTP work. Two reminders at 2-week intervals.
- [ ] Build the PRISMA 2020 flow diagram in Covidence. Lock the included corpus list. Compare against the current 18-study + 57-row database — additions and removals need explicit per-study reasoning that goes into the supplement.

---

## Phase 4 — Data extraction and reconciliation (weeks 4–5)

- [ ] **(blocker)** Resolve the Ok2013 directional contradiction documented in `Clinical_Failure_Assessment.md` (OR=0.27 from 2×2 vs OR=14.57 reported). Pull the original PDF, re-extract the 2×2 table independently, identify which group is "short TTP". Fix and document in an audit log.
- [ ] **(blocker)** Exclude Melling 2019 from the bacteremia analysis. The sputum-culture data isn't a bacteremia outcome and should not pool. Document the exclusion decision in the supplement with the quoted source text.
- [ ] Re-extract any studies added during Phase 2–3 screening using the existing `TTP_MetaAnalysis_Extraction_Complete.xlsx` template.
- [ ] Pilot dual extraction on 20% of all included studies (you + second reviewer). If >10% field-level disagreement, escalate to full dual extraction.
- [ ] Email primary-study authors for missing 2×2 cell counts, cutpoint definitions, and denominators. Up to two reminders.
- [ ] Lock the extraction database. Save a version-tagged copy (`TTP_extraction_locked_YYYYMMDD.xlsx`).

---

## Phase 5 — Risk of bias and certainty of evidence (weeks 5–6)

- [ ] Dual independent QUIPS rating across all included studies (six domains: participation, attrition, prognostic factor measurement, outcome measurement, confounding, statistical analysis). Use the original Hayden et al. 2013 rubric or the Cochrane Prognosis Methods Group template.
- [ ] Resolve QUIPS disagreements; calculate kappa on overall judgement.
- [ ] Tabulate domain-level and overall ROB ratings into `tbl_study` (replace the current `rob_overall = NA` entries).
- [ ] Apply the GRADE prognostic factor framework (Huguet et al. 2013) to assess certainty of evidence for each primary outcome. Output: a GRADE Summary of Findings table for the manuscript.

---

## Phase 6 — Re-run the locked analysis (weeks 6–7)

- [ ] Re-run the Bayesian primary mortality model on the locked corpus. Confirm the cutpoint moderation finding holds with the updated study list.
- [ ] Re-run the persistent-bacteremia model on the locked corpus (after Melling exclusion, after Ok2013 fix).
- [ ] Add prediction intervals alongside credible intervals for every pooled estimate. Top journals expect this for high-heterogeneity meta-analyses.
- [ ] Run leave-one-out cross-validation via the `loo` package; report `elpd_diff` table for the primary model and for two alternative prior specifications. This is the prior-sensitivity rigor reviewers will look for.
- [ ] Run power-scaling prior sensitivity via the `priorsense` package on the locked primary model.
- [ ] Re-run all four publication-bias methods: funnel plot, Egger, trim-and-fill, frequentist step-function, Bayesian selection (uniform and skeptical priors). Confirm the AGENTS.md narrative (frequentist step-function overadjusts because of the 91% significance rate; Bayesian models robust) survives the locked corpus.
- [ ] Re-run all seven moderator meta-regressions. Confirm TTP cutpoint remains the dominant moderator.
- [ ] **(blocker)** Consolidate the two existing reports into one canonical Quarto file. The 33-study version is primary; the 20-study version either becomes a sensitivity analysis or gets retired. Currently `TTP_MetaAnalysis_Report.qmd` and `TTP_Meta_Analysis_Report.qmd` both exist — pick one filename and delete the other (after confirming I'm reading both correctly).
- [ ] Complete the canonical Quarto report past line 340. Sections still missing: full primary pooled estimates, forest plots (mortality and persistent bacteremia, with subgroups), publication bias narrative integrating all five methods, sensitivity analyses, meta-regression results table, discussion and clinical implications, limitations, conclusions.
- [ ] Render the final report to HTML and PDF. Visual inspection of every figure and table.

---

## Phase 7 — Reproducibility deposit (week 7)

- [ ] Create an OSF project at osf.io. Upload: the analysis Quarto file, the locked extraction database (de-identified — no patient-level data), all fitted Bayesian model objects (`report_data.rds`), the V3 search strategies for all six databases, the PRISMA flow data, the QUIPS rating spreadsheet, the GRADE Summary of Findings table.
- [ ] Mint a DOI for the OSF project. Add the DOI to the PROSPERO record (it accepts updates).
- [ ] Add a README to the OSF deposit with a one-paragraph reproducibility note and the R package versions used.

---

## Phase 8 — Manuscript drafting (weeks 7–9)

- [ ] Translate Francesco's thesis sections that will carry over (background, some discussion text) from Italian to publication-quality English. Consider professional editing if any author isn't a native English speaker.
- [ ] Draft the structured abstract per CMI's specs (Background, Objectives, Sources, Content, Implications — note CMI uses unique structured headings for narrative/systematic reviews).
- [ ] Draft the Introduction: clinical relevance of TTP, prior work, gap, objectives. Be specific about how this differs from Hsieh 2022 and the IJMPR 2026 review — the four differentiators identified in our first exchange (Bayesian framework, largest k, cutpoint moderation, multiple publication-bias methods).
- [ ] Draft the Methods. Use PROSPERO field text as the spine. Add the protocol-deviation paragraph honestly disclosing the dissertation-then-registered-review timeline.
- [ ] Draft the Results: PRISMA flow, study characteristics table, primary mortality result, subgroup and meta-regression results emphasizing the cutpoint finding, persistent bacteremia result, publication bias section, sensitivity analyses, GRADE certainty.
- [ ] Draft the Discussion. Lead with the cutpoint finding as the clinically novel contribution. Address the IJMPR 2026 review head-on. Address Hsieh 2022 head-on. Discuss limitations (the dissertation-origin timeline, the persistent-bacteremia k=9, the lack of individual patient data, the heterogeneous outcome definitions).
- [ ] Draft Conclusions: short, three-to-four sentences, specific to what the data support (avoid overreach into intervention claims).
- [ ] Finalize all tables: study characteristics, primary results, subgroup and meta-regression, publication bias, GRADE Summary of Findings, sensitivity. Use `gt` or `flextable` for journal-quality formatting.
- [ ] Finalize all figures: PRISMA flow, forest plots (primary, by pathogen class, by cutpoint), funnel plot with selection-model overlay, dose-response curve for cutpoint moderation, leave-one-out plot. 300 dpi PNG and vector PDF/SVG.
- [ ] Write the PRISMA 2020 checklist (supplement S1).
- [ ] Write the PRISMA-S search-reporting checklist (supplement S2).
- [ ] Write the full search strategies, line-numbered, for all six databases (supplement S3).
- [ ] Compile the QUIPS rating supplement (S4).
- [ ] Compile the GRADE evidence profile supplement (S5).
- [ ] Compile the prior-sensitivity and LOO supplement (S6).

---

## Phase 9 — Internal review and submission (weeks 9–10)

- [ ] Circulate the full manuscript and supplements to all co-authors for review. Two-week turnaround. Track all comments centrally.
- [ ] Consider sending a near-final version to one external "friendly review" colleague (e.g., a senior ID epidemiologist not on the byline) for a methodologically critical read.
- [ ] Revise based on internal and friendly-review comments.
- [ ] Draft the cover letter. Frame the contribution: Bayesian methodology, cutpoint moderation as the novel clinical finding, larger study count than prior reviews. Disclose the IJMPR 2026 paper and explain why your contribution differs. Acknowledge the JAC conflict and confirm JAC is not the target.
- [ ] Confirm journal-specific formatting (CMI house style: structured abstract format, reference style — they use Vancouver, double-spaced submission, etc.).
- [ ] Fill in CRediT contribution statements for each author.
- [ ] Final co-author sign-off email chain confirming everyone has seen and approves the submission.
- [ ] Submit via the CMI editorial system. Save the submission confirmation, manuscript number, and date.

---

## Parallel ongoing — admin and version control

- [ ] **(can run parallel throughout)** Keep a chronological audit log in the project folder (`audit_log.md`) of every decision that deviates from the PROSPERO protocol. PRISMA 2020 item 24 requires this disclosure.
- [ ] **(can run parallel throughout)** Tag the git repo at major milestones (`protocol-locked`, `screening-complete`, `extraction-locked`, `analysis-locked`, `submission-v1`).
- [ ] **(can run parallel throughout)** Update `AGENTS.md` at the end of each phase so future sessions resume with current state.

---

## Things I can do for you right now

- Update `PROSPERO_registration_draft.md` field 13 to reference the V3 search (10 minutes)
- Translate the V3 PubMed strategy into Embase, Cochrane, WoS, CINAHL, and Scopus syntax (30 minutes)
- Reconcile the two existing reports (`TTP_MetaAnalysis_Report.qmd` vs `TTP_Meta_Analysis_Report.qmd`) and propose which to retire (1 hour)
- Draft the QUIPS rating sheet template pre-loaded with the six domains and rating rubric so you and the second reviewer can start as soon as inclusion is locked (30 minutes)
- Draft a Covidence eligibility-criteria card derived from the PROSPERO fields so it's ready to paste in (15 minutes)
- Draft the OSF README and project description (15 minutes)
- Draft the cover letter to CMI in advance, ready to refine after the data lock (30 minutes)

Pick whichever closes the most ground next.
