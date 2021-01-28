import pytest

from src.kcenter.constant.colour import Colour
from src.server.graph_loader import GraphLoader
from src.kcenter.pbs.pbs import PBS, Individual
from tests.kcenter.constant.consts import FLOAT_ERROR
from tests.kcenter.solver.pbs.test_pbs import K, STRICT_CONSTRAINTS
from tests.kcenter.util.create_test_graph import basic_graph


def test_find_next_second_nearest_to_none():
    graph = basic_graph()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)

    individual = Individual({0})
    instance.init_individual(individual)
    assert individual.cost == pytest.approx(5.5154, FLOAT_ERROR)

    assert instance.find_next(point=0, individual=individual) == None


def test_add_center():
    graph = basic_graph()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)

    individual = Individual({0, 4})
    instance.init_individual(individual)
    assert individual.cost == pytest.approx(0.8544, FLOAT_ERROR)
    expected_nearest_centers = [
        "{'nearest_center': {point: 0, cost: 0}, 'second_nearest_center': {point: 4, cost: 5.515}}",
        "{'nearest_center': {point: 0, cost: 0.51}, 'second_nearest_center': {point: 4, cost: 5.814}}",
        "{'nearest_center': {point: 0, cost: 0.854}, 'second_nearest_center': {point: 4, cost: 6.369}}",
        "{'nearest_center': {point: 4, cost: 0.707}, 'second_nearest_center': {point: 0, cost: 5.284}}",
        "{'nearest_center': {point: 4, cost: 0}, 'second_nearest_center': {point: 0, cost: 5.515}}"
    ]
    for point, expected in enumerate(expected_nearest_centers):
        assert str(individual.nearest_centers[point]) == expected

    instance.add_center(center=3, individual=individual)
    expected_nearest_centers = [
        "{'nearest_center': {point: 0, cost: 0}, 'second_nearest_center': {point: 3, cost: 5.284}}",
        "{'nearest_center': {point: 0, cost: 0.51}, 'second_nearest_center': {point: 3, cost: 5.63}}",
        "{'nearest_center': {point: 0, cost: 0.854}, 'second_nearest_center': {point: 3, cost: 6.129}}",
        "{'nearest_center': {point: 3, cost: 0}, 'second_nearest_center': {point: 4, cost: 0.707}}",
        "{'nearest_center': {point: 4, cost: 0}, 'second_nearest_center': {point: 3, cost: 0.707}}"
    ]
    for point, expected in enumerate(expected_nearest_centers):
        assert str(individual.nearest_centers[point]) == expected


def test_add_center_empty_centers():
    graph = basic_graph()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)

    individual = Individual(set())
    instance.init_individual(individual)
    assert individual.cost == pytest.approx(0.0000, FLOAT_ERROR)
    expected_nearest_centers = [
        "{'nearest_center': None, 'second_nearest_center': None}",
        "{'nearest_center': None, 'second_nearest_center': None}",
        "{'nearest_center': None, 'second_nearest_center': None}",
        "{'nearest_center': None, 'second_nearest_center': None}",
        "{'nearest_center': None, 'second_nearest_center': None}"
    ]
    for point, expected in enumerate(expected_nearest_centers):
        assert str(individual.nearest_centers[point]) == expected

    instance.add_center(center=0, individual=individual)
    expected_nearest_centers = [
        "{'nearest_center': {point: 0, cost: 0}, 'second_nearest_center': None}",
        "{'nearest_center': {point: 0, cost: 0.51}, 'second_nearest_center': None}",
        "{'nearest_center': {point: 0, cost: 0.854}, 'second_nearest_center': None}",
        "{'nearest_center': {point: 0, cost: 5.284}, 'second_nearest_center': None}",
        "{'nearest_center': {point: 0, cost: 5.515}, 'second_nearest_center': None}"
    ]
    for point, expected in enumerate(expected_nearest_centers):
        assert str(individual.nearest_centers[point]) == expected


def test_remove_center():
    graph = basic_graph()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)

    individual = Individual({0, 4})
    instance.init_individual(individual)
    assert individual.cost == pytest.approx(0.8544, FLOAT_ERROR)
    expected_nearest_centers = [
        "{'nearest_center': {point: 0, cost: 0}, 'second_nearest_center': {point: 4, cost: 5.515}}",
        "{'nearest_center': {point: 0, cost: 0.51}, 'second_nearest_center': {point: 4, cost: 5.814}}",
        "{'nearest_center': {point: 0, cost: 0.854}, 'second_nearest_center': {point: 4, cost: 6.369}}",
        "{'nearest_center': {point: 4, cost: 0.707}, 'second_nearest_center': {point: 0, cost: 5.284}}",
        "{'nearest_center': {point: 4, cost: 0}, 'second_nearest_center': {point: 0, cost: 5.515}}"
    ]

    for point, expected in enumerate(expected_nearest_centers):
        assert str(individual.nearest_centers[point]) == expected
    expected_nearest_centers = [
        "{'nearest_center': {point: 0, cost: 0}, 'second_nearest_center': None}",
        "{'nearest_center': {point: 0, cost: 0.51}, 'second_nearest_center': None}",
        "{'nearest_center': {point: 0, cost: 0.854}, 'second_nearest_center': None}",
        "{'nearest_center': {point: 0, cost: 5.284}, 'second_nearest_center': None}",
        "{'nearest_center': {point: 0, cost: 5.515}, 'second_nearest_center': None}"
    ]
    instance.remove_center(center=4, individual=individual)
    for point, expected in enumerate(expected_nearest_centers):
        assert str(individual.nearest_centers[point]) == expected


def test_find_pair(seed_random):
    graph = basic_graph()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)

    individual = Individual({0, 1})
    instance.init_individual(individual)
    assert individual.cost == pytest.approx(5.5154, FLOAT_ERROR)

    old_center, new_center = instance.find_pair(4, individual)
    assert new_center == 4
    assert old_center == 0
    instance.remove_center(old_center, individual)
    instance.add_center(new_center, individual)
    assert individual.cost == pytest.approx(0.7280, FLOAT_ERROR)


def test_find_pair_large_graph(seed_random):
    constraints = {Colour.BLUE: 50, Colour.RED: 50}
    k = 5
    graph = GraphLoader.get_graph("large")
    instance = PBS(graph, k, constraints)

    individual = Individual({32, 77, 89, 92, 106})
    instance.init_individual(individual)
    assert individual.cost == pytest.approx(130.6105, FLOAT_ERROR)

    old_center, new_center = instance.find_pair(4, individual)
    assert new_center == 38
    assert old_center == 106
    instance.remove_center(old_center, individual)
    instance.add_center(new_center, individual)
    assert individual.cost == pytest.approx(117.7075, FLOAT_ERROR)


def test_local_search(seed_random):
    graph = basic_graph()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)

    individual = Individual({0, 1})
    instance.init_individual(individual)
    assert individual.cost == pytest.approx(5.5154, FLOAT_ERROR)

    individual = instance.local_search(individual, 3)
    assert individual.centers == {2, 4}
    assert individual.cost == pytest.approx(0.8544, FLOAT_ERROR)
