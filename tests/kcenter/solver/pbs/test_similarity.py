import pytest

from kcenter.pbs.similarity import normalise

MIN = (0, 0)
MAX = (5, 5)
non_normalised_test_data = [
    ({(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)}, {(0.2, 0.2), (0.4, 0.4), (0.6, 0.6), (0.8, 0.8), (1.0, 1.0)}),
    ({(0.5, 1.5), (2.5, 3.5)}, {(0.1, 0.3), (0.5, 0.7)}),
    ({(4.75, 2.25)}, {(0.95, 0.45)}),
    ({(0, 0), (5, 5)}, {(0, 0), (1, 1)})
]


@pytest.mark.parametrize("S,expected", non_normalised_test_data)
def test_normalise(S, expected):
    assert normalise(S, MIN, MAX) == expected

