print("===== MOVIE RECOMMENDATION SYSTEM =====")

movies = {
    "Pushpa": ["Action", 2021],
    "KGF": ["Action", 2018],
    "Bahubali": ["Action", 2015],
    "Hi Nanna": ["Love", 2023],
    "Baby": ["Love", 2023],
    "Interstellar": ["Sci-Fi", 2014],
    "Avatar": ["Sci-Fi", 2009]
}

print("\nAvailable Movies:")
for movie in movies:
    print("-", movie)

fav_movie = input("\nEnter Your Favourite Movie: ")

if fav_movie in movies:

    fav_genre = movies[fav_movie][0]

    print("\nYour Favourite Genre:", fav_genre)

    print("\nRecommended Movies For You:\n")

    found = False

    for movie, details in movies.items():

        genre = details[0]
        year = details[1]

        if genre == fav_genre and movie != fav_movie:
            print(movie, "-", year)
            found = True

    if found == False:
        print("No Recommendations Found")

else:
    print("\nMovie Not Available In Database")
