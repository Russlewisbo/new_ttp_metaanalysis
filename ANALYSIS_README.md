# TTP Meta-Analysis: Complete Analysis Summary

**Date:** February 10, 2026  
**Analysis:** Bayesian Meta-Analysis of Time-to-Positivity and Mortality in Bacteremia

## 📊 Key Findings

### Primary Result
**Shorter TTP is strongly associated with increased mortality**
- **Pooled OR: 2.43** (95% CrI: 1.38-4.20) — short vs long TTP
- **99.8% probability** that shorter TTP increases mortality
- Effect is **robust** across multiple sensitivity analyses

### Critical Discovery
**TTP cutpoint choice significantly affects observed effect size**
- Studies using higher cutpoints (>20h) report smaller effects
- **-0.032 log-OR per hour** (98.6% probability negative)
- Optimal cutpoint appears to be **8-12 hours**

### Robustness
✅ Consistent across gram-positive and gram-negative infections  
✅ Similar effects in adjusted and unadjusted analyses  
✅ Robust to data extraction method (2×2 tables vs reported OR)  
✅ Stable effect from 2013-2025  

## 📁 Project Files

### Main Report
- **TTP_MetaAnalysis_Report.html** - Comprehensive HTML report (2.9 MB)
  - Open in any web browser
  - Contains all analyses, figures, and tables
  - Self-contained (embeds all resources)

### Source Files
- **TTP_MetaAnalysis_Report.qmd** - Quarto source document
- **report_data.rds** - Saved analysis data (1.57 MB)
- **TTP_MetaAnalysis_Final.xlsx** - Original structured database

### Protocol
- **TTP_meta-analysis_database_and_packages.md** - Analysis protocol

## 🔢 Data Summary

- **Studies included:** 20 studies
- **Effect sizes computed:** 32
- **Publication years:** 2006-2025
- **Mortality effect sizes:** 15 from 12 studies
- **Countries represented:** 12 countries
- **Study designs:** 16 retrospective, 4 prospective cohorts

## 📈 Analysis Overview

### Effect Size Computation
1. **2×2 tables (n=12):** Direct calculation using metafor::escalc()
2. **Reported estimates (n=18):** Back-calculated from OR/HR/RR with CI
3. **Continuous TTP (n=2):** Per-hour associations

### Statistical Methods
- **Primary analysis:** Bayesian random-effects meta-analysis
- **Software:** R + brms + Stan (4 chains × 4000 iterations)
- **Priors:** Weakly informative (Normal(0,1) for intercept, Half-Cauchy(0,0.5) for τ)
- **Convergence:** Excellent (all R̂ < 1.01, ESS > 2,600)

### Moderators Examined
1. ⚠️ **TTP cutpoint** - SIGNIFICANT moderator
2. ✅ Pathogen class - No difference
3. ✅ Data source - Robust
4. ✅ Adjustment status - Robust  
5. ✅ Publication year - Stable
6. ⚠️ Infection source - Insufficient data
7. ⚠️ Blood culture system - Insufficient variation

## 💊 Clinical Implications

### For Clinicians
1. **TTP is a valid prognostic marker** - Short TTP identifies high-risk patients
2. **Lower cutpoints are more informative** - Consider 10-12h thresholds (short TTP <10-12h = higher risk)
3. **Universal applicability** - Use regardless of gram stain
4. **Implementation ready** - Modern systems provide real-time TTP

### For Researchers
1. **Standardize cutpoints** - Recommend 10-12h for future studies
2. **Individual patient data** - Needed to characterize dose-response precisely
3. **Intervention trials** - Test TTP-guided treatment strategies
4. **More gram-positive studies** - Current sample is small (n=5)

## 🔬 Models Available in R Workspace

All fitted Bayesian models are available for further exploration:

- `fit_base` - Overall pooled effect
- `fit_gram_pos` - Gram-positive subgroup
- `fit_gram_neg` - Gram-negative subgroup  
- `fit_metareg` - Pathogen meta-regression
- `fit_cutpoint` - **TTP cutpoint meta-regression** ⭐
- `fit_2x2` - 2×2 table data only
- `fit_reported` - Reported estimates only
- `fit_adjustment` - Adjustment status meta-regression
- `fit_year` - Publication year meta-regression

## 📚 Reproducibility

### To Regenerate Report
```r
# In R, ensure workspace has all objects loaded
quarto::quarto_render("TTP_MetaAnalysis_Report.qmd")
```

### Required R Packages
- brms (≥2.23)
- metafor (≥4.4)
- tidyverse
- bayesplot, posterior, loo
- ggdist, patchwork
- gt (for tables)

### To Export to PDF
```bash
quarto render TTP_MetaAnalysis_Report.qmd --to pdf
```

## ⚠️ Important Notes

1. **AI-Generated**: This analysis was conducted using AI under human supervision
2. **Requires Review**: Results should be independently verified before publication
3. **Data Quality**: Based on structured extraction from TTP_MetaAnalysis_Final.xlsx
4. **Risk of Bias**: Not formally assessed (all rob_overall = NA)
5. **Publication Bias**: Not assessed (funnel plots not included)

## 📞 Analysis Details

For questions about methods, data extraction, or to access the full R workspace:
- Review the comprehensive HTML report
- Examine the Quarto source (.qmd) file
- Load report_data.rds in R for reproducibility

---

**Report Generated:** February 10, 2026  
**Software:** R 4.5.1, brms 2.23.0, Quarto  
**Analysis Framework:** Bayesian random-effects meta-analysis with meta-regression
