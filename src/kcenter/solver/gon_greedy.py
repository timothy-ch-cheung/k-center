from typing import Dict, Tuple, Set, List

import networkx as nx

from src.kcenter.constant.colour import Colour
from src.kcenter.solver.abstract_solver import AbstractSolver
from src.kcenter.verify.verify import verify_solution
from tests.kcenter.util.create_test_graph import basic_graph


class GonGreedy(AbstractSolver):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    @staticmethod
    def max_dist(graph: nx.Graph, centers: List[int], clusters: List[Set[int]]):
        max_dist = -float("inf")
        max_node = None
        owning_center = None
        for center, cluster in zip(centers, clusters):
            for node in cluster:
                if node == center:
                    continue
                dist = graph[center][node]["weight"]
                if dist > max_dist:
                    max_dist = dist
                    max_node = node
                    owning_center = center
        return max_node, max_dist, owning_center

    def solve(self) -> Tuple[List[int], List[Set[int]], int]:
        centers = [0]
        clusters = [set(list(self.graph.nodes))]

        for i in range(1, self.k):
            max_node, max_dist, owning_center = GonGreedy.max_dist(self.graph, centers, clusters)

            centers.append(max_node)
            new_cluster = {max_node}
            clusters[owning_center].remove(max_node)

            for center, cluster in zip(centers, clusters):
                nodes_moved = []
                for node in cluster:
                    if node != max_node and node != center \
                            and self.graph[node][max_node]["weight"] < self.graph[node][center]["weight"]:
                        new_cluster.add(node)
                        nodes_moved.append(node)

                for node in nodes_moved:
                    cluster.remove(node)

            clusters.append(new_cluster)

        radius = GonGreedy.max_dist(self.graph, centers, clusters)[1]
        return centers, clusters, radius

        # weights = nx.get_edge_attributes(self.graph, 'weight').values()
        # weights = list(set(weights))
        # weights = sorted(weights)
        #
        # for weight in weights:
        #     if verify_solution(self.graph, self.constraints, self.k, weight, centers):
        #         return centers, set(), weight


instance = GonGreedy(basic_graph(), 2, {Colour.BLUE: 2, Colour.RED: 2})
print(instance.solve())
