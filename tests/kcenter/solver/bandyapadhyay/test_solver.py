import pytest

from src.kcenter.bandyapadhyay.solver import ConstantColourfulKCenterSolver
from src.kcenter.constant.colour import Colour
from src.kcenter.verify.verify import verify_solution
from tests.kcenter.solver.greedy.test_greedy import FLOAT_ERROR_MARGIN
from tests.kcenter.util.create_test_graph import basic_graph, basic_graph_with_outlier


def test_greedy_basic_graph_clustering():
    graph = basic_graph()
    instance = ConstantColourfulKCenterSolver(graph, 2, {Colour.BLUE: 3, Colour.RED: 2})

    clusters, radius = instance.solve()

    assert radius == pytest.approx(1.456, FLOAT_ERROR_MARGIN)
    assert clusters == {
        -1: set(),
        2: {0, 1, 2},
        4: {3, 4}
    }
    centers = set(clusters.keys())
    centers.remove(-1)
    assert verify_solution(graph, {Colour.BLUE: 3, Colour.RED: 2}, k=2, radius=radius, centers=centers) is True


def test_greedy_basic_graph_with_outlier_clustering():
    graph = basic_graph_with_outlier()
    instance = ConstantColourfulKCenterSolver(graph, 2, {Colour.BLUE: 2, Colour.RED: 2})

    clusters, radius = instance.solve()
    assert radius == pytest.approx(1.414, FLOAT_ERROR_MARGIN)
    assert clusters == {
        -1: {2},
        1: {0, 1},
        4: {3, 4}}
    centers = set(clusters.keys())
    centers.remove(-1)
    assert verify_solution(graph, {Colour.BLUE: 2, Colour.RED: 2}, k=2, radius=radius, centers=centers) is True
