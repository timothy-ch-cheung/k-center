import os
from typing import Set, Tuple

import networkx as nx
import numpy

from src.kcenter.constant.colour import Colour


def get_available_graphs() -> Set[str]:
    """:return: List of names of all text files from src/server/dataset
    """
    return set(file[0:-4] for file in os.listdir(f"{os.path.dirname(__file__)}/dataset") if file.endswith(".txt"))


def calculate_edges(graph: nx.Graph):
    """calculate Euclidian distance for all edges (non self-loop) of a graph
    """
    for n in graph.nodes():
        for m in graph.nodes():
            if n == m:
                continue
            weight = numpy.linalg.norm(graph.nodes[n]["pos"] - graph.nodes[m]["pos"])
            graph.add_edge(n, m, key=str(n) + str(m), weight=weight)


class GraphLoader:
    graphs = get_available_graphs()

    @staticmethod
    def parse_header(header: str) -> Tuple[int, int, int, int, int, int, float, int]:
        """Return K-Center parameters from a space seperated string

        :param header: String formatted like the following: "NODE_COUNT K TOTAL_BLUE TOTAL_RED MIN_BLUE MIN_RED OPT OUT"
        e.g. "4 2 2 2 1 1 2.2 0"
        """
        header = header.split(" ")
        node_count = int(header[0])
        k = int(header[1])
        blue = int(header[2])
        red = int(header[3])
        min_blue = int(header[4])
        min_red = int(header[5])
        opt = float(header[6])
        outliers = int(header[7])
        return node_count, k, blue, red, min_blue, min_red, opt, outliers

    @staticmethod
    def parse_row(row: str) -> Tuple[float, float, str]:
        """Return data point properties from a space seperated string

        :param row: String formatted like the following: "X Y COLOUR"
        e.g. "1.2 2.1 blue"
        """
        row = row.split(" ")
        x = float(row[0])
        y = float(row[1])
        colour = str(row[2]).replace("\n", "")
        return x, y, colour

    @staticmethod
    def get_json(graph_name: str):
        """Create a dictionary representation of a graph, which can be sent as json
        """
        if graph_name not in GraphLoader.graphs:
            return None
        f = open(f"{os.path.dirname(__file__)}/dataset/{graph_name}.txt", "r")
        node_count, k, blue, red, min_blue, min_red, opt, outliers = GraphLoader.parse_header(f.readline())

        data = []
        for i in range(node_count):
            x, y, colour = GraphLoader.parse_row(f.readline())
            data.append({"x": x, "y": y, "colour": colour})
        f.close()

        meta_data = GraphLoader.get_json_meta_data(graph_name)
        return {**{"data": data}, **meta_data}

    @staticmethod
    def save_json(json, name: str):
        if name in GraphLoader.graphs:
            raise ValueError("Graph already exists")
        f = open(f"{os.path.dirname(__file__)}/dataset/{name}.txt", "w")
        f.write(
            f'{json["nodes"]} {json["optimalSolution"]["k"]} {json["blue"]} {json["red"]} {json["optimalSolution"]["minBlue"]} {json["optimalSolution"]["minRed"]} {json["optimalSolution"]["radius"]} {json["optimalSolution"]["outliers"]}\n')
        data = json["data"]
        for i, point in enumerate(data):
            if i > 0:
                f.write("\n")
            f.write(f'{point["x"]} {point["y"]} {point["colour"]}')
        f.close()
        GraphLoader.graphs.add(name)

    @staticmethod
    def get_json_meta_data(graph_name: str):
        """Return number of nodes, number of blue nodes and number of red nodes
        """
        if graph_name not in GraphLoader.graphs:
            return None
        with open(f"{os.path.dirname(__file__)}/dataset/{graph_name}.txt", "r") as f:
            node_count, k, blue, red, min_blue, min_red, opt, outliers = GraphLoader.parse_header(f.readline())
            return {
                "nodes": node_count,
                "blue": blue,
                "red": red,
                "optimalSolution": {
                    "k": k,
                    "minBlue": min_blue,
                    "minRed": min_red,
                    "radius": opt,
                    "outliers": outliers
                }
            }

    @staticmethod
    def get_graph(graph_name: str) -> nx.Graph:
        """Create a NetworkX representation of the graph
        """
        if graph_name not in GraphLoader.graphs:
            return None
        f = open(f"{os.path.dirname(__file__)}/dataset/{graph_name}.txt", "r")
        node_count, k, blue, red, min_blue, min_red, opt, outliers = GraphLoader.parse_header(f.readline())

        G = nx.Graph()
        for i in range(node_count):
            x, y, colour = GraphLoader.parse_row(f.readline())
            G.add_node(i, pos=numpy.array((x, y)), colour=Colour[colour.upper()])
        f.close()

        calculate_edges(G)
        return G
