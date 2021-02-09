import functools
import itertools
import time
from typing import Dict, Tuple, Set, List, Iterator

import networkx as nx

from src.kcenter.constant.colour import Colour
from src.kcenter.solver.abstract_solver import AbstractSolver
from src.kcenter.verify.verify import cluster
from util.calculation import calculate_combinations


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

    def find_candidate_cost(self, candidate: List[int]) -> float:
        max_cost = 0.0
        for point in self.graph.nodes():
            min_cost = float("inf")
            for center in candidate:
                cost = self.weights[(point, center)]
                if cost < min_cost:
                    min_cost = cost
            if min_cost > max_cost:
                max_cost = min_cost
        return max_cost

    def _iterations(self):
        candidate_centers: Iterator[List[int]] = itertools.permutations(self.graph.nodes(), self.k)
        while True:
            candidate = next(candidate_centers)
            yield functools.partial(self.find_candidate_cost, candidate)

    def predict_time(self) -> float:
        TRIALS = 10
        iterations = self._iterations()
        total = 0.0
        for i in range(TRIALS):
            candidate_test = next(iterations)
            start = time.time()
            candidate_test()
            duration = time.time() - start
            total += duration
        duration = total/TRIALS
        combinations = calculate_combinations(len(self.points), self.k)
        return duration * combinations

    def solve(self) -> Tuple[Dict[int, Set[int]], Set[int], float]:
        best_cost = float("inf")
        best_candidate = None
        candidate_centers: Iterator[List[int], None, None] = itertools.permutations(self.graph.nodes(), self.k)
        for candidate in candidate_centers:
            cost = self.find_candidate_cost(candidate)
            if cost < best_cost:
                best_cost = cost
                best_candidate = candidate

        clusters = cluster(self.graph, set(best_candidate), best_cost)
        return clusters, set(), best_cost
