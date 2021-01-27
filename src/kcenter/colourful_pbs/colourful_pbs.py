from typing import Dict

import networkx as nx

from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import PBS, Individual


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

    # def get_furthest_point(self, individual: Individual):
    #     if len(individual.centers) == 0:
    #         return 0
    #     for point in self.points:
    #         if individual.nearest_centers[point].nearest.cost == individual.cost:
    #             return point
    #     return None

    def update_cost_after_search_iteration(self, individual: Individual):
        self.find_cost(individual)

    def local_search(self, individual: Individual, generation: int) -> Individual:
        optimised_individual = super().local_search(individual, generation)
        return self.find_cost(optimised_individual)
