from typing import Tuple, Set


def sum_coord(coord_a: Tuple[float, float], coord_b: Tuple[float, float]) -> Tuple[float, float]:
    return coord_a[0] + coord_b[0], coord_a[1] + coord_b[1]


def minkowski_sum(a: Set[Tuple[float, float]], b: Set[Tuple[float, float]]):
    summed_set = set()
    for coord_a in a:
        for coord_b in b:
            summed_set.add(sum_coord(coord_a, coord_b))
    return summed_set


set_a = {(1, 0), (0, 1), (0, -1)}
set_b = {(0, 0), (1, 1), (1, -1)}

sum = minkowski_sum(set_a, set_b)
print(sum)
assert sum == {(1, 0), (2, 1), (2, -1), (0, 1), (1, 2), (1, 0), (0, -1), (1, 0), (1, -2)}
