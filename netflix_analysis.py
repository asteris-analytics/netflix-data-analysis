import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("n_movies.csv")
print(df.head())
print(df.info())

plt.figure(figsize=(12,6))
top10=df.sort_values(by=['rating'], ascending=False).head(10)
plt.bar(top10["title"], top10["rating"])
plt.xticks(rotation=45)
plt.title("Top 10 movies by Rating")
plt.show()


df["votes"] = df["votes"].astype(str)
df["votes"] = df["votes"].str.replace(",", "")
df["votes"] = df["votes"].str.extract(r"(\d+)")
df["votes"] = pd.to_numeric(df["votes"])
print(df["votes"].head())
plt.figure(figsize=(10,6))

plt.scatter(df["votes"], df["rating"])

plt.xlabel("Votes")
plt.ylabel("Rating")

plt.title("Votes vs Rating")

plt.show()
correlation = df["votes"].corr(df["rating"])

print(correlation)