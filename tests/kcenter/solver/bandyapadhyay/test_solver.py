import pytest

from src.kcenter.bandyapadhyay.solver import ConstantColourfulKCenter
from src.kcenter.constant.colour import Colour
from src.server.graph_loader import GraphLoader
from tests.kcenter.solver.greedy.test_greedy import FLOAT_ERROR_MARGIN


@pytest.mark.skip(reason="LP currently uses POSITIVE_INTEGERS which does not include 0")
def test_constant_colourful_extreme_point():
    k = 1
    constraint = {Colour.BLUE: 5, Colour.RED: 5}
    graph = GraphLoader.get_graph("extreme_point")
    solver = ConstantColourfulKCenter(graph, k, constraint)

    clusters, outliers, radius = solver.solve()
    assert radius == pytest.approx(1.456, FLOAT_ERROR_MARGIN)