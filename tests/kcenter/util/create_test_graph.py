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

def basic_graph_with_two_outliers() -> nx.Graph:
    G = nx.Graph()
    G.add_node(0, pos=numpy.array((1.3, 2.6)), colour=Colour.BLUE)
    G.add_node(1, pos=numpy.array((1.2, 2.1)), colour=Colour.BLUE)
    G.add_node(2, pos=numpy.array((0.5, 6.3)), colour=Colour.RED)
    G.add_node(3, pos=numpy.array((5.9, 5.2)), colour=Colour.RED)
    G.add_node(4, pos=numpy.array((6.4, 4.7)), colour=Colour.RED)
    G.add_node(5, pos=numpy.array((1.2, 3.5)), colour=Colour.BLUE)

    calculate_edges(G)
    return G


def medium_graph() -> nx.Graph:
    G = nx.Graph()
    G.add_node(0, pos=numpy.array((1.3, 2.6)), colour=Colour.BLUE)
    G.add_node(1, pos=numpy.array((1.2, 2.1)), colour=Colour.BLUE)
    G.add_node(2, pos=numpy.array((0.5, 6.3)), colour=Colour.RED)
    G.add_node(3, pos=numpy.array((5.9, 5.2)), colour=Colour.RED)
    G.add_node(4, pos=numpy.array((6.4, 4.7)), colour=Colour.RED)
    G.add_node(5, pos=numpy.array((1.4, 5.7)), colour=Colour.RED)
    G.add_node(6, pos=numpy.array((1.2, 5.5)), colour=Colour.RED)
    G.add_node(7, pos=numpy.array((1.5, 5.2)), colour=Colour.RED)
    G.add_node(8, pos=numpy.array((1.4, 5.1)), colour=Colour.RED)
    G.add_node(9, pos=numpy.array((1.6, 5.5)), colour=Colour.RED)

    calculate_edges(G)
    return G


def grid_graph() -> nx.Graph:
    G = nx.Graph()
    G.add_node(0, pos=numpy.array((0, 4)))
    G.add_node(1, pos=numpy.array((1, 4)))
    G.add_node(2, pos=numpy.array((2, 4)))
    G.add_node(3, pos=numpy.array((3, 4)))
    G.add_node(4, pos=numpy.array((4, 4)))
    G.add_node(5, pos=numpy.array((0, 3)))
    G.add_node(6, pos=numpy.array((1, 3)))
    G.add_node(7, pos=numpy.array((2, 3)))
    G.add_node(8, pos=numpy.array((3, 3)))
    G.add_node(9, pos=numpy.array((4, 3)))
    G.add_node(10, pos=numpy.array((0, 2)))
    G.add_node(11, pos=numpy.array((1, 2)))
    G.add_node(12, pos=numpy.array((2, 2)))
    G.add_node(13, pos=numpy.array((3, 2)))
    G.add_node(14, pos=numpy.array((4, 2)))
    G.add_node(15, pos=numpy.array((0, 1)))
    G.add_node(16, pos=numpy.array((1, 1)))
    G.add_node(17, pos=numpy.array((2, 1)))
    G.add_node(18, pos=numpy.array((3, 1)))
    G.add_node(19, pos=numpy.array((4, 1)))
    G.add_node(20, pos=numpy.array((0, 0)))
    G.add_node(21, pos=numpy.array((1, 0)))
    G.add_node(22, pos=numpy.array((2, 0)))
    G.add_node(23, pos=numpy.array((3, 0)))
    G.add_node(24, pos=numpy.array((4, 0)))

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
