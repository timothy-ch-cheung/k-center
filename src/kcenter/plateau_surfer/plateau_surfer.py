import random
from typing import Dict, Tuple, Set

import networkx as nx

from kcenter.brute_force.brute_force_k_center import BruteForceKCenter
from kcenter.constant.colour import Colour
from kcenter.solver.abstract_solver import AbstractSolver


class PlateauSurfer(BruteForceKCenter, AbstractSolver):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    def randomized_build(self, alpha: float = 1.0, beta: float = 0.1):
        P = set()
        num_initial = random.randint(0, round(self.k * alpha))
        greedy_costs = {i: 0 for i in self.points}
        for i in range(num_initial):
            f = random.choice(tuple(self.points.difference(P)))
            P.add(f)
        while len(P) < self.k:
            z_min = float("inf")
            z_max = float("-inf")
            for i in self.points.difference(P):
                cost = self.find_candidate_cost(P.union({i}))
                greedy_costs[i] = cost
                if z_min > self.find_candidate_cost(P.union({i})):
                    z_min = cost
                if z_max < cost:
                    z_max = cost
            mu = z_min + beta * (z_max - z_min)
            RCL = [i for i in self.points if greedy_costs[i] <= mu]
            P.add(random.choice(RCL))
        return P

    def plateau_surf_local_search(self, P: Set[int]):

    def solve(self) -> Tuple[Dict[int, Set[int]], Set[int], float]:
        initial_solution = self.randomized_build()
        print(self.find_candidate_cost(initial_solution))
