from unittest.mock import MagicMock

import pytest

from src.kcenter.bandyapadhyay_pseudo.radius_checker import RadiusChecker
from tests.kcenter.util.create_test_graph import basic_graph

graph = basic_graph()
checker = RadiusChecker(graph=graph, k=2, min_red_coverage=2, min_blue_coverage=3)


def test_correct_radius_guess():
    solution = checker.verify(0.854)
    expected_solution = {
        0: {'x': 0.0, 'z': 1.0},
        1: {'x': 1.0, 'z': 1.0},
        2: {'x': 0.0, 'z': 1.0},
        3: {'x': 1.0, 'z': 1.0},
        4: {'x': 0.0, 'z': 1.0}
    }
    assert solution == expected_solution


def test_large_radius_guesses():
    solution = checker.verify(6.369)
    expected_solution = {
        0: {'x': 1.0, 'z': 1.0},
        1: {'x': 0.0, 'z': 1.0},
        2: {'x': 0.0, 'z': 1.0},
        3: {'x': 0.0, 'z': 1.0},
        4: {'x': 0.0, 'z': 1.0}}
    assert solution == expected_solution


incorrect_guesses = [0.510, 0.707, 0.728]


@pytest.mark.parametrize("guess", incorrect_guesses)
def test_incorrect_radius_guess(guess):
    solution = checker.verify(guess)
    assert solution is None


def mock_pyomo_model_for_basic_graph(opt: float):
    mock_model = MagicMock()
    mock_model.N = [0, 1, 2, 3, 4]
    mock_model.opt.value = opt
    return mock_model


def test_get_surrounding_points():
    mock_model = mock_pyomo_model_for_basic_graph(opt=1.0)

    points = RadiusChecker.get_surrounding_points(0, mock_model, graph)
    assert points == [0, 1, 2]


def test_get_surrounding_points_tiny_opt():
    mock_model = mock_pyomo_model_for_basic_graph(opt=0.1)

    points = RadiusChecker.get_surrounding_points(0, mock_model, graph)
    assert points == [0]


def test_get_surrounding_points_large_opt():
    mock_model = mock_pyomo_model_for_basic_graph(opt=7.0)

    points = RadiusChecker.get_surrounding_points(0, mock_model, graph)
    assert points == [0, 1, 2, 3, 4]
