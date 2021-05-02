import os

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
        "optimalSolution": {
            "k": 2,
            "minBlue": 3,
            "minRed": 2,
            "outliers": 0,
            "radius": 0.728
        },
        "nodes": 5,
        "blue": 3,
        "red": 2,
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
        "optimalSolution": {
            "k": 2,
            "minBlue": 2,
            "minRed": 2,
            "outliers": 1,
            "radius": 0.707
        },
        "nodes": 5,
        "blue": 3,
        "red": 2
    }


def test_save_json():
    graph = {
        "data": [{
            "colour": "red",
            "y": 5.2,
            "x": 5.9
        },
            {
                "colour": "blue",
                "y": 4.7,
                "x": 6.4,
            }
        ],
        "optimalSolution": {
            "k": 1,
            "minBlue": 1,
            "minRed": 1,
            "outliers": 0,
            "radius": 0.86
        },
        "nodes": 2,
        "blue": 1,
        "red": 1
    }

    GraphLoader.save_json(graph, "test_save_json")
    assert GraphLoader.get_json("test_save_json") == graph
    os.remove(f"{os.path.dirname(__file__)}/../../src/server/dataset/test_save_json.txt")


def test_get_graph_meta_data():
    meta_data = GraphLoader.get_json_meta_data("basic")
    assert meta_data == {
        "nodes": 5,
        "blue": 3,
        "red": 2,
        "optimalSolution": {
            "k": 2,
            "minBlue": 3,
            "minRed": 2,
            "outliers": 0,
            "radius": 0.728
        }
    }


def test_get_graph_basic_graph():
    actual_graph = GraphLoader.get_graph("basic")
    expected_graph = basic_graph()

    em = nx.algorithms.isomorphism.numerical_edge_match("weight", 1)
    assert nx.is_isomorphic(actual_graph, expected_graph, edge_match=em)


def test_get_graph_basic_outlier_graph():
    actual_graph = GraphLoader.get_graph("basic_with_outlier")
    expected_graph = basic_graph_with_outlier()

    em = nx.algorithms.isomorphism.numerical_edge_match("weight", 1)
    assert nx.is_isomorphic(actual_graph, expected_graph, edge_match=em)


def test_get_problem_list():
    problems = GraphLoader.get_problem_list(dataset_name="TRAIN_COLOURFUL")
    assert set(problems) == {"train_col_n100_k10", "train_col_n100_k20", "train_col_n100_k5", "train_col_n200_k10",
                             "train_col_n200_k20", "train_col_n200_k5", "train_col_n300_k20", "train_col_n300_k40",
                             "train_col_n400_k20", "train_col_n400_k40"}


def test_get_header():
    header = GraphLoader.get_header("SYNTHETIC/syn01")
    assert header == (100, 48, 52, 3, 40, 40, 20, 133.5)


def test_get_opt():
    OPT = GraphLoader.get_opt()
    assert OPT == {
        'syn01': 133.5, 'syn02': 80.5, 'syn03': 40.5, 'syn04': 15.5, 'syn05': 80.5, 'syn06': 40.5, 'syn07': 16.5,
        'syn08': 8.5, 'syn09': 80.5, 'syn10': 27.5, 'syn11': 12.5, 'syn12': 5.5, 'syn13': 80.5, 'syn14': 16.5,
        'syn15': 12.5, 'syn16': 4.5, 'syn17': 80.5, 'syn18': 16.5, 'syn19': 12.5, 'syn20': 3.5, 'syn21': 80.5,
        'syn22': 16.5, 'syn23': 9.5, 'syn24': 2.5, 'syn25': 40.5, 'syn26': 11.5, 'syn27': 8.5, 'syn28': 2.5,
        'syn29': 40.5, 'syn30': 11.5, 'syn31': 7.5, 'syn32': 2.5, 'syn33': 27.5, 'syn34': 10.5, 'syn35': 7.5,
        'syn36': 2.5, 'syn37': 80.5, 'syn38': 40.5, 'syn39': 16.5, 'syn40': 13.5
    }
