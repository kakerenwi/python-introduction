# From the movies list, iterate over all movies and while in the iteration mode do the following:
# For hulk, make it UPPERCASE
# Replace "spiderman" with "spidy"
# If movie is "ironman" or "avengers" add to favorite movie-list and print.

movies = ["ironman", "batman", "hulk", "spiderman", "avengers"]

fav_movie = []

for i in movies:
    print(i)

    if movies == "ironman" or "avengers":
        fav_movie.append(i)
        print(fav_movie)
        


