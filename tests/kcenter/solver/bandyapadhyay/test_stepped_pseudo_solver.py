import pytest

from src.kcenter.bandyapadhyay.stepped_pseudo_solver import SteppedConstantPseudoColourful
from src.kcenter.constant.colour import Colour
from tests.kcenter.solver.greedy.test_greedy import FLOAT_ERROR_MARGIN
from tests.kcenter.util.create_test_graph import basic_graph_with_outlier


def test_generator_greedy_basic_graph_outlier_colourful_clustering():
    k = 2
    constraints = {Colour.RED: 2, Colour.BLUE: 2}
    graph = basic_graph_with_outlier()
    instance = SteppedConstantPseudoColourful(graph, k, constraints)
    solution = instance.generator()

    assert next(solution) == (
        {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}},
        set(),
        0,
        "LP1 is used to find the optimal cost to this problem instance - a solution to LP1 with a given cost means that the cost is valid. A binary search like algorithm is used to search 10 different costs that could potentially be the optimum.",
        True
    )

    assert next(solution) == (
        {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}},
        set(),
        0,
        "Run LP1 with cost=5.511 - the cost is valid, there exists a solution with this radius. We will check a lower cost in the next step.",
        True
    )

    assert next(solution) == (
        {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}},
        set(),
        0,
        "Run LP1 with cost=3.785 - the cost is valid, there exists a solution with this radius. We will check a lower cost in the next step.",
        True
    )

    assert next(solution) == (
        {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}},
        set(),
        0,
        "Run LP1 with cost=0.51 - the cost is invalid. We will check a higher cost in the next step.",
        True
    )

    assert next(solution) == (
        {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}},
        set(),
        0,
        "Run LP1 with cost=0.707 - the cost is valid, there exists a solution with this radius. We will check a lower cost in the next step.",
        True
    )

    assert next(solution) == (
        {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}},
        set(),
        0,
        "All weights are exhausted - the minimal feasible cost for LP1 is 0.707 and therefore is the optimal cost. Using this cost we can greedily cluster all points.",
        True
    )

    assert next(solution) == (
        {0: {0, 1}},
        set(),
        pytest.approx(0.7071, FLOAT_ERROR_MARGIN),
        "Create cluster at (1.3, 2.6), covering 2 points.",
        True
    )

    assert next(solution) == (
        {0: {0, 1}, 3: {3, 4}},
        set(),
        pytest.approx(0.7071, FLOAT_ERROR_MARGIN),
        "Create cluster at (5.9, 5.2), covering 2 points.",
        True
    )

    assert next(solution) == (
        {0: {0, 1}, 2: {2}, 3: {3, 4}},
        set(),
        pytest.approx(0.7071, FLOAT_ERROR_MARGIN),
        "Create cluster at (0.5, 6.3), covering 1 points.",
        True
    )

    assert next(solution) == (
        {0: {0, 1}, 2: {2}, 3: {3, 4}},
        set(),
        pytest.approx(0.7071, FLOAT_ERROR_MARGIN),
        "All points have been clustered, we will now use LP2 to find which clusters to open as centers.",
        True
    )

    assert next(solution) == (
        {0: {0, 1}, 3: {3, 4}},
        set(),
        pytest.approx(1.4142, FLOAT_ERROR_MARGIN),
        "The result of LP2 opens 2 centers with a cost of 1.414. This is at most 2 times the cost of the optimal solution.",
        False
    )
