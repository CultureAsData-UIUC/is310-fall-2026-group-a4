
import csv
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

# File locations
folder = Path(__file__).resolve().parent
source = Path(
    r"C:\Users\kings\Downloads\football-datasets-full"
    r"\datalake\transfermarkt"
)

matches_file = folder / "player_matches.csv"
profiles_file = source / "player_profiles" / "player_profiles.csv"
values_file = source / "player_market_value" / "player_market_value.csv"
performances_file = source / "player_performances" / "player_performances.csv"
output_file = folder / "ballon_dor_analysis_dataset.csv"

# Load ranked player-year entries
with matches_file.open(encoding="utf-8-sig", newline="") as f:
    rankings = list(csv.DictReader(f))

player_ids = {
    row["player_id"] for row in rankings if row["player_id"]
}

# Load player profiles
profiles = {}

with profiles_file.open(encoding="utf-8-sig", newline="") as f:
    for row in csv.DictReader(f):
        if row["player_id"] in player_ids:
            profiles[row["player_id"]] = row

# Load historical market values
# Use the most recent recorded value on or before December 31
# of the award year, not a value from a later year.
market_values = defaultdict(list)

with values_file.open(encoding="utf-8-sig", newline="") as f:
    for row in csv.DictReader(f):
        if row["player_id"] in player_ids:
            try:
                recorded = date.fromisoformat(row["date_unix"][:10])
                value = float(row["value"])
                market_values[row["player_id"]].append(
                    (recorded, value)
                )
            except (ValueError, TypeError):
                continue

for records in market_values.values():
    records.sort(key=lambda item: item[0])

# Aggregate performance by season.
# season_name is stored as a year, e.g. 2021.
performance = defaultdict(
    lambda: {
        "appearances": 0,
        "goals": 0,
        "assists": 0,
        "minutes_played": 0
    }
)

def number(value):
    try:
        return int(float(value))
    except (ValueError, TypeError):
        return 0


with performances_file.open(encoding="utf-8-sig", newline="") as f:
    for row in csv.DictReader(f):
        pid = row["player_id"]
        season = row["season_name"]

        if pid not in player_ids:
            continue

        season_to_year = {
            "20/21": "2021",
            "21/22": "2022",
            "22/23": "2023",
            "23/24": "2024",
            "24/25": "2025",
        }

        award_year = season_to_year.get(season)

        if award_year is None:
            continue

        stats = performance[(pid, award_year)]
        stats["appearances"] += number(row["nb_on_pitch"])
        stats["goals"] += number(row["goals"])
        stats["assists"] += number(row["assists"])
        stats["minutes_played"] += number(row["minutes_played"])


# Build the final dataset
results = []


for row in rankings:
    pid = row["player_id"]
    year = int(row["award_year"])
    profile = profiles.get(pid, {})

    # Age on December 31 of the award year
    age = ""
    dob = profile.get("date_of_birth", "")

    if dob:
        try:
            born = date.fromisoformat(dob[:10])
            reference = date(year, 12, 31)
            age = (
                reference.year - born.year
                - (
                    (reference.month, reference.day)
                    < (born.month, born.day)
                )
            )
        except ValueError:
            pass

    # Find the latest market value available by year-end
    market_value = ""
    market_value_date = ""

    eligible = [
        (recorded, value)
        for recorded, value in market_values.get(pid, [])
        if recorded <= date(year, 12, 31)
    ]

    if eligible:
        recorded, value = eligible[-1]
        market_value = int(value)
        market_value_date = recorded.isoformat()

    stats = performance.get((pid, str(year)))

    results.append({
        "award_year": year,
        "ballon_dor_rank": row["official_rank"],
        "player_name": row["player_name"],
        "player_id": pid,
        "match_status": row["match_status"],
        "age_at_year_end": age,
        "position": profile.get("position", ""),
        "market_value_eur": market_value,
        "market_value_date": market_value_date,
        "appearances": stats["appearances"] if stats else "",
        "goals": stats["goals"] if stats else "",
        "assists": stats["assists"] if stats else "",
        "minutes_played": stats["minutes_played"] if stats else "",
        "ranking_source": row["ranking_source"]
    })

# Save CSV
with output_file.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print(f"Total rows: {len(results)}")
print(f"Rows with player IDs: {sum(bool(r['player_id']) for r in results)}")
print(f"Rows with market values: {sum(r['market_value_eur'] != '' for r in results)}")
print(f"Rows with performance data: {sum(r['appearances'] != '' for r in results)}")
print(f"Dataset saved to: {output_file}")

