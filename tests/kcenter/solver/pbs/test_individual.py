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
    individual = Individual(centers={0, 4})
    individual.init_nearest_centers([0, 1, 2, 3, 4], {
        (0, 0): 0, (0, 1): 0.5099, (0, 2): 0.8544, (0, 3): 5.2839, (0, 4): 5.5154,
        (1, 0): 0.5099, (1, 1): 0, (1, 2): 0.728, (1, 3): 5.6303, (1, 4): 5.8138,
        (2, 0): 0.8544, (2, 1): 0.728, (2, 2): 0, (2, 3): 6.1294, (2, 4): 6.3694,
        (3, 0): 5.2839, (3, 1): 5.6303, (3, 2): 6.1294, (3, 3): 0, (3, 4): 0.7071,
        (4, 0): 5.5154, (4, 1): 5.8138, (4, 2): 6.3694, (4, 3): 0.7071, (4, 4): 0
    })
    assert individual.centers == {0, 4}
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
