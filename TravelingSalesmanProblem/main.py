import random
import timeit
from typing import Callable
from algos import brute_force
from visualize import visualize_tour

aCity = complex


def generate_cities(number_of_cities):
    seed = 111
    width = 500
    height = 300
    random.seed((number_of_cities, seed))
    return frozenset(
        aCity(random.randint(1, width), random.randint(1, height))
        for _ in range(number_of_cities))


def tsp(algoritm: Callable, cities) -> None:

    tour = algoritm(cities)
    print("Funkcja wykonywala sie w:",
          timeit.timeit(lambda: algoritm(cities), number=1), "sekundy")

    visualize_tour(tour)


if __name__ == "__main__":
    cities = generate_cities(10)
    tsp(brute_force, cities)
