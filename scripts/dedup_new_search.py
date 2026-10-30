"""
Deduplicate the 2026-05-22 update search (review_22.05.05csv.csv) against:
  (A) the prior Elicit corpus (Elicit - TTP ... Sources (1).ris)
  (B) the 57 studies already included in TTP_MetaAnalysis_Extraction_Complete.xlsx
       (sheet tbl_study)

Output: Triage_NewSearch_2026-05-22.xlsx with sheets All, NEW_only, DUP, ALREADY_INCLUDED.

Matching logic, in order:
  1. DOI exact match  -> DUP_DOI (or ALREADY_INCLUDED if matched study is in extraction)
  2. Title fuzzy match (rapidfuzz token_set_ratio >= 90) -> DUP_TITLE / ALREADY_INCLUDED
  3. Otherwise -> NEW

Key fix from prior session: the Elicit RIS contains a record with the truncated
title "Time to positivity of" which previously matched almost every TTP paper
at score 100 via token_set_ratio. Any prior-corpus record whose normalized
title has fewer than 5 tokens is dropped before fuzzy matching.
"""

from __future__ import annotations

import csv
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

import pandas as pd
from rapidfuzz import fuzz, process

# Works in both the Mac filesystem and the Linux sandbox mount.
_CANDIDATE_ROOTS = [
    Path("/Users/russelllewis/Desktop/new_ttp_metaanalysis"),
    Path("/sessions/affectionate-keen-franklin/mnt/new_ttp_metaanalysis"),
]
ROOT = next((p for p in _CANDIDATE_ROOTS if p.exists()), _CANDIDATE_ROOTS[0])
RIS_PATH = ROOT / "Elicit - TTP as a Predictor of Antibiotic Failure in Bacter - Sources (1).ris"
NEW_CSV = ROOT / "review_22.05.05csv.csv"
EXTRACTION_XLSX = ROOT / "TTP_MetaAnalysis_Extraction_Complete.xlsx"
OUT_XLSX = ROOT / "Triage_NewSearch_2026-05-22.xlsx"
OUT_MD = ROOT / "Triage_NewSearch_2026-05-22_summary.md"

FUZZY_THRESHOLD = 90
FUZZY_THRESHOLD_FOR_TRUNCATED_PRIOR = 95  # stricter when prior title looks truncated
MIN_PRIOR_TITLE_TOKENS = 5  # the "Time to positivity of" guard
_CONF_NUM_RE = re.compile(r"^\s*\d{1,4}\.\s")  # "653. Direct Identification..." conf-abstract pattern

# allow CSVs with very long abstract cells
csv.field_size_limit(sys.maxsize)


# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------

_punct_re = re.compile(r"[^\w\s]+", flags=re.UNICODE)
_ws_re = re.compile(r"\s+")


def normalize_title(t: str) -> str:
    if not t:
        return ""
    t = unicodedata.normalize("NFKD", t)
    t = t.encode("ascii", "ignore").decode("ascii")
    t = t.lower()
    t = _punct_re.sub(" ", t)
    t = _ws_re.sub(" ", t).strip()
    return t


def normalize_doi(d: str) -> str:
    if not d:
        return ""
    d = d.strip().lower()
    d = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", d)
    d = d.strip().strip(".").strip()
    return d


# ----------------------------------------------------------------------------
# Load prior corpus: Elicit RIS
# ----------------------------------------------------------------------------

def parse_ris(path: Path) -> list[dict]:
    """Minimal RIS parser — collects TI, T1, AU, PY, Y1, DO, DA per record."""
    records: list[dict] = []
    current: dict[str, list[str]] | None = None
    with path.open("r", encoding="utf-8-sig", errors="replace") as f:
        for raw in f:
            line = raw.rstrip("\n").rstrip("\r")
            m = re.match(r"^([A-Z][A-Z0-9])  - (.*)$", line)
            if not m:
                # continuation line for current tag (e.g., wrapped abstract)
                continue
            tag, val = m.group(1), m.group(2)
            if tag == "TY":
                current = defaultdict(list)
                current["TY"].append(val)
                records.append(current)
            elif current is not None:
                current[tag].append(val.strip())
            if tag == "ER":
                current = None
    rows = []
    for rec in records:
        title = (rec.get("TI") or rec.get("T1") or [""])[0]
        year = ""
        for ytag in ("PY", "Y1", "DA"):
            if rec.get(ytag):
                ym = re.search(r"\d{4}", rec[ytag][0])
                if ym:
                    year = ym.group(0)
                    break
        doi = (rec.get("DO") or [""])[0]
        authors = "; ".join(rec.get("AU", []))
        rows.append({
            "title": title,
            "title_norm": normalize_title(title),
            "year": year,
            "doi": normalize_doi(doi),
            "authors": authors,
            "source": "elicit_ris",
        })
    return rows


