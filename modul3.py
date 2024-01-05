# Data film
movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"}
]

# Fungsi untuk menampilkan data film
def show_movie_data(movie):
    print("Informasi Film:")
    print(f"Judul: {movie['title']}")
    print(f"Rating: {movie['rating']}")
    print(f"Tahun Rilis: {movie['year']}")
    print(f"Genre: {movie['genre']}\n")

# Implementasi filter pada count_movies_by_genre
def count_movies_by_genre():
    genres = set(movie['genre'] for movie in movies)
    genre_counts = {}
    for genre in genres:
        filtered_movies = filter(lambda movie: movie['genre'] == genre, movies)
        genre_counts[genre] = len(list(filtered_movies))
    return genre_counts

# Implementasi map pada average_rating_by_year
def average_rating_by_year():
    year_ratings = {}
    for movie in movies:
        year = movie['year']
        rating = movie['rating']
        if year in year_ratings:
            year_ratings[year].append(rating)
        else:
            year_ratings[year] = [rating]

    def calculate_average_rating(ratings):
        return sum(ratings) / len(ratings)

    average_ratings = dict(map(lambda item: (item[0], calculate_average_rating(item[1])), year_ratings.items()))
    return average_ratings

# Fungsi untuk mencari film dengan rating tertinggi (max)
def find_highest_rated_movie():
    highest_rated_movie = max(movies, key=lambda movie: movie['rating'])
    return highest_rated_movie

while True:
    print("Pilih tugas yang ingin dilakukan:")
    print("1. Menghitung jumlah film berdasarkan genre")
    print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
    print("3. Menemukan film dengan rating tertinggi")
    print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
    print("5. Selesai")
    choice = input("Masukkan nomor tugas (1/2/3/4/5): ")

    if choice == '1':
        genre_counts = count_movies_by_genre()
        for genre, count in genre_counts.items():
            print(f"{genre}: {count}")
    elif choice == '2':
        average_ratings = average_rating_by_year()
        for year, average in average_ratings.items():
            print(f"{year}: {average}")
    elif choice == '3':
        highest_rated_movie = find_highest_rated_movie()
        show_movie_data(highest_rated_movie)
    elif choice == '4':
        title = input("Masukkan judul film yang ingin dicari: ")
        movie = next((m for m in movies if m["title"] == title), None)
        if movie:
            show_movie_data(movie)
        else:
            print("Film dengan judul tidak ditemukan.")
    elif choice == '5':
        print("\nTerima kasih. Program selesai.")
        break
    else:
        print("Pilihan tidak valid")