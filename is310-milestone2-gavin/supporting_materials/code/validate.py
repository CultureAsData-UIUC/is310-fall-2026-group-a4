"""Validate provenance, deterministic sampling, source values and review completeness."""
import argparse
import json
import math
from collections import Counter
from pathlib import Path
from project import ROOT, HUMAN_FIELDS, JUDGMENTS, RATINGS, build_rows, keyed, read_csv, sha256


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", default=str(ROOT / "dataset.csv"))
    parser.add_argument("--final", action="store_true")
    args = parser.parse_args()
    errors = []
    manifest = json.loads((ROOT / "supporting_materials/raw_data/source_manifest.json").read_text())
    for source in manifest["files"]:
        if sha256(ROOT / source["path"]) != source["sha256"]:
            errors.append("Changed source checksum: " + source["path"])
    rows = read_csv(args.dataset)
    current = keyed(rows, "fpl_id")
    expected = keyed(build_rows(), "fpl_id")
    if set(current) != set(expected) or len(rows) != 60:
        errors.append("Expected exactly the 60 preselected, unique FPL IDs")
    if len({r["ea_id"] for r in rows}) != len(rows):
        errors.append("EA IDs are not unique")
    if Counter(r["fpl_role"] for r in rows) != {"DEF": 20, "MID": 20, "FWD": 20}:
        errors.append("Role quotas must be 20 DEF, 20 MID, 20 FWD")
    for fid in set(current) & set(expected):
        row, original = current[fid], expected[fid]
        if set(row) != set(original):
            errors.append(fid + ": unexpected/missing columns")
            continue
        for field, value in original.items():
            if row[field] != str(value):
                errors.append(fid + ": stale or altered " + field + "; rebuild into a new directory")
        if int(row["minutes"]) < 900:
            errors.append(fid + ": fewer than 900 minutes")
        for field in RATINGS:
            if not 1 <= int(row["ea_" + field.lower()]) <= 99:
                errors.append(fid + ": out-of-range rating " + field)
        for field in ("goals_p90", "fpl_assists_p90", "xg_p90", "xa_p90"):
            if not math.isfinite(float(row[field])) or float(row[field]) < 0:
                errors.append(fid + ": invalid " + field)
    if args.final:
        links = keyed(read_csv(ROOT / "supporting_materials/code/inputs/identity_crosswalk.csv"), "fpl_id")
        for row in rows:
            fid = row["fpl_id"]
            link = links[fid]
            if link["review_status"] != "reviewed" or not link["reviewer"].strip() or not link["review_evidence"].strip():
                errors.append(fid + ": identity not reviewed")
            required = [f for f in HUMAN_FIELDS if f != "context_source_url"]
            if any(not row[f].strip() for f in required) or row["review_status"] != "reviewed":
                errors.append(fid + ": note review incomplete")
            if row["alignment_judgment"] not in JUDGMENTS:
                errors.append(fid + ": choose a permitted interpretation judgment")
            dimension, metric = row["chosen_dimension"], row["primary_metric"]
            permitted = {
                "SHO": {"goals_p90", "xg_p90", "not_testable"},
                "PAS": {"xa_p90", "fpl_assists_p90", "not_testable"},
                "DEF": {"not_testable"}, "PAC": {"not_testable"},
                "DRI": {"not_testable"}, "PHY": {"not_testable"}, "OVR": {"not_testable"},
            }
            if dimension not in permitted or metric not in permitted.get(dimension, set()):
                errors.append(fid + ": unsupported rating/metric pair")
            if metric == "not_testable" and row["alignment_judgment"] != "insufficient_evidence":
                errors.append(fid + ": not_testable requires insufficient_evidence")
        audits = read_csv(ROOT / "supporting_materials/code/inputs/source_checks.csv")
        if len(audits) != 10 or len({r["fpl_id"] for r in audits}) != 10:
            errors.append("Expected 10 distinct source audit checks")
        for row in audits:
            if row["review_status"] != "reviewed" or not all(row[f].strip() for f in ("reviewer", "checked_at", "finding", "evidence_url")):
                errors.append(row["fpl_id"] + ": source audit incomplete")
        scope = json.loads((ROOT / "supporting_materials/code/inputs/rating_scope_review.json").read_text())
        if scope["decision"] not in ("verified_launch_base", "accept_frozen_extract_with_limitations") or not all(scope[f].strip() for f in ("reviewer", "evidence", "date")):
            errors.append("Researcher must resolve/document FC26 rating snapshot scope")
    if errors:
        print("NOT READY:", len(errors), "issue(s)")
        for error in errors[:15]:
            print("-", error)
        if len(errors) > 15:
            print("- Additional issues omitted from this display.")
        raise SystemExit(1)
    print("PASS:", "final completeness checks" if args.final else "60 candidate rows, role quotas, source values and checksums")
    if not args.final:
        print("Note review is recorded. Identity review, source audit and rating scope remain separate checks.")


if __name__ == "__main__":
    main()
