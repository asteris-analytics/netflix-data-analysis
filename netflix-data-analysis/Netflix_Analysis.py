import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/n_movies.csv")
print(df.columns)
print(df.info())
print(df.head())
# Remove rows with missing values in key columns
df = df.dropna(subset=["genre", "rating", "votes"])

# Convert votes from text to numeric
df["votes"] = (
    df["votes"]
    .str.replace(",", "", regex=False)
    .astype(int)
)

# Extract main genre
df["main_genre"] = df["genre"].str.split(",").str[0]

print(df.info())
print(df[["title", "main_genre", "rating", "votes"]].head())

# -----------------------------
# Distribution of IMDb Ratings
# -----------------------------

plt.figure(figsize=(10,6))

sns.histplot(
    data=df,
    x="rating",
    bins=20,
    kde=True,
    color="steelblue"
)

plt.title("Distribution of IMDb Ratings", fontsize=16)
plt.xlabel("IMDb Rating")
plt.ylabel("Number of Titles")

plt.savefig(
    "images/rating_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
# -----------------------------
# Boxplot of Votes
# -----------------------------

plt.figure(figsize=(10,6))

sns.boxplot(
    y=df["votes"],
    color="skyblue"
)

plt.title("Distribution of IMDb Votes", fontsize=16)
plt.ylabel("Votes")

plt.savefig(
    "images/boxplot_votes.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
# -----------------------------
# Rating vs Votes
# -----------------------------

plt.figure(figsize=(12,7))

sns.regplot(
    data=df,
    x="votes",
    y="rating",
    scatter_kws={"alpha":0.3},
    line_kws={"color":"red"}
)

plt.title("IMDb Rating vs Votes", fontsize=16)
plt.xlabel("Votes")
plt.ylabel("IMDb Rating")

plt.savefig(
    "images/rating_vs_votes.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
# -----------------------------
# Average Rating by Genre
# -----------------------------

genre_rating = (
    df.groupby("main_genre")["rating"]
      .mean()
      .sort_values(ascending=False)
      .head(15)
      .reset_index()
)

plt.figure(figsize=(12,7))

sns.barplot(
    data=genre_rating,
    x="rating",
    y="main_genre",
    color="steelblue"
)

plt.title("Top 15 Genres by Average IMDb Rating", fontsize=16)
plt.xlabel("Average Rating")
plt.ylabel("Genre")

plt.savefig(
    "images/top_genres.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
# -----------------------------
# Top 15 Most Voted Titles
# -----------------------------

top_movies = (
    df.sort_values("votes", ascending=False)
      .head(15)
)

plt.figure(figsize=(13,8))

sns.barplot(
    data=top_movies,
    x="votes",
    y="title",
    hue="rating",
    palette="viridis",
    dodge=False
)

plt.title("Top 15 Most Voted Titles", fontsize=16)
plt.xlabel("Votes")
plt.ylabel("Title")

plt.legend(title="IMDb Rating")

plt.savefig(
    "images/top_voted_movies.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

