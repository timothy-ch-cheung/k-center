import math
from typing import Dict, Set

import networkx as nx

from src.kcenter.constant.colour import Colour


def cluster(graph: nx.Graph, centers: Set[int], radius: float) -> Dict[int, Set[int]]:
    """Cluster points which lie within a given distance to the supplied centers.

    :param graph: NetworkX graph containing all points and edge weights
    :param centers: A set of points that all other points will be clustered to
    :param radius: The maximum distance a point can be away from a center to be considered to be within its cluster
    :return the optimal solution to the K-Center problem
    """
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

        if min_dist <= radius or math.isclose(min_dist, radius):
            clusters[nearest_center].add(node)
    return clusters


def verify_solution(graph: nx.Graph, constraints: Dict[Colour, int], k: int, radius: float, centers: Set[int]) -> bool:
    """Verify that a set of centers with a given radius satisfies the constraints of the Colourful K-Center problem.
    Ensures that the minimum coverage of Blue and Red points are met.

        :param graph: NetworkX graph containing all points and edge weights
        :param constraints: minimum blue and red coverage required
        :param k: maximum number of centers allowed in the solution
        :param radius: maximum distance a point can be away from a center to be considered to be within its cluster
        :param centers: set of points representing the centers of the solution
        :return validity of solution
        """
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
    """Verify that a set of centers with a given radius satisfies the constraints of the K-Center problem. Ensures
    that all points are covered in the solution.

        :param graph: NetworkX graph containing all points and edge weights
        :param centers: A set of points that all other points will be clustered to
        :param radius: The maximum distance a point can be away from a center to be considered to be within its cluster
        :return the optimal solution to the K-Center problem
        """
    if len(centers) > k:
        return False

    clusters = cluster(graph, centers, radius)
    total_points = 0
    for clust in clusters.values():
        total_points += len(clust)
    return total_points == len(graph.nodes())
