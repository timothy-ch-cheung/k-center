import pytest

from src.kcenter.colourful_pbs.colourful_pbs import ColourfulPBS
from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import Individual
from src.kcenter.verify.verify import verify_solution
from src.server.graph_loader import GraphLoader
from tests.kcenter.util.create_test_graph import basic_graph_with_outlier
from tests.server.test_app_solve import FLOAT_ERROR_MARGIN


def test_colourful_pbs_find_pair(seed_random):
    constraints = {Colour.BLUE: 2, Colour.RED: 2}
    k = 2
    graph = basic_graph_with_outlier()
    instance = ColourfulPBS(graph, k, constraints)

    individual = Individual({1, 2})
    instance.init_individual(individual)
    assert individual.cost == pytest.approx(5.5108, FLOAT_ERROR_MARGIN)

    furthest_point = instance.get_furthest_point(individual)
    point_to_remove, point_to_add = instance.find_pair(furthest_point, individual)
    assert point_to_remove == 2
    assert point_to_add == 3

    instance.remove_center(point_to_remove, individual)
    instance.add_center(point_to_add, individual)
    instance.find_cost(individual)

    assert individual.cost == pytest.approx(0.7071, FLOAT_ERROR_MARGIN)


def test_colourful_pbs_find_pair_medium(seed_random):
    constraints = {Colour.BLUE: 10, Colour.RED: 10}
    k = 4
    graph = GraphLoader.get_graph("medium")
    instance = ColourfulPBS(graph, k, constraints)

    individual = Individual({0, 1, 5, 3})
    instance.init_individual(individual)
    assert individual.cost == pytest.approx(11.0000, FLOAT_ERROR_MARGIN)

    furthest_point = instance.get_furthest_point(individual)
    assert furthest_point == 4

    point_to_remove, point_to_add = instance.find_pair(4, individual)
    instance.remove_center(point_to_remove, individual)
    instance.add_center(point_to_add, individual)
    instance.find_cost(individual)

    assert individual.cost == pytest.approx(5.5, FLOAT_ERROR_MARGIN)


def test_colourful_pbs_find_pair_large(seed_random):
    constraints = {Colour.BLUE: 50, Colour.RED: 50}
    k = 5
    graph = GraphLoader.get_graph("large")
    instance = ColourfulPBS(graph, k, constraints)

    individual = Individual({1, 2, 3, 107, 5})
    instance.init_individual(individual)
    assert individual.cost == pytest.approx(26.5988, FLOAT_ERROR_MARGIN)

    furthest_point = instance.get_furthest_point(individual)
    assert furthest_point == 45

    point_to_remove, point_to_add = instance.find_pair(45, individual)
    instance.remove_center(point_to_remove, individual)
    instance.add_center(point_to_add, individual)
    instance.find_cost(individual)

    assert individual.cost == pytest.approx(24.3196, FLOAT_ERROR_MARGIN)


def test_colourful_pbs_find_pair_large_almost_solved(seed_random):
    constraints = {Colour.BLUE: 50, Colour.RED: 50}
    k = 5
    graph = GraphLoader.get_graph("large")
    instance = ColourfulPBS(graph, k, constraints)

    individual = Individual({0, 1, 2, 3, 90})
    instance.init_individual(individual)
    assert individual.cost == pytest.approx(18.2266, FLOAT_ERROR_MARGIN)

    furthest_point = instance.get_furthest_point(individual)
    assert furthest_point == 107

    point_to_remove, point_to_add = instance.find_pair(107, individual)
    instance.remove_center(point_to_remove, individual)
    instance.add_center(point_to_add, individual)
    instance.find_cost(individual)
    # TODO: this should return a swap for 90 with 4
    assert individual.cost == pytest.approx(16.62087, FLOAT_ERROR_MARGIN)


def test_pbs_colourful_basic_graph_outlier(seed_random):
    constraints = {Colour.BLUE: 2, Colour.RED: 2}
    k = 2
    graph = basic_graph_with_outlier()
    instance = ColourfulPBS(graph, k, constraints)
    clusters, outliers, radius = instance.solve()

    assert radius == pytest.approx(0.707, FLOAT_ERROR_MARGIN)
    assert clusters == {0: {0, 1}, 3: {3, 4}}
    assert outliers == {2}
    assert verify_solution(graph, constraints, k, radius, set(clusters.keys())) is True


def test_local_search_large_instance(seed_random):
    graph = GraphLoader.get_graph(f"TRAIN_COLOURFUL/train_col_n300_k40")
    k = graph.graph["k"]
    min_blue = graph.graph["min_blue"]
    min_red = graph.graph["min_red"]
    constraints = {Colour.BLUE: min_blue, Colour.RED: min_red}

    instance = ColourfulPBS(graph, k, constraints)

    centers = {4, 136, 142, 271, 274, 25, 26, 292, 40, 168, 42, 44, 176, 49, 178, 52, 54, 57, 58, 187, 188, 62, 66, 195,
               198, 77, 208, 83, 84, 90, 247, 93, 223, 227, 230, 105, 106, 109, 119, 120}
    candidate = Individual(centers=centers)
    candidate.init_nearest_centers(instance.points, instance.weights)
    candidate.cost = instance.find_cost(candidate)

    assert candidate.cost == pytest.approx(1003.9398, FLOAT_ERROR_MARGIN)

    candidate = instance.local_search(candidate, generation=2)
    assert candidate.cost == pytest.approx(1003.9398, FLOAT_ERROR_MARGIN)
    assert candidate.centers == {4, 25, 26, 40, 42, 44, 49, 52, 57, 58, 62, 66, 77, 83, 84, 90, 93, 105, 109, 119, 120,
                                 136, 142, 154, 168, 176, 178, 187, 195, 198, 201, 208, 223, 227, 230, 247, 271, 274,
                                 289, 292}
