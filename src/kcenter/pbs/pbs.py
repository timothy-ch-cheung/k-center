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
    def __init__(self, centers: Set[int], cost=0, nearest_centers={}):
        self.centers = centers
        self.cost = cost
        self.nearest_centers = nearest_centers

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

    def copy(self):
        return Individual(centers=self.centers, cost=self.cost, nearest_centers=self.nearest_centers)


class PBS(AbstractSolver):
    POPULATION_SIZE = 8
    GENERATIONS = 10

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

        optimised_individual = individual.copy()
        while iteration < termination_iterations_cost and iteration < termination_iterations_count:
            furthest_point = self.get_furthest_point(optimised_individual)
            point_to_remove, point_to_add = self.find_pair(furthest_point, optimised_individual)
            self.remove_center(point_to_remove, optimised_individual)
            self.add_center(point_to_add, optimised_individual)
        furthest_point = self.get_furthest_point(individual)
        optimised_individual.cost = optimised_individual.nearest_centers[furthest_point]["nearest_center"].cost
        return optimised_individual

    def mutation_random(self, individual: Individual):
        q = random.randint(self.k // 2, self.k)
        other_points = self.points.difference(individual.centers)
        retained_centers = random.sample(individual.centers, q)
        new_centers = random.sample(other_points, self.k - q)
        child_solution = Individual(centers=set(retained_centers + new_centers))
        child_solution.init_nearest_centers(self.graph)
        furthest_point = self.get_furthest_point(child_solution)
        child_solution.cost = child_solution.nearest_centers[furthest_point]["nearest_center"].cost
        return child_solution

    def mutation_directed(self, individual: Individual):
        closest_centers = None
        closest_distance = float("inf")
        for center in individual.centers:
            for other_center in individual.centers.difference(center):
                if self.graph[center][other_center]["weight"] < closest_distance:
                    closest_distance = self.graph[center][other_center]["weight"]
                    closest_centers = (center, other_center)
        new_centers = individual.centers.difference(closest_centers)
        child_solution = Individual(centers=new_centers)
        child_solution.init_nearest_centers(self.graph)
        furthest_point = self.get_furthest_point(child_solution)
        child_solution.cost = child_solution.nearest_centers[furthest_point]["nearest_center"].cost
        return child_solution

    def crossover_random(self, first_parent: Individual, second_parent: Individual):
        new_centers = random.sample(first_parent.centers.union(second_parent.centers), self.k)
        child_solution = Individual(centers=new_centers)
        child_solution.init_nearest_centers(self.graph)
        furthest_point = self.get_furthest_point(child_solution)
        child_solution.cost = child_solution.nearest_centers[furthest_point]["nearest_center"].cost
        return child_solution

    def crossover_directed(self, first_parent: Individual, second_parent: Individual, generation: int):
        def generate_child(pbs: PBS, centers: Set[int]):
            child = Individual(centers=centers)
            if len(child.centers) > pbs.k:
                child.centers = set(random.sample(child.centers, pbs.k))
                child.init_nearest_centers(pbs.graph)
            elif len(child.centers) < pbs.k:
                child.init_nearest_centers(pbs.graph)
                pbs.local_search(child, generation)
            else:
                child.init_nearest_centers(pbs.graph)
            furthest_point = self.get_furthest_point(child)
            child.cost = child.nearest_centers[furthest_point]["nearest_center"].cost
            return child

        INTERVAL_START = 0.1
        INTERVAL_END = 0.9
        first_user = random.choice(tuple(self.points))
        second_user = random.choice(tuple(self.points))
        q = random.uniform(INTERVAL_START, INTERVAL_END)
        first_child_centers = set()
        second_child_centers = set()
        for center in first_parent.centers:
            if self.graph[center][first_user]["weight"] / self.graph[center][second_user]["weight"] <= q:
                first_child_centers.add(center)
            else:
                second_child_centers.add(center)
        for center in second_parent.centers:
            if self.graph[center][first_user]["weight"] / self.graph[center][second_user]["weight"] <= q:
                second_child_centers.add(center)
            else:
                first_child_centers.add(center)

        first_child = generate_child(self, first_child_centers)
        second_child = generate_child(self, second_child_centers)
        return first_child, second_child

    def generator(self) -> Generator[Tuple[Dict[int, Set[int]], int, str], None, None]:
        pass

    def solve(self) -> Tuple[Dict[int, Set[int]], Set[int], float]:
        population = []
        for i in range(PBS.POPULATION_SIZE):
            init_center = {random.choice(tuple(self.points))}
            individual = Individual(init_center)
            individual.init_nearest_centers(self.graph)
            population.append(individual)

        for generation in range(PBS.GENERATIONS):
            for i, individual in enumerate(population):
                for j, sibling in enumerate(population):
                    if i == j:
                        continue
                    population.append(self.local_search(self.mutation_random(individual), generation))
                    population.append(
                        self.local_search(self.mutation_directed(self.crossover_random(individual, sibling)),
                                          generation))
                    first_child, second_child = self.crossover_directed(individual, sibling)
                    population.append(self.local_search(self.mutation_directed(first_child), generation))
                    population.append(self.local_search(self.mutation_directed(second_child), generation))
            population = sorted(population, key=lambda x: x.cost)

        clusters = {}

        fittest_individual = max(population, key=lambda x: x.cost)
        for center in fittest_individual.centers:
            clusters[center] = set()
        return clusters, set(), fittest_individual.cost