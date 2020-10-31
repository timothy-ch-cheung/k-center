import pytest

from kcenter.solver.gon_greedy import GonGreedy
from tests.kcenter.util.create_test_graph import basic_graph


def test_max_dist_single_cluster():
    graph = basic_graph()
    max_node, max_dist, owning_center = GonGreedy.max_dist(graph, centers=[0], clusters=[{0: {0, 1, 2, 3, 4}}])
    assert max_node == 4
    assert max_dist == pytest.approx(5.515, 0.001)
    assert owning_center == 0


def test_max_dist_double_cluster():
    graph = basic_graph()
    max_node, max_dist, owning_center = GonGreedy.max_dist(graph, clusters={0: {0, 1, 2}, 4: {3, 4}})
    assert max_node == 2
    assert max_dist == pytest.approx(0.854, 0.001)
    assert owning_center == 0
