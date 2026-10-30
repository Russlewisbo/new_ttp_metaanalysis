# TTP Meta-Analysis — PDF Inclusion/Exclusion Report

**Date:** 2026-05-25
**Workbook updated:** `TTP_MetaAnalysis_Extraction_Complete_v2.xlsx`
**Source:** 304 PDFs in `new_ttp_pdfs/` (the user-curated screening pool of 355 papers, minus papers without downloaded PDFs)

---

## Executive summary

| | Count |
|---|---:|
| PDFs in folder `new_ttp_pdfs/` | 307 |
| PDFs that are duplicates of the 57 baseline studies (skipped) | 5 |
| PDFs full-text screened | 302 |
| **PDFs INCLUDED (extracted into workbook)** | **43** |
| PDFs EXCLUDED | 259 |
| Baseline studies (unchanged) | 57 |
| **New extraction database total** | **100 studies** |

### Exclusion breakdown

| Code | Count | Meaning |
|---|---:|---|
| `wrong_design` | 104 | Conference abstract, narrative review, case report (n<10), editorial, study protocol, correspondence |
| `no_ttp` | 65 | TTP not measured/reported. Often confused with duration-of-bacteremia (days), time-to-antibiotic, or treatment delay |
| `no_assoc` | 54 | TTP and outcome both present, but no quantitative TTP↔outcome association (descriptive only, BC-system comparison, diagnostic study only) |
| `no_outcome` | 29 | No clinical outcome reported — methods/microbiology paper only |
| `duplicate` | 5 | Duplicate of another paper (filename collision or republished) |
| `not_bsi` | 2 | Population is not bloodstream infection |

---

## INCLUDED studies (extracted into the workbook)

All 43 studies below were appended to `tbl_study`, `tbl_population`, `tbl_ttp`, and `tbl_outcomes` in the updated workbook. Each has a 6-domain QUIPS risk-of-bias rating recorded in `tbl_study`.

