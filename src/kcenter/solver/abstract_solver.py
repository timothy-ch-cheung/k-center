from abc import ABC, abstractmethod
from typing import Dict, Tuple, Set, Generator

import networkx as nx

from src.kcenter.constant.colour import Colour


class AbstractSolver(ABC):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        self.graph = graph
        self.k = k
        self.constraints = constraints

    @abstractmethod
    def solve(self) -> Tuple[Dict[int, Set[int]], Set[int], int]:
        pass

    @abstractmethod
    def generator(self) -> Generator[Tuple[Dict[int, Set[int]], int, str], None, None]:
        pass
