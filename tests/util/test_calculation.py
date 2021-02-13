import pytest

from src.util.calculation import calculate_combinations

test_data = [
    (4, 2, 6),
    (5, 3, 10),
    (100, 5, 75287520)
]


@pytest.mark.parametrize("n, r, expected", test_data)
def test_calculate_combinations(n, r, expected):
    assert calculate_combinations(n, r) == expected
