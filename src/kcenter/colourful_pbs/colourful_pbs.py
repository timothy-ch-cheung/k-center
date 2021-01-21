from typing import Dict

import networkx as nx

from kcenter.constant.colour import Colour
from kcenter.pbs.pbs import PBS, Individual


class ColourfulPBS(PBS):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    def local_search(self, individual: Individual, generation: int) -> Individual:
        optimised_individual = super().local_search(individual, generation)
        clustered_points = set()
        total = {Colour.BLUE: 0, Colour.RED: 0}
        current_indexes = {x: 0 for x in individual.centers}
        colourful_cost = 0
        for i in range(len(self.graph.nodes())):
            finished = False
            for center in individual.centers:
                new_point = self.graph.nodes()[center]["neighbours"][current_indexes[center]]
                if new_point not in clustered_points:
                    clustered_points.add(new_point)
                    cost = self.weights[(center, new_point)]
                    total[self.graph.nodes()[new_point]["colour"]] += 1
                    if cost > colourful_cost:
                        colourful_cost = cost

                current_indexes[center] += 1

                if total[Colour.BLUE] >= self.constraints[Colour.BLUE] and total[Colour.RED] >= self.constraints[
                    Colour.RED]:
                    finished = True
                    break

            if finished:
                break

        optimised_individual.cost = colourful_cost
        return optimised_individual
