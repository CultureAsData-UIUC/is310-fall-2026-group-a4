"""Write descriptive, within-role associations to a NEW report file."""
import argparse
from collections import Counter
from project import ROOT, read_csv, spearman, write_json


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", default=str(ROOT / "dataset.csv"))
    parser.add_argument("--output", required=True, help="New JSON report path")
    args = parser.parse_args()
    rows = read_csv(args.dataset)
    results = []
    for role, rating, metric in (("FWD", "ea_sho", "goals_p90"), ("FWD", "ea_sho", "xg_p90"),
                                  ("MID", "ea_pas", "xa_p90"), ("MID", "ea_sho", "goals_p90")):
        group = [r for r in rows if r["fpl_role"] == role]
        rho = spearman([float(r[rating]) for r in group], [float(r[metric]) for r in group])
        results.append({"fpl_role": role, "rating": rating, "metric": metric, "n": len(group), "spearman_rho": rho})
    write_json(args.output, {
        "status": "exploratory; identity and source review may be pending",
        "role_counts": dict(Counter(r["fpl_role"] for r in rows)),
        "review_counts": dict(Counter(r["review_status"] for r in rows)),
        "note_reviewers": dict(Counter(r["reviewed_by"] for r in rows)),
        "associations": results,
        "limits": [
            "A correlation is not rating accuracy, causation or EA's formula.",
            "xG measures chance opportunity and xA a narrow passing outcome; neither is overall ability.",
            "Twenty records per role; coarse FPL categories mix tactical roles. No inferential significance claims.",
            "Defender clean sheets are context only. No DEF, PAC, DRI, PHY or OVR accuracy test.",
            "2024-25 PL statistics are compared with an FC26 extract uploaded November 2025; effective rating date is unknown.",
        ],
    })
    print("Wrote exploratory report:", args.output)


if __name__ == "__main__":
    main()
