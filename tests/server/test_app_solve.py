import pytest

from src.server.app import create_app

test_client = create_app().test_client()
FLOAT_ERROR_MARGIN = 0.001


class Ignore:
    def __eq__(self, other):
        return True


ignore = Ignore()


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
        "nodes": 5,
        "blue": 3,
        "red": 2,
        "optimalSolution": {
            "k": 2,
            "minBlue": 3,
            "minRed": 2,
            "outliers": 0,
            "radius": 0.728},
        "solution": {
            "k": 2,
            "outliers": 0,
            "radius": pytest.approx(0.854, FLOAT_ERROR_MARGIN),
            "timeTaken": ignore
        },
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
        "nodes": 5,
        "blue": 3,
        "red": 2,
        "optimalSolution": {
            "k": 2,
            "minBlue": 3,
            "minRed": 2,
            "outliers": 0,
            "radius": 0.728
        },
        "solution": {
            "k": 2,
            "outliers": 1,
            "radius": pytest.approx(0.707, FLOAT_ERROR_MARGIN),
            "timeTaken": ignore
        },
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
        "nodes": 5,
        "blue": 3,
        "red": 2,
        "optimalSolution": {
            "k": 2,
            "minBlue": 3,
            "minRed": 2,
            "outliers": 0,
            "radius": 0.728
        },
        "solution": {
            "k": 2,
            "outliers": 0,
            "radius": pytest.approx(1.456, FLOAT_ERROR_MARGIN),
            "timeTaken": ignore
        },
        "data": [
            {"center": True, "colour": "blue", "x": 1.3, "y": 2.6},
            {"colour": "blue", "x": 1.2, "y": 2.1},
            {"colour": "blue", "x": 0.5, "y": 2.3},
            {"center": True, "colour": "red", "x": 5.9, "y": 5.2},
            {"colour": "red", "x": 6.4, "y": 4.7}
        ]
    }


def test_solve_basic_graph_with_pbs_algorithm(basic_graph, seed_random):
    basic_graph["algorithm"] = "pbs"
    response = test_client.post("/api/v1/solve", json=basic_graph)

    assert response.status_code == 200
    assert response.get_json() == {
        "nodes": 5,
        "blue": 3,
        "red": 2,
        "optimalSolution": {
            "k": 2,
            "minBlue": 3,
            "minRed": 2,
            "outliers": 0,
            "radius": 0.728
        },
        "solution": {
            "k": 2,
            "outliers": 0,
            "radius": pytest.approx(0.728, FLOAT_ERROR_MARGIN),
            "timeTaken": ignore
        },
        "data": [
            {"colour": "blue", "x": 1.3, "y": 2.6},
            {"center": True, "colour": "blue", "x": 1.2, "y": 2.1},
            {"colour": "blue", "x": 0.5, "y": 2.3},
            {"center": True, "colour": "red", "x": 5.9, "y": 5.2},
            {"colour": "red", "x": 6.4, "y": 4.7}
        ]
    }


def test_solve_basic_outlier_graph_with_greedy(basic_graph_with_outlier):
    basic_graph_with_outlier["algorithm"] = "greedy"
    response = test_client.post("/api/v1/solve", json=basic_graph_with_outlier)

    assert response.status_code == 200
    assert response.get_json() == {
        "nodes": 5,
        "blue": 3,
        "red": 2,
        "optimalSolution": {
            "k": 2,
            "minBlue": 2,
            "minRed": 2,
            "outliers": 1,
            "radius": 0.707
        },
        "solution": {
            "k": 2,
            "outliers": 0,
            "radius": pytest.approx(3.785, FLOAT_ERROR_MARGIN),
            "timeTaken": ignore
        },
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
        "nodes": 5,
        "blue": 3,
        "red": 2,
        "optimalSolution": {
            "k": 2,
            "minBlue": 2,
            "minRed": 2,
            "outliers": 1,
            "radius": 0.707
        },
        "solution": {
            "k": 2,
            "outliers": 1,
            "radius": pytest.approx(1.414, FLOAT_ERROR_MARGIN),
            "timeTaken": ignore
        },
        "data": [
            {"center": True, "colour": "blue", "x": 1.3, "y": 2.6},
            {"colour": "blue", "x": 1.2, "y": 2.1},
            {"colour": "blue", "x": 0.5, "y": 6.3},
            {"center": True, "colour": "red", "x": 5.9, "y": 5.2},
            {"colour": "red", "x": 6.4, "y": 4.7}
        ]
    }


def test_solve_basic_outlier_graph_with_pbs(basic_graph_with_outlier):
    basic_graph_with_outlier["algorithm"] = "pbs"
    response = test_client.post("/api/v1/solve", json=basic_graph_with_outlier)

    assert response.status_code == 200
    assert response.get_json() == {
        "nodes": 5,
        "blue": 3,
        "red": 2,
        "optimalSolution": {
            "k": 2,
            "minBlue": 2,
            "minRed": 2,
            "outliers": 1,
            "radius": 0.707
        },
        "solution": {
            "k": 2,
            "outliers": 0,
            "radius": pytest.approx(3.785, FLOAT_ERROR_MARGIN),
            "timeTaken": ignore
        },
        "data": [
            {"center": True, "colour": "blue", "x": 1.3, "y": 2.6},
            {"colour": "blue", "x": 1.2, "y": 2.1},
            {"colour": "blue", "x": 0.5, "y": 6.3},
            {"colour": "red", "x": 5.9, "y": 5.2},
            {"center": True, "colour": "red", "x": 6.4, "y": 4.7}
        ]
    }
