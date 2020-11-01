import pytest

from src.kcenter.solver.greedy_reduce import GreedyReduceSolver
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


def test_generator_greedy_basic_graph_outlier_colourful_clustering():
    graph = basic_graph_with_outlier()
    instance = GreedyReduceSolver(graph, K, RELAXED_CONSTRAINTS)
    solution = instance.generator()

    assert next(solution) == ({0: {0, 1, 2, 3, 4}}, pytest.approx(7.910, FLOAT_ERROR_MARGIN), 'initial center')
    assert next(solution) == ({0: {0, 1, 2}, 4: {3, 4}}, pytest.approx(5.515, FLOAT_ERROR_MARGIN), 'center 2 added')
    assert next(solution) == ({0: {0, 1, 2}, 4: {3, 4}}, pytest.approx(3.275, FLOAT_ERROR_MARGIN), 'completed solution with radius of 3.276')
    assert next(solution) == ({0: {0, 1, 2}, 4: {3, 4}}, pytest.approx(0.707, FLOAT_ERROR_MARGIN), 'decrease weight to 0.707')
    assert next(solution) == ({0: {0, 1, 2}, 4: {3, 4}}, pytest.approx(0.707, FLOAT_ERROR_MARGIN), 'completed reduced solution to radius of 0.707')