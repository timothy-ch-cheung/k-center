import pytest

from src.server.app import create_app

test_client = create_app().test_client()


@pytest.fixture
def basic_graph():
    return {
        "k": 2,
        "blue": 3,
        "red": 2,
        "graph": "basic"
    }


@pytest.fixture
def basic_graph_with_outlier():
    return {
        "k": 2,
        "blue": 2,
        "red": 2,
        "graph": "basic_with_outlier"
    }


def test_solve_basic_graph_with_greedy(basic_graph):
    basic_graph["algorithm"] = "greedy"
    response = test_client.post("/api/v1/solve", json=basic_graph)

    assert response.status_code == 200
    assert response.get_json() == {
        "centerRadius": 0.8544003745317533,
        "nodes": 5,
        "blue": 3,
        "red": 2,
        "optimalOutliers": 0,
        "optimalRadius": 0.728,
        "data": [
            {"center": True, "colour": "blue", "x": 1.3, "y": 2.6},
            {"colour": "blue", "x": 1.2, "y": 2.1},
            {"colour": "blue", "x": 0.5, "y": 2.3},
            {"colour": "red", "x": 5.9, "y": 5.2},
            {"center": True, "colour": "red", "x": 6.4, "y": 4.7}
        ]
    }


def test_solve_basic_graph_with_greedy_reduce(basic_graph):
    basic_graph["algorithm"] = "greedy_reduce"
    basic_graph["blue"] = 2
    response = test_client.post("/api/v1/solve", json=basic_graph)

    assert response.status_code == 200
    assert response.get_json() == {
        "centerRadius": 0.7071067811865476,
        "nodes": 5,
        "blue": 3,
        "red": 2,
        "optimalOutliers": 0,
        "optimalRadius": 0.728,
        "data": [
            {"center": True, "colour": "blue", "x": 1.3, "y": 2.6},
            {"colour": "blue", "x": 1.2, "y": 2.1},
            {"colour": "blue", "x": 0.5, "y": 2.3},
            {"colour": "red", "x": 5.9, "y": 5.2},
            {"center": True, "colour": "red", "x": 6.4, "y": 4.7}
        ]
    }


def test_solve_basic_graph_with_bandyapadhyay_algorithm(basic_graph):
    basic_graph["algorithm"] = "colourful_bandyapadhyay"
    response = test_client.post("/api/v1/solve", json=basic_graph)

    assert response.status_code == 200
    assert response.get_json() == {
        "centerRadius": 1.4560219778561034,
        "nodes": 5,
        "blue": 3,
        "red": 2,
        "optimalOutliers": 0,
        "optimalRadius": 0.728,
        "data": [
            {"colour": "blue", "x": 1.3, "y": 2.6},
            {"colour": "blue", "x": 1.2, "y": 2.1},
            {"center": True, "colour": "blue", "x": 0.5, "y": 2.3},
            {"colour": "red", "x": 5.9, "y": 5.2},
            {"center": True, "colour": "red", "x": 6.4, "y": 4.7}
        ]
    }


def test_solve_basic_outlier_graph_with_greedy(basic_graph_with_outlier):
    basic_graph_with_outlier["algorithm"] = "greedy"
    response = test_client.post("/api/v1/solve", json=basic_graph_with_outlier)

    assert response.status_code == 200
    assert response.get_json() == {
        "centerRadius": 3.7854986461495397,
        "nodes": 5,
        "blue": 3,
        "red": 2,
        "optimalOutliers": 1,
        "optimalRadius": 0.86,
        "data": [
            {"center": True, "colour": "blue", "x": 1.3, "y": 2.6},
            {"colour": "blue", "x": 1.2, "y": 2.1},
            {"colour": "blue", "x": 0.5, "y": 6.3},
            {"colour": "red", "x": 5.9, "y": 5.2},
            {"center": True, "colour": "red", "x": 6.4, "y": 4.7}
        ]
    }


def test_solve_basic_outlier_graph_with_greedy_reduce(basic_graph_with_outlier):
    basic_graph_with_outlier["algorithm"] = "greedy_reduce"
    response = test_client.post("/api/v1/solve", json=basic_graph_with_outlier)

    assert response.status_code == 200
    assert response.get_json() == {
        "centerRadius": 0.7071067811865476,
        "data": [
            {"center": True, "colour": "blue", "x": 1.3, "y": 2.6},
            {"colour": "blue", "x": 1.2, "y": 2.1},
            {"colour": "blue", "x": 0.5, "y": 6.3},
            {"colour": "red", "x": 5.9, "y": 5.2},
            {"center": True, "colour": "red", "x": 6.4, "y": 4.7}
        ]
    }


def test_solve_basic_outlier_graph_with_greedy_reduce(basic_graph_with_outlier):
    basic_graph_with_outlier["algorithm"] = "colourful_bandyapadhyay"
    response = test_client.post("/api/v1/solve", json=basic_graph_with_outlier)

    assert response.status_code == 200
    assert response.get_json() == {
        "centerRadius": 1.4142135623730951,
        "nodes": 5,
        "blue": 3,
        "red": 2,
        "optimalOutliers": 1,
        "optimalRadius": 0.86,
        "data": [
            {"colour": "blue", "x": 1.3, "y": 2.6},
            {"center": True, "colour": "blue", "x": 1.2, "y": 2.1},
            {"colour": "blue", "x": 0.5, "y": 6.3},
            {"colour": "red", "x": 5.9, "y": 5.2},
            {"center": True, "colour": "red", "x": 6.4, "y": 4.7}
        ]
    }
