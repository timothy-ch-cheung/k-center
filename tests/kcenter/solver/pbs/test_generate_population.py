import math

import numpy as np

from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import PBS
from src.kcenter.pbs.similarity import CompareSolution
from src.server.graph_loader import GraphLoader


def test_generate_population_medium_graph(seed_random):
    graph = GraphLoader.get_graph("medium")
    instance = PBS(graph, 4, {Colour.BLUE: 10, Colour.RED: 10})
    population = instance.generate_population()

    expected_population = [
        {8, 1, 12, 21},
        {16, 3, 4, 23},
        {9, 10, 3, 15},
        {0, 9, 4, 21},
        {17, 19, 14, 23},
        {10, 3, 14, 23},
        {18, 23, 21, 15},
        {0, 18, 3, 13}
    ]
    for i, individual in enumerate(population):
        assert individual.centers == expected_population[i]


def test_generate_population_medium_graph_is_diverse(seed_random):
    graph = GraphLoader.get_graph("medium")
    instance = PBS(graph, 4, {Colour.BLUE: 10, Colour.RED: 10})
    population = instance.generate_population()

    generated_centers = [x.centers for x in population]
    MIN = (34.78753471028318, 42.83698613479884)
    MAX = (196.61095005621613, 178.77089875665393)
    comp = CompareSolution(graph, min_value=MIN, max_value=MAX)

    similarity = {x: [] for x in range(len(population))}
    for i, a in enumerate(generated_centers):
        for b in generated_centers:
            if a == b: continue
            similarity[i].append(comp.sim(a, b))

    expected_similarity = {
        0: [0.5493, 0.5778, 0.3579, 0.2306, 0.2306, 0.4006, 0.5963],
        1: [0.5493, 0.5511, 0.2306, 0.5369, 0.5369, 0.5511, 0.5532],
        2: [0.5778, 0.5511, 0.5778, 0.3475, 0.3475, 0.5778, 0.2121],
        3: [0.3579, 0.2306, 0.5778, 0.3482, 0.3482, 0.3614, 0.5963],
        4: [0.2306, 0.5369, 0.3475, 0.3482, 0.0348, 0.3839, 0.3739],
        5: [0.2306, 0.5369, 0.3475, 0.3482, 0.0348, 0.3739, 0.3739],
        6: [0.4006, 0.5511, 0.5778, 0.3614, 0.3839, 0.3739, 0.5963],
        7: [0.5963, 0.5532, 0.2121, 0.5963, 0.3739, 0.3739, 0.5963]
    }
    comp.sim(generated_centers[3], generated_centers[0])
    for i, actual_similarity in similarity.items():
        np.testing.assert_allclose(actual_similarity, expected_similarity[i], rtol=1e-03)


def test_generate_population_medium_graph_is_cost_diverse(seed_random):
    graph = GraphLoader.get_graph("k_center")
    instance = PBS(graph, 5, {Colour.BLUE: 0, Colour.RED: 20})
    population = instance.generate_population()
    for i in population:
        for j in population:
            if i == j:
                continue
            assert math.isclose(i.cost, j.cost) == False, f"{i} is too similar to {j}"
