import pytest

from kcenter.verify.verify import verify_solution, Colour
from src.kcenter.solver.greedy import GreedySolver
from tests.kcenter.util.create_test_graph import basic_graph


CONSTRAINTS = {Colour.BLUE: 3, Colour.RED: 2}
K = 2

def test_max_dist_single_cluster():
    graph = basic_graph()
    max_node, max_dist, owning_center = GreedySolver.max_dist(graph, clusters={0: {0, 1, 2, 3, 4}})
    assert max_node == 4
    assert max_dist == pytest.approx(5.515, 0.001)
    assert owning_center == 0


def test_max_dist_double_cluster():
    graph = basic_graph()
    max_node, max_dist, owning_center = GreedySolver.max_dist(graph, clusters={0: {0, 1, 2}, 4: {3, 4}})
    assert max_node == 2
    assert max_dist == pytest.approx(0.854, 0.001)
    assert owning_center == 0


def test_greedy_basic_graph():
    graph = basic_graph()
    instance = GreedySolver(graph, K, CONSTRAINTS)
    clusters, radius = instance.solve()

    assert radius == pytest.approx(0.854, 0.001)
    assert list(clusters.keys()) == [0, 4]
    assert list(clusters.values()) == [{0, 1, 2}, {3, 4}]


def test_greedy_basic_graph_colourful_clustering():
    graph = basic_graph()
    instance = GreedySolver(graph, K, CONSTRAINTS)
    clusters, radius = instance.solve()

    assert verify_solution(graph, CONSTRAINTS, K, radius, set(clusters.keys())) is True
