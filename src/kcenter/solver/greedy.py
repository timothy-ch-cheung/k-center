from typing import Dict, Tuple, Set

import networkx as nx

from src.kcenter.constant.colour import Colour
from src.kcenter.solver.abstract_solver import AbstractSolver
from tests.kcenter.util.create_test_graph import basic_graph


class GreedySolver(AbstractSolver):
    """K-Center solver that uses a greedy heuristic.

        Based on the algorithm shown in "Clustering to minimize
        the maximum inter-cluster distance (Gonzalez 1985)".
        """
    INITIAL_HEAD = 0

    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    @staticmethod
    def max_dist(graph: nx.Graph, clusters: Dict[int, Set[int]]):
        max_dist = -float("inf")
        max_node = None
        owning_center = None
        for center, cluster in zip(clusters.keys(), clusters.values()):
            for node in cluster:
                if node == center:
                    continue
                dist = graph[center][node]["weight"]
                if dist > max_dist:
                    max_dist = dist
                    max_node = node
                    owning_center = center
        return max_node, max_dist, owning_center

    def solve(self) -> Tuple[Dict[int, Set[int]], int]:
        clusters = {GreedySolver.INITIAL_HEAD: set(self.graph.nodes)}

        for i in range(1, self.k):
            max_node, max_dist, owning_center = GreedySolver.max_dist(self.graph, clusters)

            clusters[max_node] = {max_node}
            clusters[owning_center].remove(max_node)

            for center, cluster in zip(clusters.keys(), clusters.values()):
                nodes_moved = []
                for node in cluster:
                    if node != max_node and node != center \
                            and self.graph[node][max_node]["weight"] < self.graph[node][center]["weight"]:
                        clusters[max_node].add(node)
                        nodes_moved.append(node)

                for node in nodes_moved:
                    cluster.remove(node)

        radius = GreedySolver.max_dist(self.graph, clusters)[1]
        return clusters, radius


instance = GreedySolver(basic_graph(), 2, {Colour.BLUE: 2, Colour.RED: 2})
print(instance.solve())
