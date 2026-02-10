# TTP & Antibiotic Failure Meta-Analysis: Database Structure and R Packages

**Protocol Reference — Database Design and Analytical Toolkit**
**Date:** February 2026

---

## 1. Database Architecture

The extraction database should be organized as a relational set of tables linked by `study_id`. This design separates study-level metadata from arm-level data and outcome-specific results, accommodating the heterogeneity in how primary studies report TTP associations.

### 1.1 Study Characteristics (`tbl_study`)

| Field | Type | Description |
|---|---|---|
| `study_id` | character | Unique identifier (e.g., `"AuthorYear"`) |
| `first_author` | character | First author surname |
| `pub_year` | integer | Publication year |
| `country` | character | Country of enrollment |
| `study_design` | factor | `prospective_cohort`, `retrospective_cohort`, `case_control` |
| `enrollment_start` | date | Start of enrollment period |
| `enrollment_end` | date | End of enrollment period |
| `single_center` | logical | Single- vs. multi-center |
| `n_centers` | integer | Number of centers (if multi-center) |
| `funding_source` | character | Industry, public, mixed, NR |
| `rob_domain_1` ... `rob_domain_n` | integer | Risk of bias domain scores (QUIPS tool recommended for prognostic factor studies) |
| `rob_overall` | factor | `low`, `moderate`, `high`, `critical` |
| `nos_score` | integer | Newcastle-Ottawa Scale total (if applicable) |

### 1.2 Population and Sample (`tbl_population`)

| Field | Type | Description |
|---|---|---|
| `study_id` | character | FK to `tbl_study` |
| `arm_id` | character | Subgroup identifier (e.g., `"gram_pos"`, `"all"`) |
| `n_total` | integer | Total sample size in this arm/subgroup |
| `age_mean` | numeric | Mean age (years) |
| `age_sd` | numeric | SD of age |
| `age_median` | numeric | Median age (if mean not reported) |
| `age_iqr_low` | numeric | 25th percentile |
| `age_iqr_high` | numeric | 75th percentile |
| `pct_male` | numeric | Percent male (0–100) |
| `pathogen_class` | factor | `gram_positive`, `gram_negative`, `mixed`, `fungal` |
| `pathogen_species` | character | Primary species (e.g., `"S. aureus"`, `"E. coli"`) |
| `pct_mrsa` | numeric | Percent MRSA (for S. aureus subgroups) |
| `infection_source` | factor | `endovascular`, `line_related`, `urinary`, `pulmonary`, `abdominal`, `skin_soft_tissue`, `osteoarticular`, `unknown`, `mixed` |
| `source_control` | factor | `achieved`, `not_achieved`, `mixed`, `not_applicable`, `NR` |
| `pct_icu` | numeric | Percent ICU at enrollment |
| `severity_score_type` | character | `APACHE_II`, `SOFA`, `Pitt`, `Charlson`, `other` |
| `severity_score_mean` | numeric | Mean severity score |
| `severity_score_median` | numeric | Median severity score |
| `pct_appropriate_empiric` | numeric | Percent receiving appropriate empiric therapy |
| `empiric_abx_definition` | character | How "appropriate" was defined |
| `blood_culture_system` | factor | `BacTALERT`, `BACTEC`, `other`, `NR` |
| `incubation_protocol` | character | Standard 5-day vs. extended, if reported |

### 1.3 TTP Exposure Data (`tbl_ttp`)

This table captures how each study measured and reported TTP. Many studies will contribute rows to both continuous and dichotomized formats.

