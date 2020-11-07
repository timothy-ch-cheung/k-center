from typing import Dict, Generator, Tuple, Set

import networkx as nx

from src.kcenter.greedy.greedy import GreedySolver, Colour
from src.kcenter.verify.verify import verify_solution


class GreedyReduceSolver(GreedySolver):
    """Colorful K-Center solver that uses a greedy heuristic and minimizes the cost based on
    the colour constraints.

            Calls GreedySolver to get an initial solution. Then attempts to reduce the radius
            by trying  lower radii and checking if the constraints are still satisfied".
            """

    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    @staticmethod
    def get_weights(graph: nx.Graph, radius: int):
        weights = sorted(list(nx.get_edge_attributes(graph, "weight").values()), reverse=True)
        return [x for x in weights if x < radius]

    def solve(self):
        clusters, radius = super().solve()
        weights = GreedyReduceSolver.get_weights(self.graph, radius)

        new_weight = None
        centers = set(clusters.keys())
        for weight in weights:
            if verify_solution(self.graph, self.constraints, self.k, weight, centers):
                new_weight = weight
            else:
                break

        radius = new_weight if new_weight is not None else radius
        return clusters, radius

    def generator(self) -> Generator[Tuple[Dict[int, Set[int]], int, str], None, None]:
        solution = super().generator()
        clusters, radius = {}, float("inf")
        for step in solution:
            clusters, radius, label = step
            yield clusters, radius, label

        weights = GreedyReduceSolver.get_weights(self.graph, radius)

        new_weight = None
        centers = set(clusters.keys())
        for weight in weights:
            if verify_solution(self.graph, self.constraints, self.k, weight, centers):
                new_weight = weight
                yield clusters, new_weight, f"decrease weight to {round(new_weight, 3)}"
            else:
                break

        radius = new_weight if new_weight is not None else radius
        yield clusters, radius, f"completed reduced solution to radius of {round(radius, 3)}"
