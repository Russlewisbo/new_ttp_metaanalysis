# Clinical Failure Outcomes: Feasibility Assessment

**Date:** February 10, 2026  
**Analysis:** TTP and Clinical Failure (Persistent Bacteremia / Recurrent Bacteremia)

## Executive Summary

### Question
Can we perform a meta-analysis of TTP effects on clinical failure outcomes (persistent bacteremia, bacteremia clearance, recurrent bacteremia)?

### Answer
**❌ NO - Meta-analysis is NOT recommended at this time**

### Reason
Major data quality issues and insufficient sample size make reliable pooling impossible.

---

## Data Availability

### What We Found

| Outcome Type | N Studies | N Effect Sizes | Data Sources |
|-------------|-----------|----------------|--------------|
| Persistent bacteremia | 3 | 3 | Ok2013 (×2), Minejima2019 |
| Microbiological clearance | 1 | 2 | Melling2019 (×2) |
| Bacteremia clearance | 1 | 1 | Lambregts2019 |
| **Total** | **4** | **6** | - |
| Recurrent bacteremia | 0 | 0 | None found |

**Compare to mortality analysis:** 12-15 studies with clear, consistent data

---

## Critical Data Quality Issues

### 🚨 Issue #1: Directionality Contradictions

**Ok2013 Study - Internal Contradiction:**

| Data Source | Odds Ratio | Interpretation |
|------------|-----------|----------------|
| 2×2 table (extracted) | 0.27 | Short TTP → LESS persistent bacteremia (protective) |
| Reported OR (paper) | 14.57 | Short TTP → MORE persistent bacteremia (harmful) |

**These cannot both be correct!** This indicates either:
- Data entry error in 2×2 table extraction
- Comparison groups were reversed
- Different outcome definitions used

### 🚨 Issue #2: Extreme Heterogeneity

**Effect size range:** OR = 0.27 to 1115 (over **4000-fold difference**)

| Study | Outcome | OR |
|-------|---------|-----|
| Minejima2019 | Persistent bacteremia | 0.27 |
| Lambregts2019 | Bacteremia clearance | 6.05 |
| Melling2019 | Microbiological clearance | 36.2 |
| **Melling2019** | **Microbiological clearance** | **1115** ⚠️ |

**The Melling2019 outliers:**
- OR = 36 and OR = 1115
- These are about MRSA in **sputum cultures**, not blood
- Completely dominate any pooled estimate
- Questionable relevance to bacteremia outcomes

### 🚨 Issue #3: Outcome Definition Heterogeneity

Different studies define "failure" differently:

- **Persistent ≥3 days** (Minejima2019)
- **Persistent ≥7 days** (Ok2013)
- **Bacteremia at 24 hours** (Lambregts2019)
- **Time to MRSA growth in sputum** (Melling2019) ← Not even blood!

These are fundamentally different outcomes and should not be pooled.

### 🚨 Issue #4: Insufficient Sample Size

**Statistical reality:**
- Only **4 studies** (vs 12 for mortality)
- One study (Ok2013) has contradictory data
- One study (Melling2019) has extreme outliers
- **Effectively only 2-3 usable studies**

**Minimum for reliable meta-analysis:** ≥8-10 studies

---

## Why This Matters

### If We Proceeded Anyway...

❌ **Pooled estimate would be unreliable**
- Dominated by outliers
- Directionality unclear
- Wide credible intervals
- No meaningful interpretation possible

❌ **Could be actively misleading**
- Might suggest effect where none exists
- Or miss real effect due to conflicting data
- Risk of incorrect clinical recommendations

❌ **Cannot assess heterogeneity**
- Too few studies for meta-regression
- Cannot identify moderators
- Cannot perform sensitivity analyses

---

## Comparison: Mortality vs Clinical Failure

| Feature | Mortality Analysis | Clinical Failure |
|---------|-------------------|-----------------|
| **Studies** | 12 studies | 4 studies |
| **Effect sizes** | 15 | 6 |
| **Data quality** | ✅ Consistent | ❌ Contradictory |
| **Directionality** | ✅ Clear | ❌ Confused |
| **Heterogeneity** | Moderate (I²=76%) | Extreme (>1000-fold range) |
| **Outcome definitions** | ✅ Standardized | ❌ Highly variable |
| **Outliers** | Minor | Major (OR=1115!) |
| **Meta-analysis feasible?** | ✅ YES | ❌ NO |

---

## Recommendations

### ✅ DO:

1. **Document the limitation** in the main report
   - Note that clinical failure outcomes were explored
   - Explain why meta-analysis was not performed
   - List the available studies narratively

