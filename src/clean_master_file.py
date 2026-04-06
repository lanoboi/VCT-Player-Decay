import pandas as pd

df = pd.read_csv("aggregated/master_dataset.csv")


df = df.drop(columns=["tournament"])

#dropping rows that have important feature data missing
df = df.dropna(subset=["ta_avg_acs", "tb_avg_acs", "ta_avg_kd", "tb_avg_kd"])



#filling nulls with dataset median
median_cols = [
    "ta_avg_rating", "tb_avg_rating",
    "ta_avg_adr", "tb_avg_adr",
    "ta_avg_fk", "tb_avg_fk",
    "ta_avg_hs", "tb_avg_hs"
]

for col in median_cols:
    df[col] = df[col].fillna(df[col].median())

#setting eco, kills, draft nulls to 0
zero_cols = [c for c in df.columns if any(x in c for x in ["eco", "total", "draft"])]
df[zero_cols] = df[zero_cols].fillna(0)

#binary target variable
df["winner"] = df["Match Result"].str.replace(" won", "").str.strip()
df["team_a_won"] = (df["winner"] == df["Team A"].str.strip()).astype(int)
df = df.drop(columns=["winner"])

print("Shape:", df.shape)
print("Nulls:", df.isnull().sum())
print("Target distribution:")
print(df["team_a_won"].value_counts())

df.to_csv("aggregated/cleaned_master.csv", index=False)
print("Saved to aggregated/cleaned_master.csv")



