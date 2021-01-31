from typing import Tuple, Dict, Set, Generator

import networkx as nx

from src.kcenter.bandyapadhyay.pseudo_solver import ConstantPseudoColourful
from src.kcenter.bandyapadhyay.stepped_pseudo_solver import SteppedConstantPseudoColourful
from src.kcenter.constant.colour import Colour


class ConstantColourfulSteps:
    DECIMAL_PLACES = 3

    @staticmethod
    def retry_with_k_minus_one(k: int) -> str:
        return f"Our initial run resulted in {k + 1} centers being openend. Since the algorithm produces a solution at most k+1 centers, we re-run the algorithm with k-1 to get a solution opening at most {k} centers"


class SteppedConstantColourful(ConstantPseudoColourful):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    def generator(self) -> Generator[Tuple[Dict[int, Set[int]], Set[int], float, str, bool], None, None]:
        clusters = outliers = radius = label = None
        instance = SteppedConstantPseudoColourful(self.graph, self.k, self.constraints)
        solution = instance.generator()
        for step in solution:
            clusters, outliers, radius, label, active = step
            if not active:
                break
            yield step

        yield clusters, outliers, radius, label, True

        if len(clusters.keys()) > self.k:
            yield clusters, outliers, radius, ConstantColourfulSteps.retry_with_k_minus_one(self.k), True

            instance = SteppedConstantPseudoColourful(self.graph, self.k - 1, self.constraints)
            solution = instance.generator()

            for step in solution:
                yield step
