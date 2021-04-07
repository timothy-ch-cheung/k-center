from typing import Dict

import networkx as nx

from src.kcenter.constant.solver_state import SolverState
from src.kcenter.solver.abstract_generator import AbstractGenerator
from src.kcenter.bandyapadhyay.pseudo_solver import ConstantPseudoColourful
from src.kcenter.bandyapadhyay.stepped_pseudo_solver import SteppedConstantPseudoColourful
from src.kcenter.constant.colour import Colour


class ConstantColourfulSteps:
    DECIMAL_PLACES = 3

    @staticmethod
    def retry_with_k_minus_one(k: int) -> str:
        return f"Our initial run resulted in {k + 1} centers being openend. Since the algorithm produces a solution at most k+1 centers, we re-run the algorithm with k-1 to get a solution opening at most {k} centers"


class SteppedConstantColourful(ConstantPseudoColourful, AbstractGenerator):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    def generator(self) -> AbstractGenerator.YIELD_TYPE:
        solutions = label = None
        instance = SteppedConstantPseudoColourful(self.graph, self.k, self.constraints)
        solution = instance.generator()
        for step in solution:
            solutions, label, solver_state = step
            if not solver_state.is_active():
                break
            yield step

        if solutions is not None and len(solutions[0].clusters.keys()) > self.k:
            yield solutions, label, SolverState.ACTIVE_MAIN
            yield solutions, ConstantColourfulSteps.retry_with_k_minus_one(self.k), SolverState.ACTIVE_MAIN

            instance = SteppedConstantPseudoColourful(self.graph, self.k - 1, self.constraints)
            solution = instance.generator()

            for step in solution:
                yield step
        else:
            yield solutions, label, SolverState.INACTIVE
