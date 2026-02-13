# TTP Meta-Analysis Project Memory

## Project Overview

Bayesian meta-analysis investigating the association between blood culture **time to positivity (TTP)** and clinical outcomes in bacteremia. Short TTP (reflecting higher bacterial inocula) is hypothesized to predict worse outcomes.

**Primary outcomes:**
1. **Mortality** (all-cause, typically 30-day or in-hospital)
2. **Persistent bacteremia** (microbiological clearance failure)

## Data Files

### Main Database
- **File:** `TTP_MetaAnalysis_Extraction_Complete.xlsx`
- **Format:** Excel workbook with relational tables linked by `study_id`

### Sheets/Tables
| Sheet | Description | Rows |
|-------|-------------|------|
| `tbl_study` | Study-level metadata (author, year, country, ROB scores) | 57 |
| `tbl_population` | Population characteristics (pathogen, infection source, severity) | 57 |
| `tbl_ttp` | TTP measurement details (cutpoints, reporting format) | 57 |
| `tbl_outcomes` | Outcome data (2×2 tables, effect estimates, continuous TTP) | 88 |
| `tbl_es` | Placeholder for computed effect sizes (populated in R) | — |
| `Codebook` | Field definitions | — |

### Protocol Document
- **File:** `TTP_meta-analysis_database_and_packages.md`
- Contains database architecture, R package recommendations, prior specifications, and analytical notes.

## Data Loading

```r
library(tidyverse)
library(readxl)
library(janitor)

path <- "/Users/russelllewis/Desktop/ttp metaanalysis/TTP_MetaAnalysis_Extraction_Complete.xlsx"

tbl_study      <- read_excel(path, sheet = "tbl_study") |> clean_names()
tbl_population <- read_excel(path, sheet = "tbl_population") |> clean_names()
tbl_ttp        <- read_excel(path, sheet = "tbl_ttp") |> clean_names()
tbl_outcomes   <- read_excel(path, sheet = "tbl_outcomes") |> clean_names()
```

## Data Cleaning Notes

### Key Cleaning Steps
1. **Remove `[NON-PICO]` rows** — flagged in `notes` column (13 rows)
2. **Harmonize outcome types:**
   - `mortality`, `in_hospital_mortality` → `"mortality"`
   - `persistent_bacteremia`, `bacteremia_clearance`, `microbiological_clearance` → `"persistent_bacteremia"`
3. **Effect size source classification:**
   - `reported_adjusted` — preferred (adjusted OR/HR/RR with CI)
   - `reported_unadjusted` — unadjusted OR/HR/RR with CI
   - `two_by_two` — computed from 2×2 table via `metafor::escalc()`
   - `continuous_converted` — OR per hour TTP (different scale)
   - `insufficient_data` — excluded (22 rows)

### Deduplication Rules
- Prefer **adjusted** over unadjusted when both exist (Cilloniz2017, Hou2023)
- Remove **Melling2019 row 2** (extreme sparse-cell OR = 1722)
- Keep **Marco2025** duplicate (two genuinely different subgroups)

### Moderator Join Issue (RESOLVED)
- `arm_id` values in `tbl_outcomes` don't match `tbl_population` (which uses `"all"`)
- **Solution:** Join on `study_id` only (one population row per study)

## Final Dataset (`tbl_es`)

- **42 effect sizes** from 40 unique studies
- **33 mortality** (median OR = 2.64)
- **9 persistent bacteremia** (median OR = 2.02)
- 2 continuous TTP effects (OR per hour) — kept separate

### Moderator Completeness
| Moderator | % Complete |
|-----------|------------|
| `pathogen_class` | 100% |
| `organism_saureus` | 100% |
| `rob_overall` | 100% |
| `blood_culture_system_clean` | 97.6% |
| `ttp_cutpoint_hours` | 76.2% |
| `source_control` | 42.9% (too sparse) |

## Key Results Summary

### Mortality (k=33)

| Analysis | Pooled OR | 95% CI/CrI | tau |
|----------|-----------|------------|-----|
| Frequentist REML | 2.18 | 1.72–2.75 | 0.57 |
| **Bayesian (primary)** | **2.14** | **1.69–2.79** | **0.58** |
| Trim-and-fill adjusted | 1.50 | 1.15–1.96 | 0.80 |
| Sensitivity (excl. Ji2020) | 2.00 | 1.61–2.47 | 0.50 |

- **P(OR > 1) = 100%** — posterior certainty short TTP increases mortality
- **I² = 99.3%** — substantial heterogeneity
- **Egger's test p < 0.0001** — significant funnel asymmetry
- **Prior sensitivity:** OR range 1.99–2.15 (±4%) — insensitive to prior choice
- **Meta-regression:** No moderator explained heterogeneity (pathogen class, S. aureus, ROB, blood culture system)

### Persistent Bacteremia (k=7)

| Analysis | Pooled OR | 95% CI/CrI | tau |
|----------|-----------|------------|-----|
| Frequentist REML | 7.24 | 2.07–25.38 | 1.61 |
| **Bayesian (primary)** | **4.02** | **1.08–11.11** | **1.61** |
| Sensitivity (excl. outliers, k=5) | 2.80 | 1.13–6.92 | 0.92 |

- **P(OR > 1) = 97.9%** — strong but not decisive
- Estimate heavily influenced by **Melling2019** (OR=37) and **Kassis2009** (OR=75) — sparse 2×2 cells
- **Prior sensitivity:** OR range 1.38–5.84 — more sensitive than mortality (small k)

