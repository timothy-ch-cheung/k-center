from typing import Dict, Optional

import networkx as nx

from src.kcenter.colourful_pbs.colourful_pbs import ColourfulPBS
from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.target_pbs import TargetPBS


class TargetColourfulPBS(ColourfulPBS, TargetPBS):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints, name="colourful_pbs")
