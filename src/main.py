import yaml, re
from pathlib import Path
from tqdm import tqdm
from src.ingest import parse_rss
from src.cluster_score import assign_cluster, score_fit
from src.tracker import init_db, upsert_jobs, export_csv
from src.dedupe import near_duplicate

def guess_company_location(title, snippet):
    text = f"{title} — {snippet}"
    # very rough heuristics; feel free to improve via page scraping
    company = None
    m = re.search(r" at ([A-Z][A-Za-z0-9& .-]+)", text)
    if m: company = m.group(1).strip()
    loc = None
    for cand in ["Remote UK","London","Cambridge","Oxford","Bristol","Manchester","Edinburgh","Glasgow","Leeds","Birmingham","Reading"]:
        if cand.lower() in text.lower():
            loc = cand; break
    return company, loc

def run(config_path="config/settings.yaml"):
    cfg = yaml.safe_load(Path(config_path).read_text())
    init_db()

    # 1) Ingest
    raw = []
    for url in cfg["rss_feeds"]:
        raw.extend(list(parse_rss(url, cfg["timezone"])))

    # 2) Deduplicate within batch
    unique = []
    for r in raw:
        if not any(near_duplicate(r, u) for u in unique):
            unique.append(r)

    # 3) Enrich (cluster + score + company/location)
    profile = cfg["candidate_profile"]
    for r in unique:
        text = " ".join(filter(None, [r.get("title"), r.get("snippet")]))
        r["cluster"] = assign_cluster(text)
        r["score"] = score_fit(text, profile["skills"], profile["locations_ok"])
        company, loc = guess_company_location(r.get("title",""), r.get("snippet",""))
        if company: r["company"] = company
        if loc: r["location"] = loc

    # 4) Filter out excluded terms
    excl = [t.lower() for t in cfg.get("exclude_terms",[])]
    filtered = [r for r in unique if not any(t in (r.get("snippet","")+r.get("title","")).lower() for t in excl)]

    # 5) Persist + export
    upsert_jobs(filtered)
    out_csv = export_csv()
    print(f"Exported {len(filtered)} jobs → {out_csv}")

if __name__ == "__main__":
    run()