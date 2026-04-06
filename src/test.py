import pandas as pd
scores = pd.read_csv("aggregated/scores.csv")
dupes = scores[scores.duplicated(subset=["Match Name", "Tournament", "Stage", "Match Type"], keep=False)]
print(f"Duplicate rows: {len(dupes)}")
print(dupes[["Match Name", "Tournament", "Stage", "Match Type"]].head(20).to_string())