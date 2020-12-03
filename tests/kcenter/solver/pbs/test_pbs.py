from kcenter.constant.colour import Colour
from kcenter.pbs.pbs import PBS
from tests.kcenter.util.create_test_graph import basic_graph

FLOAT_ERROR_MARGIN = 0.001
STRICT_CONSTRAINTS = {Colour.BLUE: 3, Colour.RED: 2}
K = 2

def test_pbs():
    graph = basic_graph()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)
    clusters, outliers, radius = instance.solve()

    assert len(clusters.keys()) == 2