import math

import numpy as np

from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import PBS
from src.server.graph_loader import GraphLoader


def test_generate_population_medium_graph(seed_random):
    graph = GraphLoader.get_graph("medium")
    instance = PBS(graph, 4, {Colour.BLUE: 10, Colour.RED: 10})
    population = instance.generate_population()

    expected_population = [
        {3, 2, 15, 21},
        {1, 4, 9, 21},
        {2, 6, 8, 23},
        {2, 3, 14, 23},
        {1, 2, 16, 23},
        {2, 8, 15, 23},
        {1, 2, 16, 23},
        {2, 7, 9, 21}
    ]
    for i, individual in enumerate(population):
        assert individual.centers == expected_population[i]


def test_generate_population_medium_graph_is_cost_diverse(seed_random):
    graph = GraphLoader.get_graph("large")
    instance = PBS(graph, 5, {Colour.BLUE: 50, Colour.RED: 50})
    population = instance.generate_population()
    for i in population:
        for j in population:
            if i == j:
                continue
            assert math.isclose(i.cost, j.cost) == False, f"{i} is too similar to {j}"

    np.testing.assert_allclose([individual.cost for individual in population],
                               [53.4217, 66.4290, 66.4697, 79.3426, 66.9643, 76.7321, 56.5485, 76.954], rtol=1e-03)
