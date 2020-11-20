import pytest

from src.kcenter.constant.colour import Colour
from src.kcenter.greedy.greedy_reduce import GreedyReduceSolver
from src.kcenter.verify.verify import verify_solution
from tests.kcenter.util.create_test_graph import basic_graph_with_outlier, basic_graph

RELAXED_CONSTRAINTS = {Colour.BLUE: 2, Colour.RED: 2}
K = 2
FLOAT_ERROR_MARGIN = 0.001


def test_get_weights_returns_weights_below_radius():
    graph = basic_graph()
    weights = GreedyReduceSolver.get_weights(graph, 5)

    assert weights == [0.8544003745317533, 0.7280109889280517, 0.7071067811865476, 0.5099019513592785]


def test_get_weights_returns_sorted_list():
    graph = basic_graph()
    weights = GreedyReduceSolver.get_weights(graph, 10)

    assert weights == sorted(weights, reverse=True)


def test_greedy_basic_graph_outlier_colourful_clustering():
    graph = basic_graph_with_outlier()
    instance = GreedyReduceSolver(graph, K, RELAXED_CONSTRAINTS)
    clusters, outliers, radius = instance.solve()

    assert radius == pytest.approx(0.707, FLOAT_ERROR_MARGIN)
    assert clusters == {
        0: {0, 1},
        4: {3, 4}
    }
    assert outliers == {2}
    assert verify_solution(graph, RELAXED_CONSTRAINTS, K, radius, set(clusters.keys())) is True


def test_generator_greedy_basic_graph_outlier_colourful_clustering():
    graph = basic_graph_with_outlier()
    instance = GreedyReduceSolver(graph, K, RELAXED_CONSTRAINTS)
    solution = instance.generator()

    assert next(solution) == ({0: {0, 1, 2, 3, 4}}, set(), pytest.approx(6.113, FLOAT_ERROR_MARGIN),
                              "The initial center is arbitrarily chosen, its coordinates are (1.3, 2.6). It is a blue point.")
    assert next(solution) == ({0: {0, 1, 2}, 4: {3, 4}}, set(), pytest.approx(5.515, FLOAT_ERROR_MARGIN),
                              "We find the furthest point from our previous center, which is the point at (6.4, 4.7). It is a red point 5.515 distance away. This makes the current cost 5.515.")
    assert next(solution) == ({0: {0, 1, 2}, 4: {3, 4}}, set(), pytest.approx(3.785, FLOAT_ERROR_MARGIN),
                              "Our 2 centers have been chosen. To calculate the final cost, we find the distance to the furthest point from the previous center. This makes the final cost 3.785.")
    assert next(solution) == ({0: {0, 1, 2}, 4: {3, 4}}, set(), pytest.approx(0.707, FLOAT_ERROR_MARGIN),
                              "decrease weight to 0.707")
    assert next(solution) == ({0: {0, 1, 2}, 4: {3, 4}}, set(), pytest.approx(0.707, FLOAT_ERROR_MARGIN),
                              "completed reduced solution to radius of 0.707")
