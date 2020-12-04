import pytest

from src.kcenter.pbs.pbs import PBS, Individual
from tests.kcenter.constant.consts import FLOAT_ERROR
from tests.kcenter.solver.pbs.test_pbs import K, STRICT_CONSTRAINTS
from tests.kcenter.util.create_test_graph import basic_graph


def test_add_center():
    graph = basic_graph()
    instance = PBS(graph, K, STRICT_CONSTRAINTS)

    individual = Individual({0})
    individual.init_nearest_centers(graph)
    assert individual.cost == pytest.approx(5.515, FLOAT_ERROR)
    expected_nearest_centers = [
        "{'nearest_center': {point: 0, cost: 0}, 'second_nearest_center': None}",
        "{'nearest_center': {point: 0, cost: 0.51}, 'second_nearest_center': None}",
        "{'nearest_center': {point: 0, cost: 0.854}, 'second_nearest_center': None}",
        "{'nearest_center': {point: 0, cost: 5.284}, 'second_nearest_center': None}",
        "{'nearest_center': {point: 0, cost: 5.515}, 'second_nearest_center': None}"
    ]
    for point, expected in enumerate(expected_nearest_centers):
        assert str(individual.nearest_centers[point]) == expected

    instance.add_center(center=4, individual=individual)
    expected_nearest_centers = [
        "{'nearest_center': {point: 0, cost: 0}, 'second_nearest_center': {point: 4, cost: 5.515}}",
        "{'nearest_center': {point: 0, cost: 0.51}, 'second_nearest_center': {point: 4, cost: 5.814}}",
        "{'nearest_center': {point: 0, cost: 0.854}, 'second_nearest_center': {point: 4, cost: 6.369}}",
        "{'nearest_center': {point: 4, cost: 0.707}, 'second_nearest_center': {point: 0, cost: 5.284}}",
        "{'nearest_center': {point: 4, cost: 0}, 'second_nearest_center': {point: 0, cost: 5.515}}"
    ]
    for point, expected in enumerate(expected_nearest_centers):
        assert str(individual.nearest_centers[point]) == expected
