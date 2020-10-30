import pytest
from tests.kcenter.util.create_test_graph import basic_graph

from src.kcenter.constant.colour import Colour
from src.kcenter.verify.verify import verify_solution

graph = basic_graph()
constraints = {Colour.BLUE: 3, Colour.RED: 2}
k = 2
centers = {0, 3}
radius = 0.86

valid_radii = [0.86, 1.0, 6.37]
invalid_radii = [0.73, 0.71, 0.51]
invalid_constraints = [
    {Colour.BLUE: 4, Colour.RED: 2},
    {Colour.BLUE: 3, Colour.RED: 3},
    {Colour.BLUE: 4, Colour.RED: 3}
]


@pytest.mark.parametrize("r", valid_radii)
def test_valid_center_set_valid_radius(r):
    assert verify_solution(graph, constraints, k, r, centers) is True


@pytest.mark.parametrize("r", invalid_radii)
def test_valid_center_set_invalid_radius(r):
    assert verify_solution(graph, constraints, k, r, centers) is False


def test_invalid_center_set():
    assert verify_solution(graph, constraints, k, radius, {0, 1}) is False


def test_invalid_k():
    assert verify_solution(graph, constraints, 1, radius, centers) is False


@pytest.mark.parametrize("invalid_constraint", invalid_constraints)
def test_unsatisfiable_constraints(invalid_constraint):
    assert verify_solution(graph, invalid_constraint, k, radius, centers) is False
