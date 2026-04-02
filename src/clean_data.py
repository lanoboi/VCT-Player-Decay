import pandas as pd

df = pd.read_csv("merged_player_stats.csv", low_memory=False)

#Only overall rows matter, per map is irrelevant to problem
df = df[df["stat_type"] == "overall"].copy()

# Dropping mostly-empty columns
df = df.drop(columns=["match_title", "event", "date", "format","teams", "score", "maps_played", "patch", "pick_ban_info"])

# Removing % from KAST and headshot stats (coerce for turning n/a to nan)
df["kast"] = df["kast"].astype(str).str.replace("%", "").str.strip()
df["kast"] = pd.to_numeric(df["kast"], errors="coerce")
df["hs_percent"] = df["hs_percent"].astype(str).str.replace("%", "").str.strip()
df["hs_percent"] = pd.to_numeric(df["hs_percent"], errors="coerce")

#date parsing (coerce for turning n/a to nan)
df["match_date"] = pd.to_datetime(df["match_date"], errors="coerce")
df["year"] = df["match_date"].dt.year

# Drop rows with no player
df = df.dropna(subset=["player_id", "player_name", "acs"])

df.to_csv("cleaned_player_stats.csv", index=False)
print("Done:", df.shape)
print("Unique players:", df["player_id"].nunique())