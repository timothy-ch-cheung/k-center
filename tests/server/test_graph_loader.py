import networkx as nx

from src.server.graph_loader import GraphLoader
from tests.kcenter.util.create_test_graph import basic_graph, basic_graph_with_outlier


def test_get_json_basic_graph():
    assert GraphLoader.get_json("basic") == {
        "data": [
            {
                "colour": "blue",
                "y": 2.6,
                "x": 1.3,
            },
            {
                "colour": "blue",
                "y": 2.1,
                "x": 1.2
            },
            {
                "colour": "blue",
                "y": 2.3,
                "x": 0.5
            },
            {
                "colour": "red",
                "y": 5.2,
                "x": 5.9
            },
            {
                "colour": "red",
                "y": 4.7,
                "x": 6.4,
            }
        ],
        "k": 2,
        "nodes": 5,
        "minBlue": 3,
        "minRed": 2,
        "blue": 3,
        "red": 2
    }


def test_get_json_basic_outlier_graph():
    assert GraphLoader.get_json("basic_with_outlier") == {
        "data": [
            {
                "colour": "blue",
                "y": 2.6,
                "x": 1.3,
            },
            {
                "colour": "blue",
                "y": 2.1,
                "x": 1.2
            },
            {
                "colour": "blue",
                "y": 6.3,
                "x": 0.5
            },
            {
                "colour": "red",
                "y": 5.2,
                "x": 5.9
            },
            {
                "colour": "red",
                "y": 4.7,
                "x": 6.4,
            }
        ],
        "k": 2,
        "nodes": 5,
        "minBlue": 2,
        "minRed": 2,
        "blue": 3,
        "red": 2
    }


def test_get_graph_meta_data():
    meta_data = GraphLoader.get_json_meta_data("basic")
    assert meta_data == {
        "nodes": 5,
        "blue": 3,
        "red": 2
    }


def test_get_graph_basic_graph():
    actual_graph = GraphLoader.get_graph("basic")
    expected_graph = basic_graph()

    em = nx.algorithms.isomorphism.numerical_edge_match('weight', 1)
    assert nx.is_isomorphic(actual_graph, expected_graph, edge_match=em)


def test_get_graph_basic_outlier_graph():
    actual_graph = GraphLoader.get_graph("basic_with_outlier")
    expected_graph = basic_graph_with_outlier()

    em = nx.algorithms.isomorphism.numerical_edge_match('weight', 1)
    assert nx.is_isomorphic(actual_graph, expected_graph, edge_match=em)