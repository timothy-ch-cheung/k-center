from typing import Dict, Generator, Tuple, Set

import networkx as nx

from src.kcenter.constant.colour import Colour
from src.kcenter.greedy.greedy_reduce import GreedyReduce
from src.kcenter.greedy.stepped_greedy import SteppedGreedy
from src.kcenter.verify.verify import verify_solution


class GreedyReduceSteps:
    DECIMAL_PLACES = 3

    @staticmethod
    def intermediate_cost(cost: float, k: int) -> str:
        cost = round(cost, GreedyReduceSteps.DECIMAL_PLACES)
        num_centers_label = f"{k} centers have" if k > 1 else "single center has"
        return f"Our {num_centers_label} been chosen. The current cost is {cost}, we will continue to reduce the cost until the solution does not meet the constraints."

class SteppedGreedyReduce(GreedyReduce, SteppedGreedy):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    def generator(self) -> Generator[Tuple[Dict[int, Set[int]], int, str], None, None]:
        clusters = outliers = radius = label = active = None
        solution = super().generator()
        clusters, radius = {}, float("inf")
        for step in solution:
            clusters, outliers, radius, label, active = step
            if not active:
                break
            yield clusters, outliers, radius, label

        yield clusters, outliers, radius, GreedyReduceSteps.intermediate_cost(radius, self.k)

        weights = GreedyReduce.get_weights(self.graph, radius)

        new_weight = None
        centers = set(clusters.keys())
        for weight in weights:
            if verify_solution(self.graph, self.constraints, self.k, weight, centers):
                new_weight = weight
                yield clusters, set(), new_weight, f"decrease weight to {round(new_weight, 3)}"
            else:
                break

        radius = new_weight if new_weight is not None else radius
        yield clusters, set(), radius, f"completed reduced solution to radius of {round(radius, 3)}"
