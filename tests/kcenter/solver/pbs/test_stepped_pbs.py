from src.kcenter.constant.solver_state import SolverState
from src.kcenter.pbs.stepped_pbs import SteppedPBS
from src.kcenter.solver.abstract_generator import Solution
from tests.kcenter.solver.pbs.test_pbs import K, RELAXED_CONSTRAINTS
from tests.kcenter.util.assertion import assert_step_equal
from tests.kcenter.util.create_test_graph import basic_graph_with_outlier
from tests.kcenter.util.generator import next_main


def test_stepped_pbs(seed_random):
    graph = basic_graph_with_outlier()
    instance = SteppedPBS(graph, K, RELAXED_CONSTRAINTS)
    solution = instance.generator()

    assert_step_equal(next_main(solution),
                      ([
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=3.7855, outliers=set()),
                           Solution(clusters={3: {0, 1, 2, 3}, 4: {4}}, cost=5.6302, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 4}, 2: {2, 3}}, cost=5.8137, outliers=set())
                       ],
                       "The initial population is generated, the evolution phase can now be started",
                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next_main(solution),
                      ([
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=3.7855, outliers=set()),
                           Solution(clusters={3: {0, 1, 2, 3}, 4: {4}}, cost=5.6302, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={0: {0, 2, 3, 4}, 1: {1}}, cost=5.5154, outliers=set())
                       ],
                       "The best individual in this generation is 1 with a cost of 3.785",
                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next_main(solution),
                      ([
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=3.7855, outliers=set()),
                           Solution(clusters={3: {0, 1, 2, 3}, 4: {4}}, cost=5.6302, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={0: {0, 2, 3, 4}, 1: {1}}, cost=5.5154, outliers=set())
                       ],
                       "The best individual in this generation is 1 with a cost of 3.785",
                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next_main(solution),
                      ([
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=3.7855, outliers=set()),
                           Solution(clusters={3: {0, 1, 2, 3}, 4: {4}}, cost=5.6302, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={0: {0, 2, 3, 4}, 1: {1}}, cost=5.5154, outliers=set())
                       ],
                       "The best individual in this generation is 1 with a cost of 3.785",
                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next_main(solution),
                      ([
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=3.7855, outliers=set()),
                           Solution(clusters={3: {0, 1, 2, 3}, 4: {4}}, cost=5.6302, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={0: {0, 2, 3, 4}, 1: {1}}, cost=5.5154, outliers=set())
                       ],
                       "3 generations were completed. The fittest individual was 1 with a cost of 3.785",
                       SolverState.INACTIVE))

def test_stepped_pbs_inspect_population_generation(seed_random):
    graph = basic_graph_with_outlier()
    instance = SteppedPBS(graph, K, RELAXED_CONSTRAINTS)
    solution = instance.generator()

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {0, 1, 2, 3, 4}}, cost=5.6303, outliers=set())],
                       "POPULATION GENERATION: The current individual {(5.9, 5.2)} has less than 2 centers, 1 more needs to be added",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       "POPULATION GENERATION: The point furthest away from its nearest center, the point at (1.2, 2.1), is added to the solution, the new cost is 4.258",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       "POPULATION GENERATION: At the end of local search initialisation, the set of centers is {(5.9, 5.2), (1.2, 2.1)}",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       "POPULATION GENERATION: We now enter a phase where we make swaps between points and centers.",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       """POPULATION GENERATION: The local search ended after 0 iterations, the new cost of the solution (with 
        centers {(5.9, 5.2), (1.2, 2.1)}) is 4.258""",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       "POPULATION GENERATION: The centers {(5.9, 5.2), (1.2, 2.1)} are added to the population",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={0: {0, 1, 2, 3, 4}}, cost=5.5154, outliers=set())],
                       "POPULATION GENERATION: The current individual {(1.3, 2.6)} has less than 2 centers, 1 more needs to be added",
                       SolverState.ACTIVE_SUB))
