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