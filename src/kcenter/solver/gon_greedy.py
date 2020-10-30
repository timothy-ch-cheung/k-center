from typing import Dict, Tuple, Set

import networkx as nx

from src.kcenter.constant.colour import Colour
from src.kcenter.solver.abstract_solver import AbstractSolver
from src.kcenter.verify.verify import verify_solution


class GonGreedy(AbstractSolver):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    def solve(self) -> Tuple[Set[int], Set[Set[int]], int]:
        centers = {0}
        for i in range(1, self.k):
            max_dist = -float("inf")
            max_node = None
            for node in self.graph.nodes():
                for center in centers:
                    if node not in self.graph[center]:
                        continue
                    dist = self.graph[center][node]["weight"]
                    if dist > max_dist:
                        max_dist = dist
                        max_node = node
            centers.add(max_node)

        weights = nx.get_edge_attributes(self.graph, 'weight').values()
        weights = list(set(weights))
        weights = sorted(weights)

        for weight in weights:
            if verify_solution(self.graph, self.constraints, self.k, weight, centers):
                return centers, set(), weight
