from itertools import pairwise, permutations

def find_shortest_path(distance, city_count):
    def total_distance(path):
        return sum(distance(a, b) for a, b in pairwise(path))
    # *p unpacks list, start bij 0, zet de getallen uit permutations(range(1, city_count)) in p en eindigt lijst met 0
    # e.g. [
    #       [0, 1, 2, 3, 0],
    #       [0, 2, 1, 3, 0]
    #      ]
    paths = ([0, *p, 0] for p in permutations(range(1, city_count)))
    return min(paths, key=total_distance)
