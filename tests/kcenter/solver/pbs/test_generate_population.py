import math
import random

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
        {1, 2, 8, 21},
        {1, 2, 3, 21},
        {1, 3, 4, 21},
        {2, 15, 17, 23},
        {2, 9, 13, 21},
        {2, 9, 14, 23},
        {2, 9, 15, 23},
        {2, 14, 17, 23}
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
        0: [0.02780, 0.02780, 0.23063, 0.05560, 0.23063, 0.23063, 0.23063],
        1: [0.02780, 0.02695, 0.23063, 0.02780, 0.23063, 0.23063, 0.23063],
        2: [0.02780, 0.02695, 0.23063, 0.02780, 0.23063, 0.23063, 0.23063],
        3: [0.23063, 0.23063, 0.23063, 0.23063, 0.04578, 0.04578, 0.01459],
        4: [0.05560, 0.02780, 0.02780, 0.23063, 0.23063, 0.23063, 0.23063],
        5: [0.23063, 0.23063, 0.23063, 0.04578, 0.23063, 0.01459, 0.04578],
        6: [0.23063, 0.23063, 0.23063, 0.04578, 0.23063, 0.01459, 0.04578],
        7: [0.23063, 0.23063, 0.23063, 0.01459, 0.23063, 0.04578, 0.04578]}
    comp.sim(generated_centers[3], generated_centers[0])
    for i, actual_similarity in similarity.items():
        np.testing.assert_allclose(actual_similarity, expected_similarity[i], rtol=1e-03,
                                   err_msg=f"expected {i} is incorrect")


def test_generate_population_medium_graph_is_cost_diverse(seed_random):
    random.seed(68)
    graph = GraphLoader.get_graph("large")
    instance = PBS(graph, 5, {Colour.BLUE: 50, Colour.RED: 50})
    population = instance.generate_population()
    for i in population:
        for j in population:
            if i == j:
                continue
            assert math.isclose(i.cost, j.cost) == False, f"{i} is too similar to {j}"

    np.testing.assert_allclose([individual.cost for individual in population],
                               [76.2846, 53.4217, 56.6719, 74.3989, 68.7665, 66.4290, 73.4314, 67.5112], rtol=1e-03)
