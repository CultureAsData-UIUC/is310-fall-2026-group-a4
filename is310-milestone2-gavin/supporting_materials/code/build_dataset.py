"""Join the fixed sample and review tables into a NEW output directory."""
import argparse
import json
from collections import Counter
from pathlib import Path
from project import ROOT, build_rows, sha256, write_csv, write_json


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, help="A directory that does not already exist")
    args = parser.parse_args()
    target = Path(args.output).resolve()
    if target.exists():
        parser.error("Output already exists. Choose a new path; existing work will not be overwritten.")
    manifest = json.loads((ROOT / "supporting_materials/raw_data/source_manifest.json").read_text())
    for source in manifest["files"]:
        if sha256(ROOT / source["path"]) != source["sha256"]:
            raise ValueError("Raw input checksum changed: " + source["path"])
    rows = build_rows()
    target.mkdir(parents=True, exist_ok=False)
    write_csv(target / "dataset.csv", rows)
    write_json(target / "build_manifest.json", {
        "rows": len(rows), "role_counts": dict(Counter(r["fpl_role"] for r in rows)),
        "sampling": "900+ minutes; 20 per FPL role; ascending SHA256('310:element_type:id')",
        "sampling_independent_of": ["EA ratings", "goals", "xG", "assists", "xA"],
        "interpretations": dict(Counter(r["review_status"] for r in rows)),
        "note_reviewers": dict(Counter(r["reviewed_by"] for r in rows)),
        "output_sha256": sha256(target / "dataset.csv"),
        "review_input_sha256": {str(p.relative_to(ROOT)): sha256(p) for p in sorted((ROOT / "supporting_materials/code/inputs").glob("*.csv"))},
        "source_manifest_sha256": sha256(ROOT / "supporting_materials/raw_data/source_manifest.json"),
        "readiness": "notes reviewed; run validate.py --final to check identity and source-audit completeness",
    })
    print("Created", target / "dataset.csv", "with", len(rows), "candidate rows.")


if __name__ == "__main__":
    main()
