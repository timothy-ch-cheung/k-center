from typing import Dict, List, Generator, Tuple, Set, Iterable

import networkx as nx

from src.kcenter.bandyapadhyay.clustering import cluster_generator
from src.kcenter.bandyapadhyay.pseudo_solver import ConstantPseudoColourful
from src.kcenter.bandyapadhyay.radius_checker import RadiusChecker
from src.kcenter.bandyapadhyay.red_maximiser import RedMaximiser
from src.kcenter.bandyapadhyay.search_stage import SearchStage
from src.kcenter.constant.colour import Colour


class ConstantPseudoColourfulSteps:
    DECIMAL_PLACES = 3

    @staticmethod
    def opt_search_start(weights: Iterable[float]) -> str:
        return f"LP1 is used to find the optimal cost to this problem instance - a solution to LP1 with a given cost means that the cost is valid. A binary search like algorithm is used to search {len(weights)} different costs that could potentially be the optimum."

    @staticmethod
    def valid_cost_attempt(cost: float) -> str:
        return f"Run LP1 with cost={round(cost, ConstantPseudoColourfulSteps.DECIMAL_PLACES)} - the cost is valid, there exists a solution with this radius. We will check a lower cost in the next step."

    @staticmethod
    def invalid_cost_attempt(cost: float) -> str:
        return f"Run LP1 with cost={round(cost, ConstantPseudoColourfulSteps.DECIMAL_PLACES)} - the cost is invalid. We will check a higher cost in the next step."

    @staticmethod
    def found_opt(cost: float) -> str:
        return f"All weights are exhausted - the minimal feasible cost for LP1 is {round(cost, ConstantPseudoColourfulSteps.DECIMAL_PLACES)} and therefore is the optimal cost. Using this cost we can greedily cluster all points."

    @staticmethod
    def create_cluster(center: int, cluster: Set[int]) -> str:
        return f"Create cluster at {center}, covering {len(cluster)} points."

    @staticmethod
    def cluster_creation_completed() -> str:
        return f"All points have been clustered, we will now use LP2 to find which clusters to open as centers."

    @staticmethod
    def centers_chosen(centers: Set[int], k: int, cost: float) -> str:
        num_centers = len(centers)
        label = f"The result of LP2 opens {num_centers} centers with a cost of {round(cost, ConstantPseudoColourfulSteps.DECIMAL_PLACES)}. This is at most 2 times the cost of the optimal solution."
        if k < num_centers:
            label += f" Note that to meet the 2-approximation we have opened {num_centers} instead of {k}."
        return label


class SteppedConstantPseudoColourful(ConstantPseudoColourful):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

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
                yield weight, lp_solution, SearchStage.VALID_WEIGHT
            else:
                left = mid + 1
                yield current_weight, last_valid_solution, SearchStage.INVALID_WEIGHT

        yield weight, lp_solution, SearchStage.FINISHED

    def generator(self) -> Generator[Tuple[Dict[int, Set[int]], int, str], None, None]:
        """Solves the Colourful K-Center problem using the algorithm created by Bandyapadhyay et al.

        Uses subroutines radius_checker (LP1 Section 2 figure 1), clustering (Section 2 Algorithm 1) and red_maximiser
        (LP2 Section 2.1 figure 2).
        """
        weights = ConstantPseudoColourful.get_weights(self.graph)
        clusters = {x: {x} for x in self.graph.nodes()}

        radius_checker = RadiusChecker(self.graph, self.k, self.constraints[Colour.RED], self.constraints[Colour.BLUE])

        lp_solver = SteppedConstantPseudoColourful.calculate_optimal_radius_binary(weights, radius_checker)
        opt = cost = lp_solution = None
        yield clusters, set(), 0, ConstantPseudoColourfulSteps.opt_search_start(weights), True

        for sol in lp_solver:
            cost, lp_solution, state = sol
            if state == SearchStage.VALID_WEIGHT:
                yield clusters, set(), 0, ConstantPseudoColourfulSteps.valid_cost_attempt(cost), True
            elif state == SearchStage.INVALID_WEIGHT:
                yield clusters, set(), 0, ConstantPseudoColourfulSteps.invalid_cost_attempt(cost), True
            else:
                opt = cost
                yield clusters, set(), 0, ConstantPseudoColourfulSteps.found_opt(cost), True

        for point, attributes in lp_solution.items():
            self.graph.nodes()[point]["x"] = attributes["x"]
            self.graph.nodes()[point]["z"] = attributes["z"]

        clustering_solution = cluster_generator(self.graph, opt)
        for sol in clustering_solution:
            center, clusters, stage = sol
            if stage == SearchStage.UNFINISHED:
                yield clusters, set(), opt, ConstantPseudoColourfulSteps.create_cluster(center, clusters[center]), True
            elif stage == SearchStage.FINISHED:
                yield clusters, set(), opt, ConstantPseudoColourfulSteps.cluster_creation_completed(), True

        red_maximiser = RedMaximiser(self.graph, clusters, self.constraints[Colour.BLUE])
        solution = red_maximiser.solve(self.k)
        centers = ConstantPseudoColourful.choose_centers(solution)

        unused_centers = set(clusters.keys()).difference(centers)

        outliers: Set[int] = set()
        for center in unused_centers:
            outliers = outliers.union(clusters[center])
            del clusters[center]

        cost = 2 * opt
        yield clusters, set(), cost, ConstantPseudoColourfulSteps.centers_chosen(set(clusters.keys()), self.k,
                                                                                 cost), False
