import pytest

from src.server.graph_loader import GraphLoader
from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import PBS
from src.kcenter.verify.verify import verify_solution
from tests.kcenter.constant.consts import FLOAT_ERROR
from tests.kcenter.util.create_test_graph import basic_graph, basic_graph_with_outlier, medium_graph

FLOAT_ERROR_MARGIN = 0.001
STRICT_CONSTRAINTS = {Colour.BLUE: 2, Colour.RED: 3}
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

    assert clusters == {1: {0, 1, 2}, 3: {3, 4}}
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
    instance = PBS(graph, 10, constraints)
    clusters, outliers, radius = instance.solve()

    assert radius == pytest.approx(45.4066, FLOAT_ERROR)
    assert clusters == {
        1: {1, 13, 14, 16, 19, 20, 25, 28, 32, 36, 37, 41, 53, 58, 62, 64, 69, 71, 72, 74, 78, 91, 98},
        9: {9, 45, 79, 90, 60, 94},
        10: {65, 4, 38, 10, 114, 56, 27, 92},
        12: {97, 2, 68, 70, 42, 12, 44, 110, 111, 82, 61, 83, 21, 87, 26, 29, 31},
        23: {35, 7, 43, 108, 15, 50, 86, 23, 24, 89, 59, 95, 63},
        30: {0, 33, 34, 99, 5, 6, 75, 77, 49, 81, 51, 52, 85, 22, 55, 88, 30},
        76: {3, 8, 17, 18, 39, 40, 46, 47, 48, 54, 57, 66, 76, 80, 84, 93, 96, 100, 102, 103, 109},
        106: {106},
        112: {67, 104, 73, 105, 11, 107, 112},
        113: {113, 101}
    }
    assert outliers == set()
    assert verify_solution(graph, constraints, k, radius, set(clusters.keys())) is True