# ----------------------------------------------------------------------------
# Load prior corpus: already-included studies
# ----------------------------------------------------------------------------

def load_included_fingerprints(path: Path) -> set[tuple[str, str]]:
    """tbl_study has only study_id / first_author / pub_year — no title or DOI.
    Return a set of (first_author_lower, year_str) fingerprints we can use
    to flag a new-search record as ALREADY_INCLUDED."""
    df = pd.read_excel(path, sheet_name="tbl_study")
    df.columns = [c.strip().lower() for c in df.columns]
    fps: set[tuple[str, str]] = set()
    for _, r in df.iterrows():
        author = str(r.get("first_author", "")).strip().lower()
        year_val = r.get("pub_year")
        if pd.isna(year_val):
            continue
        try:
            year = str(int(year_val))
        except (TypeError, ValueError):
            year = str(year_val).strip()
        if author and year:
            fps.add((author, year))
    return fps


def first_author_lastname(authors_field: str) -> str:
    """Best-effort: take the first author entry (split on ';' then ',') and
    return their last name lowercased."""
    if not authors_field:
        return ""
    first = authors_field.split(";")[0].strip()
    # "Wang, J." -> "wang"; "John Wang" -> "wang"
    if "," in first:
        last = first.split(",")[0].strip()
    else:
        parts = first.split()
        last = parts[-1] if parts else ""
    return last.lower()


# ----------------------------------------------------------------------------
# Load new search CSV
# ----------------------------------------------------------------------------

def load_new(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, dtype=str, keep_default_na=False, engine="python")
    df.columns = [c.strip() for c in df.columns]
    df["title_norm"] = df["Title"].fillna("").map(normalize_title)
    df["doi_norm"] = df["DOI"].fillna("").map(normalize_doi)
    return df


# ----------------------------------------------------------------------------
# Dedup
# ----------------------------------------------------------------------------

