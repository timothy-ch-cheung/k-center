import pytest

from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.target_pbs import TargetPBS
from src.kcenter.verify.verify import verify_k_center_solution
from src.server.orlib_graph_loader import ORLIBGraphLoader
from tests.kcenter.solver.pbs.test_pbs import FLOAT_ERROR_MARGIN


def test_target_pbs_no_timeout(seed_random):
    graph = ORLIBGraphLoader.get_graph("pmed1")
    k = graph.graph["k"]
    constraints = {Colour.BLUE: 100, Colour.RED: 0}
    target = 127
    instance = TargetPBS(graph, k, constraints)

    clusters, outliers, radius = instance.target_solve(target_cost=target)
    assert clusters == {
        57: {10, 11, 12, 13, 14, 15, 17, 18, 30, 37, 38, 40, 41, 42, 43, 44, 47, 55, 56, 57, 58, 69, 70, 71, 72, 73, 81,
             84, 85, 86},
        60: {2, 3, 4, 5, 6, 7, 19, 20, 21, 22, 27, 34, 35, 36, 39, 45, 46, 49, 50, 51, 52, 54, 59, 60, 61, 68, 80, 93,
             96},
        63: {64, 65, 66, 67, 31, 62, 63},
        78: {33, 74, 75, 76, 77, 78, 79, 16, 87, 88, 89, 90, 91, 92, 94},
        99: {1, 8, 9, 23, 24, 25, 26, 28, 29, 32, 48, 53, 82, 83, 95, 97, 98, 99, 100}
    }
    assert outliers == set()
    assert radius == pytest.approx(127, FLOAT_ERROR_MARGIN)
    assert verify_k_center_solution(graph, set(clusters.keys()), k, radius) == True


def test_target_pbs_timeout(seed_random):
    graph = ORLIBGraphLoader.get_graph("pmed3")
    k = graph.graph["k"]
    constraints = {Colour.BLUE: 100, Colour.RED: 0}
    target = 93
    instance = TargetPBS(graph, k, constraints)

    clusters, outliers, radius = instance.target_solve(target_cost=target, timeout=3)

    assert clusters == {
        1: {1, 66, 100},
        32: {32, 33, 42, 45, 21, 22, 26, 27, 93, 94, 31},
        37: {2, 34, 4, 5, 35, 36, 37, 38, 73, 74, 92, 85, 24, 25, 58, 28, 29, 57},
        48: {96, 65, 97, 39, 40, 41, 71, 72, 46, 47, 48, 49},
        51: {50, 51, 52},
        77: {6, 7, 8, 9, 10, 11, 53, 61, 62, 63, 64, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 84},
        82: {12, 13, 14, 15, 44, 81, 82, 83, 59, 30},
        87: {88, 86, 87},
        90: {98, 99, 16, 17, 18, 89, 90, 91},
        95: {3, 43, 19, 20, 55, 54, 23, 56, 60, 95}
    }
    assert outliers == set()
    assert radius == pytest.approx(95, FLOAT_ERROR_MARGIN)
