import pytest

from src.kcenter.brute_force.brute_force_colourful_k_center import BruteForceColourfulKCenter
from src.kcenter.constant.colour import Colour
from src.kcenter.verify.verify import verify_solution
from src.server.graph_loader import GraphLoader
from tests.kcenter.solver.greedy.test_greedy import RELAXED_CONSTRAINTS, K, FLOAT_ERROR_MARGIN
from tests.kcenter.util.create_test_graph import basic_graph


def test_greedy_basic_graph_colourful_clustering():
    graph = basic_graph()
    instance = BruteForceColourfulKCenter(graph, K, RELAXED_CONSTRAINTS)
    clusters, outliers, radius = instance.solve()

    assert radius == pytest.approx(0.707, FLOAT_ERROR_MARGIN)
    assert clusters == {
        0: {0, 1},
        3: {3, 4}
    }
    assert outliers == {2}
    assert verify_solution(graph, RELAXED_CONSTRAINTS, K, radius, set(clusters.keys())) is True


def test_greedy_medium_graph_colourful_clustering():
    graph = GraphLoader.get_graph("medium")
    k = 4
    constraints = {Colour.BLUE: 10, Colour.RED: 10}
    instance = BruteForceColourfulKCenter(graph, k, constraints)
    clusters, outliers, radius = instance.solve()

    assert radius == pytest.approx(5.5, FLOAT_ERROR_MARGIN)
    assert clusters == {
        0: {0, 19, 10, 11},
        1: {1, 6, 7, 13, 14, 15},
        2: {2, 4, 5, 12, 18},
        3: {3, 8, 9, 16, 17}
    }
    assert outliers == {20, 21, 22, 23, 24}
    assert verify_solution(graph, RELAXED_CONSTRAINTS, k, radius, set(clusters.keys())) is True
