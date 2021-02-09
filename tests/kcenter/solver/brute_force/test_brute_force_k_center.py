import pytest

from src.kcenter.brute_force.brute_force_k_center import BruteForceKCenter
from src.kcenter.constant.colour import Colour
from src.kcenter.verify.verify import verify_solution
from src.server.graph_loader import GraphLoader
from tests.kcenter.solver.greedy.test_greedy import STRICT_CONSTRAINTS, K
from tests.kcenter.util.assertion import FLOAT_ERROR_MARGIN
from tests.kcenter.util.create_test_graph import basic_graph


def test_greedy_basic_graph_colourful_clustering():
    graph = basic_graph()
    instance = BruteForceKCenter(graph, K, STRICT_CONSTRAINTS)
    clusters, outliers, radius = instance.solve()

    assert radius == pytest.approx(0.728, FLOAT_ERROR_MARGIN)
    assert clusters == {
        1: {0, 1, 2},
        3: {3, 4}
    }
    assert outliers == set()
    assert verify_solution(graph, STRICT_CONSTRAINTS, K, radius, set(clusters.keys())) is True


def test_greedy_medium_graph_colourful_clustering():
    graph = GraphLoader.get_graph("medium")
    k = 4
    constraints = {Colour.BLUE: 10, Colour.RED: 10}
    instance = BruteForceKCenter(graph, k, constraints)
    clusters, outliers, radius = instance.solve()

    assert radius == pytest.approx(45.402, FLOAT_ERROR_MARGIN)
    assert clusters == {
        1: {1, 6, 7, 13, 14, 15},
        2: {0, 2, 4, 5, 10, 11, 12, 18, 19, 20, 22, 24},
        3: {3, 8, 9, 16, 17},
        21: {21, 23}
    }
    assert outliers == set()
    assert verify_solution(graph, constraints, k, radius, set(clusters.keys())) is True
