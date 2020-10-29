import networkx as nx
from enum import Enum
from typing import Dict, List
import numpy


class Colour(Enum):
    RED = 1
    BLUE = 2


def create_graph():
    G = nx.Graph()
    G.add_node(0, pos=numpy.array((1.3, 2.6)), colour=Colour.BLUE)
    G.add_node(1, pos=numpy.array((1.2, 2.1)), colour=Colour.BLUE)
    G.add_node(2, pos=numpy.array((0.5, 2.3)), colour=Colour.BLUE)
    G.add_node(3, pos=numpy.array((5.9, 5.2)), colour=Colour.RED)
    G.add_node(4, pos=numpy.array((6.4, 4.7)), colour=Colour.RED)

    for n in G.nodes():
        for m in G.nodes():
            if n == m:
                continue
            weight = numpy.linalg.norm(G.nodes[n]["pos"] - G.nodes[m]["pos"])
            G.add_edge(n, m, key=str(n) + str(m), weight=weight)
    return G


def verify_solution(graph: nx.Graph, constraints: Dict[Colour, int], k: int, radius: float, centers: List[int]) -> bool:
    if len(centers) > k:
        return False

    clusters = {x:[] for x in centers}

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


def test(centers: List[int], radius: int):
    constraints = {Colour.BLUE: 3, Colour.RED: 2}
    k = 2
    is_valid = verify_solution(create_graph(), constraints, k, radius, centers)
    print("Solution with centers: ", centers, "valid:", is_valid)


test([0, 4], 2)
test([3, 4], 2)
