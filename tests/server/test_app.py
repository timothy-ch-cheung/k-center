from server.app import create_app

test_client = create_app().test_client()


def test_get_graph_basic():
    response = test_client.get('/api/v1/graph/basic')
    assert response.status_code == 200
    assert response.get_json() == {
        'data': [{'colour': 'BLUE', 'x': 1.3, 'y': 2.6},
                 {'colour': 'BLUE', 'x': 1.2, 'y': 2.1},
                 {'colour': 'BLUE', 'x': 0.5, 'y': 2.3},
                 {'colour': 'RED', 'x': 5.9, 'y': 5.2},
                 {'colour': 'RED', 'x': 6.4, 'y': 4.7}
                 ]
    }


def test_get_graph_basic_with_outlier():
    response = test_client.get('/api/v1/graph/basic_with_outlier')
    assert response.status_code == 200
    assert response.get_json() == {
        'data': [{'colour': 'BLUE', 'x': 1.3, 'y': 2.6},
                 {'colour': 'BLUE', 'x': 1.2, 'y': 2.1},
                 {'colour': 'BLUE', 'x': 0.5, 'y': 6.3},
                 {'colour': 'RED', 'x': 5.9, 'y': 5.2},
                 {'colour': 'RED', 'x': 6.4, 'y': 4.7}
                 ]
    }
