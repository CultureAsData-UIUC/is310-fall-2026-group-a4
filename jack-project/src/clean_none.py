#!/usr/bin/env python3
"""clean_none.py - blank out literal "none" typed into free-text columns.

Only touches athletic_keywords, intellect_keywords, comparison_player, and only when the
WHOLE cell is exactly none / n/a / na (any capitalization). The emphasis columns, where
"none" is a real code, are never touched.

  py src/clean_none.py            preview only, changes nothing
  py src/clean_none.py --apply    back up the file, then make the changes
"""
import argparse
import shutil
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
F = ROOT / "data" / "coded" / "qb_records.csv"
BACKUP = ROOT / "data" / "coded" / "qb_records_backup_before_none_cleanup.csv"
COLS = ["athletic_keywords", "intellect_keywords", "comparison_player"]
JUNK = {"none", "n/a", "na"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    df = pd.read_csv(F, dtype=str, keep_default_na=False)
    changes = []
    for c in COLS:
        mask = df[c].str.strip().str.lower().isin(JUNK)
        for i in df.index[mask]:
            changes.append((df.at[i, "pfr_player_name"], df.at[i, "season"], c, df.at[i, c]))
            if a.apply:
                df.at[i, c] = ""
    for name, season, c, v in changes:
        print(f"{name} {season}: {c} = {v!r} -> blank")
    print(f"{len(changes)} cells {'cleaned' if a.apply else 'would change (preview only)'}")
    if a.apply:
        if not BACKUP.exists():
            shutil.copy(F, BACKUP)
        df.to_csv(F, index=False)
        print("saved. Backup:", BACKUP.name)


if __name__ == "__main__":
    main()