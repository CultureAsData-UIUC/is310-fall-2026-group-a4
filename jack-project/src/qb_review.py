#!/usr/bin/env python3
"""qb_review.py - hand-coding tool for the QB scouting-language dataset.

Commands
  review    walk through sampled players not yet coded and record YOUR codes
  validate  check data/coded/qb_records.csv against docs/codebook.md
  status    show progress by stratum

The script supplies the sample and checks your entries. You read each WalterFootball report
and make every coding decision. Never paste full report text; keywords are short phrases.
"""
import argparse
import csv
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
SAMPLE = ROOT / "data" / "sample" / "qb_sample.csv"
OUT = ROOT / "data" / "coded" / "qb_records.csv"

CARRIED = ["season", "round", "pick", "team", "pfr_player_name", "pfr_player_id",
           "gsis_id", "college", "era", "round_group"]
CODED = ["report_found", "report_url", "report_year_shown", "athleticism_emphasis",
         "intellect_emphasis", "athletic_keywords", "intellect_keywords",
         "comparison_player", "overall_tone", "confidence", "notes"]
FIELDS = CARRIED + CODED
ENUMS = {
    "report_found": {"yes", "no"},
    "athleticism_emphasis": {"none", "some", "prominent"},
    "intellect_emphasis": {"none", "some", "prominent"},
    "overall_tone": {"positive", "mixed", "negative"},
    "confidence": {"high", "medium", "low"},
}
KEYWORD_FIELDS = ["athletic_keywords", "intellect_keywords"]
MAX_KEYWORDS, MAX_WORDS = 5, 4


def ask(prompt, allowed=None, required=True):
    while True:
        v = input(prompt).strip()
        if v == "":
            if required:
                print("  (required)")
                continue
            return ""
        if allowed is None or v in allowed:
            return v
        print(f"  allowed: {sorted(allowed)}")


def ask_keywords(prompt):
    while True:
        v = input(prompt).strip()
        if v == "":
            return ""
        parts = [p.strip() for p in v.split(";") if p.strip()]
        if len(parts) > MAX_KEYWORDS or any(len(p.split()) > MAX_WORDS for p in parts):
            print(f"  max {MAX_KEYWORDS} phrases, {MAX_WORDS} words each, ';'-separated")
            continue
        return ";".join(parts)


def load_out():
    if not OUT.exists():
        return []
    with OUT.open(newline="") as fh:
        return list(csv.DictReader(fh))


def cmd_review(args):
    OUT.parent.mkdir(parents=True, exist_ok=True)
    s = pd.read_csv(SAMPLE)
    done = {r["pfr_player_name"] + r["season"] for r in load_out()}
    todo = s[~(s.pfr_player_name + s.season.astype(str)).isin(done)]
    print(f"{len(todo)} players left. Type 'quit' at the first prompt to stop.")
    new_file = not OUT.exists()
    with OUT.open("a", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        if new_file:
            w.writeheader()
        for _, p in todo.iterrows():
            print("\n" + "=" * 70)
            print(f"{p.pfr_player_name} | {p.season} round {p['round']} pick {p.pick} | {p.team} | {p.college}")
            print(f'Search: site:walterfootball.com scouting report {p.pfr_player_name} {p.season}')
            first = input("report found? [yes/no/quit]: ").strip()
            if first == "quit":
                break
            if first not in ENUMS["report_found"]:
                print("  invalid; skipping for now")
                continue
            rec = {k: p[k] for k in CARRIED}
            rec["report_found"] = first
            if first == "no":
                for k in CODED[1:]:
                    rec[k] = ""
                rec["notes"] = ask("notes (where did you look?): ", required=False)
            else:
                rec["report_url"] = ask("report URL: ")
                rec["report_year_shown"] = ask("year/date shown on page (blank if none): ", required=False)
                rec["athleticism_emphasis"] = ask("athleticism emphasis [none/some/prominent]: ", ENUMS["athleticism_emphasis"])
                rec["intellect_emphasis"] = ask("intellect/leadership emphasis [none/some/prominent]: ", ENUMS["intellect_emphasis"])
                rec["athletic_keywords"] = ask_keywords("athletic keywords (; separated, <=5 phrases): ")
                rec["intellect_keywords"] = ask_keywords("intellect keywords (; separated, <=5 phrases): ")
                rec["comparison_player"] = ask("player comparison given (blank if none): ", required=False)
                rec["overall_tone"] = ask("overall tone [positive/mixed/negative]: ", ENUMS["overall_tone"])
                rec["confidence"] = ask("confidence [high/medium/low]: ", ENUMS["confidence"])
                rec["notes"] = ask("notes (interpretive decisions): ", required=False)
            w.writerow(rec)
            fh.flush()


def cmd_validate(args):
    rows = load_out()
    if not rows:
        print("no coded records yet")
        return
    problems, seen = 0, set()
    for i, r in enumerate(rows, start=2):
        def bad(msg):
            nonlocal problems
            problems += 1
            print(f"line {i} ({r.get('pfr_player_name', '?')} {r.get('season', '')}): {msg}")
        key = r["pfr_player_name"] + r["season"]
        if key in seen:
            bad("duplicate player")
        seen.add(key)
        found = r.get("report_found")
        if found not in ENUMS["report_found"]:
            bad("report_found must be yes/no")
            continue
        if found == "yes":
            for k in ("report_url", "athleticism_emphasis", "intellect_emphasis", "overall_tone", "confidence"):
                if not r.get(k):
                    bad(f"missing {k}")
            for k, allowed in ENUMS.items():
                if k != "report_found" and r.get(k) and r[k] not in allowed:
                    bad(f"{k}={r[k]!r} not allowed")
            for k in KEYWORD_FIELDS:
                parts = [p for p in r.get(k, "").split(";") if p]
                if len(parts) > MAX_KEYWORDS or any(len(p.split()) > MAX_WORDS for p in parts):
                    bad(f"{k} breaks the keyword length rule")
        else:
            filled = [k for k in CODED[1:-1] if r.get(k)]
            if filled:
                bad(f"report_found=no but these are filled: {filled}")
    print(f"{len(rows)} records checked, {problems} problems")


def cmd_status(args):
    s = pd.read_csv(SAMPLE)
    out = pd.DataFrame(load_out())
    total = s.groupby(["era", "round_group"]).size().rename("sampled")
    if out.empty:
        print(total.to_string())
        print("\n0 coded")
        return
    got = out.groupby(["era", "round_group"]).size().rename("coded")
    print(pd.concat([total, got], axis=1).fillna(0).astype(int).to_string())
    print(f"\n{len(out)} of {len(s)} coded; reports found: {(out.report_found == 'yes').sum()}, not found: {(out.report_found == 'no').sum()}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("review").set_defaults(fn=cmd_review)
    sub.add_parser("validate").set_defaults(fn=cmd_validate)
    sub.add_parser("status").set_defaults(fn=cmd_status)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
