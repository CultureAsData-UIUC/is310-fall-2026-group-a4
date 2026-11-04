
import csv
import re
import unicodedata
from pathlib import Path
from difflib import get_close_matches

# File locations
project_folder = Path(__file__).resolve().parent
rankings_file = project_folder / "ballon_dor_top20_2021_2025.csv"

profiles_file = Path(
    r"C:\Users\kings\Downloads\football-datasets-full"
    r"\datalake\transfermarkt\player_profiles\player_profiles.csv"
)

output_file = project_folder / "player_matches.csv"


def clean_name(name):
    """Standardize names to make comparisons easier."""
    name = re.sub(r"\s*\(\d+\)\s*$", "", name)
    name = unicodedata.normalize("NFKD", name)
    name = "".join(
        char for char in name
        if not unicodedata.combining(char)
    )
    name = name.lower()
    return re.sub(r"[^a-z0-9]", "", name)


# Load Transfermarkt player profiles
players = {}

with profiles_file.open(encoding="utf-8-sig", newline="") as file:
    for player in csv.DictReader(file):
        name = player["player_name"]
        key = clean_name(name)
        players.setdefault(key, []).append(player)

# Load Ballon d'Or rankings
with rankings_file.open(encoding="utf-8-sig", newline="") as file:
    rankings = list(csv.DictReader(file))

results = []

for entry in rankings:
    name = entry["player_name"]
    key = clean_name(name)

    matches = players.get(key, [])

    if len(matches) == 1:
        player = matches[0]
        status = "exact_name_match"
        player_id = player["player_id"]
        matched_name = player["player_name"]

    else:
        # Suggestions are not automatically accepted as matches.
        suggestions = get_close_matches(
            key, players.keys(), n=3, cutoff=0.65
        )

        status = (
            "ambiguous_exact_name"
            if len(matches) > 1
            else "needs_review"
        )
        player_id = ""
        matched_name = "; ".join(
            players[suggestion][0]["player_name"]
            for suggestion in suggestions
        )

    results.append({
        **entry,
        "player_id": player_id,
        "matched_name": matched_name,
        "match_status": status
    })

# Manually verified Transfermarkt player IDs
verified_ids = {
    "Jorginho": "102017",
    "Son Heung-min": "91845",
    "N'Golo Kanté": "225083",
    "Rodri": "357565",
    "Dani Carvajal": "138927",
    "Emiliano Martínez": "111873",
    "Raphinha": "411295",
    "Vitinha": "487469",
    "Nuno Mendes": "616341",
    "Luis Díaz": "480692",
    "Fabinho": "225693",
    "Yassine Bounou": "207834",
    "Luis Suárez": "44352",
}

for result in results:
    name = result["player_name"]

    if name in verified_ids:
        result["player_id"] = verified_ids[name]
        result["matched_name"] = name
        result["match_status"] = "manually_verified"

    elif name == "Simon Kjær":
        result["player_id"] = ""
        result["matched_name"] = ""
        result["match_status"] = "not_found"

# Save results
with output_file.open("w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print(f"Total entries: {len(results)}")
print(f"Exact matches: {sum(r['match_status'] == 'exact_name_match' for r in results)}")
print(f"Need review: {sum(r['match_status'] != 'exact_name_match' for r in results)}")
print(f"Results saved to: {output_file}")