| Field | Type | Description |
|---|---|---|
| `study_id` | character | FK to `tbl_study` |
| `arm_id` | character | FK to `tbl_population` |
| `ttp_reporting` | factor | `continuous`, `dichotomized`, `both`, `categorical` |
| `ttp_unit` | factor | `hours`, `minutes` (standardize to hours) |
| **Continuous TTP summary** | | |
| `ttp_mean` | numeric | Mean TTP (hours) |
| `ttp_sd` | numeric | SD of TTP |
| `ttp_median` | numeric | Median TTP (hours) |
| `ttp_iqr_low` | numeric | 25th percentile TTP |
| `ttp_iqr_high` | numeric | 75th percentile TTP |
| `ttp_range_low` | numeric | Minimum TTP |
| `ttp_range_high` | numeric | Maximum TTP |
| **Dichotomized TTP** | | |
| `ttp_cutpoint_hours` | numeric | Threshold used (hours) |
| `ttp_cutpoint_basis` | factor | `ROC_derived`, `clinical_convention`, `prior_literature`, `median_split`, `other` |
| `n_short_ttp` | integer | N in short TTP group |
| `n_long_ttp` | integer | N in long TTP group |
| `ttp_mean_short` | numeric | Mean TTP in short group (if reported) |
| `ttp_mean_long` | numeric | Mean TTP in long group (if reported) |
| **Categorical TTP (if >2 categories)** | | |
| `ttp_n_categories` | integer | Number of TTP categories |
| `ttp_cat_labels` | character | Category labels (semicolon-separated) |
| `ttp_cat_ns` | character | Category Ns (semicolon-separated) |

### 1.4 Outcome Data (`tbl_outcomes`)

One row per study × arm × outcome × TTP reporting format. This is the core extraction table.

| Field | Type | Description |
|---|---|---|
| `study_id` | character | FK to `tbl_study` |
| `arm_id` | character | FK to `tbl_population` |
| `outcome_type` | factor | `persistent_bacteremia`, `relapse`, `microbiological_clearance`, `mortality` |
| `outcome_definition` | character | Verbatim definition from study |
| `outcome_timepoint_days` | numeric | Assessment window (e.g., 2–3 for persistent, 30 for mortality) |
| `outcome_timepoint_label` | character | e.g., `"48-72h"`, `"30-day"`, `"in-hospital"` |
| **2×2 table data (dichotomized TTP)** | | |
| `events_short_ttp` | integer | Events in short TTP group |
| `n_short_ttp` | integer | Total in short TTP group |
| `events_long_ttp` | integer | Events in long TTP group |
| `n_long_ttp` | integer | Total in long TTP group |
| **Reported effect estimates** | | |
| `effect_measure` | factor | `OR`, `RR`, `HR`, `IRR` |
| `effect_estimate` | numeric | Point estimate (native scale) |
| `ci_lower` | numeric | Lower 95% CI bound |
| `ci_upper` | numeric | Upper 95% CI bound |
| `p_value` | numeric | P-value (if reported) |
| `adjusted` | logical | Whether estimate is adjusted |
| `adjustment_vars` | character | Semicolon-separated list of covariates |
| **Continuous TTP association** | | |
| `beta_per_hour` | numeric | Log-effect per hour increase in TTP |
| `se_beta` | numeric | SE of beta |
| `or_per_hour` | numeric | OR per hour TTP (if reported on native scale) |
| `or_per_hour_ci_low` | numeric | Lower 95% CI for OR per hour |
| `or_per_hour_ci_high` | numeric | Upper 95% CI for OR per hour |

### 1.5 Computed Effect Sizes for Analysis (`tbl_es`)

This table is derived programmatically from `tbl_outcomes` using `metafor::escalc()` and serves as the direct input to the Bayesian models.

| Field | Type | Description |
|---|---|---|
| `study_id` | character | FK to `tbl_study` |
| `es_id` | integer | Row-level unique ID (for multivariate models) |
| `outcome_type` | factor | Outcome category |
| `yi` | numeric | Log-OR (or log-HR) — the effect size |
| `vi` | numeric | Sampling variance of `yi` |
| `sei` | numeric | SE of `yi` (= √vi) |
| `ni` | integer | Total N contributing to this estimate |
| `es_source` | factor | `two_by_two`, `reported_adjusted`, `reported_unadjusted`, `continuous_converted` |
| **Moderator variables (for meta-regression)** | | |
| `pathogen_class` | factor | Gram-positive vs. gram-negative |
| `organism_saureus` | logical | S. aureus subgroup flag |
| `source_control` | factor | Source control status |
| `infection_source` | factor | Infection source |
| `ttp_cutpoint_hours` | numeric | Cut-point used (for dichotomized studies) |
| `pct_appropriate_empiric` | numeric | Study-level covariate |
| `blood_culture_system` | factor | Detection system |
| `rob_overall` | factor | Risk of bias rating |

