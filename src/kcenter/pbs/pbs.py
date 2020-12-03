import random
from bisect import bisect_left
from typing import Tuple, Dict, Set, Generator, List

import networkx as nx

from kcenter.constant.colour import Colour
from kcenter.solver.abstract_solver import AbstractSolver


class Neighbour:
    def __init__(self, point: int, cost: float):
        self.point = point
        self.cost = cost


class Individual:
    def __init__(self, centers: Set[int]):
        self.centers = centers
        self.cost = 0
        self.nearest_centers = {}

    def init_nearest_centers(self, graph: nx.Graph):
        points = list(graph.nodes())
        for point in points:
            nearest_center = None
            second_nearest_center = None
            for center in self.centers:
                if center == point:
                    continue

                if nearest_center is None:
                    nearest_center = Neighbour(point=center, cost=graph[point][center]["weight"])
                elif graph[point][center]["weight"] <= nearest_center.cost:
                    second_nearest_center = nearest_center
                    nearest_center = Neighbour(point=center, cost=graph[point][center]["weight"])
                elif second_nearest_center is None:
                    second_nearest_center = Neighbour(point=center, cost=graph[point][center]["weight"])
                elif graph[point][center]["weight"] <= second_nearest_center.cost:
                    Neighbour(point=center, cost=graph[point][center]["weight"])

            if point in self.centers:
                second_nearest_center = nearest_center
                nearest_center = Neighbour(point=point, cost=0)

            self.nearest_centers[point] = {
                "nearest_center": nearest_center, "second_nearest_center": second_nearest_center
            }


class PBS(AbstractSolver):
    POPULATION_SIZE = 8

    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)
        self.points = set(graph.nodes())
        PBS.order_edges(self.graph)

    @staticmethod
    def order_edges(graph: nx.Graph):
        points = list(graph.nodes())
        for point in points:
            neighbours = [adj for (_, adj) in graph.edges(point)]
            neighbours = [point] + sorted(neighbours, key=lambda x: graph[point][x]["weight"])
            graph.nodes()[point]["neighbours"] = neighbours

    @staticmethod
    def binary_search(array: List[int], target: int):
        i = bisect_left(array, target)
        if i != len(array) and array[i] == target:
            return i
        else:
            return -1

    @staticmethod
    def get_nwk(graph: nx.Graph, w: int, k: int):
        nw = graph.nodes()[w]["neighbours"]
        k_index = PBS.binary_search(nw, k)
        return nw[:k_index]

    def add_center(self, center: int, individual: Individual):
        max_center_cost = 0
        individual.centers.add(center)
        for p in self.points:
            if self.graph[p][center] < individual.nearest_centers[p]["nearest_center"].cost:
                individual.nearest_centers[p]["second_nearest_center"] = individual.nearest_centers[p]["nearest_center"]
                individual.nearest_centers[p]["nearest_center"] = Neighbour(point=center,
                                                                            cost=self.graph[p][center]["weight"])
            elif self.graph[p][center] < individual.nearest_centers[p]["second_nearest_center"].cost:
                individual.nearest_centers[p]["second_nearest_center"] = Neighbour(point=center,
                                                                                   cost=self.graph[p][center]["weight"])

            if individual.nearest_centers[p]["nearest_center"].cost > max_center_cost:
                max_center_cost = individual.nearest_centers[p]["nearest_center"].cost

    def find_next(self, point: int, individual: Individual):
        closest = individual.nearest_centers[point].point
        min_center_cost = float("inf")
        min_center = None
        for center in individual.centers:
            if center == closest:
                continue
            if min_center_cost > self.graph[point][center]["weight"]:
                min_center_cost = self.graph[point][center]["weight"]
                min_center = center
        return Neighbour(min_center, min_center_cost)

    def remove_center(self, center: int, individual: Individual):
        max_center_cost = 0
        individual.centers.remove(center)

        for p in self.points:
            if individual.nearest_centers[p]["nearest_center"].point == center:
                individual.nearest_centers[p]["nearest_center"] = individual.nearest_centers[p]["second_nearest_center"]
                individual.nearest_centers[p]["second_nearest_center"] = self.find_next(p, individual)
            elif individual.nearest_centers[p]["second_nearest_center"].point == center:
                individual.nearest_centers[p]["second_nearest_center"] = self.find_next(p, individual)

            if individual.nearest_centers[p]["nearest_center"].cost > max_center_cost:
                max_center_cost = individual.nearest_centers[p]["nearest_center"].cost

    def find_pair(self, w: int, individual: Individual):
        C = max(nx.get_edge_attributes(self.graph, "weight").values())
        L = set()
        furthest_point_facility = individual.nearest_centers[w]["nearest_center"]
        nwk = PBS.get_nwk(self.graph, w, furthest_point_facility.point)
        for i in nwk:
            self.add_center(i, individual)
            M = {}
            for center in individual.centers:
                M[center] = 0
            for point in self.points:
                second_nearest = individual.nearest_centers[point]["second_nearest_center"]
                nearest = individual.nearest_centers[point]["nearest_center"]

                min_dist = min(self.graph[i][point]["weight"], second_nearest.cost)
                if min_dist > M[nearest.point]:
                    M[nearest.point] = min_dist

            for center in individual.centers:
                if M[center] == C:
                    L.add((center, i))
                elif M[center] < C:
                    L = {(center, i)}
                    C = M[center]
            self.remove_center(i, individual)
        return random.choice(tuple(L))

    def get_furthest_point(self, individual: Individual):
        return max(self.points,
                   key=lambda x: 0
                   if individual.nearest_centers[x]["nearest_center"] is None
                   else individual.nearest_centers[x]["nearest_center"].cost
                   )

    def local_search(self, individual: Individual, generation: int):
        while len(individual.centers) < self.k:
            furthest_point = self.get_furthest_point(individual)
            furthest_point_facility = individual.nearest_centers[furthest_point]["nearest_center"]
            nwk = PBS.get_nwk(self.graph, furthest_point, furthest_point_facility.point)
            new_center = random.choice(nwk)
            self.add_center(new_center, individual)

        termination_iterations_cost = 0.1 * (generation + 1) * self.graph.number_of_nodes()
        termination_iterations_count = 2 * self.graph.number_of_nodes()
        iteration = 0
        while iteration < termination_iterations_cost and iteration < termination_iterations_count:
            furthest_point = self.get_furthest_point(individual)
            point_to_remove, point_to_add = self.find_pair(furthest_point, individual)
            self.remove_center(point_to_remove, individual)
            self.add_center(point_to_add, individual)

    def generator(self) -> Generator[Tuple[Dict[int, Set[int]], int, str], None, None]:
        pass

    def solve(self) -> Tuple[Dict[int, Set[int]], Set[int], float]:
        population = []
        for i in range(PBS.POPULATION_SIZE):
            init_center = {random.choice(tuple(self.points))}
            individual = Individual(init_center)
            individual.init_nearest_centers(self.graph)
            population.append(individual)

        for individual in population:
            self.local_search(individual)

        clusters = {}
        for center in population[-1].centers:
            clusters[center] = set()
        return clusters, set(), 0
