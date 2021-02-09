import functools
import itertools
from typing import Dict, Tuple, Set, List, Iterator

import networkx as nx

from src.kcenter.brute_force.brute_force_k_center import BruteForceKCenter
from src.kcenter.constant.colour import Colour


class BruteForceColourfulKCenter(BruteForceKCenter):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)
        self.costs = sorted(list(set(nx.get_edge_attributes(self.graph, "weight").values())))

    def check_candidate(self, candidate: List[int], candidate_cost: float) -> bool:
        total = {Colour.BLUE: 0, Colour.RED: 0}
        for point in self.graph.nodes():
            for center in candidate:
                if self.weights[(point, center)] <= candidate_cost:
                    total[self.graph.nodes()[point]["colour"]] += 1
                    break

        if total[Colour.BLUE] >= self.constraints[Colour.BLUE] and total[Colour.RED] >= self.constraints[Colour.RED]:
            return True
        else:
            return False

    def _iterations(self):
        """Create a generator which gives the next candidate to check as a function

        :return a function which executes a single iteration in the brute force algorithm - in other words it tests a
        single candidate.
        """
        candidate_centers: Iterator[List[int]] = itertools.combinations(self.graph.nodes(), self.k)
        while True:
            candidate = next(candidate_centers)
            yield functools.partial(self.check_candidate, candidate, self.costs[0])

    def predict_time(self) -> float:
        time = super().predict_time()
        return time * len(self.costs)

    def find_solution(self) -> Tuple[List[int], float]:
        """Brute force all center set candidates and cost candidates in order of cost ascending.

        :return the centers of the optimal solution to the Colourful K-Center problem
        """
        for candidate_cost in self.costs:
            candidate_centers: Iterator[List[int]] = itertools.combinations(self.graph.nodes(), self.k)
            for candidate in candidate_centers:
                valid = self.check_candidate(candidate, candidate_cost)
                if valid:
                    return candidate, candidate_cost

    def solve(self) -> Tuple[Dict[int, Set[int]], Set[int], float]:
        """Brute force all candidates for the Colourful K-Center problem

        :return the optimal solution to the K-Center problem
        """
        centers, cost = self.find_solution()
        clusters = {center: set() for center in centers}
        outliers = set()

        for point in self.points:
            min_dist = float("inf")
            nearest_center = None
            for center in centers:
                if point == center:
                    nearest_center = center
                    break
                point_cost = self.weights[(point, center)]
                if point_cost <= min_dist and point_cost <= cost:
                    min_dist = cost
                    nearest_center = center
            if nearest_center is not None:
                clusters[nearest_center].add(point)
            else:
                outliers.add(point)
        return clusters, outliers, cost
