from src.server.graph_loader import GraphLoader


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
        "blue": 2,
        "red": 2
    }
