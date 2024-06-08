def title_to_director(movies):
    return {movie.title: movie.director for movie in movies}

def director_to_titles(movies):
    return {movie.director: [movie2.title for movie2 in movies if movie.director in movie2.director]
            for movie in movies}

# SOLUTION (better?):
# def director_to_titles(movies):
#     return {
#         director: [movie.title for movie in movies if movie.director == director]
#         for director in {movie.director for movie in movies}
#     }