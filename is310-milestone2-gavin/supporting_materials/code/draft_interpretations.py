"""Render 57 new AI proposals plus 3 earlier examples into NEW review files.

Does not edit the authoritative review table, mark a record reviewed, or generate
Gavin's authorship. Copy/adopt proposals only with honest drafting provenance.
"""
import argparse
import datetime
import json
from collections import Counter
from pathlib import Path
from interpretation_drafts import DRAFTS
from project import ROOT, JUDGMENTS, keyed, read_csv, sha256, write_csv, write_json

AUTHOR = "AI-assisted initial notes"


def context(row):
    return {
        "name": row["player_name"], "minutes": str(int(row["minutes"])),
        "starts": str(int(row["starts"])), "goals": str(int(row["goals"])),
        "fpl_assists": str(int(row["fpl_assists"])),
        "clean_sheets": str(int(row["fpl_clean_sheets"])),
        "sho": row["ea_sho"], "pas": row["ea_pas"], "defending": row["ea_def"],
        "xg": format(float(row["xg"]), "g"), "xa": format(float(row["xa"]), "g"),
        "goals90": format(float(row["goals_p90"]), ".3f"),
        "xg90": format(float(row["xg_p90"]), ".3f"),
        "xa90": format(float(row["xa_p90"]), ".3f"),
    }


def render(source):
    by_id = keyed(source, "fpl_id")
    if len(source) != 60 or set(by_id) != set(DRAFTS):
        raise ValueError("Draft catalog must match exactly the 60 source IDs")
    forwards = [r for r in source if r["fpl_role"] == "FWD"]
    if max(forwards, key=lambda r: float(r["goals_p90"]))["fpl_id"] != "251":
        raise ValueError("Source no longer supports the Muniz highest-rate statement")
    # Explicit controls for numbers used in comparisons with another player.
    peer_controls = {
        "335": ("80", "0.155"), "267": ("76", "0.156"), "45": ("75", "0.194"),
        "163": ("79", "0.072"), "210": ("68", "0.107"), "348": ("82", "0.271"),
        "17": ("85", "0.406"), "168": ("85", "0.187"),
    }
    for fid, (pas, xa90) in peer_controls.items():
        if by_id[fid]["ea_pas"] != pas or format(float(by_id[fid]["xa_p90"]), ".3f") != xa90:
            raise ValueError("Source no longer supports peer comparison: " + fid)
    reviews = []
    for row in source:
        proposal = DRAFTS[row["fpl_id"]]
        facts = context(row)
        evidence = proposal["evidence_note"].format(**facts)
        limitation = proposal["limitation_note"].format(**facts)
        if "{" in evidence + limitation or "}" in evidence + limitation:
            raise ValueError("Unfilled template marker")
        dimension = proposal["chosen_dimension"]
        metric = proposal["primary_metric"]
        if proposal["alignment_judgment"] not in JUDGMENTS:
            raise ValueError("Invalid judgment")
        rating = row[{"SHO": "ea_sho", "PAS": "ea_pas", "DEF": "ea_def"}[dimension]]
        if rating not in evidence:
            raise ValueError("Evidence does not reference its own rating: " + row["fpl_id"])
        if metric != "not_testable" and format(float(row[metric]), ".3f") not in evidence:
            raise ValueError("Evidence does not reference its chosen rate: " + row["fpl_id"])
        if metric == "not_testable" and proposal["alignment_judgment"] != "insufficient_evidence":
            raise ValueError("Untestable comparison must be labelled insufficient")
        reviews.append({
            "fpl_id": row["fpl_id"], "player_name_for_reference": row["player_name"],
            "chosen_dimension": dimension, "primary_metric": metric,
            "alignment_judgment": proposal["alignment_judgment"],
            "evidence_note": evidence, "limitation_note": limitation,
            "context_source_url": "", "interpretation_author": AUTHOR,
            "review_status": "needs_review",
        })
    if len({r["evidence_note"] for r in reviews}) != 60 or len({r["limitation_note"] for r in reviews}) != 60:
        raise ValueError("Drafts must have distinct evidence and limitation text")
    return reviews


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", default=str(ROOT / "dataset.csv"))
    parser.add_argument("--output", required=True, help="A NEW directory for draft files")
    args = parser.parse_args()
    output = Path(args.output).resolve()
    if output.exists():
        parser.error("Output exists; choose a new directory. Existing work will not be overwritten.")
    source = read_csv(args.dataset)
    reviews = render(source)
    output.mkdir(parents=True, exist_ok=False)
    write_csv(output / "player_interpretations.csv", reviews)
    pages = [
        "# 60-player draft comparison notes\n",
        "**AI-written proposals: 57 new notes plus the three earlier examples. All 60 remain `needs_review`.**\n",
        "These notes have not been authored or approved by Gavin. Identity links, ten source checks and the FC26 rating-scope decision remain pending.\n",
        "The source compares 2024-25 Premier League statistics with Kaggle FC26 v1, uploaded November 24, 2025; effective rating date is unknown. Ratings and performance indicators use different scales. No note estimates a deserved numerical rating.\n",
        "The judgments are provisional interpretations, not threshold-based classifications. FPL positions and later EA positions are distinct source representations; neither alone establishes actual season tactics.\n",
        "Edit the authoritative `data/review/player_interpretations.csv` after inspecting the sources, then rebuild to a new output. Preserve an honest record of AI assistance and the researcher's contribution.\n",
    ]
    current_role = None
    for index, (row, review) in enumerate(zip(source, reviews), 1):
        if row["fpl_role"] != current_role:
            current_role = row["fpl_role"]
            pages.append("## " + {"DEF": "FPL defenders", "MID": "FPL midfielders", "FWD": "FPL forwards"}[current_role] + "\n")
        facts = context(row)
        pages.extend([
            "### " + str(index) + ". " + row["player_name"] + "\n",
            "Record: `" + row["record_id"] + "`. EA position: " + row["ea_position"] + ".\n",
            "Source facts: " + facts["minutes"] + " minutes; " + facts["goals"] + " goals; " + facts["xg"] + " xG; " + facts["xa"] + " xA; " + facts["clean_sheets"] + " FPL clean sheets.\n",
            "Proposed comparison: **" + review["chosen_dimension"] + " / " + review["primary_metric"] + "**. Proposed judgment: `" + review["alignment_judgment"] + "`.\n",
            "**Evidence note:** " + review["evidence_note"] + "\n",
            "**Limitation note:** " + review["limitation_note"] + "\n",
            "Draft author: AI-assisted initial notes. Researcher review: pending.\n",
        ])
    with (output / "player_draft_notes.md").open("x", encoding="utf-8") as stream:
        stream.write("\n".join(pages))
    write_json(output / "draft_manifest.json", {
        "generated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "source_dataset_sha256": sha256(args.dataset),
        "source_manifest_sha256": sha256(ROOT / "supporting_materials/raw_data/source_manifest.json"),
        "draft_catalog_sha256": sha256(ROOT / "supporting_materials/code/interpretation_drafts.py"),
        "draft_csv_sha256": sha256(output / "player_interpretations.csv"),
        "counts": dict(Counter(DRAFTS[r["fpl_id"]]["draft_origin"] for r in source)),
        "judgment_counts": dict(Counter(r["alignment_judgment"] for r in reviews)),
        "dimension_counts": dict(Counter(r["chosen_dimension"] for r in reviews)),
        "author": AUTHOR, "review_status": "needs_review",
        "external_context_claims_added": False,
    })
    print("Created 57 new drafts plus 3 earlier examples:", output)


if __name__ == "__main__":
    main()
