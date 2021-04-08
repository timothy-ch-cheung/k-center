import random
from typing import Dict, Tuple, Optional

import networkx as nx

from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import PBS, Individual, min2, Neighbour


class ColourfulPBS(PBS):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int], name: Optional[str] = None):
        super().__init__(graph, k, constraints, name="colourful_pbs")

    def find_cost(self, individual: Individual) -> float:
        """Calculates the cost of Colourful K-Center cover given the constraints of covering specified colours

        :param individual: individual after being optimised by PBS local search
        return: cost of meeting the coverage constraints given the centers
        """
        if len(individual.centers) == 0:
            individual.cost = self.MAX_WEIGHT
            return individual.cost

        clustered_points = set()
        total = {Colour.BLUE: 0, Colour.RED: 0}
        colourful_cost = self.MAX_WEIGHT

        nearest_centers = [(point, neighbour.nearest) for point, neighbour in individual.nearest_centers.items()]
        nearest_centers.sort(key=lambda x: x[1].cost)
        for point, nearest in nearest_centers:
            if total[Colour.BLUE] >= self.constraints[Colour.BLUE] and total[Colour.RED] >= self.constraints[
                Colour.RED]:
                break
            if point not in clustered_points:
                total[self.graph.nodes()[point]["colour"]] += 1
                clustered_points.add(point)
                colourful_cost = nearest.cost

        individual.cost = colourful_cost
        return colourful_cost

    def get_furthest_point(self, individual: Individual) -> int:
        """Calculates the point that is the furthest point covered the current K-Center Colourful cost of the individual

        :param individual: individual in the population with nearest_centers
        return: point which is furthest away from a center, if there are no centers the first point in the graph is
        returned
        """
        max_cost = 0
        max_point = 0
        for p in self.points:
            nearest = individual.nearest_centers[p].nearest
            if nearest is not None:
                if max_cost < nearest.cost <= individual.cost:
                    max_point = p
                    max_cost = nearest.cost
        return max_point

    def get_next_point(self, individual: Individual):
        return super().get_furthest_point(individual)

    def add_center(self, center: int, individual: Individual):
        """Add a center to the individual and update neighbours

        :param center: Center to add
        :param individual: Individual in population
        """
        individual.centers.add(center)

        for p in self.points:
            cost = self.weights[(center, p)]
            nearest_centers = individual.nearest_centers[p]
            nearest = nearest_centers.nearest
            second_nearest = nearest_centers.second_nearest

            if nearest is None or cost < nearest.cost:
                nearest_centers.second_nearest = nearest
                nearest_centers.nearest = Neighbour(point=center, cost=cost)
            elif second_nearest is None or cost < second_nearest.cost:
                nearest_centers.second_nearest = Neighbour(point=center, cost=cost)

    def remove_center(self, center: int, individual: Individual):
        """Remove a center to the individual and update neighbours

        :param center: Center to remove
        :param individual: Individual in population
        """
        individual.centers.remove(center)

        for p in self.points:
            nearest_centers = individual.nearest_centers[p]
            nearest = nearest_centers.nearest
            second_nearest = nearest_centers.second_nearest
            if nearest.point == center:
                nearest_centers.nearest = second_nearest
                nearest_centers.second_nearest = self.find_next(p, individual)
            elif second_nearest is None or second_nearest.point == center:
                nearest_centers.second_nearest = self.find_next(p, individual)

    def find_pair(self, w: int, individual: Individual) -> Tuple[int, int]:
        """Find the optimal center and vertex pair to swap to reduce cost

        Finds a swap between a center which covers the smallest number of points and a vertex not in the current
        solution

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

            # M stores the cost of removing facility f from the solution
            M = {center: 0 for center in individual.centers}

            for point in self.points.difference(individual.centers):
                nearest_centers = individual.nearest_centers[point]
                second_nearest = nearest_centers.second_nearest
                nearest = nearest_centers.nearest

                min_dist = min2(self.weights[(point, i)], second_nearest.cost)
                if min_dist > individual.cost:
                    M[nearest.point] += 1

            for center in individual.centers:
                if center == i:
                    continue
                if M[center] == C:
                    L.add((center, i))
                elif M[center] < C:
                    L = {(center, i)}
                    C = M[center]
            self.remove_center(i, individual)
        return random.choice(tuple(L))

    def local_search(self, individual: Individual, generation: int) -> Individual:
        optimised_individual = super().local_search(individual, generation)
        optimised_individual.cost = self.find_cost(optimised_individual)
        return optimised_individual
