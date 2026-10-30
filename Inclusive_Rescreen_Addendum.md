# TTP Meta-Analysis — Inclusive Re-Screen Addendum

**Date:** 2026-05-25 · **Workbook:** TTP_MetaAnalysis_Extraction_Complete_v4.xlsx

This addendum documents a **secondary re-screening pass** under more inclusive criteria. The strict primary pool yielded 43 included studies (see PDF_Extraction_Inclusion_Exclusion_Report.md). The 54 papers previously excluded with code `no_assoc` (TTP and outcome both present but no quantitative TTP↔outcome model) were re-screened with relaxed criteria: a paper now qualifies if it reports TTP and a clinical outcome in the same cohort, even if not analyzed together.

---

## Headline

| | Count |
|---|---:|
| Papers re-screened (previously `no_assoc`) | 54 |
| **Flipped to INCLUDE (inclusive-only pool)** | **40** |
| Remained EXCLUDED | 14 |
| New studies extracted into the workbook | 40 |

**Workbook totals:**
- v1 (baseline): 57 studies
- v2 (strict pool): +43 = 100 studies
- v3 (QC corrections): 100 studies (same set, 7 cells corrected)
- **v4 (inclusive pool): +40 = 140 studies**

New rows in v4 are highlighted **orange** to distinguish from the strict-pool rows (yellow). Inclusive-only studies have `[INCLUSIVE_ONLY]` prepended to their `study.notes` so downstream R analysis can filter the primary pool (strict) from a sensitivity-analysis pool (strict + inclusive).

---

## Still-excluded papers (14 of 54)

These remain excluded even under inclusive criteria:

| doc_id | Author | Year | Code | Reason |
|---|---|---:|---|---|
| Andry2022 | Andry | 2022 | `no_ttp` | TTP genuinely not measured (e.g., time-to-antibiotic, time-to-clearance, or transit time only) |
| Fihman2021 | Fihman | 2021 | `no_outcome` | No clinical outcome reported in the cohort (pure methods/diagnostic paper) |
| Giannella2021 | Giannella | 2021 | `wrong_design` | Narrative review, meta-analysis of methods, case series too small, or correspondence |
| Guo2022 | Guo | 2022 | `no_outcome` | No clinical outcome reported in the cohort (pure methods/diagnostic paper) |
| Medina2025 | Diez de Medina | 2025 | `wrong_design` | Narrative review, meta-analysis of methods, case series too small, or correspondence |
| Nieuwkoop2010 | van Nieuwkoop | 2010 | `no_outcome` | No clinical outcome reported in the cohort (pure methods/diagnostic paper) |
| Pardo2014 | Pardo | 2014 | `no_outcome` | No clinical outcome reported in the cohort (pure methods/diagnostic paper) |
| Romann2023 | Romann | 2023 | `ttp_is_outcome_not_exposure` | TTP is the dependent variable (predicted by pre-analytical factors); not interpretable as a prognostic exposure |
| Ruschulte2009 | Ruschulte | 2009 | `no_outcome` | No clinical outcome reported in the cohort (pure methods/diagnostic paper) |
| Sepulveda2020 | Sepulveda | 2020 | `no_outcome` | No clinical outcome reported in the cohort (pure methods/diagnostic paper) |
| Shemanski2019 | Shemanski | 2019 | `no_ttp` | TTP genuinely not measured (e.g., time-to-antibiotic, time-to-clearance, or transit time only) |
| Verroken2019 | Verroken | 2019 | `no_ttp` | TTP genuinely not measured (e.g., time-to-antibiotic, time-to-clearance, or transit time only) |
| Walsh2024 | Walsh | 2024 | `no_outcome` | No clinical outcome reported in the cohort (pure methods/diagnostic paper) |
| Zornitzki2024 | Zornitzki | 2024 | `no_ttp` | TTP genuinely not measured (e.g., time-to-antibiotic, time-to-clearance, or transit time only) |

---

## Flipped to INCLUDE (40 studies)

All studies below are now in `..._v4.xlsx` with the `[INCLUSIVE_ONLY]` tag.

**Sub-categorization** by what data was extractable:

- `population + TTP + descriptive 2x2 (if computable)`: 23 studies
- `population only`: 9 studies
- `population + TTP only`: 6 studies
- `population + TTP`: 2 studies

**Special flags applied:**

