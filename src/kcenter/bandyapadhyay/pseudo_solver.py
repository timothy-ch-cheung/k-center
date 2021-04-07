from typing import Tuple, Set, Dict, List

import networkx as nx

from src.kcenter.bandyapadhyay.clustering import cluster
from src.kcenter.bandyapadhyay.radius_checker import RadiusChecker
from src.kcenter.bandyapadhyay.red_maximiser import RedMaximiser
from src.kcenter.constant.colour import Colour
from src.kcenter.solver.abstract_solver import AbstractSolver


class ConstantPseudoColourful(AbstractSolver):
    """Implementation based on the algorithm by Bandyapadhyay et al. from
    'A Constant Approximation for Colorful k-Center (2019)'

    produces a pseudo approximation which opens at most k+1 centers with a 1
    """

    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    @staticmethod
    def get_weights(graph: nx.Graph):
        """Returns a sorted list of all weights on the graph
        """
        return sorted(list(nx.get_edge_attributes(graph, "weight").values()))

    @staticmethod
    def choose_centers(solution: Dict[int, float]):
        """given a solution to the subroutine red_maximiser (LP2), we pick centers depending on the number of fractional
        solutions"""
        potential_centers = [x for x in solution.keys() if solution[x] != 0]
        return potential_centers

    @staticmethod
    def calculate_optimal_radius_linear(weights: List[float], radius_checker: RadiusChecker) -> Tuple[
        float, Dict[int, float]]:
        """Returns the optimal radius for the graph, using a linear search

        :param weights: list of weights sorted from smallest to largest
        :param radius_checker: object which contains LP1 which can verify whether a given radius is valid
        """
        for weight in weights:
            lp_solution = radius_checker.verify(weight)
            if lp_solution is not None:
                return weight, lp_solution
        return weights[-1], {}

    @staticmethod
    def calculate_optimal_radius_binary(weights: List[float], radius_checker: RadiusChecker) -> Tuple[
        float, Dict[int, float]]:
        """Returns the optimal radius for the graph, using a modified binary search

        :param weights: list of weights sorted from smallest to largest
        :param radius_checker: object which contains LP1 which can verify whether a given radius is valid
        """
        left = 0
        right = len(weights)
        last_valid_solution = None
        weight = weights[-1]

        while left <= right:
            mid = (left + right) // 2
            current_weight = weights[mid]

            lp_solution = radius_checker.verify(current_weight)
            if lp_solution is not None:
                weight = current_weight
                last_valid_solution = lp_solution
                right = mid - 1
            else:
                left = mid + 1

        return weight, last_valid_solution

    def solve(self) -> Tuple[Dict[int, Set[int]], Set[int], int]:
        """Solves the Colourful K-Center problem using the algorithm created by Bandyapadhyay et al.

        Uses subroutines radius_checker (LP1 Section 2 figure 1), clustering (Section 2 Algorithm 1) and red_maximiser
        (LP2 Section 2.1 figure 2).
        """
        weights = ConstantPseudoColourful.get_weights(self.graph)

        radius_checker = RadiusChecker(self.graph, self.k, self.constraints[Colour.RED], self.constraints[Colour.BLUE])

        opt, lp_solution = ConstantPseudoColourful.calculate_optimal_radius_binary(weights, radius_checker)

        for point, attributes in lp_solution.items():
            self.graph.nodes()[point]["x"] = attributes["x"]
            self.graph.nodes()[point]["z"] = attributes["z"]

        clusters = cluster(self.graph, opt)

        red_maximiser = RedMaximiser(self.graph, clusters, self.constraints[Colour.BLUE])
        solution = red_maximiser.solve(self.k)

        centers = ConstantPseudoColourful.choose_centers(solution)
        unused_centers = set(clusters.keys()).difference(centers)

        outliers: Set[int] = set()
        for center in unused_centers:
            outliers = outliers.union(clusters[center])
            del clusters[center]

        return clusters, outliers, 2 * opt
