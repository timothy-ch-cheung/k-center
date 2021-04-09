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


@pytest.fixture
def basic_graph_pbs():
    return {
        "k": 2,
        "blue": 3,
        "red": 2,
        "graph": "basic",
        "algorithm": "pbs",
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
        "inspect": False,
        "label": "The initial center is arbitrarily chosen, its coordinates are (1.3, 2.6). It is a blue point."
    }

    response = test_client.post("/api/v1/step/next", json={"id": "1234"})
    assert response.get_json()["step"] == {
        "active": True,
        "inspect": False,
        "label": "We find the point which has the maximum distance from its closest center, which is the point at (6.4, 4.7). It is a red point 5.515 distance away. This makes the current cost 5.515."
    }

    response = test_client.post("/api/v1/step/next", json={"id": "1234"})
    assert response.get_json()["step"] == {
        "active": False,
        "inspect": False,
        "label": "Our 2 centers have been chosen. To calculate the final cost, we find the distance to the furthest point from the previous center. This makes the final cost 0.854."
    }

    response = test_client.post("/api/v1/step/next", json={"id": "1234"})
    assert response.status_code == 404
    assert response.get_json() == {"message": "1234 is not an active problem instance"}


def test_step_through_basic_graph_pbs(basic_graph_pbs, seed_random):
    response = test_client.post("/api/v1/step/start", json=basic_graph_pbs)
    assert response.status_code == 204

    response = test_client.post("/api/v1/step/next", json={"id": "1234"})
    assert response.get_json()["step"] == {
        "active": True,
        "inspect": False,
        "label": "The initial population is generated, the evolution phase can now be started"
    }

    response = test_client.post("/api/v1/step/next", json={"id": "1234"})
    assert response.get_json()["step"] == {
        "active": True,
        "inspect": False,
        "label": "The best individual in this generation is 0 with a cost of 0.728"
    }


def test_step_through_basic_graph_pbs_inspect(basic_graph_pbs, seed_random):
    response = test_client.post("/api/v1/step/start", json=basic_graph_pbs)
    assert response.status_code == 204

    response = test_client.post("/api/v1/step/next", json={"id": "1234"})
    assert response.get_json()["step"] == {
        "active": True,
        "inspect": False,
        "label": "The initial population is generated, the evolution phase can now be started"
    }

    response = test_client.post("/api/v1/step/inspect", json={"id": "1234"})
    assert response.get_json()["step"] == {
        "active": True,
        "inspect": True,
        "label": """INSPECT GENERATION 1: A random mutation operator is applied to the set of centers {(6.4, 4.7), (1.3, 2.6)}, where a subset of the original centers is combined with points sampled random to get the new center set {(5.9, 5.2), (6.4, 4.7)}"""}


def test_inspect_invalid(basic_graph):
    response = test_client.post("/api/v1/step/inspect", json={"id": "4567"})
    assert response.get_json() == {"message": "4567 is not an active problem instance"}


def test_inspect_terminate_generator(basic_graph_pbs):
    test_client.post("/api/v1/step/start", json=basic_graph_pbs)

    test_client.post("/api/v1/step/next", json={"id": "1234"})
    test_client.post("/api/v1/step/next", json={"id": "1234"})
    test_client.post("/api/v1/step/next", json={"id": "1234"})
    response = test_client.post("/api/v1/step/next", json={"id": "1234"})

    assert response.get_json()["step"] == {
        "active": True,
        "inspect": False,
        "label": "The best individual in this generation is 0 with a cost of 0.728"}

    response = test_client.post("/api/v1/step/inspect", json={"id": "1234"})
    assert response.status_code == 200

    assert response.get_json()["step"] == {
        "active": False,
        "inspect": False,
        "label": "3 generations were completed. The fittest individual was 0 with a cost of 0.728"}
