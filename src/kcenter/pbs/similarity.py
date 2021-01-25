import math
from typing import Tuple, Set

import numpy as np
import networkx as nx


class CompareSolution:
    ROOT_TWO = math.sqrt(2)

    def __init__(self, graph: nx, min_value: Tuple[float, float], max_value: Tuple[float, float]):
        self.graph = graph
        self.min_value = min_value
        self.max_value = max_value

    def normalise(self, S: Set[int]):
        def tup_diff(a: Tuple[float, float], b: Tuple[float, float]):
            return a[0] - b[0], a[1] - b[1]

        def tup_div(a: Tuple[float, float], b: Tuple[float, float]):
            return a[0] / (b[0] if b[0] != 0 else 1), a[1] / (b[1] if b[1] != 0 else 1)

        def apply_normalise(s: Set[int]):
            return {tup_div(tup_diff(self.graph.nodes()[x]["pos"], self.min_value),
                            tup_diff(self.max_value, self.min_value)) for x in s}

        S = apply_normalise(S)
        return S

    def sim(self, A: Set[int], B: Set[int]):
        A = self.normalise(A)
        B = self.normalise(B)

        min_distances = []
        for x in A:
            min_dist = float("inf")
            for y in B:
                d = np.linalg.norm(np.array(x) - np.array(y))
                if d < min_dist:
                    min_dist = d
            min_distances.append(min_dist)
        return max(min_distances)/CompareSolution.ROOT_TWO
