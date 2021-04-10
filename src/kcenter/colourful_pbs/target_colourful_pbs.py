from typing import Dict, Generator, Optional

import networkx as nx

from kcenter.pbs.pbs import Individual, PBS
from src.kcenter.colourful_pbs.colourful_pbs import ColourfulPBS
from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.target_pbs import TargetPBS


class TargetColourfulPBS(ColourfulPBS, TargetPBS):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int], name: str = None):
        if name is None:
            super().__init__(graph, k, constraints, name="colourful_pbs")
        else:
            super().__init__(graph, k, constraints, name=name)

    def generate_population(self) -> Generator[Optional[Individual], None, None]:
        self.population = []
        seed_candidate = self.generate_seed_candidate()
        yield seed_candidate
        self.population.append(seed_candidate)
        MAX_FAIL_COUNT = 8
        num_fail = 0
        while len(self.population) < PBS.POPULATION_SIZE:
            candidate = self.generate_candidate()
            if self.is_diverse(candidate) or num_fail >= MAX_FAIL_COUNT:
                self.population.append(candidate)
                num_fail = 0
                yield candidate
            else:
                num_fail += 1
                yield None
