import math
import random
import time
from typing import Dict, Tuple, Set, List, Optional

import networkx as nx

from src.kcenter.brute_force.brute_force_k_center import BruteForceKCenter
from src.kcenter.constant.colour import Colour
from src.kcenter.solver.abstract_solver import AbstractSolver
from src.kcenter.verify.verify import cluster
from src.util.logger import Logger


class PlateauSurfer(BruteForceKCenter, AbstractSolver):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int] = None, alpha: float = 0.25,
                 beta: float = 0.5):
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
        nearest_centers: List[int] = [0 for p in range(len(self.points) + 1)]
        nearest_costs: List[float] = [0 for p in range(len(self.points) + 1)]
        for point in self.points:
            min_cost = float("inf")
            min_center = None
            for center in P:
                cost = self.weights[(point, center)]

                if cost < min_cost:
                    min_cost = cost
                    min_center = center
            nearest_centers[point] = min_center
            nearest_costs[point] = min_cost
        return nearest_centers, nearest_costs

    def add_center(self, nearest_centers: List[int], nearest_costs: List[float], P: Set[int], center: int):
        for p in self.points:
            cost = self.weights[(p, center)]
            if cost < nearest_costs[p]:
                nearest_centers[p] = center
                nearest_costs[p] = cost
        return P.union({center})

    def find_next(self, point: int, P: Set[int]):
        min_center = None
        min_center_cost = float("inf")

        for center in P:
            cost = self.weights[(center, point)]
            if cost < min_center_cost:
                min_center = center
                min_center_cost = cost

        return min_center, min_center_cost

    def remove_center(self, nearest_centers: List[int], nearest_costs: List[float], P: Set[int], center: int):
        P = P.difference({center})
        for p in self.points:
            if nearest_centers[p] == center:
                min_center, min_center_cost = self.find_next(p, P)
                nearest_centers[p] = min_center
                nearest_costs[p] = min_center_cost
        return P

    def max_delta(self, nearest_costs: List[float], cost: float):
        critical_vertices = [x for x in nearest_costs if math.isclose(x, cost)]
        return len(critical_vertices)

    def find_cost(self, nearest_costs: List[float]):
        return max(nearest_costs)

    def randomized_build(self):
        P = set()
        num_initial = 0 if self.alpha == 0 else random.randint(1, math.ceil(self.k * self.alpha))
        greedy_costs = {i: 0 for i in self.points}
        for i in range(num_initial):
            f = random.choice(tuple(self.points.difference(P)))
            P.add(f)

        nearest_centers, nearest_costs = self.calc_nearest_centers(P)
        while len(P) < self.k:
            z_min = float("inf")
            z_max = float("-inf")
            for i in self.points.difference(P):
                P = self.add_center(nearest_centers, nearest_costs, P, i)
                cost = self.find_cost(nearest_costs)
                greedy_costs[i] = cost
                if z_min > cost:
                    z_min = cost
                if z_max < cost:
                    z_max = cost
                P = self.remove_center(nearest_centers, nearest_costs, P, i)
            mu = z_min + self.beta * (z_max - z_min)
            RCL = [i for i in self.points.difference(P) if greedy_costs[i] <= mu]
            P.add(random.choice(RCL))
        return P

    def plateau_surf_local_search(self, P: Set[int]):
        nearest_centers, nearest_costs = self.calc_nearest_centers(P)

        while True:
            modified = False
            for center in P:
                best_flip = best_cv_flip = None
                best_new_sol_value = self.find_cost(nearest_costs)
                best_cv = self.max_delta(nearest_costs, best_new_sol_value)

                P = self.remove_center(nearest_centers, nearest_costs, P, center)
                for point in self.points.difference(P).difference({center}):
                    P = self.add_center(nearest_centers, nearest_costs, P, point)
                    if new_cost := self.find_cost(nearest_costs) < best_new_sol_value:
                        best_new_sol_value = new_cost
                        best_flip = point
                    elif best_flip is None and math.isclose(new_cost, best_new_sol_value) and (
                            cv := self.max_delta(nearest_centers, new_cost)) < best_cv:
                        # likely mistake in algorithm in paper for not ensuring new_cost=best_new_sol_value
                        best_cv = cv
                        best_cv_flip = point

                    P = self.remove_center(nearest_centers, nearest_costs, P, point)

                if best_flip is not None:
                    P = self.add_center(nearest_centers, nearest_costs, P, best_flip)
                    modified = True
                elif best_cv_flip is not None:
                    P = self.add_center(nearest_centers, nearest_costs, P, best_cv_flip)
                    modified = True
                else:
                    P = self.add_center(nearest_centers, nearest_costs, P, center)
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

    def target_solve(self, target_cost: float, timeout: Optional[float] = None, log: bool = False) -> Tuple[
        Dict[int, Set[int]], Set[int], float]:

        start_time = time.time()
        logger = Logger("grasp", len(self.points), self.k, start_time)
        best_cost = self.MAX_WEIGHT
        best_solution = None

        while True:
            initial_solution = self.randomized_build()
            solution = self.plateau_surf_local_search(initial_solution)
            cost = self.find_candidate_cost(solution)

            if cost < best_cost:
                best_cost = cost
                best_solution = solution
                if log is True:
                    logger.append(best_cost)

            if math.isclose(cost, target_cost) or cost < target_cost or time.time() - start_time > timeout:
                break

        logger.dump()
        best_cluster = cluster(self.graph, best_solution, best_cost)
        return best_cluster, set(), best_cost
