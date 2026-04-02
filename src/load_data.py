import pandas as pd
import os

frames = []

for fname in os.listdir("data"):
    if fname.endswith(".csv"):
        df = pd.read_csv(os.path.join("data", fname))
        frames.append(df)

df_all = pd.concat(frames, ignore_index=True)

df_all.to_csv("merged_player_stats.csv", index=False)
print("Done:", df_all.shape)