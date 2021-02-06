import pytest

from src.kcenter.pbs.pbs import Individual, Neighbour, NearestCenters
from tests.kcenter.constant.consts import FLOAT_ERROR


def test_inividual_equality():
    first_individual = Individual({0, 1, 2, 3})
    second_individual = Individual({0, 1, 2, 3})
    assert first_individual == second_individual


def test_inividual_inquality():
    first_individual = Individual({0, 1, 2, 3})
    second_individual = Individual({0, 1, 4, 5})
    assert first_individual != second_individual


def test_inividual_inquality_different_type():
    first_individual = Individual({0, 1, 2, 3})
    assert first_individual != float(100)


def test_neighbour_equality():
    first_neighbour = Neighbour(1, 2.1)
    second_neighbour = Neighbour(1, 2.1)
    assert first_neighbour == second_neighbour


def test_neighbour_inequality():
    first_neighbour = Neighbour(2, 2.1)
    second_neighbour = Neighbour(1, 2.1)
    assert first_neighbour != second_neighbour


def test_neighbour_inequality_different_type():
    first_neighbour = Neighbour(2, 2.1)
    assert first_neighbour != float(100)


def test_neighbour_str():
    neighbour = Neighbour(2, 2.1)
    assert str(neighbour) == "Neighbour(point=2, cost=2.1)"


def test_individual_str():
    individual = Individual(centers={0}, cost=2.1,
                            nearest_centers={0: {"nearest_center": Neighbour(0, 0), "second_nearest_center": None},
                                             1: {"nearest_center": Neighbour(0, 1.5), "second_nearest_center": None}})
    assert str(
        individual) == "{centers: [0], cost: 2.1, nearest_centers: {0: {'nearest_center': Neighbour(point=0, cost=0), 'second_nearest_center': None}, 1: {'nearest_center': Neighbour(point=0, cost=1.5), 'second_nearest_center': None}}}"


def test_nearest_centers_equality():
    first_neighbour = Neighbour(2, 2.1)
    second_neighbour = Neighbour(1, 1.1)
    nearest = NearestCenters(first_neighbour, second_neighbour)
    assert nearest == NearestCenters(Neighbour(2, 2.1), Neighbour(1, 1.1))


def test_nearest_centers_inequality():
    first_neighbour = Neighbour(2, 2.1)
    second_neighbour = Neighbour(1, 1.1)
    nearest = NearestCenters(first_neighbour, second_neighbour)
    assert nearest != NearestCenters(Neighbour(5, 3), Neighbour(2, 9))


def test_nearest_centers_inequality_different_type():
    first_neighbour = Neighbour(2, 2.1)
    second_neighbour = Neighbour(1, 1.1)
    nearest = NearestCenters(first_neighbour, second_neighbour)
    assert nearest != float(100)


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
    expected_nearest_centers = [
        NearestCenters(Neighbour(0, 0), Neighbour(4, 5.5154)),
        NearestCenters(Neighbour(0, 0.5099), Neighbour(4, 5.8138)),
        NearestCenters(Neighbour(0, 0.8544), Neighbour(4, 6.3694)),
        NearestCenters(Neighbour(4, 0.7071), Neighbour(0, 5.2839)),
        NearestCenters(Neighbour(4, 0), Neighbour(0, 5.5154))
    ]
    for point, expected in enumerate(expected_nearest_centers):
        assert individual.nearest_centers[point] == expected
