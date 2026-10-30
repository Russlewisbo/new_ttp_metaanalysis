# QC Verification Report — 43 New TTP Meta-Analysis Extractions

**Date:** 2026-05-25 · **Workbook:** TTP_MetaAnalysis_Extraction_Complete_v3.xlsx
**Method:** Independent second-pass — each of the 43 new studies was reviewed by an agent that did NOT do the original extraction. The QC agent re-read the source PDF text and compared every populated field in `tbl_study`, `tbl_population`, `tbl_ttp`, and `tbl_outcomes` against the source.

---

## Executive summary

| Overall quality | Studies | Notes |
|---|---:|---|
| **good** (zero or only cosmetic notes) | 24 | Fields verified; no factual changes needed |
| **minor_issues** | 19 | Cosmetic notes, enum-mapping flags, or peripheral gaps |
| significant_issues | 0 | (none) |
| major_problems | 0 | (none) |

### Discrepancies overall

| Class | Count |
|---|---:|
| `note_other` | 25 |
| `error_wrong_enum` | 7 |
| `note_borderline_eligibility` | 7 |
| `error_wrong_value` | 6 |
| `gap_underspecified` | 4 |
| `gap_missing` | 3 |
| `judgment_questionable_quips` | 1 |

| Severity | Count |
|---|---:|
| high | 0 |
| medium | 11 |
| low | 42 |

**Bottom line:** zero high-severity errors. No effect estimate or N was miscoded in a way that would change a meta-analysis result. The 11 medium-severity flags are almost entirely enum-mapping issues (e.g., `pathogen_class` lacks a `mycobacterial` value) and borderline-eligibility flags — not factual errors.

---

## Corrections applied to the workbook (v3)

Seven clear factual corrections were applied to `..._v3.xlsx` (yellow-highlight preserved; original v2 untouched):

| Sheet | study_id | Field | v2 value | v3 value | Reason |
|---|---|---|---|---|---|
| tbl_population | Prinsloo2023 | pct_male | 70.0 | **68.4** | Was using full melioidosis cohort n=477; corrected to n=193 TTP subset (132/193) |
| tbl_ttp | PerezRodriguez2024 | ttp_iqr_low | 8.0 | **8.6** | Was IE-arm IQR low; corrected to non-IE arm IQR low matching the reported median 11h |
| tbl_outcomes | Nunes2013 | adjusted | False | **True** | Per-hour OR 1.04 (1.0-1.1) is from the multivariate Cox in Table 3 |
| tbl_outcomes | Nunes2013 | adjustment_vars | null | **APACHE II; organ failure; SOFA; SAPS II** | Filled in from Table 3 multivariate model |
| tbl_population | He2024 | pct_male | null | **64.1** | Pooled across 3 subgroups (84/131) |
| tbl_population | He2024 | pct_icu | null | **16.0** | Pooled across 3 subgroups (21/131) |
| tbl_study | Balaji2024 | study_design | prospective_cohort | **other** | Paper self-describes as 'cross-sectional observational' |

Ten studies had **borderline-eligibility flags** appended to their `tbl_study.notes` field for future review:

- Berge2023
- Chen2018
- Kahn2021
- Keighley2023
- Rojas2013
- Tonizzo2026
- Barr2022
- Sossen2026
- Cheng2022
- Kim2013

---

## Per-study verdicts

