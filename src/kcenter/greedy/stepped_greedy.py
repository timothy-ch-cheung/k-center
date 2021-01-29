from typing import Set, Dict, Tuple, Generator

import networkx as nx

from src.kcenter.constant.colour import Colour
from src.kcenter.greedy.greedy import Greedy


class GreedySteps:
    DECIMAL_PLACES = 3

    @staticmethod
    def initial_center(graph: nx.Graph, center: int) -> str:
        initial_center = graph.nodes()[center]
        x = round(initial_center["pos"][0], GreedySteps.DECIMAL_PLACES)
        y = round(initial_center["pos"][1], GreedySteps.DECIMAL_PLACES)
        return f"The initial center is arbitrarily chosen, its coordinates are ({x}, {y})." + \
               f" It is a {initial_center['colour'].name.lower()} point."

    @staticmethod
    def subsequent_center(graph: nx.Graph, center: int, cost: float) -> str:
        next_center = graph.nodes()[center]
        x = round(next_center["pos"][0], GreedySteps.DECIMAL_PLACES)
        y = round(next_center["pos"][1], GreedySteps.DECIMAL_PLACES)
        cost = round(cost, GreedySteps.DECIMAL_PLACES)
        return "We find the point which has the maximum distance from its closest center, which is the point at " + \
               f"({x}, {y}). It is a {next_center['colour'].name.lower()} point {cost} distance away. This makes " + \
               f"the current cost {cost}."

    @staticmethod
    def final_cost(cost: float, k: int) -> str:
        cost = round(cost, GreedySteps.DECIMAL_PLACES)
        num_centers_label = f"{k} centers have" if k > 1 else "single center has"
        return f"Our {num_centers_label} been chosen. To calculate the final cost, we find the distance to the " + \
               f"furthest point from the previous center. This makes the final cost {cost}."


class SteppedGreedy(Greedy):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    def generator(self) -> Generator[Tuple[Dict[int, Set[int]], int, str, bool], None, None]:
        clusters = {Greedy.INITIAL_HEAD: set(self.graph.nodes)}
        max_weight = max(list(nx.get_edge_attributes(self.graph, "weight").values()))
        label = GreedySteps.initial_center(graph=self.graph, center=Greedy.INITIAL_HEAD)
        yield clusters, set(), max_weight, label, True

        for i in range(1, self.k):
            max_node, max_dist, owning_center = Greedy.max_dist(self.graph, clusters)
            clusters[max_node] = {max_node}
            clusters[owning_center].remove(max_node)

            Greedy.move_nodes_to_new_cluster(self.graph, clusters, max_node)
            label = GreedySteps.subsequent_center(self.graph, max_node, max_dist)
            yield clusters, set(), max_dist, label, True

        radius = Greedy.max_dist(self.graph, clusters)[1]
        label = GreedySteps.final_cost(radius, self.k)
        yield clusters, set(), radius, label, False
