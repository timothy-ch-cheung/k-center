from abc import abstractmethod, ABC
from typing import Dict, Set, Tuple, Generator, List

Label = str
Active = bool


class Solution:
    def __init__(self, clusters: Dict[int, Set[int]], cost: float = 0, outliers: Set[int] = None):
        self.clusters = clusters
        self.cost = cost
        self.outliers = outliers or set()

    def to_json(self):
        centers = list(self.clusters.keys())
        return {"centers": centers, "k": len(centers), "radius": self.cost, "outliers": len(self.outliers)}


class AbstractGenerator(ABC):
    YIELD_TYPE = Tuple[List[Solution], Label, Active]

    @abstractmethod
    def generator(self) -> Generator[YIELD_TYPE, None, None]:
        pass