- `[CONTAMINATED_TTP]` (9 studies — TTP/DTP used as CRBSI definitional criterion, not a measured prognostic variable): Ahn2023, Ali2026, Cabello2010, Deliberato2012, Eden2022, Raad2009, Sabatier2015, Sibar2026, Sivakumar2020

- `[POTENTIAL_DUPLICATE]` (3 candidates):
  - Wong2016_a/Wong2016_b (same Vancouver cohort, n=255 → n=400 expansion)
  - Chen2015 (likely duplicate of Chen2013, same VGH Taipei cohort)
  - Paiva2016 (EUROBACT sub-analysis — may overlap Tabah2012 EUROBACT)

---

## All newly included studies (with extracted data summary)

| # | study_id | Author | Year | n | Design | TTP summary | Outcome summary | Data class |
|---:|---|---|---:|---:|---|---|---|---|
| 1 | Ahn2023 | Ahn | 2023 | 2189 | retrospective_cohort | DTP >2h used as definitional criterion for CRBSI … | In-hospital mortality 21.3% overall (467/2189); CRBSI vs no… | population only |
| 2 | Ali2026 | Ali | 2026 | 300 | retrospective_cohort | DTP >2h used as one of IDSA definitional criteria… | 108 deaths (36%) among CRBSI cohort; mortality associated w… | population only |
| 3 | Arendrup2011 | Arendrup | 2011 | 314 | prospective_cohort | Median TTP 2 days (range 0-10); species-specific … | 30-day mortality 37% overall; stratified by ICU (47% vs 24%… | population + TTP + descriptiv… |
| 4 | Bolukcu2018 | Bolukcu | 2018 | 251 | case_control | 97.5% of clinically important pathogens detected … | 44 deaths in the BC-positive case group (44/122 = 36%); no … | population + TTP |
| 5 | Bouza2013 | Bouza | 2013 | 243 | case_control | Mean TTP adults GN-CRBSI 10.3+/-7.4h vs other 19.… | Mortality 16/81 (19.8%) in GN-CRBSI; multivariable mortalit… | population + TTP + descriptiv… |
| 6 | Cabello2010 | Sabatier | 2014 | 52 | rct | DTP >=120 min used as binary diagnostic threshold… | In-hospital mortality 27% (7/26) DTP arm vs 19% (5/26) stan… | population only |
| 7 | Chatelard2023 | Chatelard | 2023 | 270 | prospective_cohort | Time from blood sampling to BC positivity reporte… | In-hospital mortality 11.5% overall (31/270); by period 13%… | population + TTP |
| 8 | Chen2013 | Chen | 2013 | 447 | retrospective_cohort | Mean TTP for yeast 61.9+/-21.8h overall; species-… | 30-day crude mortality 48.2% (215/447); by species: C. albi… | population + TTP + descriptiv… |
| 9 | Chen2015 | Chen | 2015 | 434 | retrospective_cohort | Mean TTP 60.6+/-22.2h; dichotomized at 48h cutoff… | 30-day mortality 48.2% (209/434); stratified by TTP categor… | population + TTP + descriptiv… |
| 10 | Davies2023 | Davies | 2023 | 988 | retrospective_cohort | Median TII (time in incubator = TTP equivalent) 1… | 30-day mortality 15.6% (130/834 with mortality data availab… | population + TTP + descriptiv… |
| 11 | Deliberato2012 | Deliberato | 2012 | 53 | retrospective_cohort | Differential time to positivity (DTP) >2h used as… | In-hospital mortality 57% (standard) vs 75% (conservative),… | population only |
| 12 | Doi2023 | Sasaki | 2023 | 49 | retrospective_cohort | Median TTP 21h (IQR 17-31) overall; 22h single-po… | 30-day mortality 13.3% (single) vs 18.2% (multiple); 90-day… | population + TTP + descriptiv… |
| 13 | Eden2022 | Eden | 2022 | 15 | other | TTP measured pre- and post-Seraph filter; median … | Primary endpoint was device safety; all 15 patients survive… | population only |
| 14 | Fernandez2009 | Fernandez | 2009 | 96 | retrospective_cohort | Mean TTP by species: C. albicans 35.3+/-18.1h, C.… | In-hospital mortality 29.2% (28/96); reported by Candida sp… | population + TTP + descriptiv… |
| 15 | Gaifer2022 | Gaifer | 2022 | 147 | retrospective_cohort | Median time to detect Brucella in BC 3 days (IQR … | Chronic brucellosis 7% (9/147) and relapsed infection 10% (… | population + TTP + descriptiv… |
| 16 | GarciaVazquez2013 | Garcia-Vazquez | 2013 | 269 | prospective_cohort | TTP dichotomized <16h vs >=16h; TTP <16h was a mu… | Persistent bacteraemia 37.1% in CSB vs 0.6% in non-CSB (p<0… | population + TTP + descriptiv… |
| 17 | Ghrenassia2019 | Ghrenassia | 2019 | 121 | retrospective_cohort | Median delay to blood culture positivity 3 days (… | Hospital mortality 60%; ICU mortality reported; multivariat… | population + TTP only |
| 18 | Hitzenbichler2017 | Hitzenbichler | 2017 | 252 | retrospective_cohort | Median TTP 14h (likely infection), 16h (possible)… | Overall mortality: 1 attributable death + 8 deaths from oth… | population + TTP + descriptiv… |
| 19 | Hwang2025 | Hwang | 2025 | 11 | retrospective_cohort | Time to culture positivity range 5-27 days (routi… | Overall mortality 91% (10/11); 50% died within 7d, 80% with… | population + TTP + descriptiv… |
| 20 | Kim2021 | Kim | 2021 | 1718 | retrospective_cohort | Median TPP 9.5h overall (aerobic 10.2h, anaerobic… | In-hospital mortality 17.1%; 90-day mortality 32.4% (CNSS 3… | population + TTP + descriptiv… |
| 21 | Kitagawa2025 | Kitagawa | 2025 | 81 | prospective_cohort | Median TTP 9.1h (IQR 8.4-10.5); ddPCR+ 8.8h vs dd… | 28-day mortality 9.9% overall (8/81); 47.1% in septic shock… | population + TTP + descriptiv… |
| 22 | Lockwood2016 | Lockwood | 2016 | 390 | retrospective_cohort | Mean time to culture positivity 22h pre vs 19h po… | In-hospital mortality 9.4% pre vs 4.9% post (p=0.07); 25% v… | population + TTP only |
| 23 | MacVane2016 | MacVane | 2016 | 68 | retrospective_cohort | Median time from blood draw to organism ID 47.7h … | In-hospital mortality 35.6% (CM) vs 26.1% (BCID), ns; 30-da… | population + TTP only |
| 24 | Nakagawa2018 | Nakagawa | 2018 | 64 | retrospective_cohort | Average time to VRE detection from BC collection … | Hospital mortality 34.1% (pre) vs 20.0% (post), ns; hospita… | population + TTP only |
| 25 | Paiva2016 | Paiva | 2016 | 1156 | prospective_cohort | Median TTP fungemia 48.7h (IQR 33-81) vs bacterem… | 28-day all-cause mortality: 40.6% fungemia (39/96), 35.4% b… | population + TTP + descriptiv… |
| 26 | Raad2009 | Raad | 2009 | 188 | retrospective_cohort | Differential TTP <12h used as CRBSI inclusion/def… | Resolution at 48h: 175/188 (93%); 4-month all-cause mortali… | population only |
| 27 | Sabatier2015 | Sabatier | 2015 | 52 | rct | DTP >=120 min used as CR-BSI diagnostic criterion… | In-hospital mortality 27% DTP arm vs 19% standard arm (p=0.… | population only |
| 28 | Seitz2022 | Seitz | 2022 | 60 | prospective_cohort | Mean time-to-positive 4.5h T2MR vs 52.5h BC in co… | 28-day mortality 53.3% (32/60) for whole cohort; invasive v… | population + TTP + descriptiv… |
| 29 | Shepard2022 | Shepard | 2022 | 14 | retrospective_cohort | Mean time to blood culture positivity 12.1 days (… | Endocarditis on echo 6/14 (42.8%); valve replacement 2/14 (… | population + TTP only |
| 30 | Sibar2026 | Sibar | 2026 | 191 | retrospective_cohort | DTP categorical (present in 64.9% of cases per ID… | In-hospital mortality 11%; predictors DM, Charlson, CRP, WB… | population only |
| 31 | Simpson1999 | Simpson | 1999 | 42 | prospective_cohort | Median TTP by BC method: Isolator 39.3h, pour pla… | Mortality 26/42 (61.9%) overall in BC-positive cohort; mort… | population + TTP + descriptiv… |
| 32 | Sivakumar2020 | Jayaweera | 2020 | 1462 | prospective_cohort | DTP used categorically to classify CLABSI vs bact… | Clinical complications: right-sided infective endocarditis … | population only |
| 33 | Steuber2021 | Steuber | 2021 | 252 | retrospective_cohort | Median time-to-detection: T2CP 9h (IQR 6-17) vs B… | In-hospital mortality 32.6% T2CP vs 28.8% BC (p=0.535); 30-… | population + TTP + descriptiv… |
| 34 | TalaIghil2025 | Tala-Ighil | 2025 | 80 | retrospective_cohort | Median TTP 72h (IQR 52.3-90); 38.4h for Mucorales… | Day-90 mortality 53%; Firth multivariable logistic regressi… | population + TTP + descriptiv… |
| 35 | Wong2016_a | Wong | 2016 | 255 | retrospective_cohort | Median TTP 20h (IQR 16.5-24.9) beta-lactam vs 18.… | Crude 28-day mortality 7.06% (n=18); adjusted OR 0.85 (0.27… | population + TTP + descriptiv… |
| 36 | Wong2016_b | Wong | 2016 | 400 | retrospective_cohort | Median TTP 20.2h (16.6-25.5) beta-lactam vs 18.5h… | Crude 28-day mortality 8.5% (n=34); adjusted OR 1.14 (0.49-… | population + TTP + descriptiv… |
| 37 | Xu2026 | Xu | 2026 | 134 | case_control | TTP categorical >=2 days vs <2 days; logistic OR … | 60-day mortality 31.34% (21/67) candidemia vs 3.0% (2/67) n… | population + TTP + descriptiv… |
| 38 | Yanai2018 | Yanai | 2018 | 63 | retrospective_cohort | Median TTP (days): overall 1 (IQR 1-2); bacteremi… | Of 27 bacteremia patients receiving appropriate antimicrobi… | population + TTP only |
| 39 | Zhang2017 | Zhang | 2017 | 248 | retrospective_cohort | Mean TTP (hours): AmpC-EC 8.33+/-2.18 vs non-AmpC… | 30-day all-cause mortality 25% overall (62/248); AmpC-EC 25… | population + TTP + descriptiv… |
| 40 | Zhang2024 | Zhang | 2024 | 94 | retrospective_cohort | Mean TTP (hours) by species: C. albicans 45.16+/-… | In-hospital/28-day mortality 23.4% (22/94); by species C. a… | population + TTP + descriptiv… |

---

## Methodological notes

1. **Inclusion threshold under inclusive criterion:** TTP reported as a summary statistic (median/mean/range/cutpoint) AND a clinical outcome (mortality/persistence/relapse/clearance) reported for the same cohort — even if not cross-tabulated.
2. **Risk of bias on inclusive-only studies skews HIGH.** The lack of a TTP↔outcome model is itself a `rob_stat_analysis = 3` concern. Most of these scored `rob_overall = high`. The primary meta-analysis should use only the 43 strict-pool studies; the inclusive-only set is for: (a) descriptive/demographic synthesis, (b) sensitivity analysis testing whether enriching the pool with low-quality studies changes the pooled estimate.
3. **Contaminated TTP** in CRBSI definitional studies — these papers use DTP > 120 min (or analogous threshold) as part of the case definition, so TTP is not freely measured and cannot be analyzed as a prognostic exposure. Population data (demographics, infection source, etc.) can still be extracted; the TTP cells contain only the definitional cutpoint.
4. **Schema/enum limitations encountered again:** Mycobacterium tuberculosis pathogen (Barr2022, Sossen2026 in strict pool; none in inclusive) gets `pathogen_class = mixed` as forced enum-fit. Endocarditis and septic shock outcomes are mapped to `persistent_bacteremia` and `mortality` respectively with `outcome_definition` clarifying.
5. **Filter recipe for downstream R:** `filter(!str_detect(notes, fixed('[INCLUSIVE_ONLY]')))` to get the strict pool; `filter(!str_detect(notes, fixed('[CONTAMINATED_TTP]')))` to drop CRBSI-definitional TTP contamination.

---

## Final v4 workbook summary

| Tier | Studies | Highlight | Notes |
|---|---:|---|---|
| Baseline (thesis) | 57 | none | Pre-existing, untouched |
| Strict new (primary) | 43 | yellow | Quantitative TTP↔outcome association extracted |
| Inclusive new (secondary) | 40 | orange | `[INCLUSIVE_ONLY]` tag — TTP + outcome both present but no formal model |
| **Total** | **140** | | |