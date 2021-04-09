from src.kcenter.constant.solver_state import SolverState
from src.kcenter.pbs.pbs import Individual
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
                           Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={2: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set())
                       ],
                       "The best individual in this generation is 1 with a cost of 3.785",
                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next_main(solution),
                      ([
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=3.7855, outliers=set()),
                           Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={2: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set())
                       ],
                       "The best individual in this generation is 1 with a cost of 3.785",
                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next_main(solution),
                      ([
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=3.7855, outliers=set()),
                           Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={2: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set())
                       ],
                       "The best individual in this generation is 1 with a cost of 3.785",
                       SolverState.ACTIVE_MAIN))

    assert_step_equal(next_main(solution),
                      ([
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=3.7855, outliers=set()),
                           Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={1: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set()),
                           Solution(clusters={2: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set())
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


def test_stepped_pbs_inspect_single_generation(seed_random):
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

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {0, 1, 2, 3}, 4: {4}}, cost=5.6303, outliers=set())],
                       """INSPECT GENERATION 1: A random mutation operator is applied to the set of centers {(6.4, 4.7), (1.3, 2.6)}, where a subset of the original centers is combined with points sampled random to get the new center set {(5.9, 5.2), (6.4, 4.7)}""",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {0, 1, 2, 3}, 4: {4}}, cost=5.6303, outliers=set())],
                       "INSPECT GENERATION 1: Local search is ran on the randomly mutated solution",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {0, 1, 2, 3}, 4: {4}}, cost=5.6303, outliers=set())],
                       "INSPECT GENERATION 1: At the end of local search initialisation, the set of centers is {(5.9, 5.2), (6.4, 4.7)}",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {0, 1, 2, 3}, 4: {4}}, cost=5.6303, outliers=set())],
                       "INSPECT GENERATION 1: We now enter a phase where we make swaps between points and centers.",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: [6.4 4.7] is removed from the set of centers and it is replaced with [1.2 2.1], the new cost is 4.258",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {3, 4}, 0: {0, 1, 2}}, cost=3.7855, outliers=set())],
                       "INSPECT GENERATION 1: [1.2 2.1] is removed from the set of centers and it is replaced with [1.3 2.6], the new cost is 3.785",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {3, 4}, 2: {0, 1, 2}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: [1.3 2.6] is removed from the set of centers and it is replaced with [0.5 6.3], the new cost is 4.258",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {3, 4}, 2: {0, 1, 2}}, cost=4.2579, outliers=set())],
                       """INSPECT GENERATION 1: The local search ended after 3 iterations, the new cost of the solution (with 
        centers {(0.5, 6.3), (5.9, 5.2)}) is 4.258""",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {3, 4}, 2: {0, 1, 2}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: {(0.5, 6.3), (5.9, 5.2)} will not improve the population so it is not added",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={0: {0, 1, 2}, 3: {3, 4}}, cost=3.7855, outliers=set())],
                       """INSPECT GENERATION 1: A random crossover operator is applied to the two parents {(5.9, 5.2), (1.2, 2.1)} and 
        {(6.4, 4.7), (1.3, 2.6)}, by randomly sampling 2 centers from them - the resulting child center set is 
        {(5.9, 5.2), (1.3, 2.6)}""",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={0: {0, 1, 2}, 3: {3, 4}}, cost=3.7855, outliers=set())],
                       "INSPECT GENERATION 1: Local search is ran on the child solution",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={0: {0, 1, 2}, 3: {3, 4}}, cost=3.7855, outliers=set())],
                       "INSPECT GENERATION 1: At the end of local search initialisation, the set of centers is {(5.9, 5.2), (1.3, 2.6)}",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={0: {0, 1, 2}, 3: {3, 4}}, cost=3.7855, outliers=set())],
                       "INSPECT GENERATION 1: We now enter a phase where we make swaps between points and centers.",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: [1.3 2.6] is removed from the set of centers and it is replaced with [0.5 6.3], the new cost is 4.258",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       """INSPECT GENERATION 1: The local search ended after 1 iterations, the new cost of the solution (with 
        centers {(0.5, 6.3), (5.9, 5.2)}) is 4.258""",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: {(0.5, 6.3), (5.9, 5.2)} will not improve the population so it is not added",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: After the child solution has been locally optimised, it is passed through a directed mutation operator",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       """INSPECT GENERATION 1: A directed mutation operator is applied to the set of centers {(0.5, 6.3), (5.9, 5.2)}, where the two 
        closest centers set() are deleted from the solution, resulting in the set of 
        centers {(0.5, 6.3), (5.9, 5.2)}""",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: Local search is ran on the directed mutated solution",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: At the end of local search initialisation, the set of centers is {(0.5, 6.3), (5.9, 5.2)}",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.25793, outliers=set())],
                       "INSPECT GENERATION 1: We now enter a phase where we make swaps between points and centers.",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: [0.5 6.3] is removed from the set of centers and it is replaced with [1.2 2.1], the new cost is 4.258",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       """INSPECT GENERATION 1: The local search ended after 1 iterations, the new cost of the solution (with 
        centers {(5.9, 5.2), (1.2, 2.1)}) is 4.258""",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: {(5.9, 5.2), (1.2, 2.1)} will not improve the population so it is not added",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {0, 1, 2, 3, 4}}, cost=5.63028, outliers=set())],
                       """INSPECT GENERATION 1: A directed crossover operator is applied to the two parents {(5.9, 5.2), (1.2, 2.1)} and 
        {(6.4, 4.7), (1.3, 2.6)}, two children are created by mixing centers from the parents - the resulting children 
        are {(5.9, 5.2)} and {(1.3, 2.6), (1.2, 2.1)}""",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {0, 1, 2, 3, 4}}, cost=5.6303, outliers=set())],
                       "INSPECT GENERATION 1: Local search is ran on the first child solution",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {0, 1, 2, 3, 4}}, cost=5.6303, outliers=set())],
                       "INSPECT GENERATION 1: The current individual {(5.9, 5.2)} has less than 2 centers, 1 more needs to be added",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       """INSPECT GENERATION 1: The point furthest away from its nearest center, the point at (1.2, 2.1), is added to the solution, the new cost is 4.258""",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: At the end of local search initialisation, the set of centers is {(5.9, 5.2), (1.2, 2.1)}",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={1: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: We now enter a phase where we make swaps between points and centers.",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={0: {0, 1, 2}, 3: {3, 4}}, cost=3.7855, outliers=set())],
                       "INSPECT GENERATION 1: [1.2 2.1] is removed from the set of centers and it is replaced with [1.3 2.6], the new cost is 3.785",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: [1.3 2.6] is removed from the set of centers and it is replaced with [0.5 6.3], the new cost is 4.258",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       """INSPECT GENERATION 1: The local search ended after 2 iterations, the new cost of the solution (with 
        centers {(0.5, 6.3), (5.9, 5.2)}) is 4.258""",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: {(0.5, 6.3), (5.9, 5.2)} will not improve the population so it is not added",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {3, 4}, 2: {0, 1, 2}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: After the first child solution has been locally optimised, it is passed through a directed mutation operator",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {0, 1, 2, 3}, 4: {4}}, cost=5.6303, outliers=set())],
                       """INSPECT GENERATION 1: A directed mutation operator is applied to the set of centers {(0.5, 6.3), (5.9, 5.2)}, where the two 
        closest centers {(0.5, 6.3)} are deleted from the solution, resulting in the set of 
        centers {(5.9, 5.2), (6.4, 4.7)}""",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {0, 1, 2, 3}, 4: {4}}, cost=5.6303, outliers=set())],
                       "INSPECT GENERATION 1: Local search is ran on the directed mutated solution",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {0, 1, 2, 3}, 4: {4}}, cost=5.6303, outliers=set())],
                       "INSPECT GENERATION 1: At the end of local search initialisation, the set of centers is {(5.9, 5.2), (6.4, 4.7)}",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {0, 1, 2, 3}, 4: {4}}, cost=5.6303, outliers=set())],
                       "INSPECT GENERATION 1: We now enter a phase where we make swaps between points and centers.",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=3.7855, outliers=set())],
                       "INSPECT GENERATION 1: [5.9 5.2] is removed from the set of centers and it is replaced with [1.3 2.6], the new cost is 3.785",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={4: {3, 4}, 2: {0, 1, 2}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: [1.3 2.6] is removed from the set of centers and it is replaced with [0.5 6.3], the new cost is 4.258",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={4: {3, 4}, 2: {0, 1, 2}}, cost=4.2579, outliers=set())],
                       """INSPECT GENERATION 1: The local search ended after 2 iterations, the new cost of the solution (with 
        centers {(0.5, 6.3), (6.4, 4.7)}) is 4.258""",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={4: {3, 4}, 2: {0, 1, 2}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: {(0.5, 6.3), (6.4, 4.7)} will not improve the population so it is not added",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=3.7855, outliers=set())],
                       "INSPECT GENERATION 1: Local search is ran on the second child solution",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={0: {0, 2, 3, 4}, 1: {1}}, cost=5.5154, outliers=set())],
                       "INSPECT GENERATION 1: At the end of local search initialisation, the set of centers is {(1.3, 2.6), (1.2, 2.1)}",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={0: {0, 2, 3, 4}, 1: {1}}, cost=5.5154, outliers=set())],
                       "INSPECT GENERATION 1: We now enter a phase where we make swaps between points and centers.",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=3.7855, outliers=set())],
                       "INSPECT GENERATION 1: [1.2 2.1] is removed from the set of centers and it is replaced with [6.4 4.7], the new cost is 3.785",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={2: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: [1.3 2.6] is removed from the set of centers and it is replaced with [0.5 6.3], the new cost is 4.258",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={2: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set())],
                       """INSPECT GENERATION 1: The local search ended after 2 iterations, the new cost of the solution (with 
        centers {(0.5, 6.3), (6.4, 4.7)}) is 4.258""",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={2: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: {(0.5, 6.3), (6.4, 4.7)} will improve the population; it replaces the lowest ranked individual in the population",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={2: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: After the second child solution has been locally optimised, it is passed through a directed mutation operator",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {0, 1, 2, 3}, 4: {4}}, cost=5.6303, outliers=set())],
                       """INSPECT GENERATION 1: A directed mutation operator is applied to the set of centers {(0.5, 6.3), (6.4, 4.7)}, where the two 
        closest centers {(0.5, 6.3)} are deleted from the solution, resulting in the set of 
        centers {(5.9, 5.2), (6.4, 4.7)}""",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {0, 1, 2, 3}, 4: {4}}, cost=5.6303, outliers=set())],
                       "INSPECT GENERATION 1: Local search is ran on the directed mutated solution",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {0, 1, 2, 3}, 4: {4}}, cost=5.6303, outliers=set())],
                       "INSPECT GENERATION 1: At the end of local search initialisation, the set of centers is {(5.9, 5.2), (6.4, 4.7)}",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {0, 1, 2, 3}, 4: {4}}, cost=5.6303, outliers=set())],
                       "INSPECT GENERATION 1: We now enter a phase where we make swaps between points and centers.",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={0: {0, 1, 2}, 3: {3, 4}}, cost=3.7855, outliers=set())],
                       "INSPECT GENERATION 1: [6.4 4.7] is removed from the set of centers and it is replaced with [1.3 2.6], the new cost is 3.785",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {3, 4}, 2: {0, 1, 2}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: [1.3 2.6] is removed from the set of centers and it is replaced with [0.5 6.3], the new cost is 4.258",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={3: {3, 4}, 2: {0, 1, 2}}, cost=4.2579, outliers=set())],
                       """INSPECT GENERATION 1: The local search ended after 2 iterations, the new cost of the solution (with 
        centers {(0.5, 6.3), (5.9, 5.2)}) is 4.258""",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={2: {0, 1, 2}, 3: {3, 4}}, cost=4.2579, outliers=set())],
                       "INSPECT GENERATION 1: {(0.5, 6.3), (5.9, 5.2)} will not improve the population so it is not added",
                       SolverState.ACTIVE_SUB))


def test_local_search_repeated_swap(seed_random):
    graph = basic_graph_with_outlier()
    instance = SteppedPBS(graph, K, RELAXED_CONSTRAINTS)
    individual = Individual(centers={0, 1})
    individual.init_nearest_centers(instance.points, instance.weights)
    solution = instance.local_search(individual, 4)

    assert_step_equal(next(solution),
                      ([Solution(clusters={0: {0, 2, 3, 4}, 1: {1}}, cost=5.5154, outliers=set())],
                       "POPULATION GENERATION: At the end of local search initialisation, the set of centers is {(1.3, 2.6), (1.2, 2.1)}",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={0: {0, 2, 3, 4}, 1: {1}}, cost=5.5154, outliers=set())],
                       "POPULATION GENERATION: We now enter a phase where we make swaps between points and centers.",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=3.7855, outliers=set())],
                       """POPULATION GENERATION: [1.2 2.1] is removed from the set of centers and it is replaced with [6.4 4.7], the new cost is 3.785""",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={2: {0, 1, 2}, 4: {3, 4}}, cost=4.2579, outliers=set())],
                       """POPULATION GENERATION: [1.3 2.6] is removed from the set of centers and it is replaced with [0.5 6.3], the new cost is 4.258""",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=3.7855, outliers=set())],
                       """POPULATION GENERATION: [0.5 6.3] is removed from the set of centers and it is replaced with [1.3 2.6], the new cost is 3.785""",
                       SolverState.ACTIVE_SUB))

    assert_step_equal(next(solution),
                      ([Solution(clusters={0: {0, 1, 2}, 4: {3, 4}}, cost=3.7855, outliers=set())],
                       """POPULATION GENERATION: [1.3 2.6] and [0.5 6.3] we identified as the best center and point pair to swap, 
            but the swap was not made as they have already been swapped before in this invocation of local search""",
                       SolverState.ACTIVE_SUB))
