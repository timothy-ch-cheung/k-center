import functools
import itertools
import math
import time
from typing import Dict, Tuple, Set, List, Iterator

import networkx as nx

from src.kcenter.constant.colour import Colour
from src.kcenter.solver.abstract_solver import AbstractSolver
from src.kcenter.verify.verify import cluster
from src.util.calculation import calculate_combinations


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
        """Find the cost of solving the K-Center problem with a given set of centers.

        :param candidate: list of centers
        :return the maximum cost that a point has to its nearest center
        """
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
        """Create a generator which gives the next candidate to check as a function

        :return a function which executes a single iteration in the brute force algorithm - in other words it tests a
        single candidate.
        """
        candidate_centers: Iterator[List[int]] = itertools.combinations(self.graph.nodes(), self.k)
        while True:
            candidate = next(candidate_centers)
            yield functools.partial(self.find_candidate_cost, candidate)

    def predict_time(self) -> float:
        """Estimate how long it would take to brute force the K-Center problem. Performs trials to get an average of
        how long it make take to test a single candidate.

        :return estimated time to solve in seconds
        """

        def time_check(trials: int):
            iterations = self._iterations()
            start = time.time()
            for i in range(trials):
                candidate_test = next(iterations)
                candidate_test()
            end = time.time()
            duration = end - start
            return duration / trials

        TRIALS = [5, 10, 100]
        time_per_check = 0.0
        for num_trials in TRIALS:
            if num_trials > calculate_combinations(len(self.points), self.k):
                break
            time_per_check = time_check(num_trials)
            if not math.isclose(0, time_per_check):
                break

        combinations = calculate_combinations(len(self.points), self.k)
        return time_per_check * combinations

    def solve(self) -> Tuple[Dict[int, Set[int]], Set[int], float]:
        """Test all candidates that use K centers and return the best solution.

        :return the optimal solution to the K-Center problem
        """
        best_cost = float("inf")
        best_candidate = None
        candidate_centers: Iterator[List[int], None, None] = itertools.combinations(self.graph.nodes(), self.k)
        for candidate in candidate_centers:
            cost = self.find_candidate_cost(candidate)
            if cost < best_cost:
                best_cost = cost
                best_candidate = candidate

        clusters = cluster(self.graph, set(best_candidate), best_cost)
        return clusters, set(), best_cost
