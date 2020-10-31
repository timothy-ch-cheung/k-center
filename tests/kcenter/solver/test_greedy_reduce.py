import pytest

from kcenter.solver.greedy_reduce import GreedyReduceSolver
from src.kcenter.verify.verify import verify_solution, Colour
from tests.kcenter.util.create_test_graph import basic_graph_with_outlier

RELAXED_CONSTRAINTS = {Colour.BLUE: 2, Colour.RED: 2}
K = 2
FLOAT_ERROR_MARGIN = 0.001


def test_greedy_basic_graph_outlier_colourful_clustering():
    graph = basic_graph_with_outlier()
    instance = GreedyReduceSolver(graph, K, RELAXED_CONSTRAINTS)
    clusters, radius = instance.solve()

    assert radius == pytest.approx(0.707, FLOAT_ERROR_MARGIN)
    assert list(clusters.keys()) == [0, 4]
    assert list(clusters.values()) == [{0, 1, 2}, {3, 4}]
    assert verify_solution(graph, RELAXED_CONSTRAINTS, K, radius, set(clusters.keys())) is True