| # | study_id | First author | Year | n | Design | Population (one-line) | TTP reporting | Outcome (headline) |
|---:|---|---|---:|---:|---|---|---|---|
| 1 | Aldemir2026 | Aldemir | 2026 | 217 | retrospective_cohort | Adult inpatients (median age 76) with positive blood cultur… | Overall median TTP 11h (IQR 8.8-15) for Gram-negative, 17h … | 30-day mortality: no significant TTP difference survivors vs non-survivors (p=0… |
| 2 | Balaji2024 | Balaji | 2024 | 57 | prospective_cohort | ICU candidemia patients (mixed adult/pediatric), tertiary h… | Median TTP 24h overall; deceased median 24h vs survivors 35… | 30-day mortality logistic regression: 1-day shorter TTP -> OR 1.397 (95% CI 1.0… |
| 3 | Barberan2010 | Martin-Gutierrez | 2016 | 332 | prospective_cohort | Adult BSI patients (E. coli, S. aureus, K. pneumoniae, P. a… | TTP categorized: short <12h (n=295), medium 12-27h (n=54), … | TTP independent predictor of mortality (HR 1.00, p=0.031); short TTP <12h HR 2.… |
| 4 | Barr2022 | Barr | 2022 | 28 | prospective_cohort | Critically-ill HIV-positive adults with M. tuberculosis blo… | Myco/F lytic blood culture time-to-positivity measured seri… | 12-week mortality 8/28 (29%); slower clearance of MTBBSI (including longer bloo… |
| 5 | Berge2023 | Berge | 2023 | 274 | retrospective_cohort | Adult Staphylococcus aureus bacteremia with CIED, populatio… | Median TTP 11h (IQR 8-17). Dichotomized at <15h. IE group m… | Definite IE (clinical outcome): TTP<15h univariate OR 8.4 (2.0-36) p=0.001; MVA… |
| 6 | Bo2011 | Bo | 2011 | 353 | retrospective_cohort | Adult E. coli bacteremia episodes, two university hospitals… | TTP cutpoint 7 hours used; TTP<=7h group vs TTP>7h group | Hospital mortality 43.3% (TTP<=7h) vs 11.9% (TTP>7h), P<0.0001; MVA OR for TTP<… |
| 7 | Chavez2022 | Chavez | 2022 | 416 | retrospective_cohort | Adults with SAB and ID consult, Barnes-Jewish Hospital St. … | Median TTP 17.8h (IQR 14-23) pre-VIRTUO vs 13.3h (IQR 10-19… | Shorter TTP independent predictor of persistent SAB (>=3 days positive BC): OR … |
| 8 | Chen2018 | Chen | 2018 | 206 | retrospective_cohort | Adults with nontyphoidal Salmonella bacteremia, National Ta… | TTP cutpoint 10h (rapid vs slow); cutoff selected by univar… | TTP <10h independent predictor of complicated NTS bacteremia (composite of 30-d… |
| 9 | Cheng2022 | Cheng | 2022 | 67 | retrospective_cohort | Pediatric (1mo-18y) nosocomial K. pneumoniae bloodstream in… | Median TTP 14.12 h (IQR 12.72-16.22); dichotomized at <=13 h | Multivariate logistic regression: TTP <=13h independently associated with septi… |
| 10 | Comba2024 | Comba | 2024 | 186 | retrospective_cohort | Adult S. aureus bacteremia with positive follow-up BCs >=24… | Median initial TTP 12h (IQR 10-15); median sequential TTP 2… | Kaplan-Meier 30-day survival significantly lower with ITTP <12h (log-rank signi… |
| 11 | Cubuk2026 | Cubuk | 2026 | 904 | retrospective_cohort | Adult ICU patients with suspected BSI, two hospitals in Siv… | Median TTP by species and HbA1c stratum (e.g., E. coli 13.7… | TTP significantly shorter in 28-day decedents for E. coli (11.2h vs 12.1h, p=0.… |
| 12 | Fenoll2022 | Garcia Fenoll | 2022 | 95 | retrospective_cohort | Adult Staphylococcus aureus bacteremia, single tertiary cen… | Mean TTP 16h (SD 17); cutpoint TTP <=12h vs >12h; 17% had T… | TTP <=12h associated with sepsis OR 2.6 (1.1-6.2); trend with 14-day mortality … |
| 13 | Gavronski2020 | Gavronski | 2020 | 774 | retrospective_cohort | ICU bloodstream infections (true BSIs) Curitiba Brazil 2013… | Mean TTP by organism; Candida 39h (SD 28.4); cutpoint 37h f… | Candida TTP<37h predicted mortality (AUC 0.733, sens 83%, spec 60%, p=0.005); n… |
| 14 | He2024 | He | 2024 | 131 | retrospective_cohort | Adult BSI cases: C. striatum-BSI (25), MRSA-BSI (62), MRSE-… | Median TTP by group: C. striatum 27h, MRSA 20h, MRSE 19h (p… | 28-day mortality compared across organisms (C. striatum 52% vs MRSA 25.8% vs MR… |
| 15 | Huang2013 | Huang | 2013 | 87 | retrospective_cohort | Adult candidemia patients, single-center China (Peking Univ… | Mean TTP 43.47 ± 19.51 h overall; by species C. glabrata 62… | 30-day mortality analyzed via logistic regression with TTP as risk factor: TTP … |
| 16 | IrigoyenvonSierakowski2024 | Irigoyen-von-Sierakowski | 2024 | 89 | retrospective_cohort | E. coli bacteremia with paired catheter lumen + peripheral … | Median TTP peripheral 8.95h, catheter lumen 8.93h; categori… | Treatment success by DTTP-defined group: CC 53.3%, C-RBSI 37.5%, non-C-RBSI 84.… |
| 17 | Jayabalakrishnan2022 | Jayabalakrishnan | 2022 | 75 | prospective_cohort | Patients with positive blood cultures (BSI), tertiary care … | median 13 h (SD 13.32); cutpoint <=10h vs >10h; short TTP 3… | Univariate OR for outcomes by TTP <=10h vs >10h: septic shock OR 3.75 (0.58-24.… |
| 18 | Kahn2021 | Kahn | 2021 | 465 | retrospective_cohort | Adult Staphylococcus aureus bacteraemia, population-based 1… | Median TTP 8.7h (IQR 7.7-10.6) for IE vs 13.3h (IQR 10.5-16… | TTP for IE: sensitivity 100% (91-100), specificity 52% (47-57); AUC 0.83 (0.78-… |
| 19 | Keighley2023 | Keighley | 2023 | 415 | prospective_cohort | Adult candidemia episodes, prospective multicenter Australi… | Median TTP 48h (IQR 33-65); species-specific medians: C. al… | Each day increase in TTP multiplies OR for 30-day survival by 1.32 (95%CI 1.06-… |
| 20 | Kim2013 | Kim | 2013 | 152 | retrospective_cohort | Adult inpatients with candidemia, single tertiary hospital … | Median TTP 27h (IQR 19-37h); cutpoint TTP ≤24h vs >24h | 6-week mortality 53%; TTP ≤24h: adjusted HR 2.74 (95% CI 1.51-4.97, p=0.001) fo… |
| 21 | Lin2016 | Lin | 2016 | 66 | retrospective_cohort | Adults with nontyphoidal Salmonella (NTS) bacteremia, singl… | Median TTP 11.5h (range 6.5-41.7); dichotomized at <10h vs … | In-hospital mortality TTP<10h vs >=10h: 21.1% vs 12.8%, OR 1.82 (0.38-7.36); 30… |
| 22 | Lin2018 | Lin | 2018 | 217 | retrospective_cohort | Adults >=50y with nontyphoid Salmonella bacteremia, derivat… | TTP <10h used as cutoff (predictor) | TTP <10h independent predictor of NTS vascular infection: OR 4.67 (1.42-15.39) … |
| 23 | Mandolfo2020_a | Mandolfo | 2020 | 40 | prospective_cohort | Hemodialysis patients with S. aureus CRBSI on tunnelled CVC… | TTP mean 16.7+/-2.8h (tCVC saved) vs 9.2+/-3.4h (tCVC repla… | Catheter salvage success vs failure: TTP <12h associated with treatment failure… |
| 24 | MartinGutierrez2017 | Martin-Gutierrez | 2017 | 361 | prospective_cohort | Adult BSI (E. coli, S. aureus, K. pneumoniae, P. aeruginosa… | TTP grouped: short <12h, medium 12-27h, long >27h (n=295/54… | Cox HR for mortality: short TTP <12h HR 2.10 p=0.047; long TTP >27h HR 3.28 p=0… |
| 25 | Nunes2013 | Nunes | 2013 | 89 | retrospective_cohort | Adult Candida albicans bloodstream infection, single-center… | Mean TTP 41.9h (range 6.7-95.2); cutpoint 36h (n=39 ≤36h vs… | In-hospital mortality OR 1.04 per hour (95% CI 1.0-1.1, p=0.035) — TTP only ind… |
| 26 | PerezRodriguez2024 | Perez-Rodriguez | 2024 | 121 | case_control | Adult E. faecalis bacteremia (39 IE cases, 82 controls), si… | median 11h (IQR 8.6-13.7) non-IE vs 10h (8-13) IE; cutpoint… | TTP<=8h not assoc with poor prognosis (RR 0.4, 95% CI 0.10-1.64); in community-… |
| 27 | Prinsloo2023 | Prinsloo | 2023 | 193 | retrospective_cohort | Adult B. pseudomallei (melioidosis) bacteremia, Cairns Hosp… | median 31h (IQR 26-39); TTP categories <24h, 24-<48h, 48-<7… | TTP<24h: 48% died vs 8% died for TTP 24-<48h (2x2 by TTP category); shorter TTP… |
| 28 | PuertaAlcalde2019 | Puerta-Alcalde | 2019 | 850 | prospective_cohort | Adult onco-haematological patients with febrile neutropenia… | median 12h (IQR 9-16.5); TTP <24h vs >=24h categorical comp… | 30-day mortality TTP<24h vs >=24h: 20.2% vs 23.9% (p=0.475); infection-related … |
| 29 | Recio2020 | Recio | 2020 | 243 | retrospective_cohort | Adults with P. aeruginosa bloodstream infection, single cen… | TTP analyzed as continuous variable (per-hour) in multivari… | Shorter TTP associated with 5-day mortality: aOR 0.88 (95% CI 0.80-0.97), p=0.0… |
| 30 | Rojas2013 | Rojas | 2013 | 112 | retrospective_cohort | Adult S. aureus bacteremia patients, Detroit Receiving Hosp… | Mean TTP 27.03h transient SAB (n=35) vs 18.42h persistent S… | Longer TTP significantly associated with transient (vs persistent) bacteremia; … |
| 31 | Sachu2024 | Sachu | 2024 | 100 | retrospective_cohort | Candidemia patients (mixed ages including some pediatric), … | Median TTP 34h (IQR 21.75-50); TTP dichotomized at 24h; spe… | TTP ≤24h: 30.2% survivors vs 40.5% died (p=0.3); Kaplan-Meier survival by TTP u… |
| 32 | Sossen2026 | Sossen | 2026 | 519 | prospective_cohort | Adult inpatients with HIV-associated TB, Khayelitsha South … | Mycobacterial blood culture TTP converted to 4-level ordina… | Day-28 mortality: logistic regression with BC TTP ordinal scale AUC 0.60; laten… |
| 33 | Sowden2008 | Sowden | 2008 | 146 | retrospective_cohort | Adults with community-acquired MSSA bacteremia, Nambour Hos… | Mean TTP 17.29h (range 8-88h); dichotomized at 12h | 30-day mortality 23.3%; multivariate logistic regression TTP<12h OR 5.91 (95% C… |
| 34 | Stromdahl2025 | Strömdahl | 2025 | 1703 | retrospective_cohort | Adults with Staphylococcus aureus bacteremia, single tertia… | Median TTP 13h (IQR 10-18); cutpoint at median (13h); analy… | Endocarditis (9%): TTP <13h independent OR 3.59 (95% CI 2.35-5.3); per-hour OR … |
| 35 | Sunnerhagen2026 | Sunnerhagen | 2026 | 463 | retrospective_cohort | Adults with Streptococcus agalactiae bacteraemia, southern … | Median TTP 9.0h overall (n=411 for TTP analysis) | 30-day mortality: TTP 8.6h vs 9.1h (p=0.4); IE: TTP 7.5h vs 9.1h (p=0.005) |
| 36 | Tang2017 | Tang | 2017 | 139 | retrospective_cohort | Adult monomicrobial Pseudomonas aeruginosa bacteremia, sing… | median 15h (range 5-120); cutpoint 13h (ROC-derived) used | 30-day mortality 54.2% (TTP<=13h) vs 15.0% (TTP>13h); multivariate OR 6.10 (2.0… |
| 37 | Taur2010 | Taur | 2010 | 106 | retrospective_cohort | Cancer patients with candidemia, single center (MSKCC) | median incubation period (TTP) 32.1h (95% CI 27.9-34.8); an… | Incubation period (TTP) significantly associated with in-hospital mortality; un… |
| 38 | Thorburn2025 | Thorburn | 2025 | 288 | retrospective_cohort | Adult haematology inpatients with BSI and central line in s… | Differential TTP (DTP) measured in 31.9%, categorized (<120… | DTP not significantly associated with line retention failure (OR 0.65, 0.20-2.1… |
| 39 | Thornley2024 | Thornley | 2024 | 65 | retrospective_cohort | Pediatric patients with S. aureus bacteremia, single-center… | Median TTP 16h (IQR 14-18) persistent SAB vs 20h (17-24) no… | Shorter TTP associated with persistent SAB (p<0.001); TTP 16.35h: sens 0.71, sp… |
| 40 | Tonizzo2026 | Tonizzo | 2026 | 973 | retrospective_cohort | Adult SAB patients with systematic ECHO, large tertiary hos… | Median TTP 11.9h (IQR 7.9-17.2); shorter in IE 8.6h vs 12.4… | TTP shorter in IE patients; NPV 86.6% for TTP>13h to rule out IE; 187/973 had IE |
| 41 | Willmann2013 | Willmann | 2013 | 74 | retrospective_cohort | Adult monomicrobial Pseudomonas aeruginosa BSI, 3 hospitals… | TTP from aerobic BACTEC bottles; cutpoint 18h identified by… | In-hospital mortality: multivariate Cox HR 3.83 (P=0.012) for TTP <=18h |
| 42 | Zhang2016 | Zhang | 2016 | 386 | retrospective_cohort | Cancer patients with BSI (Enterobacteriaceae, nonfermenters… | Mean TTP varied by organism (Enterobacteriaceae 11.4h, nonf… | In-hospital mortality higher with short TTP in Enterobacteriaceae (29.6% TTP<=8… |
| 43 | Zouggari2022 | Zouggari | 2022 | 105 | retrospective_cohort | Adult anaerobic bacteremia, single tertiary hospital Belgiu… | TTP dichotomized at median 30h; analyzed in Cox model for 3… | 30-day mortality 21.9% overall; TTP>=30h Cox HR 0.24 (0.07-0.84, p=0.025) - LOW… |

---

## EXCLUDED studies (with reasons)

### `wrong_design` (104 studies) — Conference abstract, narrative review, case report (n<10), editorial, study protocol, correspondence

| doc_id | Author | Year | Title (short) | Specific reason |
|---|---|---:|---|---|
| Agnello2019 | Agnello | 2019 | Clinical outcomes of daptomycin vs. Anti-staphyloc ... illin-suscepti… | IDWeek 2019 poster abstract (Open Forum Infect Dis Suppl). No TTP measured/reported. Also small n=29 and conference abs… |
| AlShokri2026 | Al-Shokri | 2026 | The Clinical Characteristics and Outcomes of Com ... in-susceptible S… | IDWeek 2026 poster abstract (OFID Suppl). Examines time to blood culture clearance (different concept) not TTP. Confere… |
| Andonie2021 | Andonie | 2021 | Clinical Outcomes with Ceftaroline Monotherapy ver ... e Treatment of… | IDWeek 2021 poster abstract (OFID Suppl). Small n=32. TTP not measured. Conference abstract only. |
| Arns2026 | Arns | 2026 | Predictive Score for True Coagulase-negative Staphylococcus Bloodstre… | Conference abstract (IDWeek/OFID poster P-1140). Outcome is microbiological case definition (true BSI vs contaminant), … |
| Arshad2012 | Arshad | 2012 | Comparison of composite clinical outcome in USA600 ... ST5) methicill… | ECCMID 2012 conference abstract P2366. The PDF file is a compilation of ECCMID poster abstracts. No TTP measured. Also … |
| Barsic2012 | Barsic | 2012 | Importance of early antifungal therapy and its duration | Single-page conference abstract (ECCMID S157, Barsic, Zagreb) summarizing existing literature on antifungal timing. Not… |
| Buchan2022 | Buchan | 2022 | Commentary - Can Automated Blood Culture Systems Be Both New and Impr… | Editorial/commentary, not an original study. |
| Cabanilla2023 | Cabanilla | 2023 | Impact of Ceftaroline Duration after Bacteremia ... d in Combination … | Conference poster abstract (IDWeek 2023, OFID supplement) - single-page abstract, wrong_design. Also no TTP. |
| Caniff2023 | Caniff | 2023 | Unexpected Allies - Vancomycin and Cefazolin Combination Therapy in M… | Single-page IDWeek 2023 conference abstract (OFID supplement). Exclude as wrong_design (abstract only). Also no TTP mea… |
| Chang2015 | Chang | 2015 | The effect of applying polymerase chain reaction to ... reus in blood… | Conference abstract from APSIC 2015 (single column abstract). Exclude as wrong_design. TTP used only as eligibility fil… |
| Chauhan2019 | Chauhan | 2019 | Evaluation of risk factors and clinical outcomes of patients with van… | IDWeek 2019 conference abstract (OFID supplement, Poster #575). No TTP reported. |
| Chauhan2020 | Chauhan | 2020 | Evaluation of risk factors and clinical outcomes of patients with van… | ACCP 2019 Annual Meeting abstract collection (J Am Coll Clin Pharm 2020). The relevant Chauhan VRE entry is a conferenc… |
| Chavez2020 | Chavez | 2020 | Impact of the Bact - Alert virtuo blood culture system in the managem… | IDWeek 2020 conference abstract (OFID supplement, Poster #292). Pre-print of Chavez2022 paper. Abstract-only — exclude … |
| Chen2025 | Chen | 2025 | RISK FACTORS and CLINICAL OUTCOMES of CANDIDA TROPICA ... SUS NON-TRO… | EHA2025 conference abstract (PB2552). TTP reported descriptively; no quantitative TTP-to-outcome association. Likely du… |
| Chen2026 | Chen | 2026 | Risk Factors, Clinical Outcomes and Immune Dynamics of Candidemia in … | IDWeek 2025/26 conference abstract (OFID supplement, P-1962). Same 105-patient cohort as Chen2025. No quantitative TTP-… |
| Cheng2018 | Cheng | 2018 | Daptomycin versus placebo as an adjunct to beta-lact ... aureus bacte… | Study protocol paper (BMC Trials) for the DASH RCT - no data, no analyses. Excluded as wrong_design. The full results p… |
| Cheng2020 | Cheng | 2020 | Adjunctive daptomycin in the treatment of staphylococcus aureus bacte… | Conference abstract (IDWeek 2020) of the DASH RCT; duplicate of Cheng2021 full paper. No TTP measured. |
| Chuluunkhuu2019 | Chuluunkhuu | 2019 | Antibiotics susceptibility, Biofilm Production ... Characteristics of… | Conference poster abstract (P1-GN47, ICIC & ISAAR 2019). No TTP measured. Also no_ttp applies. |
| Chung2020 | Chung | 2020 | Characteristics of persistent bacteremia caused by community-acquired… | Conference poster abstract (P13, 2020 Korean meeting). No TTP measured. wrong_design and no_ttp both apply. |
| Cisneros2016 | Cisneros | 2016 | Impact of a newly implemented antimicrobial stewa ... infections (BSI… | Conference poster abstract (IDWeek 2016). Stewardship outcomes; no time-to-positivity measured. |
| Comba2022 | Comba | 2022 | Sequential Time to Positivity as a Prognostic Indicator in Staphyloco… | Conference abstract (IDWeek 2022, abstract ID ofac492.1487). Same data as Comba2024 full paper. Excluded as conference … |
| Contrael2013 | Contrael | 2013 | Effect of appropriate initial antifungal therapy for candidemia on mo… | Conference abstract (Crit Care Med 2013 supplement). TTP compared by resistance status only; outcomes (in-hospital and … |
| Crosby2023 | Crosby | 2023 | Combination Antibiotic Therapy vs Monotherapy for Methicillin Resista… | IDWeek 2023 poster abstract (OFID 2023:10 Suppl 2). Conference abstract only. Discusses time to clearance (duration of … |
| Deliberato2010 | Deliberato | 2010 | Clinical impact of diagnosis methods for catheter-related bloodstream… | ISICEM 2010 conference abstract (Crit Care 2010 Suppl 1:P385). Compares diagnostic methods, not TTP vs outcome. Could a… |
| Dotel2023 | Dotel | 2023 | Effectiveness of adjunctive rifampicin for treatment ... a systematic… | Secondary research (systematic review/meta-analysis), not a primary study of TTP-outcome association. |
| Eden2018 | Eden | 2018 | Treatment of bacteremia during dialysis using a biomi ... rbent hemop… | Conference abstract (NDT supplement), n=8, device safety/efficacy proof-of-concept. TTP used as efficacy surrogate for … |
| Edwardson2019 | Edwardson | 2019 | Using host biomarkers and time to blood culture positiv ... or echoca… | Conference abstract only (IDWeek 2019 poster, OFID Suppl). Quantitative TTP-outcome comparison reported but as abstract… |
| Ehren2018 | Ehren | 2018 | Assessment of the clinical impact of rapid identifca ... phenoTM syst… | Conference abstract (OFID Poster Abstracts 2018). Diagnostic turnaround time study, not TTP-outcome study. |
| FernandezRufete2011 | Fernandez-Rufete | 2011 | Coagulase-negative Staphylococcus bactera ... study of clinical and m… | Conference abstract (ECCMID 2011 P1474). Outcome is microbiologic classification (true bacteremia vs contamination), no… |
| Fiala2016 | Fiala | 2016 | The 'skip phenomenon' in blood culture positivity in ... bacteremia -… | IDWeek 2016 conference oral abstract. Concerns duration of bacteremia and skip phenomenon, not TTP. No TTP-outcome asso… |
| Folan2016 | Folan | 2016 | Empiric linezolid treatment is associated with adver ... linezolid-re… | IDWeek 2016 conference oral abstract. No TTP analyzed. Exposure is linezolid resistance, not TTP. |
| Fujino2018 | Fujino | 2018 | Differentiation between true infection and contamination of coagulase… | IDWeek 2018 poster abstract (conference). Outcome is diagnostic classification (true infection vs contamination), not c… |
| Gardiner2014 | Gardiner | 2014 | Retrospective review of 2 years of candidaemia from a single health c… | Conference abstract (Internal Medicine Journal Suppl 3 RACP Congress 2014). Descriptive only; TTP reported by species, … |
| Gasca2025 | Gasca | 2025 | The Skip Phenomenon in Patients with Staphylococcus lugdunensis Blood… | Conference abstract (OFID/IDWeek 2024 Poster P-832). Descriptive only. |
| Gawrys2018 | Gawrys | 2018 | The impact of rapid diagnostic testing and antimicr ... ens for gram-… | Conference abstract (OFID 2018 Suppl Poster #1807). RDT intervention study, no TTP exposure analyzed. |
| Gonzalez2020 | Gonzalez | 2020 | Modern Blood Culture - Management Decisions and Method Options | Review article (Clin Lab Med). Not a primary study. |
| Grant2022 | Grant | 2022 | Racial Differences in Candidemic Patients at a Southern California Te… | IDWeek 2022 poster abstract (ofac492.1241). Reports TTP descriptively by racial group but no TTP-outcome regression/2x2. |
| Gregory2017 | Gregory | 2017 | Impact of an antimicrobial stewardship initiative focused on staphylo… | IDWeek 2017 poster abstract. Stewardship intervention study, no TTP measured. |
| Haghamad2023 | Haghamad | 2023 | 576. Comparison of Three Blood Culture Testing Models at a Tertiary C… | IDWeek 2023 poster abstract (ofad500.645). Lab model comparison, no TTP-outcome quantitative analysis. |
| Hashim2020 | Hashim | 2020 | A 2-year retrospective review of Carbapene ... aceae (CRE) carriers a… | Conference abstract (IJID), only 7 patients, only 3 with positive blood cultures. No TTP-outcome quantitative analysis. |
| Hauser2020 | Hauser | 2020 | Multicenter retrospective cohort study of the clini ... f staphylococ… | IDWeek 2020 poster abstract. Compares 1 vs >=2 positive sets; no TTP-outcome quantitative analysis. |
| Heinen2022 | Heinen | 2022 | Cutibacterium acnes endocarditis - A multicenter case series | ESC Congress 2022 abstract only - full paper not available. Conference abstract = wrong_design. |
| Jang2024 | Jang | 2024 | Outcome of ceftazidime - avibactam versus other alter ... Enterobacte… | Conference abstract only (Korean Society of Infectious Diseases 2024 Fall meeting OC-3). No TTP analyzed; exposure is a… |
| Jawanda2023 | Jawanda | 2023 | Impact of Rapid Identification and Resistance Gene Detection using an… | Conference poster abstract (IDWeek 2023). TTP not measured/analyzed. Time-to-active-therapy is the exposure. |
| Jo2018 | Jo | 2018 | Diagnostic usefulness of diferential time to positivity ... enic canc… | Conference abstract (IDWeek 2018). Diagnostic accuracy study (DTP vs CRC diagnosis); no clinical outcome reported. |
| Jones2023 | Jones | 2023 | Daptomycin Plus Ceftaroline Versus Monotherapy for Persistent Mrsa Ba… | Conference abstract (SCCM). No TTP measurement; bacteremia duration reported but exposure is treatment regimen, not TTP. |
| Jung2022 | Jung | 2022 | Impact of Accelerate Rapid Diagnostic Technology on T ... Optimal Ant… | Conference abstract (IDWeek 2022). TTP not measured; exposure is RDT implementation. |
| Kamath2021 | Kamath | 2021 | Ceftaroline versus Vancomycin as First-Line Therapy for MRSA Bacterem… | Conference abstract (IDWeek 2021), n=15/group, no TTP measured. Wrong design + no_ttp. |
| Karlath2025 | Karlath | 2025 | Assessment of the time taken for blood culture pos ... f beta-D-gluca… | Letter to the Editor with small case series. Reports time-from-symptom-to-positivity, not TTP of culture; descriptive o… |
| Kato2011 | Kato | 2011 | Clinical features of acute cholangitis and the evaluation of blood cu… | Conference poster abstract (J Gastroenterol Hepatol 2011 Suppl 5). TTP given as descriptive frequencies by group, no qu… |
| Keklik2025 | Keklik | 2025 | The impact of carbapenem-resistant Gram-negative catheter infections … | Conference abstract only (Critical Care 2025 ISICEM meeting abstracts, P271). Very brief; no quantitative TTP↔mortality… |
| Khan2023 | Khan | 2023 | Evaluating Clinical Outcomes of Adjunctive Beta-Lactam Use in Vancomy… | OFID conference abstract (poster, 2402); no time-to-positivity measurement. Exposure is adjunctive beta-lactam use, not… |
| Kufel2024 | Kufel | 2024 | Daptomycin Plus Oxacillin for Persistent Methicillin-Susceptible Stap… | Case series n=7, below threshold for inclusion. Also no TTP measured (uses duration of bacteraemia). |
| Kumar2026 | Kumar | 2026 | Impact of Infectious Disease Consultation in Outcome of Enterococcal … | OFID conference poster abstract (P-15). No TTP analysis - intervention is ID consultation, not TTP. |
| La2021 | La | 2021 | Comparison of anti-staphylococcal beta-lactam and glyco ... s aureus … | Conference abstract (Korean ID/Antibiotic Society 2021). Compares antibiotic regimens, not TTP. No TTP measured. |
| Lamp2012 | Lamp | 2012 | Daptomycin outcomes by duration of methicillin-resistant Staphylococc… | ACCP 2012 conference abstract (#138). Analyzes duration of bacteremia, not TTP. |
| Le2016 | Le | 2016 | Epidemiology of candidemia in hospitalized patients with acute leukem… | IDWeek 2016 poster abstract (#1597). Descriptive only - no TTP-outcome quantitative association. |
| Lecronier2016 | Lecronier | 2016 | Epidemiology, characteristics and outcomes of se ... tients after the… | Conference abstract (Reanimation 2016, O42). DTP used as part of CRBSI definition only; no quantitative TTP-outcome ana… |
| Liao2025 | Liao | 2025 | Further considerations on the clinical applicability ... ol for cathe… | Critical Care 'Matters Arising' commentary, not original research. |
| Liu2013 | Liu | 2013 | Mycobacterium abscessus bacteremia after receipt of in ... duced kill… | Case series with n=4 (<10); descriptive TTP-severity link only, no statistical analysis. Wrong design. |
| Liu2025 | Liu | 2025 | Epidemiology and outcomes of catheter-related bloodstream infections … | Conference abstract only (Antimicrobial Resistance & Infection Control 2025 Suppl, P1006). DTP used as definition for C… |
| Ma2022 | Ma | 2022 | Reducing Time to Optimal Antimicrobial Therapy (OAT) fo ... ing Rapid… | IDWeek 2022 conference abstract only; no full methods/results |
| Maakaron2019 | Maakaron | 2019 | Levofloxacin Prophylaxis for Autologous Stem Cell Transplant - A Seco… | Conference abstract; descriptive comparison of timing between groups, no TTP-outcome quantitative association |
| Mai2018 | Mai | 2018 | Evaluation of empiric vancomycin and beta-lactam therapy on outcomes … | Conference abstract (ACCP Global Conference 2018); only abstract text available, no TTP-outcome data |
| Makris2008 | Makris | 2008 | Septic embolism with subacute onset | Letter/case report (n=1) by Makris. NOTE: text file also contains an unrelated Sowden et al. 2008 letter on TTP<12h and… |
| Milin2026 | Milin | 2026 | 449. Further evidence for subphenotype E of Staphylococcus aureus bac… | Conference abstract (IDWeek 2025) - uses days of blood culture positivity (duration of bacteremia) which is not the sam… |
| Moni2019 | Moni | 2019 | Implementation of an antifungal stewardship bundle focused on candide… | Conference abstract; reports time to appropriate therapy not TTP; no TTP-outcome analysis |
| Moore2009 | Moore | 2009 | How does persistent bacteraemia affect outcome in methicillin-resista… | ECCMID 2009 conference abstract (P1862); studies duration of bacteremia (persistent bacteremia >=7d) not TTP (time to b… |
| Mortimer2022 | Mortimer | 2022 | 7 Differences in physiological - metabolic parame ... ococcus aureus … | Conference abstract; mentions time to culture positivity collected but only descriptive comparison of PWID vs non-PWID;… |
| Naeger2016 | Naeger | 2016 | Treatment of Staphylococcus aureus bacteremia pre-and post-implementa… | ACCP conference abstract only. No TTP-clinical outcome analysis reported. |
| Nagvekar2025 | Nagvekar | 2025 | Comparative Clinical profile, Anti-Fungal resista ... ed by Candida A… | IDWeek/OFID conference poster abstract. TTP reported descriptively between groups, no quantitative TTP-outcome associat… |
| Nashar2026 | Nashar | 2026 | Tigecycline for Refractory Vancomycin-Resistant Enterococcus Bacterem… | IDWeek/OFID conference poster abstract, n=19. No TTP measured. Descriptive case series. |
| Oke2019 | Oke | 2019 | Survival & fungal catheter related blood stream infections in patient… | BSG conference abstract. TTP used only diagnostically; no TTP↔outcome quantitative analysis. |
| Olion2022 | Olion | 2022 | Opportunities for antimicrobial stewardship - Time t ... tures before… | IDWeek 2022 conference abstract. Focuses on TTOT (time to optimal therapy), not TTP-blood culture positivity. No TTP-cl… |
| Osipov2020 | Osipov | 2020 | Ceftazidime-avibactam and aztreonam in the treatmen ... tropenic pati… | EHA 2020 conference abstract (EP1603); n=15 case series; no TTP measurement or TTP-outcome association. |
| Pandit2022 | Pandit | 2022 | Pos-116 Adverse Outcomes after Tunnelled Hemodialys ... ciated Bloods… | ISN Frontiers 2022 conference abstract (POS-116). No TTP measurement; focus on infecting microorganism and adverse outc… |
| Pham2022 | Pham | 2022 | Multicenter evaluation of Staphylococcus aureus prost ... arditis wit… | Conference abstract only (IDWeek 2022, OFID supplement). No TTP measurement. |
| Pinargote2022 | Pinargote | 2022 | Evaluation of Predicting Performance of POSITIVE ... ective Endocardi… | Conference abstract (IDWeek 2022, OFID supplement). Even though TTP-IE association present, abstract-only excludes per … |
| Robinson2026 | Robinson | 2026 | Group A Streptococcus (GAS) Bloodstream Infection (BSI) in Patients W… | Conference abstract (poster) only; descriptive results, no TTP-outcome quantitative analysis |
| Saksena2020 | Saksena | 2020 | Correlation between time-to-positivity of blood culture and clinical … | Conference abstract only (IJID 2020 supplement), no full paper available; sample size includes large pediatric proporti… |
| Schall2021 | Schall | 2021 | Dysgonomonas capnocytophagoides Bacteremia in a Patient With Stage IV… | Single case report (Cureus); n<10. |
| Shah2017 | Shah | 2017 | Blood cultures in patients with aneurysmal subarachnoid hemorrhage | Conference abstract (NCS 2017 poster); TTP used only for contamination adjudication, no quantitative TTP-outcome associ… |
| Shimose2018 | Shimose | 2018 | Outcomes of patients with vancomycin-resistant enterococcus blood str… | IDWeek 2018 conference abstract (poster 2441). No TTP measured/analyzed. Wrong design (abstract only) and no_ttp. |
| Smith2026_a | Smith | 2026 | Clinical Outcomes of Standard-of-Care versus Broad-S ... -Lactams for… | IDWeek 2025 conference abstract (P-10). No quantitative TTP↔outcome analysis in abstract. Wrong design (abstract only). |
| Smith2026_b | Smith | 2026 | Impact of Rapid Blood Culture Identification for Gram-Positive Bacter… | ASHP Midyear 2025 resident poster abstract, Research-in-Progress. No results reported. Wrong design. |
| Staicu2020 | Staicu | 2020 | Characterizing fungemic outcomes among adult inpatients at a communit… | Conference abstract (IDWeek/OFID 2020 poster) - descriptive only; reports TTP and outcomes but no quantitative TTP↔outc… |
| Stewart2023 | Stewart | 2023 | Central line associated and primary bloodstream infections | Narrative review/Current Opinion article. No original quantitative TTP↔outcome analysis. |
| Stromdahl2026 | Strömdahl | 2026 | Time to Positivity in Staphylococcus aureus Bacteremia - One of Many … | This file contains correspondence letters (Santos-Patarroyo et al letter + Stromdahl reply) re: the Stromdahl2025 paper… |
| Tong2016 | Tong | 2016 | CAMERA2 - combination antibiotic therapy for methicil ... s aureus in… | Study protocol paper for planned RCT; no TTP analysis |
| Trang2016 | Trang | 2016 | Assessing the impact of an automatic antimicrobial s ... n patients w… | Conference poster abstract only; not full study with TTP analysis |
| Tsuchido2022 | Tsuchido | 2022 | Clinical Characteristics of Staphylococcus aureus Bacteremia with the… | Conference abstract (IDWeek 2022 Poster Abstract 1821, OFID Supplement). TTP not measured/analyzed; concept is skip phe… |
| Um2018 | Um | 2018 | Relationship between time to positivity of blood culture and mortalit… | ESICM LIVES 2018 conference abstract 0554 (Intensive Care Medicine Experimental Suppl). Has quantitative TTP-mortality … |
| Vasoo2025 | Vasoo | 2025 | A Randomized Controlled Trial of Rapid Pathogen and Resistance Identi… | IDWeek 2024 conference abstract (OFID 2025 Suppl, abstract 302). Diagnostic intervention RCT - TTP not used as predicto… |
| Wallace2025 | Wallace | 2025 | Serratia Infections in Burn Care | Letter to the Editor, retrospective review of 22 mixed-site Serratia infections (BSI subset <10). Time to positive is d… |
| Wang2011 | Wang | 2011 | Utility of Time to Positivity for Diagnosis of Bloodstream Infection | Narrative review article (Reviews in Medical Microbiology). No primary data. Excluded as wrong_design. |
| Wang2020 | Wang | 2020 | Adjuvant β-Lactam Therapy Combined with Vancomycin or ... phylococcus… | Systematic review/meta-analysis evaluating antibiotic combinations, not TTP as exposure. Excluded as wrong_design (revi… |
| Wang2024 | Wang | 2024 | Persistent bacteremia caused by Ralstonia pickettii and Microbacteriu… | Case report (n=1), excluded per wrong_design (case report <10). |
| Wein2021 | Wein | 2021 | Assessment of Clinical Outcomes and Antibiotic Prescr ... Culture Ide… | Conference abstract only (OFID 2021 supplement, IDWeek). No TTP analyzed. |
| Williams2019 | Williams | 2019 | Nocardia bacteremia is almost always associated w ... e - Single-cent… | Conference abstract (IDWeek 2019 supplement) - single-center series of only 4 cases plus narrative review. wrong_design. |
| Yang2018 | Yang | 2018 | Improving antimicrobial prescribing and rate of infec ... ice alert a… | IDWeek 2018 conference abstract (#234). No TTP measured; quality improvement study of stewardship intervention. |
| Yarovoy2017 | Yarovoy | 2017 | Bacteremia risk factors differ between methicillin ... icillin-resist… | SAEM 2017 conference abstract #448. Compares risk factors for MRSA vs MSSA; no TTP measured. |
| Yoon2026 | Yoon | 2026 | Epidemiology and Clinical Characteristics of Bacteremia Following Por… | IDWeek 2026 conference abstract (oral, #659). Descriptive epidemiology of post-PVE bacteremia; no TTP. |
| Zhao2025 | Zhao | 2025 | β-Lactam Adjunctive Therapy Compared to Vancomycin or ... ccus aureus… | Systematic review/meta-analysis - excluded per protocol (wrong_design / narrative review category). |
| Zidaru2020 | Zidaru | 2020 | Real world experience with daptomycin (DAP) and cef ... apy for methi… | IDWeek 2020 conference abstract #1624. No TTP measured; focuses on time to bacteremia clearance after combination thera… |

### `no_ttp` (65 studies) — TTP not measured/reported. Often confused with duration-of-bacteremia (days), time-to-antibiotic, or treatment delay

| doc_id | Author | Year | Title (short) | Specific reason |
|---|---|---:|---|---|
| Albertson2015 | Albertson | 2015 | Determination of Risk Factors for Recurrent Meth ... aureus Bacteremi… | Large cohort identifying risk factors for recurrent MRSA bacteremia. Uses duration of bacteremia (days between first an… |
| Alosaimy2021 | Alosaimy | 2021 | Standardized Treatment and Assessment Pathway Imp ... Methicillin-res… | Quasi-experimental pre/post pathway study. TTP not mentioned anywhere in the paper. Duration of bacteremia (days) discu… |
| Avery2005 | Avery | 2005 | Early vancomycin-resistant enterococcus (VRE) bacter ... plantation i… | Small descriptive case series (n=10). No TTP (incubation-to-positivity) measured; the 15 days refers to days post-trans… |
| Bae2023 | Bae | 2023 | Clinical and microbiological characteristics of rifampicin-resistant … | Strong clinical outcomes study but TTP (time from bottle incubation to positivity) is not measured/reported. Excluded a… |
| Barbour2013 | Barbour | 2013 | Treatment of vancomycin-resistant enterococcal bac ... l cohort of ne… | Comparative antibiotic study (daptomycin vs linezolid) with clinical outcomes but no TTP measured. Duration of bacterem… |
| Bassetti2014 | Bassetti | 2014 | A multicenter study of septic shock due to candidemia - Outcomes and … | Exposure is time-to-treatment from positive BC, not TTP (time-to-detection of BC). No TTP variable measured/analyzed. |
| Bauer2013 | Bauer | 2013 | An antimicrobial stewardship program's evaluation of ... e treatment … | Compares nafcillin dosing regimens; outcomes are AIN/ARF/mortality vs infusion type. TTP not measured. |
| Bertucci2025 | Bertucci | 2025 | Impact of Remote Cholecystectomy on Clinical Outcomes Following Pseud… | Exposure is remote cholecystectomy status. 'Length of culture positivity' = duration of bacteremia (in days, from manua… |
| Bohard2026 | Bohard | 2026 | Combination of ertapenem and penicillin M or cefazo ... usceptible St… | Small retrospective case series (n=35) describing dual-therapy use. No TTP measurement or TTP-outcome analysis. |
| Brock2019 | Brock | 2019 | An Antimicrobial Stewardship Intervention Improves A ... e to Standar… | Quality improvement / stewardship intervention study; no TTP variable measured or analyzed. |
| Buis2023 | Buis | 2023 | Comparative effectiveness of beta-lactams for empiric ... ptible Stap… | TTP only appears in a cited reference, not measured or analyzed in this study. Duration of bacteraemia is a different e… |
| Casapao2017 | Casapao | 2017 | Early Administration of Adjuvant beta-Lactam Thera ... lococcus aureu… | No mention of time-to-positivity anywhere in text; only duration-of-bacteremia exposure analyzed. |
| Cheng2021 | Cheng | 2021 | Adjunctive Daptomycin in the Treatment of Methicilli ... ble Staphylo… | Full DASH RCT paper. Duration of bacteremia is not TTP (time-to-positivity = time from incubation to detection). No TTP… |
| Chong2016 | Chong | 2016 | Vancomycin-resistant Enterococcal Bloodstream Infect ... Hematologic … | Focus on daptomycin MIC, not TTP. No time-to-positivity measurements reported. |
| Davis2016 | Davis | 2016 | Combination of Vancomycin and β-Lactam Therapy for M ... s aureus Bac… | Duration of bacteremia (time-to-negative-culture) is reported, not TTP (time from incubation to positive signal). No TT… |
| DiazGranados2005 | DiazGranados | 2005 | Impact of vancomycin resistance on mortality among patients with neut… | Duration of bacteremia (positive-to-negative culture interval) is conceptually different from TTP (time from incubation… |
| Eichenberger2023 | Eichenberger | 2023 | Management and outcomes of heart transplant c ... ith bloodstream inf… | No time-to-positivity of blood culture measured/analyzed. Duration of bacteremia is a distinct metric. |
| Fong2009 | Fong | 2009 | Clinical features and treatment outcomes of vancomyci ... ermediate s… | Compares 'duration of culture positivity' (length of bacteremia in days) - this is bacteremia duration, NOT time to fir… |
| Fournier2019 | Fournier | 2019 | Risk of midline catheter-related bloodstream infections in medical an… | Extracted text file (127 lines) contains only an unrelated vascular access conference proceedings, not the Fournier ful… |
| Geriak2019 | Geriak | 2019 | Clinical Data on Daptomycin plus Ceftaroline versus ... e Treatment o… | Pilot RCT with mortality outcome but TTP of blood culture not measured/analyzed; the bacteremia duration variable is cl… |
| Girometti2014 | Girometti | 2014 | Klebsiella pneumoniae bloodstream infection epidemiology and impact o… | Strong mortality outcome study but TTP of blood culture not measured or analyzed. |
| Hackney2019 | Hackney | 2019 | Risk factors and outcomes of vancomycin-resistant ... coccal bloodstr… | TTP not measured. Compares VRE vs VSE outcomes. |
| Hamad2020 | Hamad | 2020 | Outcomes of outpatient parenteral antimicrobial ther ... cus aureus b… | TTP not measured. Compares antibiotic regimens, duration of bacteremia reported but no TTP. |
| Hendriks2024 | Hendriks | 2024 | Low-Risk Staphylococcus aureus Bacteremia Patient ... utine Diagnosti… | Study evaluates omission of routine imaging, not TTP. No time-to-positivity analyzed. |
| Ingram2021 | Ingram | 2021 | Laboratory and clinical impacts of an overnight laboratory service | Exposure is overnight lab service, not TTP. TTP reported only descriptively for group balance. Mortality not analyzed a… |
| Jang2025 | Jang | 2025 | Clinical Implications of the Skip Phenomenon in Patients with Persist… | Study examines skip phenomenon and bacteremia duration, not time-to-positivity of initial blood culture. |
| Jeon2024 | Jeon | 2024 | Thirty-Day Mortality of Persistent Methicillin-Resist ... coccus aure… | TTP of blood culture not measured. Bacteremia duration (days persistent) is reported, not time-to-positivity of initial… |
| Johnson2003 | Johnson | 2003 | Staphylococcus aureus bacteremia - compliance with standard treatment… | No mention of time to positivity. Focus on treatment compliance and predictors of relapse. |
| Jr1997 | White | 1997 | Effects of requiring prior authorization for sele ... ntimicrobials -… | Antimicrobial stewardship policy study; no TTP, no BSI-specific cohort analysis. Filename author parsing issue (Jr = Wh… |
| KalnUnuvar2020 | Kalın-Ünüvar | 2020 | Retrospective evaluation of positive blood culture of bacteremic case… | Turkish-language article. No TTP measurement. Descriptive only. |
| Kamboj2019 | Kamboj | 2019 | Impact of Empiric Treatment for Vancomycin-Resistan ... tients Early … | No TTP of blood culture measured/analyzed. |
| Kang2020 | Kang | 2020 | A Prospective Cohort Study of Durations of Staphyloco ... ng to Diffe… | Duration of bacteremia (time to negative culture) is a different concept than TTP (incubation time to flag positive). N… |
| Kaya2025 | Kaya | 2025 | Infections among adults hospitalized in intensive car ... the southea… | Cultures include all sites (not BSI-specific). 'Time to positivity' refers to ICU-stay timing of infection onset, not b… |
| Keighley2019 | Keighley | 2019 | Candidaemia and a risk predictive model for overall mortality - A pro… | Candidemia mortality predictive model paper; TTP not measured/analyzed. (TTP from same dataset reported separately in K… |
| Khosrovaneh2005 | Khosrovaneh | 2005 | Favorable prognosis of Staphylococcus aureus b ... ia originating fro… | Reports duration of bacteremia in days, not blood culture time-to-positivity. No TTP measurement. |
| Kim2023_a | Kim | 2023 | 1-s2.0-S1684118223001317-main | Duplicate of Kim2023_b (same file, identical md5). Exposure is bacteremia duration in days, not blood culture TTP. TTP … |
| Koh2025_a | Koh | 2025 | 1-s2.0-S1876034125001789-main | Duplicate of Koh2025_b (identical md5). No TTP analysis or measurement; focus is on antibiotic choice and source contro… |
| Kuehl2020 | Kuehl | 2020 | Defining persistent Staphylococcus aureus bacteraemia - secondary ana… | Analyzes duration of bacteraemia (days of persistent positive blood cultures under therapy), NOT time to blood culture … |
| Lecomte2024 | Lecomte | 2024 | Comparative effectiveness of empirical antibiotic ... docarditis - A … | Analyzes duration of bacteraemia (DOB), not TTP. Compares empirical antibiotic regimens. No TTP measured. |
| Lee2017 | Lee | 2017 | Implementation of a cefazolin-based stewardship pathwa ... s bloodstr… | Quasi-experimental before/after study of stewardship pathway; outcomes are duration of bacteraemia in days, not time-to… |
| Levine1991 | Levine | 1991 | Slow response to vancomycin or vancomycin plus rifampin in methicilli… | Cohort analysis of RCT focused on duration of bacteremia (days to clearance), not TTP of blood culture. |
| Li2014 | Li | 2014 | Comparison of cefazolin versus oxacillin for treatment ... ed bactere… | Antibiotic comparison study; no TTP measured or analyzed. |
| Li2025 | Li | 2025 | Time Is of the Essence - Impact of the BioFire FilmArray BCID2 Panel … | Study evaluates rapid diagnostic panel impact; 'time' refers to therapy escalation timing, not blood culture TTP. |
| Maor2009 | Maor | 2009 | Clinical features of heteroresistant vancomycin-inter ... bacteremia … | Paper measures duration of bacteremia (days from first positive to first negative), not time to positivity (TTP). No TT… |
| Mave2009 | Mave | 2009 | Vancomycin-resistant enterococcal bacteraemia - Is daptomycin as effe… | No mention of TTP/time to blood culture positivity; study compares drug treatments and reports duration of bacteremia (… |
| Mohamed2022 | Mohamed | 2022 | Ceftriaxone versus cefazolin for the treatment of methicillin-suscept… | Conference abstract; no TTP measured/reported |
| Molina2022 | Molina | 2022 | Comparison of Sequential Dalbavancin With Standard-of-Care Treatment … | No TTP measured; reports duration of bacteremia (days) which is not TTP |
| Najeeb2026 | Najeeb | 2026 | Etiology, antimicrobial resistance, and outcomes of bloodstream infec… | No time-to-positivity measured/reported. Only culture positivity rate, no TTP analysis. |
| Nori2021 | Nori | 2021 | Bacterial and fungal coinfections in COVID-19 patients hospitalized d… | Reported 'time to culture positivity 6-7 days' is interval from COVID PCR to positive culture, not the in-incubator TTP… |
| Ortwine2019 | Ortwine | 2019 | Relationship Status between Vancomycin Loading Dos ... Treatment Fail… | Exposure is vancomycin loading dose, not TTP. TTP not measured or analyzed. |
| Patel2023 | Patel | 2023 | Outcomes of daptomycin plus ceftaroline versus alter ... istent methi… | Duration of bacteraemia (days) reported, not TTP of blood cultures. No TTP measurement. |
| Pegu2025 | Pegu | 2025 | A Prospective Observational Study on the Clinical and ... alysis Pati… | Catheter dwell time analyzed but not blood culture TTP. |
| Pogue2014 | Pogue | 2014 | Automated alerts coupled with antimicrobial stewards ... decreases in… | Time to appropriate therapy (TTAT), not time to blood culture positivity (TTP). Quasi-experimental before/after design. |
| Savage2019 | Savage | 2019 | Evaluation of oral antibiotic stepdown therapy for ... ent of gram-ne… | IDWeek 2019 conference abstract; study exposure is timing of IV->PO transition, not TTP. |
| Schaffer2023 | Schaffer | 2023 | Clinical Outcomes in Patients with Bacteremia and ... Ventricular Ass… | Exposure is duration of bacteremia (persistent bacteremia), not time-to-positivity of the initial culture. Does not mee… |
| Shah2024 | Shah | 2024 | Carbapenem combination therapy versus standard of care for persistent… | Compares treatment regimens on time-to-clearance and mortality; TTP of initial blood culture is not measured/analyzed a… |
| Spaziante2020 | Spaziante | 2020 | Gram-negative septic thrombosis in critically ill patients - A retros… | Exposure is duration/persistence of bacteremia, not TTP of blood culture. Excluded as no_ttp. |
| Stevens2026 | Stevens | 2026 | Effect of hypoalbuminemia on blood culture clearan ... s bacteremia m… | Conference abstract; exposure is hypoalbuminemia, outcome is blood culture clearance. TTP not measured/analyzed. |
| Suleyman2017 | Suleyman | 2017 | Comparison of daptomycin and linezolid in the tre ... comycin-resista… | TTP (time to BC positivity) not measured. Duration of bacteremia (time to clearance) is the temporal measure - differen… |
| Tatarelli2015 | Tatarelli | 2015 | Efficacy of daptomycin lock therapy in the treatment of bloodstream i… | Small case series (n=8); no TTP measured. Also wrong_design (case series, n<10 borderline) |
| Thwaites2018 | Thwaites | 2018 | Adjunctive rifampicin to reduce early mortality from staphylococcus a… | RCT focused on rifampicin vs placebo; no TTP measurement or analysis |
| Volk2020 | Volk | 2020 | Interleukin (IL)-1beta and IL-10 host responses in pa ... staphylococ… | Cytokine biomarker study; TTP not measured or analyzed. Excluded as no_ttp. |
| Wang2023 | Wang | 2023 | Characteristics, Outcomes, and Clinical Indicators of ... tients with… | TTP/time to positivity not measured or analyzed. Risk factor analysis is for mortality with non-TTP predictors. |
| Wu2025 | Wu | 2025 | Incidence, Clinical Characteristics and Outcomes of Per ... Chinese T… | Outcome is persistence (>48h bacteremia) but TTP itself not measured/analyzed. Persistent bacteremia is defined by dura… |
| Yetukuri2024 | Yetukuri | 2024 | Impact of rapid blood culture identificationPCR p ... iotic use in me… | Study compares pre/post implementation of BCID PCR panel. No time to positivity reported or analyzed as predictor. |

### `no_assoc` (54 studies) — TTP and outcome both present, but no quantitative TTP↔outcome association (descriptive only, BC-system comparison, diagnostic study only)

| doc_id | Author | Year | Title (short) | Specific reason |
|---|---|---:|---|---|
| Ahn2023 | Ahn | 2023 | Incidence and short-term outcomes of central line-rela ... ted to the… | Differential time to positivity used only as a definitional cutoff for CRBSI diagnosis, not analyzed as a quantitative … |
| Ali2026 | Ali | 2026 | Catheter‑related bloodstream infections and risk facto ... intensive … | Neonatal/pediatric-only study. DTP only used as a CRBSI definitional criterion, not analyzed as quantitative TTP predic… |
| Andry2022 | Andry | 2022 | Epidemiology and outcome of occult bacteremia in pat ... arged from e… | Study focuses on occult bacteremia clinical reassessment after discharge. TTP mentioned only in background citation; no… |
| Arendrup2011 | Arendrup | 2011 | Diagnostic issues, clinical characteristics, and outcomes for patient… | TTP and mortality both reported but only descriptively; no OR/HR/2x2 for TTP vs outcome. Mortality univariate analysis … |
| Bolukcu2018 | Bolukcu | 2018 | Prospective assessment of blood cultures which were sent to the clini… | Turkish-language paper (with English abstract). Outcome is BC positivity itself (cases vs controls); pathogen distribut… |
| Bouza2013 | Bouza | 2013 | Catheter-related bloodstream infections caused by Gram-negative bacte… | TTP analyzed as a predictor of GN-CRBSI vs non-GN-CRBSI, not as predictor of mortality with OR/HR/CI. Mortality table s… |
| Cabello2010 | Sabatier | 2014 | Optimización en la técnica de medida de la presión ... de contrast… | PDF file Cabello2010.txt actually contains Sabatier et al 2014 (Med Intensiva). Trial compares diagnostic strategies; D… |
| Chatelard2023 | Chatelard | 2023 | Shortening identification times - comparative observational study of … | Comparative study of three early BC testing protocols (multiplex PCR vs multitest vs reference). Reports BC positivity-… |
| Chen2013 | Chen | 2013 | Associated clinical characteristics of patients with candidemia among… | TTP and mortality both reported; multivariable logistic models examine TTP-to-species (not TTP-to-outcome). Descriptive… |
| Chen2015 | Chen | 2015 | Clinical significance of time to positivity for yeast in candidemia | TTP categorized and mortality compared descriptively only (chi-square, NS). Multivariable model targets TTP-to-species,… |
| Davies2023 | Davies | 2023 | An assessment of the downstream implications of blood culture collect… | Pre-analytical workflow study. They analyze transit time vs outcome (LoS, mortality), not classical TTP vs outcome. Tim… |
| Deliberato2012 | Deliberato | 2012 | Catheter related bloodstream infection (CR-BSI) ... g the decision to… | DTP used as diagnostic criterion only. Mortality comparisons stratified by diagnostic method/group, not by TTP value. N… |
| Doi2023 | Sasaki | 2023 | Staphylococcus lugdunensis bacteremia - clinical implications of sing… | TTP descriptively reported by group (single vs multiple positive sets); no quantitative TTP-by-outcome association (no … |
| Eden2022 | Eden | 2022 | Safety and efficacy of the Seraph 100 Microbind Affin ... bacteria fr… | TTP used only as efficacy surrogate (bacterial load reduction) of the device, not as a predictor of clinical outcome. N… |
| Fernandez2009 | Fernandez | 2009 | Time to positive culture and identification for Candida blood stream … | Primarily a microbiology/TTP-by-species descriptive paper. Single t-test of time-to-appropriate-therapy by survival; no… |
| Fihman2021 | Fihman | 2021 | Blood cultures for the diagnosis of infective endocarditis - What is … | Study aim is whether prolonged incubation (>5d) helps IE diagnosis. TTP described per pathogen but not analyzed vs any … |
| Gaifer2022 | Gaifer | 2022 | Risk factors, outcomes and time to detect positive blood culture amon… | Exposure analyzed is bacteremia status (positive vs negative blood culture), not TTP. TTP described descriptively only;… |
| GarciaVazquez2013 | Garcia-Vazquez | 2013 | When is coagulase-negative Staphylococcus bacteraemia clinically sign… | Outcome is CDC/NHSN-defined clinically-significant bacteraemia classification, not mortality/persistent bacteraemia/cli… |
| Ghrenassia2019 | Ghrenassia | 2019 | Candidemia in critically ill immunocompromised patients - report of a… | TTP reported but not analyzed against mortality. 'Days to first AF therapy' (time to treatment) was in Table 1 but not … |
| Giannella2021 | Giannella | 2021 | Antimicrobial and resource utilization with T2 m ... fections - syste… | Diagnostic methods comparison meta-analysis; TTP not the exposure in any patient-level outcome analysis. |
| Guo2022 | Guo | 2022 | Impact of satellite blood culture on early diagnosis of sepsis | Method comparison study (satellite vs laboratory blood culture). TTP reported but only compared between methods, not an… |
| Hitzenbichler2017 | Hitzenbichler | 2017 | Clinical significance of coagulase-negative ... than S. epidermidis b… | TTP used solely for contamination vs infection discrimination, not for predicting mortality/clinical outcomes. Only 1 d… |
| Hwang2025 | Hwang | 2025 | Coccidioides Fungemia in Central California - A 10-Years Experience | Small case series (n=11), descriptive only, no quantitative TTP-outcome association. |
| Kim2021 | Kim | 2021 | Characteristics and clinical outcomes of culture-negat ... re-positiv… | TTP↔mortality assessed but explicitly null and only as descriptive median comparison; no formal regression or HR with C… |
| Kitagawa2025 | Kitagawa | 2025 | Clinical diagnostic performance of droplet digita ... richia coli blo… | TTP reported and compared by septic shock status and ddPCR status, but no quantitative TTP↔clinical outcome (mortality/… |
| Lockwood2016 | Lockwood | 2016 | Integrating rapid diagnostics and antimicrobial s ... ty hospitals im… | ASP intervention study; TTP is reference timepoint only, no quantitative TTP-outcome association reported |
| MacVane2016 | MacVane | 2016 | Impact of a rapid multiplex polymerase chain react ... utcomes in pat… | ASP/rapid diagnostic intervention study; TTP reported as descriptive characteristic, no TTP-outcome quantitative associ… |
| Medina2025 | Diez de Medina | 2025 | Invasive infections by Capnocytophaga spp. in immunocompromised patie… | Small case series (n=9) with TTP reported but no quantitative TTP-outcome association; zero mortality events; in Spanis… |
| Nakagawa2018 | Nakagawa | 2018 | Optimization of antimicrobial therapy in vancomyc ... bacteraemia usi… | Study evaluates rapid diagnostic assay impact on time-to-therapy and LOS. No TTP↔clinical outcome regression. |
| Nieuwkoop2010 | van Nieuwkoop | 2010 | Procalcitonin reflects bacteremia and bacterial load in urosepsis syn… | Main outcome is PCT predicting bacteremia presence. TTP analyzed only vs PCT biomarker, not vs clinical outcome. |
| Paiva2016 | Paiva | 2016 | Characteristics and risk factors for 28-day mortality of hospital acq… | TTP reported descriptively comparing fungemia vs bacteremia. TTP not entered into mortality risk-factor analyses; no qu… |
| Pardo2014 | Pardo | 2014 | Time to positivity of blood cultures supports antibiotic de-escalatio… | Descriptive TTP distribution and test characteristics for de-escalation decisions. Mortality only listed for 15 late-de… |
| Raad2009 | Raad | 2009 | Management of the catheter in documented catheter-related coagulase-n… | TTP only used as definition criterion (<12h differential) for CRBSI diagnosis; no quantitative TTP-outcome analysis. |
| Romann2023 | Romann | 2023 | Factors impacting the pre-Analytical quality of blood cultures-Analys… | Pre-analytical methods paper; TTP treated as outcome, not predictor of clinical outcomes |
| Ruschulte2009 | Ruschulte | 2009 | Prevention of central venous catheter related in ... gluconate impreg… | RCT of dressings; TTP used only as diagnostic tool, no TTP-outcome quantitative analysis |
| Sabatier2015 | Sabatier | 2015 | Blood culture differential time to positivity ena ... atheter-related… | RCT of DTP-guided catheter management strategy; TTP is the diagnostic tool, not the exposure for clinical outcome |
| Seitz2022 | Seitz | 2022 | Rapid Detection of Bacterial and Fungal Pathogens Using the T2MR vers… | Diagnostic test comparison (T2MR vs blood culture); TTP not analyzed as a predictor of clinical outcome. |
| Sepulveda2020 | Sepulveda | 2020 | Bacteremia and blood culture utilization during covid-19 surge in New… | TTP reported descriptively to inform laboratory workflow change. No quantitative TTP-outcome (mortality/clinical failur… |
| Shemanski2019 | Shemanski | 2019 | Centralized Communication of Blood Culture Results Leveraging Antimic… | Quasi-experimental stewardship intervention; TTP used only as time-zero anchor, not analyzed as exposure for clinical o… |
| Shepard2022 | Shepard | 2022 | Bartonella quintana Infection in People Experiencing Homelessness in … | Small descriptive case series; TTP reported only as mean to motivate prolonged incubation. No quantitative TTP-outcome … |
| Sibar2026 | Sibar | 2026 | Catheter-related bloodstream infections in hemodialy ... , antimicrob… | DTP reported only descriptively (presence/absence per IDSA criteria for CRBSI diagnosis). No quantitative DTP↔outcome a… |
| Simpson1999 | Simpson | 1999 | A comparison of lysis centrifugation, pour plate, ... nal blood cultu… | Methods comparison paper. TTP reported per BC method; mortality stratified by quantitative bacterial counts, not by TTP… |
| Sivakumar2020 | Jayaweera | 2020 | Asymptomatic central line-associated bloo ... indwelling central veno… | Pediatric-only study. DTP used only diagnostically (categorical classification). No quantitative DTP↔outcome analysis. |
| Steuber2021 | Steuber | 2021 | Comparison of blood cultures versus T2 Candida Panel in management of… | BC system comparison study (T2 Candida Panel vs BC). Time-to-detection compared between methods, not analyzed as a cont… |
| TalaIghil2025 | Tala-Ighil | 2025 | Epidemiology and Prognostic Factors Associated ... -Year Data From a … | TTP described descriptively by mold genus but not analyzed as a predictor of mortality. Multivariable model omits TTP. … |
| Verroken2019 | Verroken | 2019 | The Impact of a Rapid Molecular Identification Te ... s from Critical… | Pre-post intervention study of FA-BCID. TTP not measured as exposure; outcome was time-to-treatment, not clinical outco… |
| Walsh2024 | Walsh | 2024 | Prospective observational pilot study of the T2Resis ... for detectio… | Diagnostic accuracy / pilot study of T2Resistance panel. TTP comparison is between rapid molecular test and BC, not as … |
| Wong2016_a | Wong | 2016 | Comparative effectiveness of beta-lactam versus vanco ... with methic… | TTP reported descriptively as baseline characteristic; no quantitative TTP-outcome association analyzed. |
| Wong2016_b | Wong | 2016 | Comparison of outcomes in patients with methicillin-s ... s-lactam vs… | TTP reported only as descriptive baseline characteristic. No TTP-outcome quantitative analysis. Likely overlaps with Wo… |
| Xu2026 | Xu | 2026 | Retrospective analysis of the epidemiological character ... nd constr… | Logistic regression uses TTP to predict candidemia diagnosis (classification), not a clinical outcome (mortality/persis… |
| Yanai2018 | Yanai | 2018 | Retrospective evaluation of the clinical characteristics associated w… | TTP compared between bacteremia and contamination groups, which is a microbiologic classification, not a clinical outco… |
| Zhang2017 | Zhang | 2017 | Bacteraemia due to AmpC β-lactamase-producing Escher ... ized cancer … | TTP analyzed as a microbiologic marker (predicting AmpC) and compared between resistance groups; no quantitative TTP-cu… |
| Zhang2024 | Zhang | 2024 | Clinical manifestations and treatment of candidemia caused by differe… | TTP compared between Candida species only; not analyzed as predictor of mortality or other clinical outcome. No regress… |
| Zornitzki2024 | Zornitzki | 2024 | Rate and predictors of blood culture positivity after antibiotic admi… | Study examines TIME-FROM-ANTIBIOTIC-TO-BC, not blood-culture TTP. No TTP/TTP-categorized mortality model. |

### `no_outcome` (29 studies) — No clinical outcome reported — methods/microbiology paper only

| doc_id | Author | Year | Title (short) | Specific reason |
|---|---|---:|---|---|
| Appelbaum1983 | Appelbaum | 1983 | Enhanced detection of bacteremia with a new BACTEC resin blood cultur… | Microbiology methods paper comparing two BACTEC blood culture media. Reports TTP as a laboratory performance metric. No… |
| Bailly2016 | Bailly | 2016 | Impact of Systemic Antifungal Therapy on the Detection of Candida Spe… | TTP is the dependent variable (modeled vs SAT and bottle type), not the exposure. No TTP-mortality or TTP-clearance ass… |
| BenAmi2008 | Ben-Ami | 2008 | Time to Blood Culture Positivity as a Marker for Catheter-Related Can… | TTP analyzed as diagnostic marker for catheter-related candidemia (source attribution). No clinical outcome (mortality/… |
| Coullioud1993_a | Coullioud | 1993 | Prospective multicentric study of the etiology of 1051 ... s. CEMIC (… | Authors state: 'Neither the source of bacteremia nor the death of the patient had to be recorded.' Only TTP-vs-CDC-sign… |
| Crump2011 | Crump | 2011 | Controlled comparison of BacT - Alert MB system, man ... ator 10 syst… | Blood culture system comparison study only - no patient outcomes assessed vs TTP. |
| Deawtrakulchai2022 | Deawtrakulchai | 2022 | The comparative accuracy of pooled vs. indi ... pling methods for dia… | Diagnostic accuracy / method comparison: pooled vs individual blood culture sampling. Outcome is sensitivity/specificit… |
| DiazNavarro2023 | Diaz-Navarro | 2023 | Understanding the diagnosis of catheter-relat ... toring of biofilm g… | Microbiology/in vitro methods study; not a clinical cohort. |
| Hajjar2023 | Hajjar | 2023 | Blood culture collection practices in NICU; A national survey | National survey of NICU practices, not a patient cohort. No outcomes measured. |
| Hang2024 | Hang | 2024 | Comparison and evaluation of neutralization of clinic ... gents using… | In vitro simulation study using ATCC reference strains, no patients. Lab/methods comparison. |
| Jawaheer1997 | Jawaheer | 1997 | Blood culture volume and detection of coagulase negative staphylococc… | Methods paper on blood culture volume vs TTP; no TTP-clinical outcome analysis. Pediatric/neonatal. |
| Kaasch2014 | Kaasch | 2014 | Differential time to positivity is not predictive f ... Staphylococcu… | Diagnostic accuracy study for DTP vs CRBSI diagnosis; no clinical outcome (mortality, persistence, etc.) analyzed again… |
| Lai2011 | Lai | 2011 | Time to blood culture positivity as a predictor of methicillin resist… | Letter to editor. TTP analyzed only for predicting methicillin resistance (microbiologic), not clinical outcome. |
| Lau2010 | Lau | 2010 | Comparison of whole blood, serum, and plasma for early detection of c… | Microbiologic methods paper comparing PCR vs blood culture for candidemia detection. No TTP-clinical outcome analysis. |
| Ling2021 | Ling | 2021 | Impact of delays to incubation and storage temperature on blood cultu… | Pre-clinical/laboratory methodology study with no patient outcomes. |
| Malgrange2001 | Malgrange | 2001 | Validity of Earlier Positivity o ... ultures for Diagnosing Catheter-… | Diagnostic accuracy study - outcome is CRB diagnosis (microbiological classification), not clinical outcome (mortality/… |
| Mitteregger2013 | Mitteregger | 2013 | Neutralization of antimicrobial substances in new BacT - Alert FA and… | In vitro blood culture system evaluation, no patient outcomes |
| Mushtaq2016 | Mushtaq | 2016 | Clinical significance of coryneform Gram-positive ... etry and their … | TTP analyzed but outcome is healthcare team treatment decision, not a patient clinical outcome. Many isolates considere… |
| Ombelet2021 | Ombelet | 2021 | Nonautomated blood cultures in a low-resource setting - Optimizing th… | Methods paper on optimizing blind subculture timing for B. pseudomallei detection. No patient-level clinical outcomes. |
| Oppenheim1998 | Oppenheim | 1998 | The use of continuous monitoring blood culture systems in the diagnos… | Methods study evaluating TTP as diagnostic for catheter-related sepsis. No mortality/failure/clinical outcome. |
| Pandit2021 | Pandit | 2021 | Catheter-related blood stream infections - prevalence, risk factors a… | Uses DTP only for diagnosing CRBSI. No clinical outcomes (mortality, failure) analyzed vs TTP. |
| Passerini2009 | Passerini | 2009 | Interference of antibiotic therapy on blood cult ... sitivity - Analy… | Microbiology paper examining factors affecting TTP. No clinical outcomes (mortality, failure) analyzed. |
| Rai2023 | Rai | 2023 | Surveillance of central line associated bloodstream in ... n of curre… | Surveillance/methods comparison study (CDC vs modified criteria for CLABSI). No TTP-clinical outcome association. |
| Ransom2021 | Ransom | 2021 | Evaluation of optimal blood culture incubation time ... results from … | Methods paper assessing optimal incubation time; descriptive TTP distributions only, no TTP-outcome quantitative analys… |
| Rijnders2001 | Rijnders | 2001 | Difference in time to positivity of hub-blood versus non ... of cathe… | Diagnostic accuracy study for DTTP→CR-BSI diagnosis only; only n=3 CR-BSI; no mortality/clinical failure analysis |
| RodriguezAranda2011 | Rodriguez-Aranda | 2011 | Endoluminal colonization as a risk factor ... cal catheter-related bl… | TTP analyzed as a diagnostic predictor of subsequent CRBSI episodes, not as predictor of clinical outcome in BSI patien… |
| Solarte2026 | Micolta Solarte | 2026 | Real-life evaluation of supplemental anaer ... iagnosis and therapeut… | BC bottle comparison study. TTP compared between bottle types only, not associated with mortality/clinical failure. |
| Tabak2018 | Tabak | 2018 | Blood culture turnaround time in U.S. acute care hospitals and implic… | Microbiology/lab workflow paper. Reports lab turnaround times by organism but no patient-level clinical outcomes (morta… |
| Tanguy2005 | Tanguy | 2005 | Hub qualitative blood culture is useful for diagnosis of catheter-rel… | Diagnostic accuracy paper for CRBSI diagnosis; no quantitative TTP-clinical outcome (mortality/failure) analysis |
| Yoshida2024 | Yoshida | 2024 | Rapid differentiation of Staphylococcus aureu ... od cultures using t… | Microbiology methods paper - TTP used as predictor of organism identification, not clinical outcome. |

### `duplicate` (5 studies) — Duplicate of another paper (filename collision or republished)

| doc_id | Author | Year | Title (short) | Specific reason |
|---|---|---:|---|---|
| Bo2021 | Bo | 2021 | Relationship between time to positivity of blood culture with clinica… | DUPLICATE of Bo2011. The text file Bo2021.txt is byte-identical to Bo2011.txt (md5 75cab02bed3db7b35c9f8f644adf56c1). T… |
| Coullioud1993_b | Coullioud | 1993 | Prospective multicentric study of the etiology of 1051 bacteremic epi… | Duplicate of Coullioud1993_a (diff returns identical files, same line count). Would also be no_outcome on its own merit… |
| Kim2023_b | Kim | 2023 | Factors for mortality in patients with persistent Stap ... The import… | Duplicate of Kim2023_a (identical file md5 f032a4cef...). Also fails no_ttp criterion: exposure is duration in days, no… |
| Koh2025_b | Koh | 2025 | Risk factors for mortality and implications on therapy for Stenotroph… | Duplicate of Koh2025_a (identical file md5 b6bca7c84cb...). Also fails no_ttp criterion. |
| Mandolfo2020_b | Mandolfo | 2020 | mandolfo-et-al-2019-high-success-rate-in-salvage-of-catheter-related-… | Duplicate of Mandolfo2020_a (same JVA 2020 paper, DOI 10.1177/1129729819875323) |

### `not_bsi` (2 studies) — Population is not bloodstream infection

| doc_id | Author | Year | Title (short) | Specific reason |
|---|---|---:|---|---|
| Brehm2024 | Brehm | 2024 | The impact of direct inoculation of ascites into blood culture bottle… | Population is SBP/ascites cultures, not bloodstream infection. Excluded as not_bsi. |
| Vandresen2021 | Vandresen | 2021 | Associated factors of Acinetobacter baumannii complex in hospitalized… | Population is not bacteremia/BSI - samples were primarily tracheal aspirates, wounds. No blood culture TTP. Excluded as… |

---

## Notes on extraction methodology

1. **Strict inclusion** was applied: a paper must report a quantitative TTP↔outcome association (2x2 table by TTP category, OR/HR/RR with CI, or beta-per-hour with SE). Descriptive-only "TTP was X and mortality was Y" papers are coded `no_assoc`.
2. **Population must be BSI** (bacteremia, candidemia, or BSI confirmed by blood culture). Studies of pneumonia or UTI without BSI are coded `not_bsi`.
3. **Pediatric studies were retained** when they reported TTP↔outcome; flagged in `notes` for sensitivity analysis.
4. **Study design**: case reports (n<10), conference abstracts, narrative reviews, editorials, and study protocols are excluded as `wrong_design` even if they nominally meet the other criteria — these don't contribute valid effect estimates.
5. **Two studies were technically eligible but lacked enough numeric detail to extract** (no exact TTP descriptive statistics or no effect estimate). They were included with available data and `null` for unreported fields.
6. **QUIPS risk of bias** was scored across all 6 domains for every new study, with the overall judgment following QUIPS guidance (worst-domain-dominates, not arithmetic mean).
7. **Outcome enum constraint**: the Codebook permits only `mortality | persistent_bacteremia | microbiological_clearance | relapse`. Endocarditis (IE) and metastatic infection outcomes were mapped to `persistent_bacteremia` with the original outcome labeled in `outcome_definition` and `notes`. This matches the convention used for some baseline rows (e.g., Krus2021, Oldberg2021).

## Notable filename / file integrity issues encountered

- **`Barberán et al. 2010 - Predictive model …amputation.pdf`** actually contained the Martin-Gutiérrez et al. 2016 mixed-BSI TTP paper. Extracted under `study_id = MartinGutierrez2016` with a note.
- **`bo-et-al-2021-relationship-between-ti…hospital.pdf`** (slug-form filename) extracted to identical text as `Bo et al. 2011`. Treated as duplicate of Bo2011; user should verify whether the actual 2021 paper was downloaded or whether the file was mis-copied.
- **Several conference-abstract PDFs** turned out to contain abstract compilations (e.g., ECCMID poster books). The actual abstract was located inside but data were insufficient for inclusion.
- **`Coullioud1993_a` / `_b`, `Kim2023_a` / `_b`, `Koh2025_a` / `_b`, `Mandolfo2020_a` / `_b`** were filename duplicates (different filename in the source but identical content). The `_a` version was screened; `_b` marked as duplicate.
- **Five PDFs were duplicates of already-extracted baseline studies** (Álvarez 2012, Bläckberg 2022, Bläckberg 2023, Cillóniz 2017, Martínez 2006) — skipped without screening.
