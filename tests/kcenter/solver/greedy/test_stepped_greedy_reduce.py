from src.kcenter.constant.solver_state import SolverState
from src.kcenter.greedy.stepped_greedy_reduce import SteppedGreedyReduce
from src.kcenter.solver.abstract_generator import Solution
from tests.kcenter.solver.greedy.test_greedy import K
from tests.kcenter.solver.greedy.test_greedy_reduce import RELAXED_CONSTRAINTS
from tests.kcenter.util.assertion import assert_step_equal
from tests.kcenter.util.create_test_graph import basic_graph_with_outlier


def test_generator_greedy_reduce_basic_graph_outlier_colourful_clustering():
    graph = basic_graph_with_outlier()
    instance = SteppedGreedyReduce(graph, K, RELAXED_CONSTRAINTS)
    solution = instance.generator()

    assert_step_equal(next(solution), ([Solution(clusters={0: {0, 1, 2, 3, 4}}, cost=6.113, outliers=set())],
                                       "The initial center is arbitrarily chosen, its coordinates are (1.3, 2.6). It is a blue point.",
                                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next(solution), ([Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=5.515, outliers=set())],
                                       "We find the point which has the maximum distance from its closest center, which is the point at (6.4, 4.7). It is a red point 5.515 distance away. This makes the current cost 5.515.",
                                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next(solution), ([Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=3.785, outliers=set())],
                                       "Our 2 centers have been chosen. The current cost is 3.785, we will continue to reduce the cost until the solution does not meet the constraints.",
                                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next(solution), ([Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=0.707, outliers=set())],
                                       "decrease weight to 0.707",
                                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next(solution), ([Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=0.707, outliers=set())],
                                       "completed reduced solution to radius of 0.707",
                                       SolverState.INACTIVE))
