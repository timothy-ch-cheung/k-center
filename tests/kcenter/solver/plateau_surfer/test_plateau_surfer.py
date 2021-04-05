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

    assert radius == pytest.approx(96, FLOAT_ERROR_MARGIN)
    assert clusters == {
        13: {74, 12, 13, 14, 15, 16, 17, 44, 82, 57, 58, 30},
        21: {33, 2, 41, 45, 46, 47, 83, 84, 21, 23},
        24: {89, 34, 35, 4, 36, 37, 73, 92, 85, 24, 25, 59, 28, 29},
        26: {32, 42, 81, 22, 26, 27, 93, 94, 31},
        39: {66, 67, 68, 38, 39, 40, 18, 53},
        51: {1, 50, 51},
        77: {3, 5, 6, 7, 8, 9, 10, 11, 61, 62, 63, 64, 69, 70, 71, 75, 76, 77, 78, 79, 80},
        86: {86, 87},
        95: {96, 65, 72, 43, 48, 49, 19, 20, 54, 55, 56, 60, 95},
        99: {97, 98, 99, 100, 52, 88, 90, 91}
    }
    assert outliers == set()
