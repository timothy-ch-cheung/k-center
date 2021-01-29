from typing import Dict, Generator, Tuple, Set, List, Callable

import networkx as nx

from src.kcenter.constant.colour import Colour
from src.kcenter.greedy.greedy import Greedy
from src.kcenter.verify.verify import verify_solution


class GreedyReduce(Greedy):
    """Colorful K-Center solver that uses a greedy heuristic and minimizes the cost based on
    the colour constraints.

    Calls GreedySolver to get an initial solution. Then attempts to reduce the radius
    by trying  lower radii and checking if the constraints are still satisfied".
    """

    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    @staticmethod
    def get_weights(graph: nx.Graph, radius: float):
        """Gets all weights on the graph less than a given length in reverse order
        """
        weights = sorted(list(nx.get_edge_attributes(graph, "weight").values()), reverse=True)
        return [x for x in weights if x < radius]

    def calculate_optimal_radius_binary(self, weights: List[float], centers: Set[int]) -> float:
        """Returns the optimal radius for the graph, using a modified binary search

        :param weights: list of weights sorted from largest to smallest
        """
        left = 0
        right = len(weights)
        weight = weights[-1]

        while left <= right:
            mid = (left + right) // 2
            current_weight = weights[mid]
            valid_solution = verify_solution(self.graph, self.constraints, self.k, current_weight, centers)
            if valid_solution:
                weight = current_weight
                left = mid + 1
            else:
                right = mid - 1

        return weight

    def solve(self) -> Tuple[Dict[int, Set[int]], Set[int], float]:
        clusters, outliers, radius = super().solve()
        weights = GreedyReduce.get_weights(self.graph, radius)

        centers = set(clusters.keys())
        new_weight = self.calculate_optimal_radius_binary(weights, centers)

        outliers = set()
        for center in clusters.keys():
            points_to_remove = set()
            for point in clusters[center]:
                if center != point and self.graph[center][point]["weight"] > new_weight:
                    outliers.add(point)
                    points_to_remove.add(point)
            clusters[center].difference_update(points_to_remove)
        radius = new_weight

        return clusters, outliers, radius
