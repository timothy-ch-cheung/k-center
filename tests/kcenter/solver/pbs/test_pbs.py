from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import PBS
from tests.kcenter.util.create_test_graph import basic_graph
import pytest

FLOAT_ERROR_MARGIN = 0.001
STRICT_CONSTRAINTS = {Colour.BLUE: 3, Colour.RED: 2}
K = 2


def test_linear_search():
    pass


def test_get_nwk():
    graph = basic_graph()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)

    nwk = instance.get_nwk(graph, 0, 3)
    assert nwk == [0, 1, 2]


def test_pbs():
    graph = basic_graph()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)
    clusters, outliers, radius = instance.solve()

    assert len(clusters.keys()) == 2
