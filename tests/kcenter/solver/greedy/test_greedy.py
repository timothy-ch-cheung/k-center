import pytest

from src.kcenter.constant.colour import Colour
from src.kcenter.greedy.greedy import GreedySolver
from src.kcenter.verify.verify import verify_solution
from tests.kcenter.util.create_test_graph import basic_graph, basic_graph_with_outlier

FLOAT_ERROR_MARGIN = 0.001
STRICT_CONSTRAINTS = {Colour.BLUE: 3, Colour.RED: 2}
RELAXED_CONSTRAINTS = {Colour.BLUE: 2, Colour.RED: 2}
K = 2


def test_max_dist_single_cluster():
    graph = basic_graph()
    max_node, max_dist, owning_center = GreedySolver.max_dist(graph, clusters={0: {0, 1, 2, 3, 4}})
    assert max_node == 4
    assert max_dist == pytest.approx(5.515, FLOAT_ERROR_MARGIN)
    assert owning_center == 0


def test_max_dist_double_cluster():
    graph = basic_graph()
    max_node, max_dist, owning_center = GreedySolver.max_dist(graph, clusters={0: {0, 1, 2}, 4: {3, 4}})
    assert max_node == 2
    assert max_dist == pytest.approx(0.854, FLOAT_ERROR_MARGIN)
    assert owning_center == 0


def test_move_nodes_to_new_cluster():
    graph = basic_graph()
    clusters = {0: {0, 1, 2, 3}, 4: {4}}
    GreedySolver.move_nodes_to_new_cluster(graph, clusters=clusters, new_center=4)

    assert clusters[0] == {0, 1, 2}
    assert clusters[4] == {3, 4}


def test_greedy_basic_graph_colourful_clustering():
    graph = basic_graph()
    instance = GreedySolver(graph, K, STRICT_CONSTRAINTS)
    clusters, radius = instance.solve()

    assert radius == pytest.approx(0.854, FLOAT_ERROR_MARGIN)
    assert list(clusters.keys()) == [0, 4]
    assert list(clusters.values()) == [{0, 1, 2}, {3, 4}]
    assert verify_solution(graph, STRICT_CONSTRAINTS, K, radius, set(clusters.keys())) is True


def test_greedy_basic_graph_outlier_colourful_clustering():
    """This is an example of a colourful k-center graph that is not solved optimally with the standard greedy algorithm
    by Gonzalez. The computed centers are still [0, 4], but node 2 becomes an outlier. The distance between node 2 and
    the center 0 is 3.275. When we relax the constraints, we don't need to cover node 2, which means we cluster
    with a much lower cost of 0.707"""
    graph = basic_graph_with_outlier()
    instance = GreedySolver(graph, K, RELAXED_CONSTRAINTS)
    clusters, radius = instance.solve()

    assert radius == pytest.approx(3.275, FLOAT_ERROR_MARGIN)
    assert list(clusters.keys()) == [0, 4]
    assert list(clusters.values()) == [{0, 1, 2}, {3, 4}]
    assert verify_solution(graph, RELAXED_CONSTRAINTS, K, radius, set(clusters.keys())) is True


def test_generator_greedy_basic_graph_colourful_clustering():
    graph = basic_graph()
    instance = GreedySolver(graph, K, STRICT_CONSTRAINTS)
    solution = instance.generator()

    assert next(solution) == ({0: {0, 1, 2, 3, 4}}, pytest.approx(6.369, FLOAT_ERROR_MARGIN), 'initial center')
    assert next(solution) == ({0: {0, 1, 2}, 4: {3, 4}}, pytest.approx(5.515, FLOAT_ERROR_MARGIN), 'center 2 added')
    assert next(solution) == (
        {0: {0, 1, 2}, 4: {3, 4}}, pytest.approx(0.854, FLOAT_ERROR_MARGIN), 'completed solution with radius of 0.854')


def test_generator_greedy_basic_graph_outlier_colourful_clustering():
    graph = basic_graph_with_outlier()
    instance = GreedySolver(graph, K, RELAXED_CONSTRAINTS)
    solution = instance.generator()

    assert next(solution) == ({0: {0, 1, 2, 3, 4}}, pytest.approx(7.910, FLOAT_ERROR_MARGIN), 'initial center')
    assert next(solution) == ({0: {0, 1, 2}, 4: {3, 4}}, pytest.approx(5.515, FLOAT_ERROR_MARGIN), 'center 2 added')
    assert next(solution) == (
        {0: {0, 1, 2}, 4: {3, 4}}, pytest.approx(3.275, FLOAT_ERROR_MARGIN), 'completed solution with radius of 3.276')
