import pytest

from src.kcenter.colourful_pbs.alternative_architecture.abstract_genetic_colourful_pbs import calculate_offspring_size

test_data = [
    (4, (1, 1, 1, 1)),
    (5, (2, 1, 1, 1)),
    (8, (2, 2, 2, 2)),
    (15, (4, 4, 4, 3)),
    (16, (4, 4, 4, 4))
]


@pytest.mark.parametrize("population_size, expected", test_data)
def test_calculate_combinations(population_size, expected):
    assert calculate_offspring_size(population_size) == expected
