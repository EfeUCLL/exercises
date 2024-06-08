def group_movies_by_year(movies):
    return {
        year: [movie.title for movie in movies if movie.year == year]
        for year in {movie.year for movie in movies}
    }


# for understanding purposes
def group_movies_by_year2(movies):
    # Create an empty dictionary to store the results
    result = {}

    # Create a set of unique years from the movies list
    unique_years = set(movie.year for movie in movies)

    # Iterate over each unique year
    for year in unique_years:
        # Create an empty list to store the movie titles for this year
        result[year] = []

        # Iterate over each movie in the movies list
        for movie in movies:
            # If the movie's year matches the current year, add its title to the list
            if movie.year == year:
                result[year].append(movie.title)

    # Return the result dictionary
    return result
