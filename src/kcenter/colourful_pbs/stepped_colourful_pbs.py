from typing import Dict

import networkx as nx

from kcenter.colourful_pbs.colourful_pbs import ColourfulPBS
from kcenter.constant.colour import Colour
from kcenter.pbs.stepped_pbs import SteppedPBS


class SteppedColourfulPBS(ColourfulPBS, SteppedPBS):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    def generator(self):
        generator = super().generator()
        for step in generator:
            yield step
