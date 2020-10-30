import networkx as nx
from typing import Dict, Tuple, Set
from abc import ABC, abstractmethod

from src.kcenter.constant.colour import Colour


class AbstractSolver(ABC):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        self.graph = graph
        self.k = k
        self.constraints = constraints

    @abstractmethod
    def solve(self) -> Tuple[Set[int], Set[Set[int]], int]:
        pass
