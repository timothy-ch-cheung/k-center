import math
import random
from typing import Dict, Tuple, Set

import networkx as nx

from kcenter.brute_force.brute_force_k_center import BruteForceKCenter
from kcenter.constant.colour import Colour
from kcenter.pbs.pbs import Neighbour
from kcenter.solver.abstract_solver import AbstractSolver


class PlateauSurfer(BruteForceKCenter, AbstractSolver):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)
        self.weights = {}
        for i in self.points:
            for j in self.points:
                if i == j:
                    graph.add_edge(i, j, weight=0)
                self.weights[(i, j)] = graph[i][j]["weight"]

    def calc_nearest_centers(self, P: Set[int]):
        nearest_centers = {}
        for point in self.points:
            min_cost = float("inf")
            min_center = None
            for center in P:
                cost = self.weights[(point, center)]

                if cost < min_cost:
                    min_cost = cost
                    min_center = center
            nearest_centers[point] = Neighbour(point=min_center, cost=min_cost)
        return nearest_centers

    def max_delta(self, nearest_centers: Dict[int, Neighbour]):
        max_cost = 0
        delta = 0
        for neighbour in nearest_centers.values():
            if neighbour.cost < max_cost:
                max_cost = neighbour.cost
                delta = 1
            elif math.isclose(neighbour.cost, max_cost):
                delta += 1
        return delta

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
        while True:
            modified = False
            for center in P:
                best_flip = best_cv_flip = None
                best_new_sol_value = self.find_candidate_cost(P)
                best_cv = self.max_delta(self.calc_nearest_centers(P))

                for point in self.points.difference(P):
                    new_P = P.difference({center}).union({point})
                    if (new_cost := self.find_candidate_cost(new_P)) < best_new_sol_value:
                        best_new_sol_value = new_cost
                        best_flip = point
                    elif best_flip is None and (cv := self.max_delta(self.calc_nearest_centers(new_P))) < best_cv:
                        best_cv = cv
                        best_cv_flip = point

                if best_flip is not None:
                    P = P.difference({center}).union({best_flip})
                    modified = True
                elif best_cv_flip is not None:
                    P = P.difference({center}).union({best_cv_flip})
                    modified = True

            if not modified:
                break

        return P

    def solve(self) -> Tuple[Dict[int, Set[int]], Set[int], float]:
        initial_solution = self.randomized_build()
        solution = self.plateau_surf_local_search(initial_solution)
        print(self.find_candidate_cost(solution))
