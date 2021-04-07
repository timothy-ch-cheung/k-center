from src.kcenter.constant.solver_state import SolverState
from src.kcenter.greedy.stepped_greedy import SteppedGreedy
from src.kcenter.solver.abstract_generator import Solution
from tests.kcenter.solver.greedy.test_greedy import RELAXED_CONSTRAINTS, K, STRICT_CONSTRAINTS
from tests.kcenter.util.assertion import assert_step_equal
from tests.kcenter.util.create_test_graph import basic_graph_with_outlier, basic_graph


def test_generator_greedy_basic_graph_colourful_clustering():
    graph = basic_graph()
    instance = SteppedGreedy(graph, K, STRICT_CONSTRAINTS)
    solution = instance.generator()

    assert_step_equal(next(solution), ([Solution(clusters={0: {0, 1, 2, 3, 4}}, cost=6.369, outliers=set())],
                                       "The initial center is arbitrarily chosen, its coordinates are (1.3, 2.6). It is a blue point.",
                                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next(solution), ([Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=5.515, outliers=set())],
                                       "We find the point which has the maximum distance from its closest center, which is the point at (6.4, 4.7). It is a red point 5.515 distance away. This makes the current cost 5.515.",
                                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next(solution), ([Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=0.854, outliers=set())],
                                       "Our 2 centers have been chosen. To calculate the final cost, we find the distance to the furthest point from the previous center. This makes the final cost 0.854.",
                                       SolverState.INACTIVE))


def test_generator_greedy_basic_graph_outlier_colourful_clustering():
    graph = basic_graph_with_outlier()
    instance = SteppedGreedy(graph, K, RELAXED_CONSTRAINTS)
    solution = instance.generator()

    assert_step_equal(next(solution), ([Solution(clusters={0: {0, 1, 2, 3, 4}}, cost=6.113, outliers=set())],
                                       "The initial center is arbitrarily chosen, its coordinates are (1.3, 2.6). It is a blue point.",
                                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next(solution), ([Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=5.515, outliers=set())],
                                       "We find the point which has the maximum distance from its closest center, which is the point at (6.4, 4.7). It is a red point 5.515 distance away. This makes the current cost 5.515.",
                                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next(solution), ([Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=3.785, outliers=set())],
                                       "Our 2 centers have been chosen. To calculate the final cost, we find the distance to the furthest point from the previous center. This makes the final cost 3.785.",
                                       SolverState.INACTIVE))
