import pytest

from src.kcenter.colourful_pbs.alternative_architecture.roulette_colourful_pbs import RouletteColourfulPBS
from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import Individual, PBS
from tests.kcenter.util.assertion import FLOAT_ERROR_MARGIN
from tests.kcenter.util.create_test_graph import basic_graph_with_outlier
from tests.kcenter.util.genetic import generate_test_population_basic_graph


@pytest.fixture
def instance():
    constraints = {Colour.BLUE: 2, Colour.RED: 2}
    k = 2
    graph = basic_graph_with_outlier()
    instance = RouletteColourfulPBS(graph, k, constraints)
    instance.population = generate_test_population_basic_graph()
    return instance


@pytest.fixture
def instance_two():
    constraints = {Colour.BLUE: 2, Colour.RED: 2}
    k = 2
    graph = basic_graph_with_outlier()
    instance = RouletteColourfulPBS(graph, k, constraints, mating_pool_size=2)
    instance.population = generate_test_population_basic_graph()
    return instance


def test_roulette_selection(seed_random, instance):
    mating_pool = instance.selection()
    assert len(mating_pool) == 4
    assert mating_pool == [Individual({3, 4}), Individual({0, 1}), Individual({1, 2}), Individual({0, 1})]


def test_gen_crossover_1_offspring(seed_random, instance_two):
    mating_pool = instance_two.selection()

    offspring = []
    offspring_gen = instance_two.gen_offspring_crossover_1(mating_pool, 4, generation=1)
    for child in offspring_gen:
        offspring.append(child)
    assert len(offspring) == 4
    assert offspring == [Individual({0, 3}), Individual({3, 1}), Individual({3, 1}), Individual({3, 1})]


def test_gen_crossover_2_offspring(seed_random, instance_two):
    mating_pool = instance_two.selection()

    offspring = []
    offspring_gen = instance_two.gen_offspring_crossover_2(mating_pool, 3, generation=1)
    for child in offspring_gen:
        offspring.append(child)
    assert len(offspring) == 3
    assert offspring == [Individual({1, 3}), Individual({0, 4}), Individual({0, 4})]


def test_gen_mutation_1_offspring(seed_random, instance_two):
    mating_pool = instance_two.selection()

    offspring = []
    offspring_gen = instance_two.gen_offspring_mutation_1(mating_pool, 2, generation=1)
    for child in offspring_gen:
        offspring.append(child)
    assert len(offspring) == 2
    assert offspring == [Individual({1, 3}), Individual({0, 4})]


def test_gen_mutation_2_offspring(seed_random, instance_two):
    mating_pool = instance_two.selection()

    offspring = []
    offspring_gen = instance_two.gen_offspring_mutation_2(mating_pool, 1, generation=1)
    for child in offspring_gen:
        offspring.append(child)
    assert len(offspring) == 1
    assert offspring == [Individual({0, 4})]


def test_evolve(seed_random, instance):
    generator = instance.evolve()
    new_population = []
    for i in range(PBS.POPULATION_SIZE):
        new_population.append(next(generator))
    assert new_population == [Individual({3, 1}), Individual({0, 3}), Individual({0, 4}), Individual({1, 4}),
                              Individual({1, 4}), Individual({1, 4}), Individual({0, 4}), Individual({0, 4})]


def test_target_solve(seed_random):
    graph = basic_graph_with_outlier()
    constraints = {Colour.BLUE: 2, Colour.RED: 2}
    k = 2
    instance = RouletteColourfulPBS(graph, k, constraints)

    clusters, outliers, cost = instance.target_solve(0.708)
    assert cost == pytest.approx(0.7071, FLOAT_ERROR_MARGIN)
    assert outliers == set()
    assert clusters == {1: {0, 1}, 4: {3, 4}}
