import math
from typing import Dict, Set

import networkx as nx

from src.kcenter.constant.colour import Colour


def cluster(graph: nx.Graph, centers: Set[int], radius: float):
    clusters = {x: set() for x in centers}

    for node in graph.nodes():
        nearest_center = None
        min_dist = float("inf")
        if node in centers:
            clusters[node].add(node)
            continue

        for center in centers:
            edge = graph[center][node]
            weight = edge["weight"] if edge is not None else float("inf")
            if weight < min_dist:
                min_dist = weight
                nearest_center = center

        if min_dist < radius or math.isclose(min_dist, radius):
            clusters[nearest_center].add(node)
    return clusters


def verify_solution(graph: nx.Graph, constraints: Dict[Colour, int], k: int, radius: float, centers: Set[int]) -> bool:
    if len(centers) > k:
        return False

    clusters = cluster(graph, centers, radius)
    coverage = {k: 0 for (k, v) in constraints.items()}

    for (center, members) in clusters.items():
        for member in members:
            coverage[graph.nodes[member]["colour"]] += 1

    for colour in constraints.keys():
        if coverage[colour] < constraints[colour]:
            return False
    return True


def verify_k_center_solution(graph: nx.Graph, centers: Set[int], k: int, radius: float) -> bool:
    if len(centers) > k:
        return False

    clusters = cluster(graph, centers, radius)
    total_points = 0
    for clust in clusters.values():
        total_points += len(clust)
    return total_points == len(graph.nodes())
