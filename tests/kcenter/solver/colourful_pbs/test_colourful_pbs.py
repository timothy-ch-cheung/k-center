import pytest

from kcenter.colourful_pbs.colourful_pbs import ColourfulPBS
from kcenter.constant.colour import Colour
from kcenter.verify.verify import verify_solution
from prototypes.Bandyapadhyay_Clustering import basic_graph_with_outlier
from tests.server.test_app_solve import FLOAT_ERROR_MARGIN


def test_pbs_colourful_basic_graph_outlier(seed_random):
    constraints = {Colour.BLUE: 2, Colour.RED: 2}
    k = 2
    graph = basic_graph_with_outlier()
    instance = ColourfulPBS(graph, k, constraints)
    clusters, outliers, radius = instance.solve()

    assert radius == pytest.approx(0.707, FLOAT_ERROR_MARGIN)
    assert clusters == {
        0: {0, 1},
        3: {3, 4}
    }
    assert outliers == {2}
    assert verify_solution(graph, constraints, k, radius, set(clusters.keys())) is True