## Bayesian Model Specification

```r
# Primary model (brms)
fit <- brm(
  yi | se(sei) ~ 1 + (1 | study_id),
  data = es_data,
  prior = c(
    prior(normal(0, 1), class = "Intercept"),
    prior(cauchy(0, 0.5), class = "sd")
  ),
  backend = "rstan",  # or "cmdstanr" if available

  chains = 4, iter = 4000, warmup = 1000,
  control = list(adapt_delta = 0.95)
)
```

### Prior Rationale
- **Intercept:** `Normal(0, 1)` — 95% prior mass OR 0.14–7.4
- **tau:** `Half-Cauchy(0, 0.5)` — moderate heterogeneity allowed

## Key Fitted Model Objects (in R session)

| Object | Description |
|--------|-------------|
| `fit_mort` | Bayesian RE mortality (k=33) |
| `fit_mort_sens` | Bayesian RE mortality excl. Ji2020 |
| `fit_pb` | Bayesian RE persistent bacteremia (k=7) |
| `fit_pb_sens` | Bayesian RE PB excl. outliers (k=5) |
| `fit_pathogen`, `fit_saureus`, `fit_rob`, `fit_bcs` | Meta-regression models (mortality) |
| `rma_mort`, `rma_pb` | Frequentist REML models |
| `tf_mort_L` | Trim-and-fill (mortality) |
| `sel_mort`, `sel_mort_beta`, `sel_mort_negexp` | Frequentist selection models (metafor) |
| `fit_selection` | Bayesian selection model (Stan, uniform prior on δ) |
| `fit_selection_skep` | Bayesian selection model (Stan, skeptical prior δ ~ Beta(2,5)) |

## Report Status

- **File:** `TTP_Meta_Analysis_Report.qmd` 
- **Status:** INCOMPLETE — truncates at line 340 mid-sentence in moderator completeness table
- **Completed sections:**
  - Introduction & Background ✓
  - Data Loading & Preparation ✓
  - Effect Size Computation ✓
  - Descriptive Summary (partial)
- **Missing sections:**
  - Primary Meta-Analysis (Bayesian + Frequentist pooled estimates)
  - Forest Plots
  - Publication Bias Assessment
  - Sensitivity Analyses
  - Meta-Regression
  - Discussion/Conclusions

## Publication Bias: Bayesian Selection Models

**NEW ANALYSIS** (completed 2026-02-13): Fully Bayesian selection models using Stan

### Frequentist vs Bayesian Selection Models

| Model | Pooled OR | 95% CI/CrI | Selection δ | Significant? |
|-------|-----------|------------|-------------|--------------|
| Unadjusted (REML) | 2.18 | 1.72–2.75 | — | Yes |
| Trim-and-Fill | 1.50 | 1.15–1.96 | — | Yes |
| **Freq. Step-function** | **1.09** | **0.67–1.79** | **0.037** | **No** |
| Bayesian Selection (uniform prior) | 2.14 | 1.70–2.78 | 0.84 | Yes |
| Bayesian Selection (skeptical prior) | 2.14 | 1.71–2.80 | 0.50 | Yes |

### Key Findings

1. **Frequentist step-function shows extreme adjustment** — δ = 0.037 means non-significant studies have only 3.7% publication probability; adjusted OR = 1.09 (non-significant)

2. **Bayesian models are robust to publication bias** — Even with skeptical priors, pooled OR remains ~2.14 with P(OR>1) = 100%

3. **Why the discrepancy?**
   - Only 3/33 studies (9%) are non-significant
   - Frequentist MLE pushes δ to extreme values with sparse data
   - Bayesian priors regularize estimates
   - 91% significance rate exceeds expectation even for OR=3.0 (~68% expected)

4. **Interpretation:** Some publication bias likely exists. True effect probably lies between OR 1.50 (trim-and-fill) and 2.14 (unadjusted). The frequentist step-function (1.09) likely overadjusts.

5. **Conclusion:** Short TTP robustly associated with mortality across all Bayesian approaches, though exact magnitude uncertain due to probable publication bias.

### Stan Model Implementation

Custom Stan model implements step-function selection:
- Prior on μ: Normal(0, 1)
- Prior on τ: Half-Cauchy(0, 0.5)
- Prior on δ: Beta(2, 5) for skeptical version (mean = 0.29)
- Selection mechanism: `target += log(delta)` for non-significant studies

## Packages Required

```r
# Core
library(tidyverse)
library(readxl)
library(janitor)
library(metafor)
library(brms)

# Bayesian diagnostics
library(posterior)
library(bayesplot)
library(ggdist)

# Visualization
library(patchwork)

# Stan (for custom selection models)
library(rstan)
```

## Next Steps / TODO

1. **URGENT: Complete Quarto report** — file still truncated at line 340
   - Fix moderator completeness table
   - Add all primary analysis sections (pooled estimates, forest plots)
   - Add publication bias section with ALL models (funnel, Egger, trim-and-fill, frequentist selection, Bayesian selection)
   - Add sensitivity analyses
   - Add meta-regression results
   - Add discussion/conclusions
   
2. ~~Consider **Bayesian selection model**~~ ✓ COMPLETED — implemented via Stan

3. **Dose-response modeling** for continuous TTP studies (currently excluded from pooling)

4. **Manuscript preparation** — once report is complete, extract key tables/figures for publication
