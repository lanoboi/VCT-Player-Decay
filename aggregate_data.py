import pandas as pd
import os

TOURNAMENTS = ["bangkok", "paris", "toronto"]
FILES = [
    "matches",
    "detailed_matches_player_stats",
    "performance_data",
    "economy_data",
    "detailed_matches_maps",
    "player_stats",
    "maps_stats"
]

for file in FILES:
    frames = []
    for tournament in TOURNAMENTS:
        path = os.path.join("data", tournament, f"{file}.csv")
        if not os.path.exists(path):
            print(f"missing: {tournament}/{file}.csv")
            continue
        df = pd.read_csv(path)
        df["tournament"] = tournament
        frames.append(df)
        print(f"good: {tournament}/{file}.csv → {len(df)} rows")

    combined = pd.concat(frames, ignore_index=True)
    combined.to_csv(f"aggregated_{file}.csv", index=False)
    print("done")