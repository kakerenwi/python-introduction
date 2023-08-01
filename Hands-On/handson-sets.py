# Famous for non-duplicate items.
groceries = {"eggs", "milk", "veggies", "eggs"}
print(groceries) # set doesn't have any order when printing the values

# From dir({"vamsi", "avi"}) we can get the functions to go along e.g add, union, intersection, etc.
groceries.add("candies")
print(groceries)

marvel_movies = {"ironman", "black panther", "spiderman", "hulk"}

fav_movies = {"ironman", "black panther", "superman"}

combined_movies = marvel_movies.union(fav_movies)
print(combined_movies)

common_movies = marvel_movies.intersection(fav_movies)

print(common_movies)

for i in marvel_movies:
    print(i)
