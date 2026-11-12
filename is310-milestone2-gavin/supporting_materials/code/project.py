"""Shared, standard-library-only tools for the IS310 season comparison."""
import csv
import hashlib
import io
import json
import math
import re
import unicodedata
import zipfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROLES = {"2": "DEF", "3": "MID", "4": "FWD"}
RATINGS = ("OVR", "PAC", "SHO", "PAS", "DRI", "DEF", "PHY")
HUMAN_FIELDS = (
    "chosen_dimension", "primary_metric", "alignment_judgment",
    "evidence_note", "limitation_note", "context_source_url",
    "reviewed_by", "review_date", "review_status",
)
JUDGMENTS = {"broadly_consistent", "apparent_tension", "mixed_evidence", "insufficient_evidence"}


def read_csv(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def write_csv(path, rows, fields=None):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields or list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(data, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write("\n")


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def normalize(name):
    text = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", text)


def sample_key(row):
    return hashlib.sha256(("310:" + row["element_type"] + ":" + row["id"]).encode()).hexdigest()


def inputs():
    players = read_csv(ROOT / "supporting_materials/raw_data/fpl_players_2024-25.csv")
    teams = {r["id"]: r["name"] for r in read_csv(ROOT / "supporting_materials/raw_data/fpl_teams_2024-25.csv")}
    with zipfile.ZipFile(ROOT / "supporting_materials/raw_data/kaggle_fc26_v1.zip") as archive:
        ratings = list(csv.DictReader(io.StringIO(archive.read("EAFC26-Men.csv").decode("utf-8-sig"))))
    return players, teams, ratings


def select(players):
    selected = []
    for code in ROLES:
        eligible = [r for r in players if r["element_type"] == code and int(r["minutes"]) >= 900]
        if len(eligible) < 20:
            raise ValueError("Insufficient eligible players in role " + code)
        selected.extend(sorted(eligible, key=lambda r: (sample_key(r), int(r["id"])))[:20])
    return selected


def keyed(rows, field):
    result = {}
    for row in rows:
        value = row[field]
        if not value or value in result:
            raise ValueError("Missing or duplicate " + field + ": " + value)
        result[value] = row
    return result


def build_rows():
    players, teams, ratings = inputs()
    ea = keyed(ratings, "ID")
    links = keyed(read_csv(ROOT / "supporting_materials/code/inputs/identity_crosswalk.csv"), "fpl_id")
    reviews = keyed(read_csv(ROOT / "supporting_materials/code/inputs/player_interpretations.csv"), "fpl_id")
    rows = []
    for source in select(players):
        fid = source["id"]
        link, review = links[fid], reviews[fid]
        rating = ea[link["ea_id"]]
        minutes = int(source["minutes"])
        row = {
            "record_id": "FC26-2425-FPL-" + fid,
            "fpl_id": fid, "fpl_code": source["code"], "ea_id": rating["ID"],
            "player_name": rating["Name"],
            "fpl_name": source["first_name"] + " " + source["second_name"],
            "competition": "Premier League", "season": "2024-25",
            "club_2024_25_end": teams[source["team"]], "club_fc26": rating["Team"],
            "fpl_role": ROLES[source["element_type"]], "ea_position": rating["Position"],
            "minutes": minutes, "starts": int(source["starts"]),
            "goals": int(source["goals_scored"]), "fpl_assists": int(source["assists"]),
            "xg": float(source["expected_goals"]), "xa": float(source["expected_assists"]),
            "fpl_clean_sheets": int(source["clean_sheets"]),
        }
        for output, raw in (("goals_p90", "goals_scored"), ("fpl_assists_p90", "assists"),
                            ("xg_p90", "expected_goals"), ("xa_p90", "expected_assists")):
            row[output] = round(90 * float(source[raw]) / minutes, 6)
        row.update({"ea_" + field.lower(): int(rating[field]) for field in RATINGS})
        row.update({
            "ea_dataset_version": "Kaggle v1",
            "ea_dataset_uploaded_utc": "2025-11-24T17:14:17.667Z",
            "ea_rating_effective_date": "unknown",
            "ea_launch_scope_status": "not_verified",
            "ea_profile_url_as_recorded": rating["url"],
            "ea_source_locator": "supporting_materials/raw_data/kaggle_fc26_v1.zip::EAFC26-Men.csv#ID=" + rating["ID"],
            "season_source_locator": "supporting_materials/raw_data/fpl_players_2024-25.csv#id=" + fid,
            "match_method": link["match_method"], "identity_review_status": link["review_status"],
            "sample_key": sample_key(source),
            "computed_context": (
                "FPL clean sheets describe team outcomes with appearance rules; no direct DEF test."
                if row["fpl_role"] == "DEF" else
                "xA is a narrow chance-creation indicator; PAS also covers other passing skills."
                if row["fpl_role"] == "MID" else
                "Goals and xG depend on role, chances and penalties; SHO is a broader ability rating."
            ),
        })
        row.update({field: review[field] for field in HUMAN_FIELDS})
        rows.append(row)
    return rows


def ranks(values):
    ordered = sorted(enumerate(values), key=lambda pair: pair[1])
    result = [0.0] * len(values)
    start = 0
    while start < len(ordered):
        end = start + 1
        while end < len(ordered) and ordered[end][1] == ordered[start][1]:
            end += 1
        average = (start + 1 + end) / 2
        for index, _ in ordered[start:end]:
            result[index] = average
        start = end
    return result


def spearman(xs, ys):
    if len(xs) != len(ys) or len(xs) < 3:
        return None
    x, y = ranks(xs), ranks(ys)
    mx, my = sum(x) / len(x), sum(y) / len(y)
    numerator = sum((a - mx) * (b - my) for a, b in zip(x, y))
    denominator = math.sqrt(sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in y))
    return None if denominator == 0 else numerator / denominator
