from typing import Set, Dict

import networkx as nx
import numpy

from kcenter.constant.colour import Colour
from tests.kcenter.util.create_test_graph import calculate_edges


def basic_graph() -> nx.Graph:
    G = nx.Graph()
    G.add_node(0, pos=numpy.array((1.3, 2.6)), colour=Colour.BLUE, x=1.0, z=1.0)
    G.add_node(1, pos=numpy.array((1.2, 2.1)), colour=Colour.BLUE, x=0.0, z=1.0)
    G.add_node(2, pos=numpy.array((0.5, 2.3)), colour=Colour.BLUE, x=0.0, z=1.0)
    G.add_node(3, pos=numpy.array((5.9, 5.2)), colour=Colour.RED, x=1.0, z=1.0)
    G.add_node(4, pos=numpy.array((6.4, 4.7)), colour=Colour.RED, x=0.0, z=1.0)

    # min weight = 0.5099
    # max weight = 6.3695
    calculate_edges(G)
    return G


def get_max_zj(graph: nx.Graph, unclustered_points: Set[int]) -> int:
    max_zj = -float("inf")
    max_node = None
    for node in unclustered_points:
        if graph.nodes()[node]["z"] > max_zj:
            max_node = node
    return max_node


def sum_xi(graph: nx.Graph, j: int, p: float) -> float:
    # note that the sum is over all points in the ball B(j, ρ), as opposed to the points in B(j, ρ) ∩ P
    # (Bandyapadhyay et al. 2019)
    total = 0;
    for node in graph:
        if node != j and graph[j][node]["weight"] < p:
            total += graph.nodes()[node]["x"]
    total += graph.nodes()[j]["x"]
    return min(1, total)


def ball(graph: nx.graph, j, p) -> Set[int]:
    nodes = set()
    for node in graph:
        if node != j and graph[j][node]["weight"] < p:
            nodes.add(node)
    nodes.add(j)
    return nodes


def cluster(graph: nx.Graph, p) -> Dict[int, Set[int]]:
    clusters = {}
    unclustered_points = set(graph.nodes())

    # len() is O(1) since a variable keeps track of size
    while len(unclustered_points) > 0:
        j = get_max_zj(graph, unclustered_points)

        xj = sum_xi(graph, j, p)
        graph.nodes()[j]["x"] = sum_xi(graph, j, p)
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


solution = cluster(basic_graph(), 0.854)
print(solution)
