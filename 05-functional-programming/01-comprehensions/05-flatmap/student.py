from util import Card


def genres(movies):
    return {genre for movie in movies for genre in movie.genres}


def actors(movies):
    return {actor for movie in movies for actor in movie.actors}


def repeat_consecutive(xs, n):
    return [item for item in xs for repeat in range(n)]


# for understanding purposes
def repeat_consecutive_forloop(xs, n):
    list = []
    for item in xs:
        for repeat in range(n):
            list.append(item)
    return list


def repeat_alternating(xs, n):
    return [item for alternate in range(n) for item in xs]


def cards(values, suits):
    return {Card(value, suit) for value in values for suit in suits}
