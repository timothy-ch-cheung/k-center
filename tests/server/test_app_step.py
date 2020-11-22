import pytest

from src.server.app import create_app

test_client = create_app().test_client()
FLOAT_ERROR_MARGIN = 0.001


@pytest.fixture
def basic_graph():
    return {
        "k": 2,
        "blue": 3,
        "red": 2,
        "graph": "basic",
        "algorithm": "greedy",
        "id": "1234"
    }

def test_step_through_non_existing_instance(basic_graph):
    response = test_client.post("/api/v1/step/next", json={"id": "abcdef"})
    assert response.status_code == 404
    assert response.get_json() == {"message": "abcdef is not an active problem instance"}


def test_step_through_basic_graph(basic_graph):
    response = test_client.post("/api/v1/step/start", json=basic_graph)
    assert response.status_code == 204

    response = test_client.post("/api/v1/step/next", json={"id": "1234"})
    assert response.get_json()["step"] == {
        "active": True,
        "label": "The initial center is arbitrarily chosen, its coordinates are (1.3, 2.6). It is a blue point."
    }

    response = test_client.post("/api/v1/step/next", json={"id": "1234"})
    assert response.get_json()["step"] == {
        "active": True,
        "label": "We find the point which has the maximum distance from its closest center, which is the point at (6.4, 4.7). It is a red point 5.515 distance away. This makes the current cost 5.515."
    }

    response = test_client.post("/api/v1/step/next", json={"id": "1234"})
    assert response.get_json()["step"] == {
        "active": False,
        "label": "Our 2 centers have been chosen. To calculate the final cost, we find the distance to the furthest point from the previous center. This makes the final cost 0.854."
    }

    response = test_client.post("/api/v1/step/next", json={"id": "1234"})
    assert response.status_code == 404
    assert response.get_json() == {"message": "1234 is not an active problem instance"}
