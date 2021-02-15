from typing import Set

from kcenter.brute_force.brute_force_k_center import BruteForceKCenter
from server.orlib_graph_loader import ORLIBGraphLoader


def brute_force_partial(graph, k, centers: Set[int]):
    candidates = set(graph.nodes()).difference(centers)
    brute_force = BruteForceKCenter(graph, k, {})
    for candidate in candidates:
        cost = brute_force.find_candidate_cost(list(centers.union({candidate})))
        print(f"swap {candidate} with {cost}")

graph = ORLIBGraphLoader.get_graph("pmed3")
solution = {77, 81, 82, 85, 21, 88, 99, 48, 51, 54}
brute_force_partial(graph, graph.graph["k"], {77, 14, 20, 87, 24, 26, 91, 48, 50})