---

## 2. R Package Ecosystem

### 2.1 Core Bayesian Analysis

| Package | Role | Notes |
|---|---|---|
| **`brms`** (≥2.21) | Primary modeling engine | Bayesian multilevel/meta-regression via Stan. Supports custom priors, random effects, and multivariate outcomes. Use `brm()` with `yi | se(sei)` syntax for meta-analysis. |
| **`cmdstanr`** | Stan backend | Preferred over `rstan` — faster compilation, better diagnostics, easier installation. Install CmdStan via `cmdstanr::install_cmdstan()`. |
| **`metafor`** (≥4.4) | Classical meta-analysis + effect size computation | Essential for `escalc()` (effect size calculation), `rma.mv()` for comparison frequentist models, and diagnostic plots. |
| **`bayesmeta`** | Dedicated Bayesian MA | Useful for simple normal-normal hierarchical models and as a sanity check against `brms`. |

### 2.2 Bayesian Diagnostics and Post-Processing

| Package | Role |
|---|---|
| **`posterior`** | Posterior draws manipulation, summary statistics, convergence diagnostics (R-hat, ESS) |
| **`loo`** | Leave-one-out cross-validation, WAIC, model comparison via `loo_compare()` |
| **`bayesplot`** | Trace plots, rank histograms, posterior predictive checks |
| **`tidybayes`** | Tidy extraction of posterior draws, integration with ggplot2 |
| **`priorsense`** | Prior sensitivity analysis — power-scaling diagnostics |
| **`bridgesampling`** | Bayes factors for model comparison (if needed) |

### 2.3 Data Handling

| Package | Role |
|---|---|
| **`tidyverse`** | Core data manipulation (dplyr, tidyr, ggplot2, readr, stringr, purrr, forcats) |
| **`readxl`** | Import .xlsx extraction sheets |
| **`janitor`** | Column name cleaning, duplicate detection |
| **`naniar`** | Missing data visualization and patterns |
| **`assertr`** | Data validation pipelines (verify constraints on extracted data) |

### 2.4 Effect Size Conversion Utilities

| Package | Role |
|---|---|
| **`metafor`** | `escalc()` for computing log-OR, log-RR from 2×2 tables |
| **`esc`** | Convert between effect size types (d, r, OR, etc.) |
| **`estmeansd`** | Estimate mean/SD from median, IQR, range (for TTP distributions) |

### 2.5 Visualization

| Package | Role |
|---|---|
| **`ggplot2`** | Base plotting framework |
| **`ggdist`** | Posterior distribution visualization (half-eyes, interval plots) |
| **`forestploter`** | Publication-quality forest plots with subgroups |
| **`patchwork`** | Multi-panel figure composition |
| **`ggrepel`** | Non-overlapping labels for funnel/influence plots |
| **`MetBrewer`** or **`ggsci`** | Color palettes suitable for publication |

### 2.6 Reporting

| Package | Role |
|---|---|
| **`rmarkdown`** | Reproducible report generation |
| **`knitr`** | Code chunk execution |
| **`gt`** or **`flextable`** | Formatted tables for manuscripts |
| **`papaja`** | APA-formatted manuscripts (optional, if targeting psych/medical journals) |
| **`grateful`** | Auto-generate package citation list |

---

## 3. Key Analytical Notes

### 3.1 Effect Size Computation Strategy

Studies will report TTP associations in heterogeneous formats. The extraction database accommodates this by capturing raw data wherever possible, then computing standardized effect sizes:

1. **2×2 tables available** → `metafor::escalc(measure = "OR", ai, bi, ci, di)` to get log-OR and variance directly.

