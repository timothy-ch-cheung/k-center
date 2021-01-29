from typing import Dict, Tuple, Set

import networkx as nx

from src.kcenter.constant.colour import Colour
from src.kcenter.bandyapadhyay.pseudo_solver import ConstantPseudoColourfulKCenter


class ConstantColourfulKCenter(ConstantPseudoColourfulKCenter):
    """Implementation based on the algorithm by Bandyapadhyay et al. from
    'A Constant Approximation for Colorful k-Center (2019)'

    produces a pseudo approximation which opens at most k centers with a 17-approximation
    """

    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    def get_potential_centers(self, lp_solution) -> Set[int]:
        return {point for point, sol in lp_solution.items() if sol['x'] > 0}

    def calc_min_dist(self, potential_centers: Set[int]):
        min_dist = float("inf")
        for i in potential_centers:
            for j in potential_centers.difference({i}):
                dist = self.graph[i][j]["weight"]
                if dist < min_dist:
                    min_dist = dist
        return min_dist

    def solve(self) -> Tuple[Dict[int, Set[int]], Set[int], int]:
        """Solves the Colourful K-Center problem using the algorithm created by Bandyapadhyay et al.

        Uses subroutines radius_checker (LP1 Section 2 figure 1), clustering (Section 2 Algorithm 1) and red_maximiser
        (LP2 Section 2.1 figure 2).
        """
        solver = ConstantPseudoColourfulKCenter(self.graph, self.k, self.constraints)
        clusters, outliers, radius = solver.solve()
        if len(clusters.keys()) > self.k:
            solver = ConstantPseudoColourfulKCenter(self.graph, self.k - 1, self.constraints)
            return solver.solve()
        return clusters, outliers, radius
