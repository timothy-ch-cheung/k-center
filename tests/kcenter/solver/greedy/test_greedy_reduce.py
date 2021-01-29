import pytest

from src.kcenter.constant.colour import Colour
from src.kcenter.greedy.greedy_reduce import GreedyReduce
from src.kcenter.verify.verify import verify_solution
from tests.kcenter.util.create_test_graph import basic_graph_with_outlier, basic_graph

RELAXED_CONSTRAINTS = {Colour.BLUE: 2, Colour.RED: 2}
K = 2
FLOAT_ERROR_MARGIN = 0.001


def test_get_weights_returns_weights_below_radius():
    graph = basic_graph()
    weights = GreedyReduce.get_weights(graph, 5)

    assert weights == [0.8544003745317533, 0.7280109889280517, 0.7071067811865476, 0.5099019513592785]


def test_get_weights_returns_sorted_list():
    graph = basic_graph()
    weights = GreedyReduce.get_weights(graph, 10)

    assert weights == sorted(weights, reverse=True)


def test_greedy_basic_graph_outlier_colourful_clustering():
    graph = basic_graph_with_outlier()
    instance = GreedyReduce(graph, K, RELAXED_CONSTRAINTS)
    clusters, outliers, radius = instance.solve()

    assert radius == pytest.approx(0.707, FLOAT_ERROR_MARGIN)
    assert clusters == {
        0: {0, 1},
        4: {3, 4}
    }
    assert outliers == {2}
    assert verify_solution(graph, RELAXED_CONSTRAINTS, K, radius, set(clusters.keys())) is True
