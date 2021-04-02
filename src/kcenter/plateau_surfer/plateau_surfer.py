import math
import random
from typing import Dict, Tuple, Set

import networkx as nx

from kcenter.brute_force.brute_force_k_center import BruteForceKCenter
from kcenter.constant.colour import Colour
from kcenter.pbs.pbs import Neighbour
from kcenter.solver.abstract_solver import AbstractSolver
from kcenter.verify.verify import cluster


class PlateauSurfer(BruteForceKCenter, AbstractSolver):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int] = None, alpha: float = 0.25, beta: float = 0.5):
        super().__init__(graph, k, constraints)
        self.weights = {}
        self.points = set(graph.nodes())
        for i in self.points:
            for j in self.points:
                if i == j:
                    graph.add_edge(i, j, weight=0)
                self.weights[(i, j)] = graph[i][j]["weight"]

        if constraints is None:
            self.constraints = {Colour.BLUE: 0, Colour.RED: 0}
        self.alpha = alpha
        self.beta = beta

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

    def max_delta(self, nearest_centers: Dict[int, Neighbour], cost: float):
        critical_vertices = [x for x in nearest_centers.values() if math.isclose(x.cost, cost)]
        return len(critical_vertices)

    def randomized_build(self):
        P = set()
        num_initial = 0 if self.alpha == 0 else random.randint(1, math.ceil(self.k * self.alpha))
        greedy_costs = {i: 0 for i in self.points}
        for i in range(num_initial):
            f = random.choice(tuple(self.points.difference(P)))
            P.add(f)

        nearest_centers = self.calc_nearest_centers(P)
        while len(P) < self.k:
            z_min = float("inf")
            z_max = float("-inf")
            for i in self.points.difference(P):
                P = self.add_center(nearest_centers, P, i)
                cost = self.find_cost(nearest_centers)
                greedy_costs[i] = cost
                if z_min > cost:
                    z_min = cost
                if z_max < cost:
                    z_max = cost
                P = self.remove_center(nearest_centers, P, i)
            mu = z_min + self.beta * (z_max - z_min)
            RCL = [i for i in self.points.difference(P) if greedy_costs[i] <= mu]
            P.add(random.choice(RCL))
        return P

    def add_center(self, nearest_centers: Dict[int, Neighbour], P: Set[int], center: int):
        for p in self.points:
            cost = self.weights[(p, center)]
            if cost < nearest_centers[p].cost:
                nearest_centers[p] = Neighbour(point=center, cost=cost)
        return P.union({center})

    def find_next(self, point: int, P:Set[int]):
        min_center = None
        min_center_cost = float("inf")

        for center in P:
            cost = self.weights[(center, point)]
            if cost < min_center_cost:
                min_center = center
                min_center_cost = cost

        return Neighbour(point=min_center, cost=min_center_cost)


    def remove_center(self, nearest_centers: Dict[int, Neighbour], P: Set[int], center: int):
        P = P.difference({center})
        for p in self.points:
            if nearest_centers[p].point == center:
                nearest_centers[p] = self.find_next(p, P)
        return P

    def find_cost(self, nearest_centers: Dict[int, Neighbour]):
        return max(nearest_centers.values(), key=lambda x: x.cost).cost

    def plateau_surf_local_search(self, P: Set[int]):
        nearest_centers = self.calc_nearest_centers(P)

        while True:
            modified = False
            for center in P:
                best_flip = best_cv_flip = None
                best_new_sol_value = self.find_cost(nearest_centers)
                best_cv = self.max_delta(nearest_centers, best_new_sol_value)

                P = self.remove_center(nearest_centers, P, center)
                for point in self.points.difference(P).difference({center}):
                    P = self.add_center(nearest_centers, P, point)
                    if new_cost := self.find_cost(nearest_centers) < best_new_sol_value:
                        best_new_sol_value = new_cost
                        best_flip = point
                    elif best_flip is None and math.isclose(new_cost, best_new_sol_value) and (
                            cv := self.max_delta(nearest_centers, new_cost)) < best_cv:
                        # likely mistake in algorithm in paper for not ensuring new_cost=best_new_sol_value
                        best_cv = cv
                        best_cv_flip = point

                    P = self.remove_center(nearest_centers, P, point)

                if best_flip is not None:
                    P = self.add_center(nearest_centers, P, best_flip)
                    modified = True
                elif best_cv_flip is not None:
                    P = self.add_center(nearest_centers, P, best_cv_flip)
                    modified = True
                else:
                    P = self.add_center(nearest_centers, P, center)
            if not modified:
                break

        return P

    def solve(self, iterations=10) -> Tuple[Dict[int, Set[int]], Set[int], float]:
        best_cost = float("inf")
        best_cluster = None
        for i in range(iterations):
            initial_solution = self.randomized_build()
            solution = self.plateau_surf_local_search(initial_solution)
            cost = self.find_candidate_cost(solution)

            if cost < best_cost:
                best_cost = cost
                best_cluster = cluster(self.graph, solution, cost)
        return best_cluster, set(), best_cost
