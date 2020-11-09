from typing import Tuple, Set, Generator, Dict

import networkx as nx

from src.kcenter.bandyapadhyay.clustering import cluster
from src.kcenter.bandyapadhyay.radius_checker import RadiusChecker
from src.kcenter.bandyapadhyay.red_maximiser import RedMaximiser
from src.kcenter.constant.colour import Colour
from src.kcenter.solver.abstract_solver import AbstractSolver


class ConstantColourfulKCenterSolver(AbstractSolver):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    @staticmethod
    def get_weights(graph: nx.Graph):
        """Returns a sorted list of all weights on the graph
        """
        return sorted(list(nx.get_edge_attributes(graph, "weight").values()))

    def generator(self) -> Generator[Tuple[Dict[int, Set[int]], int, str], None, None]:
        pass

    def solve(self) -> Tuple[Dict[int, Set[int]], Set[int], int]:
        weights = ConstantColourfulKCenterSolver.get_weights(self.graph)

        radius_checker = RadiusChecker(self.graph, self.k, self.constraints[Colour.RED], self.constraints[Colour.BLUE])

        opt = weights[-1]
        lp_solution = {}
        for weight in weights:
            lp_solution = radius_checker.verify(weight)
            if lp_solution is not None:
                opt = weight
                break

        for point, attributes in lp_solution.items():
            self.graph.nodes()[point]["x"] = attributes["x"]
            self.graph.nodes()[point]["z"] = attributes["z"]

        clusters = cluster(self.graph, opt)

        red_maximiser = RedMaximiser(self.graph, clusters, self.constraints[Colour.BLUE])
        solution = red_maximiser.solve(self.k)

        centers = set(sorted(solution, key=solution.get)[-self.k:])
        unused_centers = set(clusters.keys()).difference(centers)

        outliers = set()
        for center in unused_centers:
            outliers = outliers.union(clusters[center])
            del clusters[center]

        return clusters, outliers, 2 * opt
