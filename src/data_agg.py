import pandas as pd
import os

TOURNAMENTS = ["vct_2023", "vct_2024", "vct_2025"]

FILES = [
    "scores",
    "overview",
    "eco_stats",
    "kills_stats",
    "draft_phase",
    "maps_scores",
    "maps_played",
    "teams_picked_agents",
    "players_stats",
    "tournaments_stages_matches_games_ids"
]

os.makedirs("aggregated", exist_ok=True)

for file in FILES:
    frames = []
    for tournament in TOURNAMENTS:
        path = os.path.join("data", tournament, "matches", f"{file}.csv")
        if not os.path.exists(path):
            print(f"missing: {tournament}/{file}.csv")
            continue
        df = pd.read_csv(path)
        df["tournament"] = tournament
        frames.append(df)
        print(f"ok: {tournament}/{file}.csv → {len(df)} rows")

    combined = pd.concat(frames, ignore_index=True)
    combined.to_csv(f"aggregated/{file}.csv", index=False)
    print(f"saved: aggregated/{file}.csv → {len(combined)} rows")

print("Done.")