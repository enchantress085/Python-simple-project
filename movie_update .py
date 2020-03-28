# -*- coding: utf-8 -*-
"""
- Enter 'a' to add a movie,
        'l' to see your movie,
        'f' to find a movie,
        'q' to quit:
            
"""
movies = []  # --- store movies
"""
movie = {
    'name':...(string),
    'director':...(string),
    'year':...(int)
}
"""


def menu():
    user_input = input(
        "Enter 'a' to add a movie, 'l' to see your movie, 'f' to find a movie, 'q' to quit :>")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movie()
        elif user_input == 'f':
            find_movie(movies)
        else:
            print("Unknown commend-plese try again.")

        user_input = input(
            "\nEnter 'a' to add a movie, 'l' to see your movie, 'f' to find a movie, 'q' to quit :> ")


def add_movie():
    name = input("Enter the movie name:> ")
    director = input("Enter the movie director:> ")
    year = int(input("Enter the movie release year:> "))

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movie(movie_list):
    for movie in movie_list:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release Year :{movie['year']}")


def find_movie():
    # -- year , name, director
    find_by = input("What property of the movir looking for? ")
    looking_for = input("What are you searching for? ")

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movie(found_movies)


"""
############-------------

"""


def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)
    return found


menu()
# ------------
