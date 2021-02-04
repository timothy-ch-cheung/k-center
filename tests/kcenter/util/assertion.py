from typing import Tuple, List

import pytest

from src.kcenter.solver.abstract_generator import Solution

FLOAT_ERROR_MARGIN = 0.001
Step = Tuple[List[Solution], str, bool]


def assert_solution_equal(actual_solution: Solution, expected_solution: Solution):
    assert expected_solution.cost == pytest.approx(actual_solution.cost, FLOAT_ERROR_MARGIN)
    assert expected_solution.outliers == actual_solution.outliers
    assert expected_solution.clusters == actual_solution.clusters


def assert_step_equal(actual_step: Step, expected_step: Step):
    expected_solutions, expected_label, expected_active = expected_step
    actual_solutions, actual_label, actual_active = actual_step

    for expected, actual in zip(expected_solutions, actual_solutions):
        assert_solution_equal(actual_solution=actual, expected_solution=expected)
    assert expected_label == actual_label
    assert expected_active == actual_active
