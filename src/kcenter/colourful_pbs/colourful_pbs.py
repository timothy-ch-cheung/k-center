import random
from typing import Dict, Tuple

import networkx as nx

from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import PBS, Individual, min2


class ColourfulPBS(PBS):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    def find_cost(self, individual: Individual) -> Individual:
        """Calculates the cost of Colourful K-Center cover given the constraints of covering specified colours

        :param individual: individual after being optimised by PBS local search
        """
        if len(individual.centers) == 0:
            individual.cost = self.MAX_WEIGHT
            return individual

        clustered_points = set()
        total = {Colour.BLUE: 0, Colour.RED: 0}
        colourful_cost = self.MAX_WEIGHT

        nearest_centers = [(point, neighbour.nearest) for point, neighbour in individual.nearest_centers.items()]
        nearest_centers.sort(key=lambda x: x[1].cost)
        for point, nearest in nearest_centers:
            if total[Colour.BLUE] >= self.constraints[Colour.BLUE] and total[Colour.RED] >= self.constraints[Colour.RED]:
                break
            if point not in clustered_points:
                total[self.graph.nodes()[point]["colour"]] += 1
                clustered_points.add(point)
                colourful_cost = nearest.cost

        individual.cost = colourful_cost
        return individual

    def get_furthest_point(self, individual: Individual):
        if len(individual.centers) == 0:
            return next(iter(self.points))
        for point in self.points:
            if individual.nearest_centers[point].nearest.cost == individual.cost:
                return point

    def find_pair(self, w: int, individual: Individual) -> Tuple[int, int]:
        """Find the optimal center and vertex pair to swap to reduce cost

        :param w: point to get neighbours from
        :param individual: Individual in population
        :return: (center, vertex) pair to swap
        """
        C = self.graph.number_of_nodes()
        L = set()
        furthest_point_facility = individual.nearest_centers[w].nearest
        neighbours = self.graph.nodes()[w]["neighbours"]
        k = PBS.linear_search(neighbours, furthest_point_facility.point)
        nwk = PBS.get_nwk(self.graph, w, k, neighbours)
        for i in nwk:
            if i in individual.centers:
                continue

            self.add_center(i, individual)

            # M stores the cost of remove facility f from the solution
            M = {}
            for center in individual.centers:
                M[center] = 0

            for point in self.points.difference(individual.centers):
                nearest_centers = individual.nearest_centers[point]
                second_nearest = nearest_centers.second_nearest
                nearest = nearest_centers.nearest

                min_dist = min2(self.weights[(point, i)], second_nearest.cost)
                if min_dist < individual.cost:
                    M[nearest.point] += 1

            for center in individual.centers.difference({i}):
                if M[center] == C:
                    L.add((center, i))
                elif M[center] < C:
                    L = {(center, i)}
                    C = M[center]
            self.remove_center(i, individual)
        return random.choice(tuple(L))

    def local_search(self, individual: Individual, generation: int) -> Individual:
        optimised_individual = super().local_search(individual, generation)
        return self.find_cost(optimised_individual)
