from typing import Dict

import networkx as nx

from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import PBS, Individual


class ColourfulPBS(PBS):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    def find_colourful_cost(self, optimised_individual: Individual) -> Individual:
        """Calculates the cost of Colourful K-Center cover given the constraints of covering specified colours

        :param optimised_individual: individual after being optimised by PBS local search
        """
        clustered_points = set()
        total = {Colour.BLUE: 0, Colour.RED: 0}
        current_indexes = {x: 0 for x in optimised_individual.centers}
        colourful_cost = self.MAX_WEIGHT
        while total[Colour.BLUE] < self.constraints[Colour.BLUE] or total[Colour.RED] < self.constraints[Colour.RED]:
            min_cost = float("inf")
            min_point = None
            min_center = None
            for center in optimised_individual.centers:
                new_point = self.graph.nodes()[center]["neighbours"][current_indexes[center]]
                if new_point not in clustered_points:
                    cost = self.weights[(center, new_point)]
                    if cost < min_cost:
                        min_cost = cost
                        min_point = new_point
                        min_center = center
                else:
                    current_indexes[center] += 1
            if min_center is None:
                continue
            current_indexes[min_center] += 1
            total[self.graph.nodes()[min_point]["colour"]] += 1
            clustered_points.add(min_point)
            colourful_cost = min_cost

        optimised_individual.cost = colourful_cost
        return optimised_individual

    def local_search(self, individual: Individual, generation: int) -> Individual:
        optimised_individual = super().local_search(individual, generation)
        return self.find_colourful_cost(optimised_individual)
