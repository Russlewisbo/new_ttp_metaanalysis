# Tier 3 sample screening with PubMed abstract enrichment

_Generated 2026-05-23. Source: PubMed via bio-research MCP._

## Method

Tier 3 (`TIER_3_BC_ONLY`) contains 2,086 papers whose Elicit-exported record had a blood-culture-concept term but no explicit TTP keyword. 692 of those (33%) have an empty Abstract field in the export; 636 of those have a DOI and so are precisely resolvable.

I drew a **random sample of 50** from the 636 empty-abstract + DOI subset, looked each one up on PubMed by DOI, fetched the abstract, and decided by eye whether the abstract revealed a TTP signal that the title alone hadn't.

## Results

| Outcome | n / 50 | % |
|---|---|---|
| **PROMOTE_TIER_1** (explicit TTP signal in abstract) | **9** | **18%** |
| KEEP_TIER_3 (resolved but no TTP signal) | 11 | 22% |
| UNRESOLVED (no PubMed match — older or non-biomedical journal) | 30 | 60% |

Of the 20 papers PubMed could resolve, **9 (45%) actually deserved Tier 1 promotion** — their abstracts contained explicit phrases like "time to detection", "time to positivity", or "TTD/TTPR/TTAST".

## The 9 promoted papers

| DOI | Journal / Year | TTP signal |
|---|---|---|
| [10.1128/JCM.00849-19](https://doi.org/10.1128/JCM.00849-19) | J Clin Microbiol 2019 | "times to detection (TTD)" across blood culture bottle types |
| [10.3390/antibiotics15040335](https://doi.org/10.3390/antibiotics15040335) | Antibiotics 2026 | TTD/TTPR/TTAST KPIs; median TTD 12.6 h |
| [10.1097/INF.0000000000004439](https://doi.org/10.1097/INF.0000000000004439) | Pediatr Infect Dis J 2024 | "shorter time to culture positivity" in persistent SAB (16h vs 20h) |
| [10.1128/JCM.00307-17](https://doi.org/10.1128/JCM.00307-17) | J Clin Microbiol 2017 | BacT/Alert Virtuo vs BTA3D, shorter time to detection |
| [10.1016/S1525-1578(10)60498-9](https://doi.org/10.1016/S1525-1578(10)60498-9) | J Mol Diagn 2004 | "time to positivity of these microorganisms" (Candida) |
| [10.1128/JCM.02091-06](https://doi.org/10.1128/JCM.02091-06) | J Clin Microbiol 2007 | "times to detection" comparison |
| [10.1128/jcm.18.1.43-48.1983](https://doi.org/10.1128/jcm.18.1.43-48.1983) | J Clin Microbiol 1983 | "time to detection of positive blood cultures" |
| [10.1186/1471-2334-14-233](https://doi.org/10.1186/1471-2334-14-233) | BMC Infect Dis 2014 | "shorter time to positivity" for BACTEC vs cooked-meat broth |
| [10.1128/jcm.27.7.1588-1593.1989](https://doi.org/10.1128/jcm.27.7.1588-1593.1989) | J Clin Microbiol 1989 | multiple "time to detection" comparisons |

Some of these may already be cited in your prior corpus or are not the right population/intervention for your meta-analysis, but they are at minimum in scope for screening.

Based on articles retrieved from PubMed.

## Extrapolation to the full Tier 3 empty-abstract pool

The empty-abstract + DOI subset is 636 papers. If the yield rate holds:

| Assumption | Estimated extra Tier-1 promotions |
|---|---|
| Lower bound (treat all 30 unresolved as Tier 3) | **~114** |
| Upper bound (unresolved match the resolved 45% rate) | ~286 |

A more realistic point estimate is **~150 extra Tier-1 promotions** hiding in Tier 3 with empty abstracts — too many to ignore.

## Recommendation

**Yes — pull PubMed abstracts for the full empty-abstract + DOI pool (636 papers)** and re-run the tier classifier. That's 7 batches of ~100 DOI lookups via `convert_article_ids` plus matched calls to `get_article_metadata`, which is well within the MCP's reach. The script can append the enriched abstracts into the `Abstract` column and re-tier in one pass.

I'd skip enriching:
- Tier 3 rows that already have a non-empty abstract (1,394 rows — the abstract is already in the Elicit export and didn't contain a TTP keyword, so PubMed is unlikely to add new signal)
- Tier 3 rows without a DOI (56 rows — would require title-based search, much higher false-match rate)
- Tier 5 (off-topic) — neither concept present in title or abstract, very low yield expected

Want me to proceed with the full enrichment of the 636-row pool?
