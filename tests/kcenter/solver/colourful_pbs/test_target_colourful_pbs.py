from src.kcenter.colourful_pbs.target_colourful_pbs import TargetColourfulPBS
from src.kcenter.pbs.pbs import Individual
from tests.kcenter.solver.pbs.test_pbs import K, RELAXED_CONSTRAINTS
from tests.kcenter.util.create_test_graph import basic_graph_with_outlier


def test_set_name():
    graph = basic_graph_with_outlier()
    instance = TargetColourfulPBS(graph, K, RELAXED_CONSTRAINTS, name="test_name")
    assert instance.name == "test_name"


def test_generate_population(seed_random):
    graph = basic_graph_with_outlier()

    expected_population = [Individual({0, 3}), Individual({0, 3}), Individual({1, 3}), Individual({0, 3}),
                           Individual({0, 4}), Individual({0, 4}), Individual({1, 4}), Individual({0, 3})]
    instance = TargetColourfulPBS(graph, K, RELAXED_CONSTRAINTS)
    population_generator = instance.generate_population()

    actual_population = []
    for individual in population_generator:
        actual_population.append(individual)

    actual_population = [individual for individual in actual_population if individual is not None]
    assert actual_population == expected_population
