import pytest

from src.kcenter.greedy.stepped_greedy import SteppedGreedy
from tests.kcenter.solver.greedy.test_greedy import RELAXED_CONSTRAINTS, K, FLOAT_ERROR_MARGIN, STRICT_CONSTRAINTS
from tests.kcenter.util.create_test_graph import basic_graph_with_outlier, basic_graph


def test_generator_greedy_basic_graph_colourful_clustering():
    graph = basic_graph()
    instance = SteppedGreedy(graph, K, STRICT_CONSTRAINTS)
    solution = instance.generator()

    assert next(solution) == ({0: {0, 1, 2, 3, 4}}, set(), pytest.approx(6.369, FLOAT_ERROR_MARGIN),
                              "The initial center is arbitrarily chosen, its coordinates are (1.3, 2.6). It is a blue point.",
                              True)
    assert next(solution) == ({0: {0, 1, 2}, 4: {3, 4}}, set(), pytest.approx(5.515, FLOAT_ERROR_MARGIN),
                              "We find the point which has the maximum distance from its closest center, which is the point at (6.4, 4.7). It is a red point 5.515 distance away. This makes the current cost 5.515.",
                              True)
    assert next(solution) == ({0: {0, 1, 2}, 4: {3, 4}}, set(), pytest.approx(0.854, FLOAT_ERROR_MARGIN),
                              "Our 2 centers have been chosen. To calculate the final cost, we find the distance to the furthest point from the previous center. This makes the final cost 0.854.",
                              False)


def test_generator_greedy_basic_graph_outlier_colourful_clustering():
    graph = basic_graph_with_outlier()
    instance = SteppedGreedy(graph, K, RELAXED_CONSTRAINTS)
    solution = instance.generator()

    assert next(solution) == ({0: {0, 1, 2, 3, 4}}, set(), pytest.approx(6.113, FLOAT_ERROR_MARGIN),
                              "The initial center is arbitrarily chosen, its coordinates are (1.3, 2.6). It is a blue point.",
                              True)
    assert next(solution) == ({0: {0, 1, 2}, 4: {3, 4}}, set(), pytest.approx(5.515, FLOAT_ERROR_MARGIN),
                              "We find the point which has the maximum distance from its closest center, which is the point at (6.4, 4.7). It is a red point 5.515 distance away. This makes the current cost 5.515.",
                              True)
    assert next(solution) == (
        {0: {0, 1, 2}, 4: {3, 4}}, set(), pytest.approx(3.785, FLOAT_ERROR_MARGIN),
        "Our 2 centers have been chosen. To calculate the final cost, we find the distance to the furthest point from the previous center. This makes the final cost 3.785.",
        False)
