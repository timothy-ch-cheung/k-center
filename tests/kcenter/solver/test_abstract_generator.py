from kcenter.solver.abstract_generator import Solution

sol = Solution(clusters={1: {1, 2}, 3: {3, 4}}, outliers={5}, cost=1.5)


def test_solution_equality():
    assert sol == Solution(clusters={1: {1, 2}, 3: {3, 4}}, outliers={5}, cost=1.5)


def test_solution_inequality():
    assert sol != Solution(clusters={})


def test_solution_inequality_type():
    assert sol != float("inf")


def test_solution_to_str():
    assert str(sol) == "clusters: {1: {1, 2}, 3: {3, 4}}, cost: 1.5, outliers: {5}"
