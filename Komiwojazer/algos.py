from itertools import permutations
from distance import distance_points, distance_tour

alltours = permutations


def shortest_tour(tours):
    return min(tours, key=distance_tour)


def brute_force(cities):
    """Wygeneruj wszystkie mozliwe trasy i wybierz najkrotsza z nich."""
    return shortest_tour(alltours(cities))


def first(collection):
    return next(iter(collection))


def nearest_neighbour(A, cities):
    return min(cities, key=lambda C: distance_points(C, A))


def greedy_alogithm(cities, start=None):
    pass