import pytest

from src.kcenter.pbs.pbs import Individual, PBS
from tests.kcenter.constant.consts import FLOAT_ERROR
from tests.kcenter.solver.pbs.test_pbs import K, STRICT_CONSTRAINTS

from tests.kcenter.util.create_test_graph import basic_graph


def test_crossover_random(seed_random):
    graph = basic_graph()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)

    first_parent = Individual({0, 4})
    first_parent.init_nearest_centers(instance.points, instance.weights)

    second_parent = Individual({1, 3})
    second_parent.init_nearest_centers(instance.points, instance.weights)

    child = instance.crossover_random(first_parent, second_parent)

    assert child.centers == {1, 4}
    assert child.cost == pytest.approx(0.728, FLOAT_ERROR)


def test_crossover_directed(seed_random):
    graph = basic_graph()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)

    first_parent = Individual({0, 4})
    first_parent.init_nearest_centers(instance.points, instance.weights)

    second_parent = Individual({1, 3})
    second_parent.init_nearest_centers(instance.points, instance.weights)

    first_child, second_child = instance.crossover_directed(first_parent, second_parent, 3)

    assert first_child.centers == {1}
    assert second_child.centers == {0, 4}
    assert second_child.cost == pytest.approx(0.854, FLOAT_ERROR)