import networkx as nx

from src.kcenter.bandyapadhyay.clustering import cluster
from tests.kcenter.util.create_test_graph import basic_graph, basic_graph_with_outlier


def basic_graph_post_lp1():
    graph = basic_graph()
    nx.set_node_attributes(graph, {
        0: 0.0,
        1: 1.0,
        2: 0.0,
        3: 0.0,
        4: 1.0
    }, "x")
    nx.set_node_attributes(graph, 1.0, "z")
    return graph


def basic_graph_with_outlier_post_lp1():
    graph = basic_graph_with_outlier()
    nx.set_node_attributes(graph, {
        0: {"x": 1.0, "z": 1.0},
        1: {"x": 0.0, "z": 1.0},
        2: {"x": 0.0, "z": 0.0},
        3: {"x": 1.0, "z": 1.0},
        4: {"x": 0.0, "z": 1.0}
    })
    return graph


def test_cluster_nodes():
    lp1_graph = basic_graph_post_lp1()
    clusters = cluster(lp1_graph, 0.854)

    assert len(clusters.keys()) == 2
    assert clusters[2] == {0, 1, 2}
    assert clusters[4] == {3, 4}


def test_cluster_nodes_with_outliers():
    lp1_graph_with_outliers = basic_graph_with_outlier_post_lp1()
    clusters = cluster(lp1_graph_with_outliers, 0.854)
    assert len(clusters.keys()) == 3
    assert clusters[1] == {0, 1}
    assert clusters[2] == {2}
    assert clusters[4] == {3, 4}
