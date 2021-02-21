from enum import IntEnum


class SolverState(IntEnum):
    ACTIVE_MAIN = 1
    ACTIVE_SUB = 2
    ACTIVE_SUB_END = 3
    INACTIVE = 4

    def active(self):
        return self != SolverState.INACTIVE