2. **Describe studies individually**
   - Minejima2019: OR = 1.17 (per hour increase)
   - Ok2013: Contradictory results requiring verification
   - Lambregts2019: Bacteremia at 24h associated with longer TTP
   - Melling2019: Extreme values, questionable relevance

3. **Call for more research**
   - Need standardized outcome definitions
   - Need larger studies with clear 2×2 data
   - Focus on blood culture clearance (not sputum)
   - Distinguish persistent from recurrent bacteremia

### ❌ DO NOT:

1. **Do not pool these data**
   - Results would be unreliable
   - Could be misleading
   - Violates basic meta-analysis principles

2. **Do not attempt Bayesian analysis**
   - Garbage in, garbage out
   - Priors cannot fix bad data
   - Models will converge but produce meaningless results

3. **Do not hide the problems**
   - Be transparent about data quality issues
   - Acknowledge limitations honestly
   - This builds trust in the main findings

---

## Alternative Approaches

### Option 1: Narrative Review (RECOMMENDED)

Create a brief section in the report:

> **Clinical Failure Outcomes**
> 
> We identified 4 studies reporting associations between TTP and clinical failure outcomes (persistent bacteremia or bacteremia clearance). However, meta-analysis was not feasible due to:
> 
> 1. Small sample size (n=4 studies)
> 2. Inconsistent outcome definitions
> 3. Directionality inconsistencies requiring data verification
> 4. Extreme outliers (OR >1000)
>
> Individual study results were heterogeneous and should be interpreted cautiously. Additional primary studies with standardized outcome definitions are needed before meta-analysis can be reliably performed.

### Option 2: Data Quality Audit (If Resources Available)

1. Return to Ok2013 original paper
2. Verify 2×2 table extraction
3. Clarify which comparison group is which
4. Re-extract if necessary
5. Contact authors if ambiguous

### Option 3: Wait for More Studies

- Revisit when ≥8-10 studies available
- Lobby for standardized outcome definitions
- Encourage researchers to report both 2×2 and adjusted OR

---

## Lessons Learned

### For Future Meta-Analyses

1. **Data quality matters more than sample size**
   - Better to have 5 good studies than 10 questionable ones
   
2. **Verify internal consistency**
   - When 2×2 and reported OR conflict, investigate
   - Don't assume all extracted data are correct

3. **Outcome homogeneity is critical**
   - "Persistent bacteremia" at 3 days ≠ 7 days
   - Sputum cultures ≠ blood cultures
   - Clearance ≠ persistence (inverse outcomes)

4. **Be willing to say "no"**
   - Sometimes the data don't support meta-analysis
   - Honesty about limitations strengthens overall report
   - Don't force analysis where it's not appropriate

---

## Conclusion

**Unlike the mortality analysis (which was robust and reliable), the clinical failure data are NOT suitable for meta-analysis at this time.**

**Key takeaway:** The mortality finding (OR = 2.43) is on solid ground with 12 studies. The clinical failure question remains **unanswered** and requires:
- More primary studies
- Better outcome standardization
- Data quality verification for existing studies

**This limitation does NOT undermine the main mortality findings,** which remain valid and clinically important.

---

## Supporting Data

### Individual Study Details

**1. Minejima2019**
- Outcome: Persistent bacteremia ≥3 days
- OR per hour increase in TTP: 1.17 (95% CI: 1.06-1.29)
- Note: Continuous TTP, different from dichotomized studies
- ✅ Most reliable estimate

**2. Ok2013**
- Outcome: Persistent bacteremia ≥7 days
- Sample: 67 patients (31 short TTP, 36 long TTP)
- 2×2 extracted: 9/31 vs 22/36 → OR = 0.27
- Reported: OR = 14.57 (95% CI: 3.52-60.3)
- ⚠️ Internal contradiction - requires verification

**3. Lambregts2019**
- Outcome: Bacteremia present at 24 hours
- Reported: 1.8 (95% CI: 1.46-2.14)
- Note: Unclear if value is OR or log-OR
- ⚠️ Needs clarification

**4. Melling2019**
- Outcome: Microbiological clearance (MRSA in sputum)
- Two estimates: OR = 36 and OR = 1115
- ⚠️ Extreme outliers
- ⚠️ Sputum (not blood) - different biology

**5. SantosPatarroyo2025**
- Outcome: Extended bacteremia ≥2 days
- Beta = -0.36 (per hour)
- ⚠️ No standard error reported - cannot use

---

**Report prepared:** February 10, 2026  
**Analyst:** Meta-analysis team  
**Status:** Clinical failure meta-analysis NOT RECOMMENDED
