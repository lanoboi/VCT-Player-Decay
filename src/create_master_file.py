import pandas as pd

matches = pd.read_csv("data/aggregated data/aggregated_matches.csv")
maps = pd.read_csv("data/aggregated data/aggregated_detailed_matches_maps.csv")
player_stats = pd.read_csv("data/aggregated data/aggregated_detailed_matches_player_stats.csv")
economy = pd.read_csv("data/aggregated data/aggregated_economy_data.csv")
performance = pd.read_csv("data/aggregated data/aggregated_performance_data.csv")


name_map = {
    "EDG": "EDward Gaming",
    "TL": "Team Liquid",
    "DRX": "DRX",
    "SEN": "Sentinels",
    "VIT": "Team Vitality",
    "T1": "T1",
    "G2": "G2 Esports",
    "TE": "Team Heretics",
    "PRX": "Paper Rex",
    "XLG": "Xi Lai Gaming",
    "GX": "GIANTX",
    "NRG": "NRG",
    "DRG": "Dragon Ranger Gaming",
    "TH": "Team Heretics",
    "BLG": "Bilibili Gaming",
    "MIBR": "MIBR",
    "RRQ": "Rex Regum Qeon",
    "FNC": "FNATIC",
    "WOL": "Wolves Esports",
    "GEN": "Gen.G"
}

economy["Team"] = economy["Team"].map(name_map).fillna(economy["Team"])
player_agg = (
    player_stats[player_stats["stat_type"] == "overall"]
    .groupby(["match_id", "player_team"])
    .agg(
        avg_rating=("rating", "mean"),
        avg_acs=("acs", "mean"),
        avg_kd=("kd_diff", "mean"),
        avg_adr=("adr", "mean"),
        avg_fk=("fk", "mean"),
    )
    .reset_index()
)

matches["match_id"] = matches["match_id"].astype(str)
player_agg["match_id"] = player_agg["match_id"].astype(str)

team1_stats = player_agg.merge(
    matches[["match_id", "team1"]], on="match_id"
)

team1_stats = team1_stats[team1_stats["player_team"] == team1_stats["team1"]]
team1_stats = team1_stats.drop(columns=["player_team", "team1"])
team1_stats.columns = ["match_id"] + [f"t1_{c}" for c in team1_stats.columns if c != "match_id"]

team2_stats = player_agg.merge(
    matches[["match_id", "team2"]], on="match_id"
)
team2_stats = team2_stats[team2_stats["player_team"] == team2_stats["team2"]]
team2_stats = team2_stats.drop(columns=["player_team", "team2"])
team2_stats.columns = ["match_id"] + [f"t2_{c}" for c in team2_stats.columns if c != "match_id"]

# --- Economy: average per team per match ---
economy["match_id"] = economy["match_id"].astype(str)
eco_agg = (
    economy.groupby(["match_id", "Team"])
    .agg(
        pistol_won=("Pistol Won", "sum"),
        eco_won=("Eco (won)", "sum"),
        full_buy_won=("Full buy(won)", "sum"),
    )
    .reset_index()
)



eco_t1 = eco_agg.merge(matches[["match_id", "team1"]], on="match_id")
eco_t1 = eco_t1[eco_t1["Team"] == eco_t1["team1"]].drop(columns=["Team", "team1"])
eco_t1.columns = ["match_id"] + [f"t1_{c}" for c in eco_t1.columns if c != "match_id"]

eco_t2 = eco_agg.merge(matches[["match_id", "team2"]], on="match_id")
eco_t2 = eco_t2[eco_t2["Team"] == eco_t2["team2"]].drop(columns=["Team", "team2"])
eco_t2.columns = ["match_id"] + [f"t2_{c}" for c in eco_t2.columns if c != "match_id"]

master = matches.copy()
master = master.merge(team1_stats, on="match_id", how="left")
master = master.merge(team2_stats, on="match_id", how="left")
master = master.merge(eco_t1, on="match_id", how="left")
master = master.merge(eco_t2, on="match_id", how="left")

print("Master shape:", master.shape)
print("Columns:", master.columns.tolist())
print("Null counts:\n", master.isnull().sum())

master.to_csv("data/aggregated data/master_dataset.csv", index=False)
print("\nSaved to master_dataset.csv")