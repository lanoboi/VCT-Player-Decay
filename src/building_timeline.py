import pandas as pd

df = pd.read_csv("cleaned_player_stats.csv")

#sortinng matches by when they happened per player
df["match_date"] = pd.to_datetime(df["match_date"])
df = df.sort_values(["player_id", "match_date"]).reset_index(drop=True)

#adding condition that player neeeds at least 10 matches to keep integrity
match_counts = df.groupby("player_id")["match_id"].count()
qualified = match_counts[match_counts >= 10].index
df = df[df["player_id"].isin(qualified)].copy()

#print result of script
print("Players with 10+ matches:", df["player_id"].nunique())
print("Total rows:", len(df))
print("\nTop 10 players by match count:")
print(df.groupby("player_name")["match_id"].count().sort_values(ascending=False).head(10))

df.to_csv("player_timelines.csv", index=False)
print("\nSaved to player_timelines.csv")