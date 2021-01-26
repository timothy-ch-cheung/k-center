import pytest

from src.kcenter.pbs.pbs import Individual
from src.kcenter.colourful_pbs.colourful_pbs import ColourfulPBS
from src.kcenter.constant.colour import Colour
from src.kcenter.verify.verify import verify_solution
from tests.kcenter.util.create_test_graph import basic_graph_with_outlier
from tests.server.test_app_solve import FLOAT_ERROR_MARGIN


def test_colourful_pbs_find_pair(seed_random):
    constraints = {Colour.BLUE: 2, Colour.RED: 2}
    k = 2
    graph = basic_graph_with_outlier()
    instance = ColourfulPBS(graph, k, constraints)
    individual = Individual({0, 2}, 5.5154)
    individual.init_nearest_centers(instance.points, instance.weights)
    furthest_point = instance.get_furthest_point(individual)
    point_to_remove, point_to_add = instance.find_pair(furthest_point, individual)
    assert point_to_remove == 2
    assert point_to_add == 4


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
