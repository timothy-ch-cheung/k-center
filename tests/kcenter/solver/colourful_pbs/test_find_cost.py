import pytest

from src.kcenter.colourful_pbs.colourful_pbs import ColourfulPBS
from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import Individual, NearestCenters, Neighbour
from src.server.graph_loader import GraphLoader
from tests.kcenter.solver.pbs.test_pbs import FLOAT_ERROR_MARGIN
from tests.kcenter.util.create_test_graph import basic_graph_with_outlier


def test_find_cost_basic_graph_outlier(seed_random):
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


def test_find_cost_large_graph_bad_centers(seed_random):
    constraints = {Colour.BLUE: 2, Colour.RED: 2}
    k = 2
    graph = GraphLoader.get_graph("basic_with_outlier")
    instance = ColourfulPBS(graph, k, constraints)

    nearest_centers = {
        0: NearestCenters(Neighbour(3, 5.2839), Neighbour(4, 5.5154)),
        1: NearestCenters(Neighbour(3, 5.6303), Neighbour(4, 5.8138)),
        2: NearestCenters(Neighbour(3, 5.5109), Neighbour(4, 6.1131)),
        3: NearestCenters(Neighbour(3, 0.0), Neighbour(4, 0.7071)),
        4: NearestCenters(Neighbour(4, 0.0), Neighbour(3, 0.7071))
    }
    optimised_individual = Individual({3, 4}, 5.6303, nearest_centers)

    optimised_individual = instance.find_colourful_cost(optimised_individual)
    assert optimised_individual.cost == pytest.approx(5.511, FLOAT_ERROR_MARGIN)


def test_find_cost_large_graph(seed_random):
    constraints = {Colour.BLUE: 50, Colour.RED: 50}
    k = 2
    graph = GraphLoader.get_graph("large")
    instance = ColourfulPBS(graph, k, constraints)

    optimised_individual = Individual({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 46.0624)
    optimised_individual.init_nearest_centers(instance.points, instance.weights)

    optimised_individual = instance.find_colourful_cost(optimised_individual)
    assert optimised_individual.cost == pytest.approx(12.5, FLOAT_ERROR_MARGIN)
