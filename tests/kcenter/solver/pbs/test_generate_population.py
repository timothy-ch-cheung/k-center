import pytest
import numpy as np

from kcenter.constant.colour import Colour
from kcenter.pbs.pbs import PBS
from kcenter.pbs.similarity import CompareSolution
from server.graph_loader import GraphLoader
from tests.kcenter.solver.pbs.test_pbs import FLOAT_ERROR_MARGIN


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
        0: [0.2673, 0.2069, 0.1117, 0.1134, 0.1223, 0.1035, 0.2469],
        1: [0.2636, 0.3463, 0.1899, 0.2467, 0.2571, 0.3585, 0.3282],
        2: [0.2205, 0.2245, 0.2952, 0.1173, 0.1041, 0.2910, 0.1351], 
        3: [0.1117, 0.1837, 0.3002, 0.2070, 0.2102, 0.1848, 0.1636], 
        4: [0.1134, 0.2569, 0.1048, 0.2070, 0.0142, 0.2738, 0.2145], 
        5: [0.1223, 0.2521, 0.0905, 0.2052, 0.0142, 0.2078, 0.2234], 
        6: [0.1035, 0.3547, 0.2910, 0.1848, 0.2031, 0.2078, 0.3329], 
        7: [0.2559, 0.4090, 0.1306, 0.3454, 0.1680, 0.1662, 0.3438]
    }

    for i, actual_similarity in expected_similarity.items():
        np.testing.assert_allclose(actual_similarity, expected_similarity[i], rtol=1e-03)
