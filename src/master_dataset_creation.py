import pandas as pd

#loading files
scores      = pd.read_csv("aggregated/scores.csv")
overview    = pd.read_csv("aggregated/overview.csv")
eco_stats   = pd.read_csv("aggregated/eco_stats.csv")
kills_stats = pd.read_csv("aggregated/kills_stats.csv")
draft_phase = pd.read_csv("aggregated/draft_phase.csv")
maps_scores = pd.read_csv("aggregated/maps_scores.csv")


#fixing error with overview file before aggregating
overview["Headshot %"] = overview["Headshot %"].astype(str).str.replace("%", "").str.strip()
overview["Headshot %"] = pd.to_numeric(overview["Headshot %"], errors="coerce")

overview["Kill, Assist, Trade, Survive %"] = overview["Kill, Assist, Trade, Survive %"].astype(str).str.replace("%", "").str.strip()
overview["Kill, Assist, Trade, Survive %"] = pd.to_numeric(overview["Kill, Assist, Trade, Survive %"], errors="coerce")

#player performance per match: aggregate overview by match + team
overview_agg = (
    overview[overview["Side"] == "both"]
    .groupby(["Match Name", "Tournament", "Stage", "Team"])
    .agg(
        avg_rating=("Rating", "mean"),
        avg_acs=("Average Combat Score", "mean"),
        avg_kd=("Kills - Deaths (KD)", "mean"),
        avg_adr=("Average Damage Per Round", "mean"),
        avg_fk=("First Kills", "mean"),
        avg_hs=("Headshot %", "mean"),
    )
    .reset_index()
)


#eco stats per match: aggregate by match + team
eco_agg = (
    eco_stats.groupby(["Match Name", "Tournament", "Stage", "Team","Type"])["Won"]
    .sum()
    .unstack(fill_value=0)
    .reset_index()
)
eco_agg.columns.name = None

#kills stats per match: aggregate by match + team
kills_agg = (
    kills_stats.groupby(["Match Name", "Tournament", "Stage", "Team"])
    .agg(
        total_2k=("2k", "sum"),
        total_3k=("3k", "sum"),
        total_4k=("4k", "sum"),
        total_5k=("5k", "sum"),
        total_clutches=("1v1", "sum"),
    )
    .reset_index()
)

#draft: count picks and bans per team per match
draft_agg = (
    draft_phase.groupby(["Match Name", "Tournament", "Stage", "Team", "Action"])
    .size()
    .unstack(fill_value=0)
    .reset_index()
)
draft_agg.columns.name = None

#build master 
master = scores.copy()

#split into team a and b
for team_col, prefix in [("Team A", "ta"), ("Team B", "tb")]:
   
    temp = overview_agg.copy()
    temp = temp.rename(columns={"Team": team_col})
    temp.columns = ["Match Name", "Tournament", "Stage", team_col] + [f"{prefix}_{c}" for c in temp.columns[4:]]
    master = master.merge(temp, on=["Match Name", "Tournament", "Stage", team_col], how="left")

   
    temp = eco_agg.copy()
    temp = temp.rename(columns={"Team": team_col})
    temp.columns = ["Match Name", "Tournament", "Stage", team_col] + [f"{prefix}_eco_{c}" for c in temp.columns[4:]]
    master = master.merge(temp, on=["Match Name", "Tournament", "Stage", team_col], how="left")

    temp = kills_agg.copy()
    temp = temp.rename(columns={"Team": team_col})
    temp.columns = ["Match Name", "Tournament", "Stage", team_col] + [f"{prefix}_{c}" for c in temp.columns[4:]]
    master = master.merge(temp, on=["Match Name", "Tournament", "Stage", team_col], how="left")

    temp = draft_agg.copy()
    temp = temp.rename(columns={"Team": team_col})
    temp.columns = ["Match Name", "Tournament", "Stage", team_col] + [f"{prefix}_draft_{c}" for c in temp.columns[4:]]
    master = master.merge(temp, on=["Match Name", "Tournament", "Stage", team_col], how="left")
    
print("Master shape:", master.shape)
print("Columns:", master.columns.tolist())
print("Null counts:\n", master.isnull().sum())

master.to_csv("aggregated/master_dataset.csv", index=False)
print("\nSaved to aggregated/master_dataset.csv")