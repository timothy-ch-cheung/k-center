from typing import Dict, Optional

import networkx as nx

from src.kcenter.colourful_pbs.colourful_pbs import ColourfulPBS
from src.kcenter.constant.colour import Colour
from src.kcenter.constant.solver_state import SolverState
from src.kcenter.pbs.pbs import Individual
from src.kcenter.pbs.stepped_pbs import SteppedPBS


class ColourfulPBSSteps:
    DECIMAL_PLACES = 3

    @staticmethod
    def inspect_header(generation: int):
        if generation == 0:
            return "POPULATION GENERATION: "
        else:
            return f"INSPECT GENERATION {generation}: "

    @staticmethod
    def inspect_find_colourful_cost(individual: Individual, constraints: Dict[Colour, int], generation: int):
        header = ColourfulPBSSteps.inspect_header(generation)
        return header + f"""Post local search, the cost of covering the required colours needs to be calculated.
         The. A radius of {round(individual.cost, ColourfulPBSSteps.DECIMAL_PLACES)} is required to cover 
         {constraints[Colour.BLUE]} blue points and {constraints[Colour.RED]} red points"""


class SteppedColourfulPBS(ColourfulPBS, SteppedPBS):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int], name: Optional[str] = None):
        if name is None:
            super().__init__(graph, k, constraints)
        else:
            super().__init__(graph, k, constraints, name=name)

    def local_search(self, individual: Individual, generation: int):
        local_search_steps = SteppedPBS.local_search(self, individual, generation)
        for step in local_search_steps:
            yield step
        individual.cost = self.find_cost(individual)
        yield self.yield_candidate(individual), ColourfulPBSSteps.inspect_find_colourful_cost(individual,
                                                                                              self.constraints,
                                                                                              generation), SolverState.ACTIVE_SUB

    def generator(self):
        generator = super().generator()
        for step in generator:
            yield step
