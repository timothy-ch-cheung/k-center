import pytest

from kcenter.verify.verify import verify_k_center_solution
from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.target_pbs import TargetPBS
from src.server.orlib_graph_loader import ORLIBGraphLoader
from tests.kcenter.solver.pbs.test_pbs import FLOAT_ERROR_MARGIN


def test_target_pbs(seed_random):
    graph = ORLIBGraphLoader.get_graph("pmed1")
    k = graph.graph["k"]
    constraints = {Colour.BLUE: 100, Colour.RED: 0}
    target = 127
    instance = TargetPBS(graph, k, constraints)

    clusters, outliers, radius = instance.target_solve(target_cost=target)
    assert clusters == {
        7: {2, 3, 4, 5, 6, 7, 8, 19, 20, 21, 22, 27, 35, 36, 39, 45, 46, 49, 50, 51, 52, 53, 59, 60, 61, 62, 63, 68, 80,
            92, 93, 96},
        13: {10, 11, 12, 13, 14, 15, 17, 18, 30, 37, 38, 40, 41, 42, 43, 44, 47, 54, 55, 56, 57, 58, 69, 70, 71, 72, 73,
             81, 82, 84, 85, 86},
        78: {33, 74, 75, 76, 77, 78, 79, 16, 87, 88, 89, 90, 91},
        94: {64, 65, 34, 67, 66, 94, 95},
        99: {32, 1, 97, 98, 99, 100, 9, 48, 83, 23, 24, 25, 26, 28, 29, 31}}
    assert outliers == set()
    assert radius == pytest.approx(127, FLOAT_ERROR_MARGIN)
    assert verify_k_center_solution(graph, set(clusters.keys()), k, radius) == True
