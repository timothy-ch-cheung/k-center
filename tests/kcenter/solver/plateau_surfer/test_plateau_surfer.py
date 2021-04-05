import random

import pytest
from numpy.testing import assert_almost_equal

from src.kcenter.constant.colour import Colour
from src.kcenter.plateau_surfer.plateau_surfer import PlateauSurfer
from src.kcenter.verify.verify import verify_solution
from src.server.orlib_graph_loader import ORLIBGraphLoader
from tests.kcenter.constant.consts import FLOAT_ERROR
from tests.kcenter.util.assertion import FLOAT_ERROR_MARGIN
from tests.kcenter.util.create_test_graph import basic_graph


def test_nearest_centers():
    K = 2
    constraints = {Colour.BLUE: 3, Colour.RED: 2}
    graph = basic_graph()
    instance = PlateauSurfer(graph, K, constraints)

    nearest_centers, nearest_costs = instance.calc_nearest_centers({1, 2})

    assert nearest_centers == [1, 1, 2, 1, 1, 0]
    assert_almost_equal(nearest_costs, [0.5099, 0, 0, 5.6302, 5.8137, 0], FLOAT_ERROR_MARGIN)


def test_add_center():
    K = 2
    constraints = {Colour.BLUE: 3, Colour.RED: 2}
    graph = basic_graph()
    instance = PlateauSurfer(graph, K, constraints)

    P = {1, 2}
    nearest_centers, nearest_costs = instance.calc_nearest_centers(P)

    P = instance.add_center(nearest_centers, nearest_costs, P, 3)

    assert nearest_centers == [1, 1, 2, 3, 3, 0]
    assert_almost_equal(nearest_costs, [0.5099, 0, 0, 0, 0.7071, 0], FLOAT_ERROR_MARGIN)
    assert P == {1, 2, 3}


def test_remove_center():
    K = 2
    constraints = {Colour.BLUE: 3, Colour.RED: 2}
    graph = basic_graph()
    instance = PlateauSurfer(graph, K, constraints)

    P = {1, 2}
    nearest_centers, nearest_costs = instance.calc_nearest_centers(P)
    P = instance.remove_center(nearest_centers, nearest_costs, P, 2)

    assert nearest_centers == [1, 1, 1, 1, 1, 0]
    assert_almost_equal(nearest_costs, [0.5099, 0, 0.7280, 5.6303, 5.8138, 0], FLOAT_ERROR_MARGIN)
    assert P == {1}


def test_local_search(seed_random):
    K = 2
    constraints = {Colour.BLUE: 3, Colour.RED: 2}
    graph = basic_graph()
    instance = PlateauSurfer(graph, K, constraints)

    P = {3, 4}
    P = instance.plateau_surf_local_search(P)
    assert P == {1, 4}


def test_plateau_surfer(seed_random):
    K = 2
    constraints = {Colour.BLUE: 3, Colour.RED: 2}
    graph = basic_graph()
    instance = PlateauSurfer(graph, K, constraints)
    clusters, outliers, radius = instance.solve()

    assert clusters == {1: {0, 1, 2}, 3: {3, 4}}
    assert outliers == set()
    assert radius == pytest.approx(0.728, FLOAT_ERROR)
    assert verify_solution(graph, constraints, K, radius, set(clusters.keys())) is True


def test_target_plateau_surfer(seed_random):
    random.seed(0)
    graph = ORLIBGraphLoader.get_graph("pmed3")
    k = graph.graph["k"]
    constraints = {Colour.BLUE: 100, Colour.RED: 0}
    target = 93
    instance = PlateauSurfer(graph, k, constraints)

    clusters, outliers, radius = instance.target_solve(target_cost=target, timeout=5)

    assert radius == pytest.approx(98, FLOAT_ERROR_MARGIN)
    assert clusters == {
        1: {1, 2, 66, 100, 51},
        12: {96, 97, 72, 43, 12, 13, 14, 15, 44, 48, 81, 82, 30},
        24: {34, 35, 4, 36, 37, 38, 73, 92, 85, 24, 28, 29},
        25: {25, 59, 60, 45},
        32: {32, 33, 41, 42, 46, 47, 52, 21, 22, 26, 27, 93, 94, 31},
        56: {74, 49, 19, 20, 55, 54, 23, 56, 57, 58, 83, 84, 95},
        62: {64, 65, 5, 6, 7, 8, 9, 10, 11, 75, 76, 77, 78, 79, 80, 61, 62, 63},
        70: {3, 67, 68, 69, 39, 40, 70, 71, 50, 53},
        87: {88, 86, 87},
        90: {98, 99, 16, 17, 18, 89, 90, 91}
    }
    assert outliers == set()
