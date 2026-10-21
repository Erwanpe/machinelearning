import sys, pandas as pd

df = pd.read_csv("df_full_premierleague.csv")
print(df.head())
print(df.info())
print(df.isna().sum())

big = df.groupby("home_team")["goal_home_ft"].mean()
print(big)