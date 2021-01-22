import math
import numpy as np

root_two = math.sqrt(2)


def normalise(S, graph, min_value, max_value):
    def tup_diff(a, b):
        return a[0] - b[0], a[1] - b[1]

    def tup_div(a, b):
        return a[0] / (b[0] if b[0] != 0 else 1), a[1] / (b[1] if b[1] != 0 else 1)

    def apply_normalise(s):
        return {tup_div(tup_diff(graph.nodes()[x]["pos"], min_value), tup_diff(max_value, min_value)) for x in s}

    S = apply_normalise(S)
    return S


def sim(A, B, graph, min_value, max_value):
    A = normalise(A, graph, min_value, max_value)
    B = normalise(B, graph, min_value, max_value)

    score = 0
    for x in A:
        min_center = None
        min_dist = float("inf")
        for y in B:
            d = np.linalg.norm(np.array(x) - np.array(y))
            if d < min_dist:
                min_center = y
                min_dist = d
        B.remove(min_center)
        score += min_dist
    return score / (len(A) * root_two)
