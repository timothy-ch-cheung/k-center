import random

import pytest

from src.kcenter.pbs.pbs import Individual, PBS
from tests.kcenter.constant.consts import FLOAT_ERROR
from tests.kcenter.solver.pbs.test_pbs import K, STRICT_CONSTRAINTS
from tests.kcenter.util.create_test_graph import basic_graph


def test_random_mutation():
    random.seed(4)
    graph = basic_graph()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)

    individual = Individual({0, 4})
    individual.init_nearest_centers(graph)

    individual = instance.mutation_random(individual)

    assert individual.cost == pytest.approx(0.728, FLOAT_ERROR)
    assert individual.centers == {1, 4}


def test_mutation_directed(seed_random):
    graph = basic_graph()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)

    individual = Individual({0, 4})
    individual.init_nearest_centers(graph)

    individual = instance.mutation_directed(individual)

    assert individual.centers == set()


def test_mutation_directed_deletes_closest_centers(seed_random):
    graph = basic_graph()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)

    individual = Individual({0, 4, 3})
    individual.init_nearest_centers(graph)

    individual = instance.mutation_directed(individual)

    assert individual.centers == {0}
    assert individual.cost == pytest.approx(5.515, FLOAT_ERROR)
