import itertools
from typing import Dict, Tuple, Set

import networkx as nx

from kcenter.constant.colour import Colour
from kcenter.solver.abstract_solver import AbstractSolver
from kcenter.verify.verify import cluster


class BruteForceKCenter(AbstractSolver):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        self.points = set(graph.nodes())
        self.weights = {}
        for i in self.points:
            for j in self.points:
                if i == j:
                    graph.add_edge(i, j, weight=0)
                self.weights[(i, j)] = graph[i][j]["weight"]
        self.MAX_WEIGHT = max(nx.get_edge_attributes(graph, "weight").values())
        super().__init__(graph, k, constraints)

    def solve(self) -> Tuple[Dict[int, Set[int]], Set[int], float]:
        best_cost = float("inf")
        best_candidate = None
        candidate_centers = list(itertools.permutations(self.graph.nodes(), self.k))
        for candidate in candidate_centers:
            max_cost = 0
            for point in self.graph.nodes():
                min_cost = float("inf")
                for center in candidate:
                    cost = self.weights[(point, center)]
                    if cost < min_cost:
                        min_cost = cost
                if min_cost > max_cost:
                    max_cost = min_cost
            if max_cost < best_cost:
                best_cost = max_cost
                best_candidate = candidate

        clusters = cluster(self.graph, best_candidate, best_cost)
        return clusters, set(), best_cost
