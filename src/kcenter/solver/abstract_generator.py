from abc import abstractmethod, ABC
from typing import Dict, Set, Tuple, Generator, List
import networkx as nx

Label = str
Active = bool


class Solution:
    def __init__(self, clusters: Dict[int, Set[int]], cost: float = 0, outliers: Set[int] = None):
        self.clusters = clusters
        self.cost = cost
        self.outliers = outliers or set()

    def __str__(self):
        return f"clusters: {self.clusters}, cost: {round(self.cost, 3)}, outliers: {self.outliers}"

    def __repr__(self):
        return self.__str__()

    def to_json(self, graph: nx.Graph):
        centers = list(self.clusters.keys())
        center_coords = [{"x": pos[0], "y": pos[1]} for pos in [graph.nodes()[i]["pos"] for i in centers]]
        return {"centers": center_coords, "k": len(centers), "radius": self.cost, "outliers": len(self.outliers)}


class AbstractGenerator(ABC):
    YIELD_TYPE = Tuple[List[Solution], Label, Active]

    @abstractmethod
    def generator(self) -> Generator[YIELD_TYPE, None, None]:
        pass
