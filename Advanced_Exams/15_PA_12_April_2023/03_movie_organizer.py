"""
exam: 03. Movie Organizer
url: https://judge.softuni.org/Contests/Practice/Index/3893#2
"""


# test codes
def movie_organizer(*args):
    genres_db = {}

    for movie_info in args:
        movie, genre = movie_info
        if genre not in genres_db:
            genres_db[genre] = []
        genres_db[genre].append(movie)

    result = ''
    for genre, movies in sorted(genres_db.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
        result += f'{genre} - {len(movies)}\n'
        result += '\n'.join(f'* {movie}' for movie in sorted(movies)) + '\n'

    return result


print(movie_organizer(
    ("The Matrix", "Sci-fi")))

print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
