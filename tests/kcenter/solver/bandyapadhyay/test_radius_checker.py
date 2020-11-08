import pytest

from src.kcenter.bandyapadhyay.radius_checker import RadiusChecker
from tests.kcenter.util.create_test_graph import basic_graph
from unittest.mock import MagicMock

graph = basic_graph()
checker = RadiusChecker(graph=graph, k=2, min_red_coverage=2, min_blue_coverage=3)

correct_guesses = [0.854, 5.155, 6.369]


@pytest.mark.parametrize("guess", correct_guesses)
def test_correct_radius_guess(guess):
    assert checker.verify(guess) is True


incorrect_guesses = [0.510, 0.707, 0.728]


@pytest.mark.parametrize("guess", incorrect_guesses)
def test_incorrect_radius_guess(guess):
    assert checker.verify(guess) is False


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
