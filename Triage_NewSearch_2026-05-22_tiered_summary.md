# Tiered triage of the 4,183 NEW records
_Generated 2026-05-22 16:37_

## Inputs
- Source: `Triage_NewSearch_2026-05-22.xlsx` (sheet `NEW_only`, 4,183 rows)
- Empty abstracts: 1,565 (37.4%)

## Tier definitions
1. **TIER_1_HIGH** — explicit TTP phrase (e.g., "time to positivity", "time to detection", "DTP") + blood-culture concept (blood culture, bacteremia, BSI, candidemia, septicemia…)
2. **TIER_2_MED** — standalone abbreviation "TTP" + blood-culture concept, excluding rows where "TTP" plausibly means something else: thrombotic thrombocytopenic purpura, time to progression (oncology), total testing process (lab QC)
3. **TIER_3_BC_ONLY** — blood-culture concept but no TTP signal in title/abstract
4. **TIER_4_TTP_ONLY** — TTP signal but no blood-culture concept
5. **TIER_5_OFF_TOPIC** — neither concept matched

## Result
- **TIER_1_HIGH**: 859
- **TIER_2_MED**: 23
- **TIER_3_BC_ONLY**: 2,086
- **TIER_4_TTP_ONLY**: 118
- **TIER_5_OFF_TOPIC**: 1,097

## Recommended screening order
1. **TIER_1_HIGH** (859) — almost certainly relevant; screen everything.
2. **TIER_2_MED** (23) — likely relevant; screen everything but expect more borderline.
3. **TIER_3_BC_ONLY** (2,086) — bacteremia/BSI papers without an explicit TTP keyword. Many will be off-topic but full-text may still report TTP. Sample-screen first to estimate yield.
4. **TIER_4_TTP_ONLY** (118) — TTP signal but no blood-culture term; mostly off-topic. Quick scan.
5. **TIER_5_OFF_TOPIC** (1,097) — neither concept; skip unless you want to spot-check for missing keywords.

Each row's `ttp_keywords_matched` and `bc_keywords_matched` columns show the exact phrases that fired, so you can audit the classification.