def main() -> None:
    print("Loading Elicit RIS …")
    elicit = parse_ris(RIS_PATH)
    print(f"  {len(elicit):,} records parsed")

    print("Loading extraction DB (already-included studies) …")
    included_fps = load_included_fingerprints(EXTRACTION_XLSX)
    print(f"  {len(included_fps):,} (first_author, year) fingerprints")

    print("Loading new search CSV …")
    new_df = load_new(NEW_CSV)
    print(f"  {len(new_df):,} new records")

    # Prior corpus to match against = the Elicit RIS (the previous search).
    # tbl_study has no title/DOI, so it's used separately as a fingerprint
    # check downstream rather than mixed in here.
    prior_all = elicit

    doi_index: dict[str, dict] = {}
    for p in prior_all:
        if p["doi"]:
            doi_index.setdefault(p["doi"], p)

    prior = [p for p in prior_all
             if p["title_norm"] and len(p["title_norm"].split()) >= MIN_PRIOR_TITLE_TOKENS]
    dropped_short = [p for p in prior_all
                     if p["title_norm"] and len(p["title_norm"].split()) < MIN_PRIOR_TITLE_TOKENS]
    print(f"  Dropping {len(dropped_short)} prior records from fuzzy index "
          f"(<{MIN_PRIOR_TITLE_TOKENS}-token titles); DOI still indexed:")
    for d in dropped_short[:10]:
        print(f"    - [{d['source']}] {d['title']!r}")
    print(f"  Prior fuzzy-index size: {len(prior):,};  DOI index size: {len(doi_index):,}")

    # Build title list once for rapidfuzz
    prior_titles = [p["title_norm"] for p in prior]

    statuses: list[str] = []
    match_scores: list[float] = []
    matched_titles: list[str] = []
    matched_sources: list[str] = []
    matched_dois: list[str] = []
    already_included_flags: list[str] = []

    for i, row in enumerate(new_df.itertuples(index=False), 1):
        title_norm = getattr(row, "title_norm")
        doi_norm = getattr(row, "doi_norm")
        authors = getattr(row, "Authors", "") or ""
        year_raw = getattr(row, "_4", "")  # 'Published Year' becomes _4 via itertuples
        # safer: pull by column name via the dict view
        # (itertuples sanitizes names; build a fallback below)

        status = "NEW"
        score = 0.0
        matched_title = ""
        matched_source = ""
        matched_doi = ""

        # 1) DOI match
        if doi_norm and doi_norm in doi_index:
            hit = doi_index[doi_norm]
            score = 100.0
            matched_title = hit["title"]
            matched_source = hit["source"]
            matched_doi = hit["doi"]
            status = "DUP_DOI"
        # 2) Fuzzy title match
        elif title_norm and len(title_norm.split()) >= 4:
            best = process.extractOne(title_norm, prior_titles, scorer=fuzz.token_set_ratio)
            if best is not None:
                cand_title_norm, cand_score, cand_idx = best
                if cand_score >= FUZZY_THRESHOLD:
                    hit = prior[cand_idx]
                    score = float(cand_score)
                    matched_title = hit["title"]
                    matched_source = hit["source"]
                    matched_doi = hit["doi"]
                    # Tighten threshold for truncated/conference-abstract prior titles —
                    # they over-match arbitrary longer titles via token_set_ratio.
                    looks_truncated = (
                        _CONF_NUM_RE.match(hit["title"] or "") is not None
                        or len(hit["title_norm"].split()) <= 8
                    )
                    if looks_truncated and cand_score < FUZZY_THRESHOLD_FOR_TRUNCATED_PRIOR:
                        status = "NEEDS_REVIEW"
                    else:
                        status = "DUP_TITLE"

        statuses.append(status)
        match_scores.append(score)
        matched_titles.append(matched_title)
        matched_sources.append(matched_source)
        matched_dois.append(matched_doi)
        already_included_flags.append("")  # filled in below

        if i % 1000 == 0:
            print(f"  matched {i:,} / {len(new_df):,}")

    new_df["status"] = statuses
    new_df["match_score"] = match_scores
    new_df["matched_title"] = matched_titles
    new_df["matched_source"] = matched_sources
    new_df["matched_doi"] = matched_dois

    # Secondary author+year fingerprint pass — flags any new-search record
    # whose first author + year matches an extraction-DB study. If status
    # was already DUP_DOI / DUP_TITLE we still surface it via a separate flag.
    def _fp(authors_field: str, year_field: str) -> tuple[str, str]:
        ln = first_author_lastname(authors_field)
        yr = re.search(r"\d{4}", str(year_field) or "")
        return (ln, yr.group(0)) if (ln and yr) else ("", "")

    fps_for_rows = [_fp(a, y) for a, y in zip(new_df["Authors"].fillna(""),
                                              new_df["Published Year"].fillna(""))]
    in_extraction = [fp in included_fps for fp in fps_for_rows]
    matched_study_ids = []
    fp_to_studies: dict[tuple[str, str], list[str]] = defaultdict(list)
    # rebuild reverse index of fp -> study_ids for reporting
    _xdf = pd.read_excel(EXTRACTION_XLSX, sheet_name="tbl_study")
    _xdf.columns = [c.strip().lower() for c in _xdf.columns]
    for _, r in _xdf.iterrows():
        ln = str(r.get("first_author", "")).strip().lower()
        yv = r.get("pub_year")
        try:
            yr = str(int(yv))
        except (TypeError, ValueError):
            yr = str(yv).strip() if pd.notna(yv) else ""
        if ln and yr:
            fp_to_studies[(ln, yr)].append(str(r.get("study_id", "")))
    for fp in fps_for_rows:
        matched_study_ids.append(",".join(fp_to_studies.get(fp, [])))
    new_df["author_year_in_extraction"] = in_extraction
    new_df["matched_study_id"] = matched_study_ids

    # Promote status where the author-year fingerprint hits an included study.
    # If the row is ALSO matched against the Elicit corpus (DOI or title),
    # we're confident it's ALREADY_INCLUDED. Otherwise label AUTHOR_YEAR_HIT —
    # could be the included paper, could be a same-surname coincidence.
    ay_hit = new_df["author_year_in_extraction"]
    elicit_matched = new_df["status"].isin(["DUP_DOI", "DUP_TITLE"])
    new_df.loc[ay_hit & elicit_matched, "status"] = "ALREADY_INCLUDED"
    new_df.loc[ay_hit & ~elicit_matched, "status"] = "AUTHOR_YEAR_HIT"

    # Reorder for readability
    front = ["status", "match_score", "matched_source", "matched_study_id",
             "Title", "Authors", "Published Year", "Journal", "DOI",
             "matched_title", "matched_doi", "author_year_in_extraction"]
    other = [c for c in new_df.columns if c not in front]
    new_df = new_df[front + other]

    # Sanity counts
    counts = new_df["status"].value_counts().to_dict()
    print("\nStatus counts:")
    for k, v in counts.items():
        print(f"  {k:>18}: {v:,}")

    # Write Excel
    print(f"\nWriting {OUT_XLSX} …")
    with pd.ExcelWriter(OUT_XLSX, engine="openpyxl") as xw:
        new_df.to_excel(xw, sheet_name="All", index=False)
        new_df[new_df["status"] == "NEW"].to_excel(xw, sheet_name="NEW_only", index=False)
        new_df[new_df["status"] == "NEEDS_REVIEW"].to_excel(xw, sheet_name="NEEDS_REVIEW", index=False)
        new_df[new_df["status"] == "AUTHOR_YEAR_HIT"].to_excel(xw, sheet_name="AUTHOR_YEAR_HIT", index=False)
        new_df[new_df["status"].isin(["DUP_DOI", "DUP_TITLE"])].to_excel(xw, sheet_name="DUP", index=False)
        new_df[new_df["status"] == "ALREADY_INCLUDED"].to_excel(xw, sheet_name="ALREADY_INCLUDED", index=False)

    # Recompute counts after the status promotions
    counts = new_df["status"].value_counts().to_dict()

    summary = []
    summary.append("# Triage of update search vs prior corpus")
    summary.append(f"_Generated {pd.Timestamp.now():%Y-%m-%d %H:%M}_\n")
    summary.append("## Inputs")
    summary.append(f"- New search: `{NEW_CSV.name}` ({len(new_df):,} records)")
    summary.append(f"- Prior Elicit RIS: `{RIS_PATH.name}` ({len(elicit):,} records)")
    summary.append(f"- Already-included studies: {len(included_fps):,} (first-author + year fingerprints from `tbl_study`)")
    summary.append(f"- Prior records dropped from fuzzy index as too-short titles: {len(dropped_short)} "
                   "(DOI still indexed)\n")
    summary.append("## Matching rules (in order)")
    summary.append(f"1. **DOI exact match** → `DUP_DOI`")
    summary.append(f"2. **Fuzzy title match** (rapidfuzz token_set_ratio ≥ {FUZZY_THRESHOLD}, or "
                   f"≥ {FUZZY_THRESHOLD_FOR_TRUNCATED_PRIOR} when the prior title looks truncated) → `DUP_TITLE`")
    summary.append("3. **Borderline fuzzy match** against a truncated prior title → `NEEDS_REVIEW`")
    summary.append("4. **Author + year fingerprint** matches an included study:")
    summary.append("   - also matched on Elicit → `ALREADY_INCLUDED`")
    summary.append("   - not matched on Elicit → `AUTHOR_YEAR_HIT` (likely the included paper, confirm by eye)")
    summary.append("5. Otherwise → `NEW`\n")
    summary.append("## Result")
    order = ["NEW", "NEEDS_REVIEW", "AUTHOR_YEAR_HIT", "DUP_DOI", "DUP_TITLE", "ALREADY_INCLUDED"]
    for k in order:
        if k in counts:
            summary.append(f"- **{k}**: {counts[k]:,}")
    summary.append("")
    summary.append("## How to screen")
    summary.append(f"Open **`{OUT_XLSX.name}`** and work the sheets in this order:")
    summary.append("1. **`NEW_only`** — primary screening target.")
    summary.append("2. **`NEEDS_REVIEW`** — borderline fuzzy matches; ~1 minute each to adjudicate.")
    summary.append("3. **`AUTHOR_YEAR_HIT`** — confirm these really are the included studies, then ignore.")
    summary.append("4. **`DUP_DOI`** / **`DUP_TITLE`** / **`ALREADY_INCLUDED`** — already screened in the prior review, no action needed unless you want to spot-check.")
    OUT_MD.write_text("\n".join(summary), encoding="utf-8")
    print(f"Wrote {OUT_MD}")
    print("\nDone.")


if __name__ == "__main__":
    main()
