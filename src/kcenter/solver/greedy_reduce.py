from typing import Dict

from kcenter.solver.greedy import GreedySolver, Colour
import networkx as nx

from kcenter.verify.verify import verify_solution


class GreedyReduceSolver(GreedySolver):
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
