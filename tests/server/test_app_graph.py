from src.server.app import create_app

test_client = create_app().test_client()


def test_get_graph_basic():
    response = test_client.get("/api/v1/graph/basic")
    assert response.status_code == 200
    assert response.get_json() == {
        "data": [{"colour": "blue", "x": 1.3, "y": 2.6},
                 {"colour": "blue", "x": 1.2, "y": 2.1},
                 {"colour": "blue", "x": 0.5, "y": 2.3},
                 {"colour": "red", "x": 5.9, "y": 5.2},
                 {"colour": "red", "x": 6.4, "y": 4.7}
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
        "red": 2
    }


def test_get_graph_basic_with_outlier():
    response = test_client.get("/api/v1/graph/basic_with_outlier")
    assert response.status_code == 200
    assert response.get_json() == {
        "data": [{"colour": "blue", "x": 1.3, "y": 2.6},
                 {"colour": "blue", "x": 1.2, "y": 2.1},
                 {"colour": "blue", "x": 0.5, "y": 6.3},
                 {"colour": "red", "x": 5.9, "y": 5.2},
                 {"colour": "red", "x": 6.4, "y": 4.7}
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
        "red": 2,
    }
