from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import Neighbour
from src.kcenter.plateau_surfer.plateau_surfer import PlateauSurfer
from src.server.tsplib_graph_loader import TSPLIBGraphLoader
from tests.kcenter.util.assertion import FLOAT_ERROR_MARGIN
from tests.kcenter.util.create_test_graph import basic_graph
from numpy.testing import assert_almost_equal


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
