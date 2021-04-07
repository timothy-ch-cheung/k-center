import random

import pytest

from src.server.graph_loader import GraphLoader
from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import PBS
from src.kcenter.verify.verify import verify_solution
from tests.kcenter.constant.consts import FLOAT_ERROR
from tests.kcenter.util.create_test_graph import basic_graph, basic_graph_with_outlier, medium_graph

FLOAT_ERROR_MARGIN = 0.001
STRICT_CONSTRAINTS = {Colour.BLUE: 2, Colour.RED: 3}
RELAXED_CONSTRAINTS = {Colour.BLUE: 2, Colour.RED: 2}
K = 2


def test_linear_search():
    pass


def test_get_nwk():
    graph = basic_graph()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)

    nwk = instance.get_nwk(graph, 0, 3)
    assert nwk == [0, 1, 2]
    assert nwk == [0, 1, 2]


def test_pbs_basic_graph(seed_random):
    constraints = {Colour.BLUE: 3, Colour.RED: 2}
    graph = basic_graph()
    instance = PBS(graph, K, constraints)
    clusters, outliers, radius = instance.solve()

    assert clusters == {1: {0, 1, 2}, 4: {3, 4}}
    assert outliers == set()
    assert radius == pytest.approx(0.728, FLOAT_ERROR)
    assert verify_solution(graph, constraints, K, radius, set(clusters.keys())) is True


def test_pbs_basic_graph_with_outlier(seed_random):
    graph = basic_graph_with_outlier()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)
    clusters, outliers, radius = instance.solve()

    assert clusters == {0: {0, 1, 2}, 3: {3, 4}}
    assert outliers == set()
    assert radius == pytest.approx(3.785, FLOAT_ERROR)
    assert verify_solution(graph, STRICT_CONSTRAINTS, K, radius, set(clusters.keys())) is True


def test_pbs_medium_graph(seed_random):
    random.seed(2)
    graph = medium_graph()
    instance = PBS(graph, 3, STRICT_CONSTRAINTS)
    clusters, outliers, radius = instance.solve()

    assert clusters == {1: {0, 1}, 4: {3, 4}, 6: {2, 5, 6, 7, 8, 9}}
    assert outliers == set()
    assert radius == pytest.approx(1.063, FLOAT_ERROR)
    assert verify_solution(graph, STRICT_CONSTRAINTS, 3, radius, set(clusters.keys())) is True


@pytest.mark.skip(reason="Takes too long to run")
def test_pbs_large_graph(seed_random):
    constraints = {Colour.BLUE: 50, Colour.RED: 50}
    k = 5
    graph = GraphLoader.get_graph("large")
    instance = PBS(graph, k, constraints)
    clusters, outliers, radius = instance.solve()

    assert radius == pytest.approx(51.2189, FLOAT_ERROR)
    assert clusters == {
        42: {2, 11, 12, 21, 26, 29, 31, 42, 44, 61, 67, 68, 70, 73, 82, 83, 87, 97, 104, 105, 109, 110, 111, 112},
        77: {0, 33, 34, 99, 5, 6, 75, 77, 49, 81, 51, 52, 85, 22, 55, 88, 30},
        89: {3, 7, 8, 15, 17, 18, 23, 24, 35, 39, 40, 43, 46, 47, 48, 50, 54, 57, 59, 63, 66, 76, 80, 84, 86, 89, 93,
             95, 96, 100, 102, 103, 108},
        92: {1, 4, 9, 10, 13, 14, 16, 19, 20, 25, 27, 28, 32, 36, 37, 38, 41, 45, 53, 56, 58, 60, 62, 64, 65, 69, 71,
             72, 74, 78, 79, 90, 91, 92, 94, 98, 101, 107, 113, 114},
        106: {106}
    }
    assert outliers == set()
    assert verify_solution(graph, constraints, k, radius, set(clusters.keys())) is True
