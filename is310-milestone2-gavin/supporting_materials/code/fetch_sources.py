"""Freeze public inputs. Existing downloads are reused, never overwritten."""
import datetime
import hashlib
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "supporting_materials" / "raw_data"
RAW.mkdir(parents=True, exist_ok=True)
COMMIT = "59c767596750f554ba464de94cf4fce8664a6cbe"
BASE = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/" + COMMIT
SOURCES = {
    "fpl_players_2024-25.csv": BASE + "/data/2024-25/players_raw.csv",
    "fpl_teams_2024-25.csv": BASE + "/data/2024-25/teams.csv",
    "fpl_README.md": BASE + "/README.md",
    "fpl_LICENSE.txt": BASE + "/LICENSE",
    "fpl_getters.py": BASE + "/getters.py",
    "kaggle_metadata.json": "https://www.kaggle.com/api/v1/datasets/view/flynn28/eafc26-player-database",
    "kaggle_fc26_v1.zip": "https://www.kaggle.com/api/v1/datasets/download/flynn28/eafc26-player-database?datasetVersionNumber=1",
}
for filename, url in SOURCES.items():
    target = RAW / filename
    if target.exists():
        print(filename, "already exists; unchanged")
        continue
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "IS310-source-audit/1.0"})
        with urllib.request.urlopen(request, timeout=40) as response:
            payload = response.read()
            final_url = response.geturl().split("?")[0]
        if filename.endswith(".json"):
            json.loads(payload)
        if filename.endswith(".zip") and not payload.startswith(b"PK"):
            raise ValueError("Download did not return a ZIP")
        with target.open("xb") as stream:
            stream.write(payload)
        record = {
            "source_url": url,
            "retrieved_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "sha256": hashlib.sha256(payload).hexdigest(),
            "bytes": len(payload),
            "github_commit": COMMIT if "githubusercontent" in url else None,
        }
        (RAW / (filename + ".provenance.json")).write_text(json.dumps(record, indent=2) + "\n")
        print(filename, len(payload), record["sha256"])
    except Exception as error:
        print(filename, type(error).__name__, str(error))