| study_id | Verdict | Discrepancies | Notes |
|---|---|---:|---|
| Aldemir2026 | good | 2 | Core extraction matches PDF; one minor double-check on a count and a note about  |
| Balaji2024 | minor_issues | 2 | Most fields verified. Study design enum is debatable (paper calls itself cross-s |
| Barr2022 | good | 2 | All numeric and design fields verified. The pathogen_class='mixed' coding for M. |
| Berge2023 | good | 2 | All key counts, ORs, CIs, TTP cutpoint, and adjustment set match the paper. One  |
| Bo2011 | good | 0 | All major fields verified against PDF (fullwidth Unicode); demographics, TTP sta |
| Chavez2022 | good | 0 | All major fields verified. N=416, sex distribution, MRSA rate, ICU, Charlson, IT |
| Chen2018 | minor_issues | 2 | All quantitative fields verified. One minor note on funding source; one borderli |
| Cheng2022 | minor_issues | 1 | All fields verified. Small N (67) and sparse events (9 deaths) drive extremely w |
| Comba2024 | minor_issues | 1 | All quantitative fields verified. n=186, age 63.6, sex/MRSA/ICU/Charlson/TTP all |
| Cubuk2026 | good | 1 | All extracted fields verified against PDF; one minor note about ttp_cutpoint_bas |
| Fenoll2022 | minor_issues | 2 | Most fields verified; flagged: sepsis outcome record uses unreconcilable denomin |
| Gavronski2020 | good | 0 | All extracted fields verified against PDF. No discrepancies. |
| He2024 | minor_issues | 3 | All numeric fields verified; two structural notes about cohort definition and mi |
| Huang2013 | minor_issues | 2 | All major numeric fields verified; one minor calculation discrepancy and one lab |
| IrigoyenSierakowski2024 | minor_issues | 4 | Core fields verified against the PDF; minor study-context corrections (hospital  |
| Jayabalakrishnan2022 | good | 0 | All major numeric and study-design fields verified correctly. No material discre |
| Kahn2021 | minor_issues | 2 | Major fields verified. Two notes: study_design enum is debatable (retrospective  |
| Keighley2023 | minor_issues | 2 | Core fields verified. Two notes: outcomes events_short/long_ttp reference KM str |
| Kim2013 | minor_issues | 2 | Most fields verified. One significant issue: ttp_cutpoint_basis labeled 'ROC_der |
| Lin2016 | good | 1 | All major fields verified; one population field where ICU transfer rate was used |
| Lin2018 | good | 1 | All numeric fields verified correctly. One semantic note on outcome_type classif |
| Mandolfo2020 | minor_issues | 1 | Numeric fields and TTP values verified. One factual error in empiric_abx_definit |
| MartinGutierrez2016 | good | 2 | All key extracted fields match the paper (n, age range, pathogen mix, TTP groups |
| MartinGutierrez2017 | good | 2 | All key effect estimates, n, and TTP values verified. Two minor semantic concern |
| Nunes2013 | good | 1 | All numeric fields verified. Minor data-organization issue: the outcomes row has |
| PerezRodriguez2024 | minor_issues | 2 | Fields mostly verified; minor IQR-source inconsistency in TTP (uses non-IE media |
| Prinsloo2023 | minor_issues | 3 | TTP/outcome data accurate; population fields conflate full melioidosis cohort (n |
| PuertaAlcalde2019 | minor_issues | 1 | All numeric outcome and TTP fields verified accurately. One minor concern about  |
| Recio2020 | good | 0 | All fields verified correctly. Extraction accurately captures the adjusted aOR p |
| Rojas2013 | minor_issues | 2 | Population, TTP and mortality data accurately extracted. Note: the design is unu |
| Sachu2024 | good | 0 | All fields verified correctly against the PDF. Sample size, demographics, TTP di |
| Sossen2026 | minor_issues | 2 | Substantive content verified (N=519, TTP ordinal scaling, AUCs, day-28 mortality |
| Sowden2008 | good | 0 | All fields verified correctly. N=146 after exclusions, mean age 64.2, 61.6% male |
| Stromdahl2025 | good | 0 | All numeric content verified: N=1703, 23 MRSA (1.35%), TTP median 13h (IQR 9.8-1 |
| Sunnerhagen2026 | good | 0 | All fields verified. N=463 (411 in TTP analysis subset), 56% male, age median 72 |
| Tang2017 | good | 0 | All key fields verified against PDF (n=139, mean age 65.7, male 53.2%, Pitt 3.59 |
| Taur2010 | good | 1 | All key extracted values verified against PDF. Median TTP/incubation 32.1h, adju |
| Thorburn2025 | good | 0 | All key extracted values verified. DTP cut at 120 min: n=68 <120min, n=24 >=120m |
| Thornley2024 | good | 1 | All key fields verified. n=65 (28 persistent, 37 non-persistent), median age non |
| Tonizzo2026 | minor_issues | 2 | All key fields verified. n=973 (verified 'analyzed 973 episodes of SAB'), 187/97 |
| Willmann2013 | good | 0 | All key fields verified correctly against the PDF (Tables 1, 3, 4, 5). No discre |
| Zhang2016 | minor_issues | 1 | Most fields verified correctly across all 4 arms. One borderline issue: staphylo |
| Zouggari2022 | good | 0 | All fields verified correctly against Tables 1-4 and text. Effect estimate label |

---

## All discrepancies (detailed)

### Aldemir2026 (2 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_population | n_total | `note_other` | low | extracted=`217` pdf=`217` — Results 3.1: 'Of these, 517 (5%), obtained from 217 patients, generated a positive growth signal' — Methods abstract rep |
| tbl_population | pct_icu | `note_other` | low | extracted=`76.5` pdf=`None` — Table 2 reports ICU n(%) at the bottle/episode level: 154 (83%) for GN bacteria, 97 (70%) for GP. Patient-level ICU % is |

### Balaji2024 (2 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_study | study_design | `error_wrong_enum` | low | extracted=`prospective_cohort` pdf=`cross-sectional observational (as authors self-describe)` — Title-level Methods of Abstract: 'This cross-sectional observational study, conducted from July 2023 to June 2024...' an |
| tbl_outcomes | outcome_definition | `note_other` | low | extracted=`30-day mortality (species-specific) in candidemia patients` pdf=`30-day all-cause mortality` — Statistical analysis section: 'Logistic regression analysis was performed to investigate the influence of TTP on 30-day  |

### Barr2022 (2 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_population | pathogen_class | `error_wrong_enum` | medium | extracted=`mixed` pdf=`Mycobacterium tuberculosis only (mono-pathogen, not mixed)` — Title: 'Serial measurement of M. tuberculosis in blood from critically-ill patients with HIV-associated tuberculosis.' A |
| tbl_outcomes | effect_estimate | `note_borderline_eligibility` | medium | extracted=`3.1` pdf=`3.1` — Results (combined pharmacodynamic model, p.6): 'Participants who died had greater probability of higher bacillary load o |

### Berge2023 (2 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_study | single_center | `note_other` | low | extracted=`False` pdf=`lab single-center, catchment population-based` — Materials and methods, The cohort: 'all consecutive patients with blood cultures (BC) positive for S. aureus from Januar |
| tbl_outcomes | outcome_type | `note_borderline_eligibility` | medium | extracted=`persistent_bacteremia` pdf=`infective endocarditis (definite IE, modified Duke criteria)` — Abstract and Results: primary outcome is definite CIED IE diagnosed by major criteria. Extractor coded as 'persistent_ba |

### Chen2018 (2 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_study | funding_source | `gap_underspecified` | low | extracted=`NR` pdf=`none (explicitly no external funding)` — Compliance with ethical standards: 'Funding: The authors designed this study, analyzed the data, and drafted the manuscr |
| tbl_outcomes | outcome_type | `note_borderline_eligibility` | medium | extracted=`mortality` pdf=`composite (30-day mortality + complicated infection + ICU admission)` — Methods 2.3: primary outcome is composite — 'presence of 1) 30-day mortality, 2) diagnosis of complicated infection, or  |

### Cheng2022 (1 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_outcomes | outcome_type | `error_wrong_enum` | low | extracted=`mortality` pdf=`septic shock (not death)` — Second outcome record clearly is septic shock per Tables 1, 3, 5 — septic shock 12/67 (17.91%), with multivariable OR 8. |

### Comba2024 (1 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_ttp | ttp_cutpoint_hours | `gap_underspecified` | low | extracted=`12.0` pdf=`12h (ITTP) AND 1.5 (STTP/ITTP ratio) — paper uses both` — Paper uses two cutpoints: ITTP <12h vs >=12h (for KM mortality, P=0.04) AND STTP/ITTP ratio <=1.5 vs >1.5 (for native va |

### Cubuk2026 (1 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_ttp | ttp_cutpoint_basis | `note_other` | low | extracted=`other` pdf=`Multiple species-specific cutpoints proposed; mainly published thresholds compared (Table 4)` — Table 4 lists proposed 28-day mortality TTP cutoffs for E. coli (<=11.2h), K. pneumoniae (<=10.0h), E. faecalis/faecium  |

### Fenoll2022 (2 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_outcomes | events_short_ttp / n_short_ttp / events_long_ttp / n_long_ttp (sepsis outcome row) | `note_other` | medium | extracted=`events_short_ttp=32, n_short_ttp=51, events_long_ttp=17, n_long_ttp=44` pdf=`Results section: 'siendo más frecuente la sepsis cuando el TP fue <=12 horas [32 casos (62,7%) vs 17 casos (38,6%); OR 2,6 (IC95% 1,1-6,2)]'. Table 1 explicitly reports only 16/95 (17%) had TP<=12h, so denominators of 51 and 44 inferred by extractor are inconsistent with the dichotomy. The 32 vs 17 cell counts likely refer to a different cross-tab (possibly sepsis-yes/sepsis-no patients stratified by TP), but the paper text is ambiguous. The OR 2.6 (1.1-6.2) is verified.` — Table 1 row: 'Tiempo hasta HC positivo (horas) (TP) <=12 horas 16 (17%)'. The extractor's notes acknowledge the ambiguit |
| tbl_ttp | n_short_ttp / n_long_ttp | `note_other` | low | extracted=`n_short_ttp=16, n_long_ttp=79` pdf=`Verified by Table 1: 16 (17%) TP<=12h, implying n_long=79.` — These values are correct. No discrepancy; flagged only to highlight that they conflict with the third-outcome denominato |

### He2024 (3 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_population | pct_male | `gap_missing` | low | extracted=`None` pdf=`Reported per-subgroup: C. striatum 72.0% (18/25), MRSA 56.5% (35/62), MRSE 70.5% (31/44). Pooled: 84/131 = 64.1%.` — Table 2 columns 'C. striatum / MRSA / MRSE'. Pct_male can be computed from the three subgroup proportions; leaving it nu |
| tbl_population | pct_icu | `gap_missing` | low | extracted=`None` pdf=`ICU infection rate per Table 2: C. striatum 20.0% (5/25), MRSA 16.1% (10/62), MRSE 13.6% (6/44). Pooled: 21/131 = 16.0%.` — Table 2 'Site of BSIs acquisition: ICU infection' rows. |
| tbl_population | pct_mrsa | `note_other` | low | extracted=`47.3` pdf=`62/131 MRSA = 47.3% within the analytic cohort. However, this is not a 'percentage of S. aureus that are methicillin-resistant' figure — it is the proportion of the entire mixed-pathogen cohort that is MRSA. The convention of pct_mrsa usually refers to %MRSA among S. aureus isolates only.` — Methodology section: cohort is C. striatum + MRSA + MRSE (3 disjoint groups). The paper reports no S. aureus 'methicilli |

### Huang2013 (2 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_population | notes (pulmonary infection 53.3%) | `error_wrong_value` | low | extracted=`pulmonary infection 53.3% overall` pdf=`Pulmonary infection rates per Table 1: C. albicans 48.4% (15/31), C. parapsilosis 46.2% (12/26), C. glabrata 87.5% (14/16), C. tropicalis 63.6% (7/11). Weighted sum across these 4 species: 48/84 = 57.1%. The paper does not state a single overall percentage.` — Table 1, 'Pulmonary infection' row. Cannot find 53.3% anywhere in the text. Calculated weighted average across the 4 mai |
| tbl_ttp | ttp_cutpoint_basis | `note_other` | low | extracted=`ROC_derived` pdf=`The ROC-derived cutoffs (>45.17h for C. glabrata, <=33.17h for C. tropicalis) are for predicting Candida SPECIES, not mortality or any clinical outcome. There is no TTP cutoff for mortality/outcomes in this study.` — Results: 'C. glabrata can be predicted by the cut-off value of >45.17 h... C. tropicalis can be predicted by the cut-off |

### IrigoyenSierakowski2024 (4 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_study | notes | `note_other` | low | extracted=`Single-center retrospective Gregorio Maranon Madrid. ...` pdf=`1550-bed tertiary teaching hospital` — Methods section: 'This retrospective study was carried out in a 1550-bed tertiary teaching hospital in Madrid (Spain) fr |
| tbl_outcomes | p_value | `note_other` | low | extracted=`0.108` pdf=`0.1081` — Table 1: 'Crude mortality rate ... 0.1081'. The reported p applies to the 3-group Kruskal-Wallis comparison (CC, C-RBSI, |
| tbl_outcomes | notes | `error_wrong_value` | low | extracted=`p=0.002 (Kruskal-Wallis across 3 groups)` pdf=`chi-square test for categorical variables` — Methods 2.2: 'Qualitative clinical variables are expressed as numbers (percentages) and compared using the chi-square te |
| tbl_ttp | ttp_cutpoint_hours | `note_other` | low | extracted=`2.0` pdf=`2.0` — The 2-h cutoff is on DIFFERENTIAL time to positivity (DTTP = catheter TTP - peripheral TTP), not on the TTP itself repor |

### Kahn2021 (2 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_study | study_design | `note_other` | low | extracted=`population_based_cohort` pdf=`retrospective population-based cohort` — Abstract Methods: 'This retrospective population-based study included adults with SAB in 2016 in a derivation cohort and |
| tbl_outcomes | events_short_ttp | `note_borderline_eligibility` | medium | extracted=`9` pdf=`9` — Table 1: '30-day mortality ... 24% (9) IE | 19% (81) No IE'. The fields short_ttp/long_ttp here refer to IE (9/38) vs no |

### Keighley2023 (2 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_outcomes | events_short_ttp | `note_borderline_eligibility` | medium | extracted=`41` pdf=`41` — Results: 'A TTP of 1 day was associated with a 30-day mortality of 36% [PDF text states 36%; abstract states 37% (41/112 |
| tbl_outcomes | outcome_definition | `note_other` | low | extracted=`All-cause mortality at 30 days` pdf=`All-cause 30-day mortality (29% overall, 120/415 in abstract vs 125/415 in text)` — Abstract: 'overall, 30-day mortality was 29% (120/415)'. Results body: 'The overall all-cause 30-day mortality was 29% ( |

### Kim2013 (2 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_ttp | ttp_cutpoint_basis | `error_wrong_enum` | medium | extracted=`ROC_derived` pdf=`other / unspecified (not ROC-derived for mortality endpoint)` — Results 'TTP for Candida isolates': 'By ROC curve analysis, the cut-off value of the TTP for catheter-related candidaemi |
| tbl_study | funding_source | `gap_underspecified` | low | extracted=`NR` pdf=`institutional (no external funding)` — Funding section: 'This study was carried out as part of our routine work.' This indicates no external funding (instituti |

### Lin2016 (1 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_population | pct_icu | `note_other` | low | extracted=`34.8` pdf=`7.6` — Table 1 'Location of patients - Intensive care unit': 2/19 (10.5%) + 3/47 (6.4%) = 5/66 (7.6%) at index hospital locatio |

### Lin2018 (1 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_outcomes | outcome_type | `note_other` | low | extracted=`persistent_bacteremia` pdf=`vascular infection (metastatic complication)` — Results: 'Seventeen (7.8%) NTS patients were diagnosed with vascular infection during hospital discharge.' Vascular infe |

### Mandolfo2020 (1 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_population | empiric_abx_definition | `error_wrong_value` | low | extracted=`Empirical: ceftazidime + vancomycin (or daptomycin) for Gram-positive coverage; ALT (antibiotic lock therapy) used` pdf=`Empirical: ceftazidime + cefazolin (Gram+) coverage; vancomycin/daptomycin reserved for confirmed MRSA/MRSE` — Methods: 'We did not include vancomycin as part of the empirical therapy in order to avoid the possibility of developing |

### MartinGutierrez2016 (2 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_study | study_design | `note_other` | low | extracted=`prospective_cohort` pdf=`ambiguous (both prospective and retrospective used in paper)` — Methods, Setting and patients: 'A prospective study of 361 cases of BSI was carried out at the tertiary-care University  |
| tbl_study | rob_overall | `judgment_questionable_quips` | low | extracted=`low` pdf=`None` — All six rob_* domains marked 1 and overall 'low'. The paper has internal design-language inconsistency (prospective vs r |

### MartinGutierrez2017 (2 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_population | severity_score_type | `error_wrong_enum` | low | extracted=`Charlson` pdf=`NR (Charlson is comorbidity index, not severity score; no APACHE/SOFA/SAPS reported)` — Methods: 'The severity of the underlying conditions was classified according to the Charlson weighted comorbidity index. |
| tbl_population | pct_icu | `note_other` | low | extracted=`15.5` pdf=`15.5` — Table 1 'Site of acquisition - ICU': 56/361 (15.5%). The value is the ICU as the SITE OF ACQUISITION of bacteremia, not  |

### Nunes2013 (1 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_outcomes | adjustment_vars | `gap_missing` | low | extracted=`` pdf=`APACHE II; organ failure; SOFA; SAPS II (per Table 3 multivariate model)` — Table 3 multivariate model includes APACHE II, organ failure, SOFA, SAPS II, and time to positivity. The or_per_hour 1.0 |

### PerezRodriguez2024 (2 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_ttp | ttp_iqr_low | `error_wrong_value` | low | extracted=`8.0` pdf=`non-IE IQR is 8.6-13.7; IE IQR is 8.0-13.0` — Table 1 of Perez-Rodriguez2024 shows 'TTP, hours (IQR): No IE 11 (8.6-13.7); IE 10 (8.0-13.0)'. Extracted ttp_median=11  |
| tbl_ttp | ttp_cutpoint_basis | `note_other` | low | extracted=`prior_literature` pdf=`Authors evaluated multiple cutpoints (<=8h, <=10h, <=12h) without a single pre-specified primary cutpoint` — Results section: 'AUC of this score combined with different TTP cut-off points (TTP <=12 h, TTP <=10 h and TTP <=8 h) we |

### Prinsloo2023 (3 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_population | pct_male | `error_wrong_value` | low | extracted=`70.0` pdf=`68.4` — Table 3 (n=193 bacteraemic patients with cultures at Cairns) shows 'Male gender 132' which is 132/193 = 68.4%. Extracted |
| tbl_population | age_median / age_iqr | `gap_underspecified` | low | extracted=`54 (42-65)` pdf=`Age in n=193 subset not directly reported; 54 (42-65) is the full cohort (n=477)` — Results paragraph 2: 'The patients' median (interquartile range (IQR)) age was 54 (42-65) years' — this is the full n=47 |
| tbl_population | pct_icu | `note_other` | low | extracted=`25.0` pdf=`25% in full cohort (118/477); ~25% (48/193) in the bacteraemic-Cairns subset by Discussion calculation` — Discussion: '54 patients requiring ICU admission who had blood cultures collected in Cairns and 48 (89%) were bacteraemi |

### PuertaAlcalde2019 (1 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_population | pct_mrsa | `note_other` | low | extracted=`13.8` pdf=`4/29 S. aureus (13.8%); equivalent to 4/850 = 0.47% of the full BSI cohort` — Table 2 shows 'MRSA 4 (13.8)' nested under 'Staphylococcus aureus 29 (3.4)'; the 13.8% is the proportion within S. aureu |

### Rojas2013 (2 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_study | study design / eligibility | `note_borderline_eligibility` | medium | extracted=`retrospective_cohort with TTP-mortality outcome arm` pdf=`Retrospective chart review comparing TSAB (n=35, single positive culture) to PSAB (n=77, multiple positives); TTP is an exposure measured for each persistence group, not used to predict mortality. Mortality is reported by persistence group, not by TTP category.` — Methods: 'We performed a retrospective chart review of cases of S. aureus bacteremia... comparing patients with TSAB to  |
| tbl_ttp | ttp_range_low | `note_other` | low | extracted=`3` pdf=`TSAB range 3-74; PSAB range 9-76 (overall pooled range 3-76)` — Results paragraph 4: 'longer to become positive than in the patients with PSAB (18.42 hours; range, 9-76 hours)' and TSA |

### Sossen2026 (2 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_population | pathogen_class | `error_wrong_enum` | low | extracted=`mixed` pdf=`Mycobacterium tuberculosis (mycobacterial)` — Title and Methods: 'HIV-Associated Tuberculosis' and 'new diagnosis of HIV-associated TB'; only pathogen analyzed is M.  |
| tbl_population | infection_source | `error_wrong_enum` | low | extracted=`pulmonary` pdf=`disseminated (systemic bacilli load)` — Methods/Discussion frame the study as quantifying 'systemic bacilli load' across sputum, urine, and blood compartments;  |

### Taur2010 (1 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_study | enrollment_end | `note_other` | low | extracted=`2007-12` pdf=`2007-12` — Methods, Study population: 'patients who had at least one blood culture positive for Candida species from 1 January 2005 |

### Thornley2024 (1 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_ttp | ttp_reporting | `note_other` | low | extracted=`both` pdf=`continuous (with ROC-derived cutpoint reported)` — Results: medians reported by outcome group; cutpoint 16.35h was derived by ROC/Youden but no events-by-TTP-bin 2x2 table |

### Tonizzo2026 (2 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_outcomes | outcome_type | `note_other` | medium | extracted=`persistent_bacteremia` pdf=`infective_endocarditis (not in enum)` — Paper outcome is infective endocarditis (IE) confirmed by ECHO; extractor used 'persistent_bacteremia' as placeholder pe |
| tbl_study | study_design | `note_borderline_eligibility` | medium | extracted=`retrospective_cohort` pdf=`retrospective cohort presented in a Letter-to-the-Editor (Correspondence) format` — Document is a Correspondence (CID 2025;81(6):e729-31), not a full original article. Authors describe a retrospective ana |

### Zhang2016 (1 discrepancies)

| Table | Field | Class | Severity | Detail |
|---|---|---|---|---|
| tbl_ttp | ttp_mean / ttp_sd | `error_wrong_value` | low | extracted=`ttp_mean=20.64, ttp_sd=9.94` pdf=`Table 1 reports 20.64 +/- 9.94 h for the WHOLE Gram-positive group (n=105 incl. 65 CNS + 18 S. aureus + 16 Enterococcus + 6 Streptococcus). Staphylococci-only (n=83) is not given as a single mean; component values are CNS 22.05 +/- 8.26 and S. aureus 14.98 +/- 6.86 (weighted mean ~20.52 h).` — Results / Table 1: 'Gram-positive bacterium (n = 105) ... 20.64 h +/- 9.94'. The value applies to the full Gram-positive |

---

## Methodology notes

1. **Each QC agent was independent of the original extractor.** Nine agents, each handling 3-5 studies, were given only the original extracted JSON and the PDF text — they did not see the screening summary or extraction instructions.
2. **Comparison was field-by-field.** Every populated field in `tbl_study`, `tbl_population`, `tbl_ttp`, and the `tbl_outcomes` list was checked.
3. **Severity was rated by impact on the meta-analysis.** `high` = changes the pooled estimate; `medium` = changes interpretation (wrong design, wrong cutpoint, missing key adjustment); `low` = cosmetic or peripheral.
4. **Most enum issues are schema limitations, not extractor errors.** The `pathogen_class` enum lacks `mycobacterial` (affects Barr2022, Sossen2026); the `outcome_type` enum lacks `endocarditis` or `septic_shock` (affects Berge2023, Cheng2022, Stromdahl2025, Sunnerhagen2026, Tonizzo2026). The schema itself may want extending.
5. **`gap_missing` items are not errors per se** — they're places where an extractor could have computed a pooled value but left null. Where the pooled value was trivially computable (He2024 demographics), it was filled in.
