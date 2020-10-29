import networkx as nx
from typing import Dict, List

from src.kcenter.constant.colour import Colour


def verify_solution(graph: nx.Graph, constraints: Dict[Colour, int], k: int, radius: float, centers: List[int]) -> bool:
    if len(centers) > k:
        return False

    clusters = {x: [] for x in centers}

    # Calculate which center the node is clustered with
    for node in graph.nodes():
        nearest_center = None
        min_dist = float("inf")
        for center in centers:
            if node not in graph[center]:
                continue
            edge = graph[center][node]
            weight = edge["weight"] if edge is not None else float("inf")
            if weight < min_dist:
                min_dist = weight
                nearest_center = center

        if min_dist <= radius:
            clusters[nearest_center].append(node)

    coverage = {k: 0 for (k, v) in constraints.items()}

    for (center, members) in clusters.items():
        coverage[graph.nodes[center]["colour"]] += 1
        for member in members:
            coverage[graph.nodes[member]["colour"]] += 1

    for colour in constraints.keys():
        if coverage[colour] < constraints[colour]:
            return False
    return True
