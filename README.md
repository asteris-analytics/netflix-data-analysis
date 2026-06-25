# 🎬 Netflix Data Analysis

## 📌 Project Overview

This project explores a Netflix Movies & TV Shows dataset using Python for data cleaning, exploratory data analysis (EDA), and data visualization.

The goal is to identify trends in IMDb ratings, votes, genres, and popular titles using Pandas, Matplotlib, and Seaborn.

---

## 📊 Dataset

The dataset contains information about Netflix movies and TV shows, including:

- Title
- Release Year
- Genre
- IMDb Rating
- IMDb Votes
- Certificate
- Duration
- Description
- Cast

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 🧹 Data Cleaning

The following preprocessing steps were performed:

- Removed missing values from important columns
- Converted IMDb votes to numeric format
- Extracted the primary genre from multi-genre entries
- Prepared the dataset for visualization

---

## 📈 Exploratory Data Analysis

The analysis includes:

- IMDb Rating Distribution
- Rating vs Votes
- Top Genres by Average Rating
- Top 15 Most Voted Titles
- Boxplot of IMDb Votes

---

## 📂 Project Structure

```
netflix-data-analysis/
│
├── data/
├── images/
├── netflix_analysis.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python netflix_analysis.py
```

---
## 🔍 Key Insights

- Most Netflix titles have IMDb ratings between **6.0 and 8.0**.
- There is **no strong linear relationship** between IMDb ratings and the number of votes.
- Genres such as **Film-Noir**, **Music**, and **Animation** achieved the highest average ratings.
- A small number of titles account for the majority of IMDb votes, indicating a highly skewed distribution.
## 📈 Future Improvements

Possible future enhancements include:

- Interactive dashboards with Power BI
- Additional feature engineering
- Time-series analysis by release year
- Machine Learning models for IMDb rating prediction
## 👨‍💻 Author

Asterios Alexandris