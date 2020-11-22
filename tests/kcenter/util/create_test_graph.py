import numpy
import networkx as nx

from src.kcenter.constant.colour import Colour


def calculate_edges(graph: nx.Graph):
    for n in graph.nodes():
        for m in graph.nodes():
            if n == m:
                continue
            weight = numpy.linalg.norm(graph.nodes[n]["pos"] - graph.nodes[m]["pos"])
            graph.add_edge(n, m, key=str(n) + str(m), weight=weight)


def basic_graph() -> nx.Graph:
    G = nx.Graph()
    G.add_node(0, pos=numpy.array((1.3, 2.6)), colour=Colour.BLUE)
    G.add_node(1, pos=numpy.array((1.2, 2.1)), colour=Colour.BLUE)
    G.add_node(2, pos=numpy.array((0.5, 2.3)), colour=Colour.BLUE)
    G.add_node(3, pos=numpy.array((5.9, 5.2)), colour=Colour.RED)
    G.add_node(4, pos=numpy.array((6.4, 4.7)), colour=Colour.RED)

    # min weight = 0.5099
    # max weight = 6.3695
    calculate_edges(G)
    return G


def basic_graph_with_outlier() -> nx.Graph:
    G = nx.Graph()
    G.add_node(0, pos=numpy.array((1.3, 2.6)), colour=Colour.BLUE)
    G.add_node(1, pos=numpy.array((1.2, 2.1)), colour=Colour.BLUE)
    G.add_node(2, pos=numpy.array((0.5, 6.3)), colour=Colour.RED)
    G.add_node(3, pos=numpy.array((5.9, 5.2)), colour=Colour.RED)
    G.add_node(4, pos=numpy.array((6.4, 4.7)), colour=Colour.RED)

    # min weight = 0.5099
    # max weight = 6.3695
    calculate_edges(G)
    return G


def extreme_point_graph() -> nx.Graph:
    G = nx.Graph()
    G.add_node(0, pos=numpy.array((1.2, 2.1)), colour=Colour.RED)
    G.add_node(1, pos=numpy.array((1.3, 2.9)), colour=Colour.RED)
    G.add_node(2, pos=numpy.array((2.5, 3.1)), colour=Colour.RED)
    G.add_node(3, pos=numpy.array((2.0, 2.5)), colour=Colour.RED)
    G.add_node(4, pos=numpy.array((2.9, 1.9)), colour=Colour.BLUE)
    G.add_node(5, pos=numpy.array((7.1, 2.5)), colour=Colour.BLUE)
    G.add_node(6, pos=numpy.array((7.6, 3.4)), colour=Colour.BLUE)
    G.add_node(7, pos=numpy.array((8.0, 2.5)), colour=Colour.BLUE)
    G.add_node(8, pos=numpy.array((8.6, 3.3)), colour=Colour.BLUE)
    G.add_node(9, pos=numpy.array((8.8, 1.7)), colour=Colour.RED)
    calculate_edges(G)
    return G
