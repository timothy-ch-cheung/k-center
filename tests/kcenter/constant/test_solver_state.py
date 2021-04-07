import pytest

from src.kcenter.constant.solver_state import SolverState

test_data = [
    (SolverState.INACTIVE, False),
    (SolverState.ACTIVE_MAIN, True),
    (SolverState.ACTIVE_SUB, True),
    (SolverState.ACTIVE_SUB_END, True)
]


@pytest.mark.parametrize("solver_state, expected", test_data)
def test_solver_state_active(solver_state, expected):
    assert solver_state.is_active() == expected
