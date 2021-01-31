from enum import IntEnum


class SearchStage(IntEnum):
    VALID_WEIGHT = 1
    INVALID_WEIGHT = 2
    FINISHED = 3
    UNFINISHED = 4