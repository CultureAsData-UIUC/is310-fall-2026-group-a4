#!/usr/bin/env python3
"""analyze.py - first computation on the hand-coded QB scouting-language dataset.

Reads : data/coded/qb_records.csv   (your hand coding)
        data/audit/draft_picks.csv  (nflverse draft picks, the audit target)
Writes: data/output/availability_by_stratum.csv   report found vs not found
        data/output/emphasis_by_round_group.csv   emphasis codes among found reports
        data/output/qb_joined.csv                 your codes joined to nflverse fields
        data/output/emphasis_chart.png            one chart
Prints a short summary, including how well the join to nflverse worked.

Run: py src/analyze.py      (needs pandas and matplotlib)
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
CODED = ROOT / "data" / "coded" / "qb_records.csv"
DRAFT = ROOT / "data" / "audit" / "draft_picks.csv"
OUT = ROOT / "data" / "output"
NFLVERSE_FIELDS = ["position", "category", "age", "games", "w_av", "dr_av",
                   "allpro", "probowls", "seasons_started"]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    r = pd.read_csv(CODED, dtype=str, keep_default_na=False)
    r["found"] = r.report_found.eq("yes")
    strata = ["era", "round_group"]

    # 1. Which players have a report at all?
    avail = r.groupby(strata).agg(sampled=("found", "size"), found=("found", "sum"))
    avail["not_found"] = avail.sampled - avail.found
    avail["pct_found"] = (100 * avail.found / avail.sampled).round(0).astype(int)
    avail.to_csv(OUT / "availability_by_stratum.csv")
    print("REPORT AVAILABILITY (by era and round group)")
    print(avail.to_string(), "\n")

    # 2. Among found reports, how prominent are the two kinds of language?
    f = r[r.found]
    rows = []
    for col, label in [("athleticism_emphasis", "athleticism"), ("intellect_emphasis", "intellect")]:
        t = pd.crosstab(f.round_group, f[col]).reindex(columns=["none", "some", "prominent"], fill_value=0)
        t.insert(0, "language", label)
        t["n_reports"] = t[["none", "some", "prominent"]].sum(axis=1)
        rows.append(t.reset_index())
    emph = pd.concat(rows, ignore_index=True)
    emph.to_csv(OUT / "emphasis_by_round_group.csv", index=False)
    print("EMPHASIS AMONG FOUND REPORTS (counts, by round group)")
    print(emph.to_string(index=False), "\n")

    # 3. Join to nflverse
    d = pd.read_csv(DRAFT, dtype={"pfr_player_id": str, "gsis_id": str})
    keep = ["pfr_player_id"] + [c for c in NFLVERSE_FIELDS if c in d.columns]
    d1 = d[keep].drop_duplicates("pfr_player_id")
    j = r.merge(d1, on="pfr_player_id", how="left", suffixes=("", "_nflverse"), indicator=True)
    matched = (j["_merge"] == "both").sum()
    j.drop(columns="_merge").to_csv(OUT / "qb_joined.csv", index=False)
    print(f"JOIN TO NFLVERSE on pfr_player_id: {matched} of {len(r)} matched")
    missing = j[j["_merge"] != "both"]
    if len(missing):
        print("not matched:", ", ".join(missing.pfr_player_name))
    print("nflverse fields joined:", ", ".join(keep[1:]))
    print("nflverse columns that describe scouting language: none (that is what your dataset adds)\n")

    # 4. One chart
    order = ["R1", "R2-3", "R4-7"]
    pct = {}
    for col, label in [("athleticism_emphasis", "athleticism"), ("intellect_emphasis", "intellect/leadership")]:
        pct[label] = [100 * (f[f.round_group == g][col] == "prominent").mean() if (f.round_group == g).any() else 0
                      for g in order]
    n = [int((f.round_group == g).sum()) for g in order]
    x = range(len(order))
    fig, ax = plt.subplots(figsize=(7, 4.2))
    w = 0.38
    ax.bar([i - w / 2 for i in x], pct["athleticism"], w, label="athleticism", color="#1f6f8b")
    ax.bar([i + w / 2 for i in x], pct["intellect/leadership"], w, label="intellect/leadership", color="#e07a2f")
    ax.set_xticks(list(x))
    ax.set_xticklabels([f"{g}\n(n={k} reports)" for g, k in zip(order, n)])
    ax.set_ylabel("% of found reports coded 'prominent'")
    ax.set_title("Prominent scouting language by round group (WalterFootball, 2013-2022 QBs)")
    ax.legend()
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(OUT / "emphasis_chart.png", dpi=150)
    print("saved tables and chart to data/output/")


if __name__ == "__main__":
    main()
