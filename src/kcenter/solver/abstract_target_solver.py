from abc import ABC, abstractmethod
from typing import Dict, Tuple, Set, Optional


class AbstractTargetSolver(ABC):

    @abstractmethod
    def target_solve(self, target_cost: float, timeout: Optional[float] = None, log: bool = False) -> Tuple[
        Dict[int, Set[int]], Set[int], float]:
        pass
