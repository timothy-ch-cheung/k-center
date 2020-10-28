import networkx as nx
from enum import Enum
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
            weight = numpy.linalg.norm(G.nodes[n]["pos"]-G.nodes[m]["pos"])
            G.add_edge(n, m, weight=weight)
    return G


def verify_solution():
    pass