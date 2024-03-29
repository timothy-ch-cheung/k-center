import pytest

from src.kcenter.constant.colour import Colour
from src.kcenter.greedy.greedy import Greedy
from src.kcenter.verify.verify import verify_solution
from tests.kcenter.util.create_test_graph import basic_graph, basic_graph_with_outlier

FLOAT_ERROR_MARGIN = 0.001
STRICT_CONSTRAINTS = {Colour.BLUE: 3, Colour.RED: 2}
RELAXED_CONSTRAINTS = {Colour.BLUE: 2, Colour.RED: 2}
K = 2


def test_max_dist_single_cluster():
    graph = basic_graph()
    max_node, max_dist, owning_center = Greedy.max_dist(graph, clusters={0: {0, 1, 2, 3, 4}})
    assert max_node == 4
    assert max_dist == pytest.approx(5.515, FLOAT_ERROR_MARGIN)
    assert owning_center == 0


def test_max_dist_double_cluster():
    graph = basic_graph()
    max_node, max_dist, owning_center = Greedy.max_dist(graph, clusters={0: {0, 1, 2}, 4: {3, 4}})
    assert max_node == 2
    assert max_dist == pytest.approx(0.854, FLOAT_ERROR_MARGIN)
    assert owning_center == 0


def test_move_nodes_to_new_cluster():
    graph = basic_graph()
    clusters = {0: {0, 1, 2, 3}, 4: {4}}
    Greedy.move_nodes_to_new_cluster(graph, clusters=clusters, new_center=4)

    assert clusters[0] == {0, 1, 2}
    assert clusters[4] == {3, 4}


def test_greedy_basic_graph_colourful_clustering():
    graph = basic_graph()
    instance = Greedy(graph, K, STRICT_CONSTRAINTS)
    clusters, outliers, radius = instance.solve()

    assert radius == pytest.approx(0.854, FLOAT_ERROR_MARGIN)
    assert clusters == {
        0: {0, 1, 2},
        4: {3, 4}
    }
    assert outliers == set()
    assert verify_solution(graph, STRICT_CONSTRAINTS, K, radius, set(clusters.keys())) is True


def test_greedy_basic_graph_max_centers():
    graph = basic_graph()
    instance = Greedy(graph, 5, STRICT_CONSTRAINTS)
    clusters, outliers, radius = instance.solve()

    assert radius == pytest.approx(0, FLOAT_ERROR_MARGIN)
    assert clusters == {
        0: {0},
        1: {1},
        2: {2},
        3: {3},
        4: {4}
    }
    assert outliers == set()
    assert verify_solution(graph, STRICT_CONSTRAINTS, 5, radius, set(clusters.keys())) is True


def test_greedy_basic_graph_outlier_colourful_clustering():
    """This is an example of a colourful k-center graph that is not solved optimally with the standard greedy algorithm
    by Gonzalez. The computed centers are still [0, 4], but node 2 becomes an outlier. The distance between node 2 and
    the center 0 is 3.785. When we relax the constraints, we do not need to cover node 2, which means we cluster
    with a much lower cost of 0.707"""
    graph = basic_graph_with_outlier()
    instance = Greedy(graph, K, RELAXED_CONSTRAINTS)
    clusters, outliers, radius = instance.solve()

    assert radius == pytest.approx(3.785, FLOAT_ERROR_MARGIN)
    assert clusters == {
        0: {0, 1, 2},
        4: {3, 4}
    }
    assert outliers == set()
    assert verify_solution(graph, RELAXED_CONSTRAINTS, K, radius, set(clusters.keys())) is True
