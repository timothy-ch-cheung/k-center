from typing import Dict, Generator, Tuple, Set

import networkx as nx

from src.kcenter.solver.abstract_generator import Solution, AbstractGenerator
from src.kcenter.constant.colour import Colour
from src.kcenter.greedy.greedy_reduce import GreedyReduce
from src.kcenter.greedy.stepped_greedy import SteppedGreedy
from src.kcenter.verify.verify import verify_solution


class GreedyReduceSteps:
    DECIMAL_PLACES = 3

    @staticmethod
    def intermediate_cost(cost: float, k: int) -> str:
        cost = round(cost, GreedyReduceSteps.DECIMAL_PLACES)
        num_centers_label = f"{k} centers have" if k > 1 else "single center has"
        return f"Our {num_centers_label} been chosen. The current cost is {cost}, we will continue to reduce the cost until the solution does not meet the constraints."

    @staticmethod
    def decrease_cost(new_cost: float) -> str:
        return f"decrease weight to {round(new_cost, GreedyReduceSteps.DECIMAL_PLACES)}"

    @staticmethod
    def final_cost(cost: float) -> str:
        return f"completed reduced solution to radius of {round(cost, GreedyReduceSteps.DECIMAL_PLACES)}"


class SteppedGreedyReduce(GreedyReduce, SteppedGreedy):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    def generator(self) -> AbstractGenerator.YIELD_TYPE:
        solutions = []
        generator = super().generator()
        for step in generator:
            solutions, label, active = step
            if not active:
                break
            yield solutions, label, True

        solution = solutions[0]
        yield solutions, GreedyReduceSteps.intermediate_cost(solution.cost, self.k), True

        weights = GreedyReduce.get_weights(self.graph, solution.cost)

        new_weight = None
        centers = set(solution.clusters.keys())
        for weight in weights:
            if verify_solution(self.graph, self.constraints, self.k, weight, centers):
                new_weight = weight
                yield [Solution(solution.clusters, new_weight)], GreedyReduceSteps.decrease_cost(new_weight), True
            else:
                break

        radius = new_weight if new_weight is not None else solution.cost
        yield [Solution(solution.clusters, radius)], GreedyReduceSteps.final_cost(radius), False
