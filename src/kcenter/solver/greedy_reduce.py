from typing import Dict

import networkx as nx

from src.kcenter.solver.greedy import GreedySolver, Colour
from src.kcenter.verify.verify import verify_solution


class GreedyReduceSolver(GreedySolver):
    """Colorful K-Center solver that uses a greedy heuristic and minimizes the cost based on
    the colour constraints.

            Calls GreedySolver to get an initial solution. Then attempts to reduce the radius
            by trying  lower radii and checking if the constraints are still satisfied".
            """

    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    def solve(self):
        clusters, radius = super().solve()
        weights = sorted(list(nx.get_edge_attributes(self.graph, "weight").values()), reverse=True)

        new_weight = None
        centers = set(clusters.keys())
        for weight in weights:
            if weight < radius and verify_solution(self.graph, self.constraints, self.k, weight, centers) is True:
                new_weight = weight

        radius = new_weight if new_weight is not None else radius
        return clusters, radius
