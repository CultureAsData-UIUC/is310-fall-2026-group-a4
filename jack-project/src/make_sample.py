#!/usr/bin/env python3
"""make_sample.py - build a documented, reproducible sampling frame of drafted quarterbacks.

Frame: every player nflverse records at position QB, drafted 2013-2022.
Strata: 2 draft eras x 3 round groups. Sample up to PER_STRATUM players per stratum
(fixed seed), so the sample is not hand-picked and anyone can regenerate it.

Input : data/audit/draft_picks.csv   (nflverse draft picks, downloaded from the nflverse-data releases)
Output: data/sample/qb_frame.csv     (full frame, 113 rows)
        data/sample/qb_sample.csv    (sampled rows, identifiers only)
"""
from pathlib import Path

import pandas as pd

SEED = 310
PER_STRATUM = 10
ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "audit" / "draft_picks.csv"
OUT = ROOT / "data" / "sample"

KEEP = ["season", "round", "pick", "team", "pfr_player_name", "pfr_player_id",
        "gsis_id", "college", "games"]


def main():
    d = pd.read_csv(SRC)
    f = d[(d.position == "QB") & d.season.between(2013, 2022)].copy()
    f["era"] = pd.cut(f.season, [2012, 2017, 2022], labels=["2013-17", "2018-22"])
    f["round_group"] = pd.cut(f["round"], [0, 1, 3, 7], labels=["R1", "R2-3", "R4-7"])
    OUT.mkdir(parents=True, exist_ok=True)
    f[KEEP + ["era", "round_group"]].to_csv(OUT / "qb_frame.csv", index=False)

    parts = []
    for (era, rg), g in f.groupby(["era", "round_group"], observed=True):
        parts.append(g.sample(n=min(PER_STRATUM, len(g)), random_state=SEED))
    s = pd.concat(parts).sort_values(["season", "pick"])
    s[KEEP + ["era", "round_group"]].to_csv(OUT / "qb_sample.csv", index=False)
    print(f"frame: {len(f)} QBs | sample: {len(s)} QBs | seed={SEED}")
    print(s.groupby(["era", "round_group"], observed=True).size().to_string())


if __name__ == "__main__":
    main()
