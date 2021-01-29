import pytest

from src.kcenter.pbs.similarity import CompareSolution
from tests.kcenter.util.create_test_graph import grid_graph
from tests.server.test_app_solve import FLOAT_ERROR_MARGIN

MIN = (0, 0)
MAX = (4, 4)

non_normalised_test_data = [
    ({4, 8, 12, 16, 20}, {(0.5, 0.5), (0.75, 0.75), (0.0, 0.0), (1.0, 1.0), (0.25, 0.25)}),
    (({0, 3}), {(0.0, 1.0), (0.75, 1.0)}),
    (({14, 19}), {(1.0, 0.5), (1.0, 0.25)})
]


@pytest.mark.parametrize("S,expected", non_normalised_test_data)
def test_normalise(S, expected):
    graph = grid_graph()
    comp = CompareSolution(graph, min_value=MIN, max_value=MAX)
    assert comp.normalise(S) == expected


similarity_test_data = [
    ({1, 2, 3}, 0),
    ({2, 3, 4}, pytest.approx(0.1767, FLOAT_ERROR_MARGIN)),
    ({21, 22, 23}, pytest.approx(0.7071, FLOAT_ERROR_MARGIN)),
    ({22, 23, 24}, pytest.approx(0.7288, FLOAT_ERROR_MARGIN)),
    ({14, 19, 24}, pytest.approx(0.7288, FLOAT_ERROR_MARGIN)),
    ({1, 7, 13}, pytest.approx(0.3535, FLOAT_ERROR_MARGIN))
]


@pytest.mark.parametrize("S,expected", similarity_test_data)
def test_sim(S, expected):
    graph = grid_graph()
    comp = CompareSolution(graph, min_value=MIN, max_value=MAX)
    center_set = {1, 2, 3}
    assert comp.sim(center_set, S) == expected
