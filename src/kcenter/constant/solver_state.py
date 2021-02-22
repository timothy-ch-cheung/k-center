from enum import IntEnum


class SolverState(IntEnum):
    ACTIVE_MAIN = 1
    ACTIVE_SUB = 2
    ACTIVE_SUB_END = 3
    INACTIVE = 4

    def is_active(self):
        return self != SolverState.INACTIVE

    def is_sub_solve(self):
        return self == SolverState.ACTIVE_SUB
