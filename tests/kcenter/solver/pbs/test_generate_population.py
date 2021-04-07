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
        {3, 4, 15, 23},
        {2, 9, 13, 23},
        {3, 6, 2, 23},
        {4, 9, 13, 23},
        {2, 6, 9, 23},
        {3, 2, 15, 21},
        {1, 2, 8, 23}
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
                               [53.4218, 66.4291, 66.4698, 66.9643, 68.7666, 74.399, 73.4314, 75.1955], rtol=1e-03)
