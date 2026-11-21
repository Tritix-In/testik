import matplotlib.pyplot as plt
import numpy as np
from collections import Counter



# блок 1

with open("movies.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
h = lines[0].strip().split(";")

movies = []

for line in lines[1:]:
    p = line.strip().split(";")
    movies.append({"title": p[0], "year": int(p[1]), "genre": p[2], "rating": float(p[3]), "votes": int(p[4]), "duration": int(p[5]), "budget": int(p[6]), "gross": int(p[7]), "type": p[8]})
print("Число строк данных:", len(movies))
print("Первые 5 записей:")
for m in movies[:5]:
    print(m)
years = [m["year"] for m in movies]
print("min: ", min(years))
print('max: ', max(years))

# Блок 2

rat = [m["rating"] for m in movies]
genre_counts = Counter(m["genre"] for m in movies)
top10 = genre_counts.most_common(10)
top5 = genre_counts.most_common(5)
othr = len(movies) - sum(c for _, c in top5)
pie_labels = [g for g, _ in top5] + ["Другие"]
pie_values = [c for _, c in top5] + [othr]

fig, axes = plt.subplots(1, 3, figsize=(20, 6))
axes[0].hist(rat, bins=20, color='steelblue', edgecolor='black')
axes[0].set_xlabel("Рейтинг IMDb")
axes[0].set_ylabel("Количество фильмов")
axes[0].set_title("Распределение рейтингов")
axes[0].grid(axis="y", linestyle="--", alpha=0.7)
genres10 = [g for g, _ in top10]
counts10 = [c for _, c in top10]
axes[1].barh(genres10, counts10, color="seagreen", edgecolor="black")
axes[1].invert_yaxis()
axes[1].set_xlabel("Количество фильмов")
axes[1].set_title("Топ-10 жанров по количеству фильмов")
colors = ["#4e79a7", "#f28e2b", "#e15759", "#76b7b2", "#59a14f", "#bab0ac"]

axes[2].pie(pie_values, labels=pie_labels, autopct="%1.1f%%",
            colors=colors, startangle=90)
axes[2].set_title("Доли жанров")
plt.tight_layout()
plt.savefig("part2_charts.png", dpi=150)
plt.show()

# Блок 3

movies_1990 = [m for m in movies if m["year"] >= 1990]
by_year = {}
for m in movies_1990:
    by_year.setdefault(m["year"], []).append(m["rating"])
years_sorted = sorted(by_year.keys())
avg_by_year = [sum(by_year[y]) / len(by_year[y]) for y in years_sorted]
all_ratings = [m["rating"] for m in movies_1990]
overall_avg = sum(all_ratings) / len(all_ratings)
max_idx = avg_by_year.index(max(avg_by_year))
best_year = years_sorted[max_idx]
best_rating = avg_by_year[max_idx]
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(years_sorted, avg_by_year, color="steelblue", marker="o", markersize=3)
ax.set_xlabel("Год")
ax.set_ylabel("Средний рейтинг IMDb")
ax.set_title("Средний рейтинг фильмов по годам (с 1990)")
plt.grid(True)
ax.annotate(f"{best_year}: {best_rating:.2f}",
            xy=(best_year, best_rating),
            xytext=(best_year - 8, best_rating + 0.3),
            arrowprops=dict(arrowstyle="->", color="red"),
            color="red", fontsize=11)
ax.scatter([best_year], [best_rating], color="red", zorder=5)
ax.axhline(overall_avg, color="green", linestyle="--", linewidth=1.5)
ax.text(years_sorted[0], overall_avg + 0.02,
        f"Общий средний: {overall_avg:.2f}",
        color="green", fontsize=11)

plt.tight_layout()
plt.savefig("part3_avg_rating_by_year.png", dpi=150)
plt.show()