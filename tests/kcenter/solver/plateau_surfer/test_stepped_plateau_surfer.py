from src.kcenter.constant.solver_state import SolverState
from src.kcenter.plateau_surfer.stepped_plateau_surfer import SteppedPlateauSurfer
from src.kcenter.solver.abstract_generator import Solution
from tests.kcenter.solver.pbs.test_pbs import RELAXED_CONSTRAINTS, K
from tests.kcenter.util.assertion import assert_step_equal
from tests.kcenter.util.create_test_graph import basic_graph_with_outlier


def test_stepped_plateau_surfer(seed_random):
    graph = basic_graph_with_outlier()
    instance = SteppedPlateauSurfer(graph, K, RELAXED_CONSTRAINTS)
    solution = instance.generator(iterations=2)

    assert_step_equal(next(solution), ([], "Start of GRASP iteration 1.", SolverState.ACTIVE_MAIN))

    assert_step_equal(next(solution), ([Solution({0: {0, 1, 2}, 3: {3, 4}}, 3.7855)],
                                       "An initial solution is created using the Greedy Randomised Build algorithm. The centers are {(5.9, 5.2), (1.3, 2.6)}, which has a cost of 3.785.",
                                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next(solution), ([Solution({0: {0, 1, 2}, 3: {3, 4}}, 3.7855)],
                                       "After the Plateau Surfer local search is performed on the initial solution, we get the centers {(5.9, 5.2), (1.3, 2.6)}. The cost is 3.785.",
                                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next(solution), ([Solution({0: {0, 1, 2}, 3: {3, 4}}, 3.7855)],
                                       "The new solution {(5.9, 5.2), (1.3, 2.6)} has  cost 3.785. Since this is lower than the best cost inf the best solution is updated.",
                                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next(solution), ([], "Start of GRASP iteration 2.", SolverState.ACTIVE_MAIN))

    assert_step_equal(next(solution), ([Solution({0: {0, 1, 2}, 4: {3, 4}}, 3.7855)],
                                       "An initial solution is created using the Greedy Randomised Build algorithm. The centers are {(6.4, 4.7), (1.3, 2.6)}, which has a cost of 3.785.",
                                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next(solution), ([Solution({0: {0, 1, 2}, 4: {3, 4}}, 3.7855)],
                                       "After the Plateau Surfer local search is performed on the initial solution, we get the centers {(6.4, 4.7), (1.3, 2.6)}. The cost is 3.785.",
                                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next(solution), ([Solution({0: {0, 1, 2}, 3: {3, 4}}, 3.7855)],
                                       "The new solution has cost 3.785 which is not lower than the best cost 3.785. Therefore the best solution is not updated.",
                                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next(solution), ([Solution({0: {0, 1, 2}, 3: {3, 4}}, 3.7855)],
                                       "2 iterations of GRASP have been completed. The best cost is 3.785 with the centers {(5.9, 5.2), (1.3, 2.6)}",
                                       SolverState.INACTIVE))
