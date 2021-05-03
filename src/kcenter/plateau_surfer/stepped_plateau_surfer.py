from typing import Dict, Tuple, Set

import networkx as nx

from kcenter.constant.colour import Colour
from kcenter.plateau_surfer.plateau_surfer import PlateauSurfer
from kcenter.solver.abstract_generator import AbstractGenerator
from kcenter.verify.verify import cluster


class PBSSteps:
    DECIMAL_PLACES = 3

    @staticmethod
    def round_coord(coord: Tuple[float, float]):
        return round(coord[0], PBSSteps.DECIMAL_PLACES), round(coord[1], PBSSteps.DECIMAL_PLACES)

    @staticmethod
    def nodes_to_coords(graph: nx.Graph, centers: Set[int]) -> Set[Tuple[float, float]]:
        coordinates = set()
        for center in centers:
            coord = tuple(graph.nodes()[center]["pos"])
            coordinates.add(PBSSteps.round_coord(coord))
        return coordinates

    @staticmethod
    def greedy_randomised_build():
        return ""

    @staticmethod
    def plateau_surfer_search():
        return ""

    @staticmethod
    def best_so_far():
        return ""

    @staticmethod
    def grasp_start():
        return ""

    @staticmethod
    def grasp_complete():
        return ""


class SteppedPlateauSurfer(AbstractGenerator, PlateauSurfer):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super.__init__(graph, k, constraints)

    def generator(self, iterations=5):
        best_cost = float("inf")
        best_cluster = None
        for i in range(iterations):
            initial_solution = self.randomized_build()
            solution = self.plateau_surf_local_search(initial_solution)
            cost = self.find_candidate_cost(solution)

            if cost < best_cost:
                best_cost = cost
                best_cluster = cluster(self.graph, solution, cost)
        return best_cluster, set(), best_cost
