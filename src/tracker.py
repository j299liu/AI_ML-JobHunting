import duckdb, pandas as pd
from pathlib import Path

DB = "data/jobs.duckdb"

def init_db():
    con = duckdb.connect(DB)
    con.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id TEXT PRIMARY KEY,
        title TEXT,
        company TEXT,
        location TEXT,
        url TEXT,
        source TEXT,
        published_at TIMESTAMP,
        snippet TEXT,
        cluster TEXT,
        score DOUBLE,
        status TEXT DEFAULT 'To apply',
        next_action TEXT,
        notes TEXT
    );
    """)
    con.close()

def upsert_jobs(rows):
    con = duckdb.connect(DB)
    for r in rows:
        con.execute("""
            INSERT OR REPLACE INTO jobs
            SELECT ?,?,?,?,?,?,?,?,?,?,?,?,?
        """, (
            r["id"], r.get("title"), r.get("company"), r.get("location"),
            r.get("url"), r.get("source"), r.get("published_at"),
            r.get("snippet"), r.get("cluster"), r.get("score"),
            r.get("status","To apply"), r.get("next_action"), r.get("notes")
        ))
    con.close()

def export_csv(path="data/exports/today.csv"):
    con = duckdb.connect(DB)
    df = con.execute("SELECT * FROM jobs ORDER BY published_at DESC").df()
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    con.close()
    return path