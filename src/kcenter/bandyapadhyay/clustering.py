from typing import Set, Dict

import networkx as nx


def get_point_with_max_coverage(graph: nx.Graph, unclustered_points: Set[int]) -> int:
    """From a set of un-clustered points, returns point point which is most covered by the centers
    """
    max_zj = -float("inf")
    max_node = None
    for node in unclustered_points:
        if graph.nodes()[node]["z"] > max_zj:
            max_node = node
    return max_node


def sum_centers_around_point(graph: nx.Graph, j: int, p: float) -> float:
    """Sum all the degree that a point is fractionally openend as a center for all points within p distance of point j

    note that the sum is over all points in the ball B(j, ρ), as opposed to the points in B(j, ρ) ∩ P
    (Bandyapadhyay et al. 2019)
    :param j: point to sum around (center)
    :param p: radius length
    :return: total value of fractionally opened centers around point j
    """
    total = 0;
    for node in graph:
        if node != j and graph[j][node]["weight"] < p:
            total += graph.nodes()[node]["x"]
    total += graph.nodes()[j]["x"]
    return min(1, total)


def ball(graph: nx.graph, j: int, p: float) -> Set[int]:
    """Get all points within p distance of point j

    :param j: center
    :param p: radius length
    """
    nodes = set()
    for node in graph:
        if node != j and graph[j][node]["weight"] < p:
            nodes.add(node)
    nodes.add(j)
    return nodes


def cluster(graph: nx.Graph, p) -> Dict[int, Set[int]]:
    """Greedily cluster points within 2p distance from the center

    :param p: radius length
    :return: dictionary of clusters with their centers as the key
    """
    clusters = {}
    unclustered_points = set(graph.nodes())

    # len() is O(1) since a variable keeps track of size
    while len(unclustered_points) > 0:
        j = get_point_with_max_coverage(graph, unclustered_points)

        xj = sum_centers_around_point(graph, j, p)
        graph.nodes()[j]["x"] = xj
        graph.nodes()[j]["z"] = xj

        Cj = ball(graph, j, 2 * p).intersection(unclustered_points)
        for i in Cj:
            if j == i:
                continue
            graph.nodes()[i]["x"] = 0
            graph.nodes()[i]["z"] = graph.nodes()[j]["z"]

        clusters[j] = Cj
        unclustered_points = unclustered_points.difference(Cj)
    return clusters
