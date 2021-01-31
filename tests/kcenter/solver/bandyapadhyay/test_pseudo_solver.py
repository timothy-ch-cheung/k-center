import pytest

from src.kcenter.bandyapadhyay.pseudo_solver import ConstantPseudoColourful
from src.kcenter.constant.colour import Colour
from src.kcenter.verify.verify import verify_solution
from tests.kcenter.solver.greedy.test_greedy import FLOAT_ERROR_MARGIN
from tests.kcenter.util.create_test_graph import basic_graph, basic_graph_with_outlier


def test_greedy_basic_graph_clustering():
    graph = basic_graph()
    instance = ConstantPseudoColourful(graph, 2, {Colour.BLUE: 3, Colour.RED: 2})

    clusters, outliers, radius = instance.solve()

    assert radius == pytest.approx(1.456, FLOAT_ERROR_MARGIN)
    assert clusters == {
        0: {0, 1, 2},
        3: {3, 4}
    }
    assert outliers == set()
    assert verify_solution(graph, {Colour.BLUE: 3, Colour.RED: 2}, k=2, radius=radius,
                           centers=set(clusters.keys())) is True


def test_greedy_basic_graph_with_outlier_clustering():
    graph = basic_graph_with_outlier()
    instance = ConstantPseudoColourful(graph, 2, {Colour.BLUE: 2, Colour.RED: 2})

    clusters, outliers, radius = instance.solve()
    assert radius == pytest.approx(1.414, FLOAT_ERROR_MARGIN)
    assert clusters == {
        0: {0, 1},
        3: {3, 4}
    }
    assert outliers == {2}
    assert verify_solution(graph, {Colour.BLUE: 2, Colour.RED: 2}, k=2, radius=radius,
                           centers=set(clusters.keys())) is True