2. **Adjusted OR/HR reported with CI** → Back-calculate log-OR and SE: `yi = log(effect_estimate)`, `sei = (log(ci_upper) - log(ci_lower)) / (2 * 1.96)`.

3. **Continuous TTP (beta per hour)** → If log-OR per hour is reported, use directly. These studies contribute to a separate sub-model or can be pooled with dichotomized studies via dose-response modeling.

4. **HR → OR conversion** → For short follow-up windows (e.g., 30-day mortality), HRs approximate ORs reasonably well when event rates are moderate. Flag and sensitivity-analyze these conversions.

### 3.2 brms Model Specification Sketch

```r
# Basic Bayesian random-effects meta-analysis
fit_base <- brm(
  yi | se(sei) ~ 1 + (1 | study_id),
  data = tbl_es %>% filter(outcome_type == "persistent_bacteremia"),
  prior = c(
    prior(normal(0, 1), class = "Intercept"),       # weakly informative on log-OR scale
    prior(half_cauchy(0, 0.5), class = "sd")          # τ prior
  ),
  backend = "cmdstanr",
  chains = 4, iter = 4000, warmup = 1000,
  control = list(adapt_delta = 0.95)
)

# Meta-regression with moderators
fit_reg <- brm(
  yi | se(sei) ~ 1 + pathogen_class + source_control + (1 | study_id),
  data = tbl_es %>% filter(outcome_type == "persistent_bacteremia"),
  prior = c(
    prior(normal(0, 1), class = "Intercept"),
    prior(normal(0, 0.5), class = "b"),               # moderator coefficients
    prior(half_cauchy(0, 0.5), class = "sd")
  ),
  backend = "cmdstanr",
  chains = 4, iter = 4000, warmup = 1000
)
```

### 3.3 Prior Specification Rationale

For a meta-analysis of prognostic associations in bacteremia:

- **Intercept (pooled log-OR):** `Normal(0, 1)` centers at null with ~95% prior mass between OR 0.14 and 7.4 — broad enough for clinically plausible associations.
- **Between-study SD (τ):** `Half-Cauchy(0, 0.5)` allows moderate heterogeneity while regularizing against implausibly large τ. Alternative: `Half-Normal(0, 0.5)` for slightly tighter constraint.
- **Moderator coefficients:** `Normal(0, 0.5)` — moderately skeptical that any single moderator shifts the log-OR by more than ~1 unit.
- **Sensitivity:** Run models with `Normal(0, 2)` and `Normal(0, 0.35)` priors and use `priorsense` to assess influence.

### 3.4 Handling Multiple Outcomes per Study

When studies report >1 outcome, the effect sizes within a study are correlated. Options:

1. **Multivariate meta-analysis** via `brms` with `mvbind()` or correlated random effects.
2. **Robust variance estimation** as a frequentist sensitivity check via `clubSandwich` + `metafor`.
3. **Separate models per outcome** (simplest; appropriate if outcome-specific pooling is the primary goal, with cross-outcome comparison as secondary).

### 3.5 Recommended File Format

Store the extraction database as an **.xlsx workbook** with one sheet per table (`tbl_study`, `tbl_population`, `tbl_ttp`, `tbl_outcomes`). Include a **codebook sheet** with field definitions and permitted values. The computed `tbl_es` is generated in R and should not be manually edited.

---

## 4. Suggested Package Installation

```r
# Core
install.packages(c("brms", "cmdstanr", "metafor", "bayesmeta"))
cmdstanr::install_cmdstan()

# Bayesian diagnostics
install.packages(c("posterior", "loo", "bayesplot", "tidybayes", "priorsense", "bridgesampling"))

# Data handling
install.packages(c("tidyverse", "readxl", "janitor", "naniar", "assertr"))

# Effect sizes
install.packages(c("esc", "estmeansd"))

# Visualization
install.packages(c("ggdist", "forestploter", "patchwork", "ggrepel", "MetBrewer"))

# Reporting
install.packages(c("gt", "flextable", "grateful"))
```

---

*Prepared for: TTP and Antibiotic Failure in Bacteremia — Bayesian Meta-Analysis Protocol*
