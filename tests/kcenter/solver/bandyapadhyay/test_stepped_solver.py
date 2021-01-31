import pytest

from src.kcenter.bandyapadhyay.stepped_solver import SteppedConstantColourful
from src.kcenter.constant.colour import Colour
from tests.kcenter.solver.greedy.test_greedy import FLOAT_ERROR_MARGIN
from tests.kcenter.util.create_test_graph import basic_graph_with_two_outliers


def test_generator_greedy_basic_graph_outlier_colourful_clustering():
    k = 2
    constraints = {Colour.RED: 2, Colour.BLUE: 2}
    graph = basic_graph_with_two_outliers()
    instance = SteppedConstantColourful(graph, k, constraints)
    solution = instance.generator()

    assert next(solution) == (
        {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}, 5: {5}},
        set(),
        0,
        "LP1 is used to find the optimal cost to this problem instance - a solution to LP1 with a given cost means that the cost is valid. A binary search like algorithm is used to search 15 different costs that could potentially be the optimum.",
        True
    )

    assert next(solution) == (
        {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}, 5: {5}},
        set(),
        0,
        "Run LP1 with cost=4.998 - the cost is valid, there exists a solution with this radius. We will check a lower cost in the next step.",
        True
    )

    assert next(solution) == (
        {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}, 5: {5}},
        set(),
        0,
        "Run LP1 with cost=1.4 - the cost is valid, there exists a solution with this radius. We will check a lower cost in the next step.",
        True
    )

    assert next(solution) == (
        {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}, 5: {5}},
        set(),
        0,
        "Run LP1 with cost=0.707 - the cost is valid, there exists a solution with this radius. We will check a lower cost in the next step.",
        True
    )

    assert next(solution) == (
        {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}, 5: {5}},
        set(),
        0,
        "Run LP1 with cost=0.51 - the cost is invalid. We will check a higher cost in the next step.",
        True
    )

    assert next(solution) == (
        {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}, 5: {5}},
        set(),
        0,
        "All weights are exhausted - the minimal feasible cost for LP1 is 0.707 and therefore is the optimal cost. Using this cost we can greedily cluster all points.",
        True
    )

    assert next(solution) == (
        {0: {0, 1, 5}},
        set(),
        pytest.approx(0.7071, FLOAT_ERROR_MARGIN),
        "Create cluster at 0, covering 3 points.",
        True
    )

    assert next(solution) == (
        {0: {0, 1, 5}, 3: {3, 4}},
        set(),
        pytest.approx(0.7071, FLOAT_ERROR_MARGIN),
        "Create cluster at 3, covering 2 points.",
        True
    )

    assert next(solution) == (
        {0: {0, 1, 5}, 2: {2}, 3: {3, 4}},
        set(),
        pytest.approx(0.7071, FLOAT_ERROR_MARGIN),
        "Create cluster at 2, covering 1 points.",
        True
    )

    assert next(solution) == (
        {0: {0, 1, 5}, 2: {2}, 3: {3, 4}},
        set(),
        pytest.approx(0.7071, FLOAT_ERROR_MARGIN),
        "All points have been clustered, we will now use LP2 to find which clusters to open as centers.",
        True
    )

    assert next(solution) == (
        {0: {0, 1, 5}, 2: {2}, 3: {3, 4}},
        set(),
        pytest.approx(1.4142, FLOAT_ERROR_MARGIN),
        "The result of LP2 opens 3 centers with a cost of 1.414. This is at most 2 times the cost of the optimal solution. Note that to meet the 2-approximation we have opened 3 instead of 2.",
        True
    )

    assert next(solution) == (
        {0: {0, 1, 5}, 2: {2}, 3: {3, 4}},
        set(),
        pytest.approx(1.4142, FLOAT_ERROR_MARGIN),
        "Our initial run resulted in 3 centers being openend. Since the algorithm produces a solution at most k+1 centers, we re-run the algorithm with k-1 to get a solution opening at most 2 centers",
        True
    )

    assert next(solution) == (
        {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}, 5: {5}},
        set(),
        0,
        "LP1 is used to find the optimal cost to this problem instance - a solution to LP1 with a given cost means that the cost is valid. A binary search like algorithm is used to search 15 different costs that could potentially be the optimum.",
        True
    )

    assert next(solution) == (
        {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}, 5: {5}},
        set(),
        0,
        "Run LP1 with cost=4.998 - the cost is valid, there exists a solution with this radius. We will check a lower cost in the next step.",
        True
    )

    assert next(solution) == (
        {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}, 5: {5}},
        set(),
        0,
        "Run LP1 with cost=1.4 - the cost is invalid. We will check a higher cost in the next step.",
        True
    )

    assert next(solution) == (
        {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}, 5: {5}},
        set(),
        0,
        "Run LP1 with cost=3.785 - the cost is invalid. We will check a higher cost in the next step.",
        True
    )

    assert next(solution) == (
        {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}, 5: {5}},
        set(),
        0,
        "Run LP1 with cost=4.258 - the cost is invalid. We will check a higher cost in the next step.",
        True
    )

    assert next(solution) == (
        {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}, 5: {5}},
        set(),
        0,
        "All weights are exhausted - the minimal feasible cost for LP1 is 4.998 and therefore is the optimal cost. Using this cost we can greedily cluster all points.",
        True
    )

    assert next(solution) == (
        {0: {0, 1, 2, 3, 4, 5}},
        set(),
        pytest.approx(4.9979, FLOAT_ERROR_MARGIN),
        "Create cluster at 0, covering 6 points.",
        True
    )

    assert next(solution) == (
        {0: {0, 1, 2, 3, 4, 5}},
        set(),
        pytest.approx(4.997, FLOAT_ERROR_MARGIN),
        "All points have been clustered, we will now use LP2 to find which clusters to open as centers.",
        True
    )

    assert next(solution) == (
        {0: {0, 1, 2, 3, 4, 5}},
        set(),
        pytest.approx(9.995, FLOAT_ERROR_MARGIN),
        "The result of LP2 opens 1 centers with a cost of 9.996. This is at most 2 times the cost of the optimal solution.",
        False
    )
