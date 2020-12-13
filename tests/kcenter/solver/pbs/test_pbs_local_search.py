import pytest

from src.kcenter.pbs.pbs import PBS, Individual
from tests.kcenter.constant.consts import FLOAT_ERROR
from tests.kcenter.solver.pbs.test_pbs import K, STRICT_CONSTRAINTS
from tests.kcenter.util.create_test_graph import basic_graph


def test_find_next_second_nearest_to_none():
    graph = basic_graph()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)

    individual = Individual({0})
    individual.init_nearest_centers(graph)

    assert instance.find_next(point=0, individual=individual) == None


def test_add_center():
    graph = basic_graph()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)

    individual = Individual({0, 4})
    individual.init_nearest_centers(graph)
    assert individual.cost == pytest.approx(0.854, FLOAT_ERROR)
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
    individual.init_nearest_centers(graph)
    assert individual.cost == pytest.approx(0, FLOAT_ERROR)
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
    individual.init_nearest_centers(graph)
    assert individual.cost == pytest.approx(0.854, FLOAT_ERROR)
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
    individual.init_nearest_centers(graph)
    assert individual.cost == pytest.approx(5.515, FLOAT_ERROR)

    old_center, new_center = instance.find_pair(4, individual)
    assert new_center == 4
    assert old_center == 0


def test_local_search(seed_random):
    graph = basic_graph()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)

    individual = Individual({0, 1})
    individual.init_nearest_centers(graph)

    instance.local_search(individual, 0)
    assert individual.centers == {1, 4}
