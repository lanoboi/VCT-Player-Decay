import pandas as pd

df = pd.read_csv("master_dataset.csv")

# 1 if team1 won, 0 if team2 won
df["team1_won"] = (df["winner"] == df["team1"]).astype(int)

print("Target distribution:")
print(df["team1_won"].value_counts())

df.to_csv("master_dataset.csv", index=False)
print("Saved")