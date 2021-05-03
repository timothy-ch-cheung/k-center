from typing import Dict, Tuple, Set

import networkx as nx

from src.kcenter.constant.colour import Colour
from src.kcenter.constant.solver_state import SolverState
from src.kcenter.plateau_surfer.plateau_surfer import PlateauSurfer
from src.kcenter.solver.abstract_generator import AbstractGenerator, Solution
from src.kcenter.verify.verify import cluster, cluster_nearest


class PlateauSurferSteps:
    DECIMAL_PLACES = 3

    @staticmethod
    def round_coord(coord: Tuple[float, float]):
        return round(coord[0], PlateauSurferSteps.DECIMAL_PLACES), round(coord[1], PlateauSurferSteps.DECIMAL_PLACES)

    @staticmethod
    def nodes_to_coords(graph: nx.Graph, centers: Set[int]) -> Set[Tuple[float, float]]:
        coordinates = set()
        for center in centers:
            coord = tuple(graph.nodes()[center]["pos"])
            coordinates.add(PlateauSurferSteps.round_coord(coord))
        return coordinates

    @staticmethod
    def greedy_randomised_build(initial_solution: Set[Tuple[float, float]], initial_cost: float):
        return f"""An initial solution is created using the Greedy Randomised Build algorithm. The centers are {initial_solution}, which has a cost of {round(initial_cost, PlateauSurferSteps.DECIMAL_PLACES)}."""

    @staticmethod
    def plateau_surfer_search(solution: Set[Tuple[float, float]], cost: float):
        return f"After the Plateau Surfer local search is performed on the initial solution, we get the centers {solution}. The cost is {round(cost, PlateauSurferSteps.DECIMAL_PLACES)}."

    @staticmethod
    def new_best(old_cost: float, new_cost: float, new_solution: Set[Tuple[float, float]]):
        return f"""The new solution {new_solution} has  cost {round(new_cost, PlateauSurferSteps.DECIMAL_PLACES)}. Since this is lower than the best cost {round(old_cost, PlateauSurferSteps.DECIMAL_PLACES)} the best solution is updated."""

    @staticmethod
    def not_new_best(best_cost: float, new_cost: float):
        return f"""The new solution has cost {round(new_cost, PlateauSurferSteps.DECIMAL_PLACES)} which is not lower than the best cost {round(best_cost, PlateauSurferSteps.DECIMAL_PLACES)}. Therefore the best solution is not updated."""

    @staticmethod
    def grasp_start_iteration(iteration):
        return f"Start of GRASP iteration {iteration + 1}."

    @staticmethod
    def grasp_complete(iterations: int, best_solution: Set[Tuple[float, float]], best_cost: float):
        return f"""{iterations} iterations of GRASP have been completed. The best cost is {round(best_cost, PlateauSurferSteps.DECIMAL_PLACES)} with the centers {best_solution}"""


class SteppedPlateauSurfer(AbstractGenerator, PlateauSurfer):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    def generator(self, iterations=5):
        best_cost = float("inf")
        best_cluster = None
        for i in range(iterations):
            yield [], PlateauSurferSteps.grasp_start_iteration(iteration=i), SolverState.ACTIVE_MAIN

            initial_solution = self.randomized_build()
            initial_cluster = cluster_nearest(self.graph, initial_solution)
            initial_cost = self.find_candidate_cost(initial_solution)
            yield [Solution(initial_cluster, initial_cost)], \
                  PlateauSurferSteps.greedy_randomised_build(
                      PlateauSurferSteps.nodes_to_coords(self.graph, initial_solution),
                      initial_cost), SolverState.ACTIVE_MAIN

            solution = self.plateau_surf_local_search(initial_solution)
            cost = self.find_candidate_cost(solution)
            clusters = cluster_nearest(self.graph, solution)
            yield [Solution(clusters, cost)], PlateauSurferSteps.plateau_surfer_search(
                PlateauSurferSteps.nodes_to_coords(self.graph, solution), cost), SolverState.ACTIVE_MAIN

            if cost < best_cost:
                best_cluster = cluster(self.graph, solution, cost)
                yield [Solution(clusters, cost)], PlateauSurferSteps.new_best(best_cost, cost,
                                                                              PlateauSurferSteps.nodes_to_coords(
                                                                                  self.graph,
                                                                                  solution)), SolverState.ACTIVE_MAIN
                best_cost = cost
            else:
                yield [Solution(best_cluster, best_cost)], PlateauSurferSteps.not_new_best(best_cost,
                                                                                           cost), SolverState.ACTIVE_MAIN

        yield [Solution(best_cluster, best_cost)], \
              PlateauSurferSteps.grasp_complete(iterations, PlateauSurferSteps.nodes_to_coords(self.graph, set(
                  best_cluster.keys())), best_cost), SolverState.INACTIVE
