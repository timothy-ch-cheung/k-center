import pytest

from src.kcenter.colourful_pbs.colourful_pbs import ColourfulPBS
from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import Individual, NearestCenters, Neighbour
from tests.kcenter.solver.pbs.test_pbs import FLOAT_ERROR_MARGIN
from tests.kcenter.util.create_test_graph import basic_graph_with_outlier


def test_pbs_colourful_basic_graph_outlier(seed_random):
    constraints = {Colour.BLUE: 2, Colour.RED: 2}
    k = 2
    graph = basic_graph_with_outlier()
    instance = ColourfulPBS(graph, k, constraints)

    nearest_centers = {
        0: NearestCenters(Neighbour(0, 0.0), Neighbour(3, 5.284)),
        1: NearestCenters(Neighbour(0, 0.5099), Neighbour(3, 5.6303)),
        2: NearestCenters(Neighbour(0, 3.7855), Neighbour(3, 5.5109)),
        3: NearestCenters(Neighbour(3, 0.0), Neighbour(0, 5.2839)),
        4: NearestCenters(Neighbour(3, 0.7071), Neighbour(0, 5.5154))
    }
    optimised_individual = Individual({0, 3}, 0.7071, nearest_centers)
    optimised_individual = instance.find_colourful_cost(optimised_individual)
    assert optimised_individual.cost == pytest.approx(0.707, FLOAT_ERROR_MARGIN)
