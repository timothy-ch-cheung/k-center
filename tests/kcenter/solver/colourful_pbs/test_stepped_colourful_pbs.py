from src.kcenter.colourful_pbs.stepped_colourful_pbs import SteppedColourfulPBS
from src.kcenter.constant.solver_state import SolverState
from src.kcenter.solver.abstract_generator import Solution
from tests.kcenter.solver.pbs.test_pbs import K, RELAXED_CONSTRAINTS
from tests.kcenter.util.assertion import assert_step_equal
from tests.kcenter.util.create_test_graph import basic_graph_with_outlier
from tests.kcenter.util.generator import next_main


def test_stepped_pbs(seed_random):
    graph = basic_graph_with_outlier()
    instance = SteppedColourfulPBS(graph, K, RELAXED_CONSTRAINTS)
    solution = instance.generator()

    assert_step_equal(next_main(solution),
                      ([
                           Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={0: {0, 1}, 4: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={3: {0, 1, 2, 3}, 4: {4}}, cost=5.6302, outliers=set()),
                           Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={1: {0, 1}, 4: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={1: {0, 1}, 4: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={0: {0, 1, 3}, 2: {2}}, cost=5.2839, outliers={4})
                       ],
                       "The initial population is generated, the evolution phase can now be started",
                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next_main(solution),
                      ([
                           Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={0: {0, 1}, 4: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={1: {0, 1}, 4: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={1: {0, 1}, 4: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={0: {0, 1, 3}, 2: {2}}, cost=5.2839, outliers={4})
                       ],
                       "The best individual in this generation is 0 with a cost of 0.707",
                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next_main(solution),
                      ([
                           Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={0: {0, 1}, 4: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={1: {0, 1}, 4: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={1: {0, 1}, 4: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={0: {0, 1, 3}, 2: {2}}, cost=5.2839, outliers={4})
                       ],
                       "The best individual in this generation is 0 with a cost of 0.707",
                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next_main(solution),
                      ([
                           Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={0: {0, 1}, 4: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={1: {0, 1}, 4: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={1: {0, 1}, 4: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={0: {0, 1, 3}, 2: {2}}, cost=5.2839, outliers={4})
                       ],
                       "The best individual in this generation is 0 with a cost of 0.707",
                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next_main(solution),
                      ([
                           Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={0: {0, 1}, 4: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={1: {0, 1}, 4: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={1: {0, 1}, 4: {3, 4}}, cost=0.7071, outliers={2}),
                           Solution(clusters={0: {0, 1, 3}, 2: {2}}, cost=5.2839, outliers={4})
                       ],
                       "3 generations were completed. The fittest individual was 0 with a cost of 0.707",
                       SolverState.INACTIVE))


def test_stepped_pbs_inspect_local_search(seed_random):
    graph = basic_graph_with_outlier()
    instance = SteppedColourfulPBS(graph, K, RELAXED_CONSTRAINTS)
    solution = instance.generator()

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {0, 1, 2, 3, 4}}, cost=5.6303, outliers=set())],
                       "POPULATION GENERATION: The current individual {(5.9, 5.2)} has less than 2 centers, 1 more needs to be added",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2})],
                       "POPULATION GENERATION: The point furthest away from its nearest center, the point at (1.2, 2.1), is added to the solution, the new cost is 5.63",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2})],
                       "POPULATION GENERATION: At the end of local search initialisation, the set of centers is {(5.9, 5.2), (1.2, 2.1)}",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2})],
                       "POPULATION GENERATION: We now enter a phase where we make swaps between points and centers.",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2})],
                       """POPULATION GENERATION: The local search ended after 0 iterations, the new cost of the solution (with 
        centers {(5.9, 5.2), (1.2, 2.1)}) is 0.707""",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={1: {0, 1}, 3: {3, 4}}, cost=0.7071, outliers={2})],
                       """POPULATION GENERATION: Post local search, the cost of covering the required colours needs to be calculated.
         The. A radius of 0.707 is required to cover 
         2 blue points and 2 red points""",
                       SolverState.ACTIVE_SUB))
