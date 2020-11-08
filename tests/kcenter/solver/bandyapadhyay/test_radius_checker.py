import pytest

from src.kcenter.bandyapadhyay.radius_checker import RadiusChecker
from tests.kcenter.util.create_test_graph import basic_graph

graph = basic_graph()
checker = RadiusChecker(graph=graph, k=2, min_red_coverage=2, min_blue_coverage=3)

correct_guesses = [0.854]


@pytest.mark.parametrize("guess", correct_guesses)
def test_correct_radius_guess(guess):
    assert checker.verify(guess) is True


incorrect_guesses = [0.5]


@pytest.mark.parametrize("guess", incorrect_guesses)
def test_incorrect_radius_guess(guess):
    assert checker.verify(guess) is False
