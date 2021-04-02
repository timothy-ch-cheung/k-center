from kcenter.constant.colour import Colour
from kcenter.pbs.pbs import Neighbour
from kcenter.plateau_surfer.plateau_surfer import PlateauSurfer
from server.tsplib_graph_loader import TSPLIBGraphLoader
from tests.kcenter.util.create_test_graph import basic_graph


def test_nearest_centers():
    K = 2
    constraints = {Colour.BLUE: 3, Colour.RED: 2}
    graph = basic_graph()
    instance = PlateauSurfer(graph, K, constraints)

    expected_nearest_centers = [
        Neighbour(point=1, cost=0.5099),
        Neighbour(point=1, cost=0),
        Neighbour(point=2, cost=0),
        Neighbour(point=1, cost=5.6303),
        Neighbour(point=1, cost=5.8138)
    ]

    nearest_centers = instance.calc_nearest_centers({1, 2})

    for point, expected in enumerate(expected_nearest_centers):
        assert str(nearest_centers[point]) == str(expected)


def test_add_center():
    K = 2
    constraints = {Colour.BLUE: 3, Colour.RED: 2}
    graph = basic_graph()
    instance = PlateauSurfer(graph, K, constraints)

    expected_nearest_centers = [
        Neighbour(point=1, cost=0.5099),
        Neighbour(point=1, cost=0),
        Neighbour(point=2, cost=0),
        Neighbour(point=3, cost=0),
        Neighbour(point=3, cost=0.7071)
    ]

    P = {1, 2}
    nearest_centers = instance.calc_nearest_centers(P)
    P = instance.add_center(nearest_centers, P, 3)

    assert P == {1, 2, 3}
    for point, expected in enumerate(expected_nearest_centers):
        assert str(nearest_centers[point]) == str(expected)


def test_remove_center():
    K = 2
    constraints = {Colour.BLUE: 3, Colour.RED: 2}
    graph = basic_graph()
    instance = PlateauSurfer(graph, K, constraints)

    expected_nearest_centers = [
        Neighbour(point=1, cost=0.5099),
        Neighbour(point=1, cost=0),
        Neighbour(point=1, cost=0.728),
        Neighbour(point=1, cost=5.6303),
        Neighbour(point=1, cost=5.8138)
    ]

    P = {1, 2}
    nearest_centers = instance.calc_nearest_centers(P)
    P = instance.remove_center(nearest_centers, P, 2)

    assert P == {1}
    for point, expected in enumerate(expected_nearest_centers):
        assert str(nearest_centers[point]) == str(expected)


def test_local_search(seed_random):
    K = 2
    constraints = {Colour.BLUE: 3, Colour.RED: 2}
    graph = basic_graph()
    instance = PlateauSurfer(graph, K, constraints)

    P = {3, 4}
    P = instance.plateau_surf_local_search(P)
    assert P == {1, 4}


def test_solver(seed_random):
    K = 40
    graph = TSPLIBGraphLoader.get_graph("pr226")
    instance = PlateauSurfer(graph, K)

    cluster, outliers, cost = instance.solve(iterations=5)
    assert cost == 650

