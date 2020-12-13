import pytest

from src.kcenter.pbs.pbs import Individual, Neighbour
from tests.kcenter.constant.consts import FLOAT_ERROR
from tests.kcenter.util.create_test_graph import basic_graph


def test_neighbour_equality():
    first_neighbour = Neighbour(1, 2.1)
    second_neighbour = Neighbour(1, 2.1)
    assert first_neighbour == second_neighbour


def test_neighbour_inequality():
    first_neighbour = Neighbour(2, 2.1)
    second_neighbour = Neighbour(1, 2.1)
    assert first_neighbour != second_neighbour


def test_neighbour_str():
    neighbour = Neighbour(2, 2.1)
    assert str(neighbour) == "{point: 2, cost: 2.1}"


def test_individual_str():
    individual = Individual(centers={0}, cost=2.1,
                            nearest_centers={0: {"nearest_center": Neighbour(0, 0), "second_nearest_center": None},
                                             1: {"nearest_center": Neighbour(0, 1.5), "second_nearest_center": None}})
    assert str(
        individual) == "{centers: [0], cost: 2.1, nearest_centers: {0: {'nearest_center': {point: 0, cost: 0}, 'second_nearest_center': None}, 1: {'nearest_center': {point: 0, cost: 1.5}, 'second_nearest_center': None}}}"


def test_individual_init_centers():
    graph = basic_graph()
    individual = Individual(centers={0, 4})
    individual.init_nearest_centers(graph)
    assert individual.centers == {0, 4}
    assert individual.cost == pytest.approx(0.854, FLOAT_ERROR)
    expected_nearest_centers = [
        "{'nearest_center': {point: 0, cost: 0}, 'second_nearest_center': {point: 4, cost: 5.515}}",
        "{'nearest_center': {point: 0, cost: 0.51}, 'second_nearest_center': {point: 4, cost: 5.814}}",
        "{'nearest_center': {point: 0, cost: 0.854}, 'second_nearest_center': {point: 4, cost: 6.369}}",
        "{'nearest_center': {point: 4, cost: 0.707}, 'second_nearest_center': {point: 0, cost: 5.284}}",
        "{'nearest_center': {point: 4, cost: 0}, 'second_nearest_center': {point: 0, cost: 5.515}}"
    ]
    for point,expected in enumerate(expected_nearest_centers):
        assert str(individual.nearest_centers[point]) == expected
