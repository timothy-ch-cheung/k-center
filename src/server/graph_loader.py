import os
from typing import Set, Tuple

import networkx as nx
import numpy

from src.kcenter.constant.colour import Colour


def get_available_graphs() -> Set[str]:
    return set(file[0:-4] for file in os.listdir(f"{os.path.dirname(__file__)}/dataset") if file.endswith(".txt"))


def calculate_edges(graph: nx.Graph):
    for n in graph.nodes():
        for m in graph.nodes():
            if n == m:
                continue
            weight = numpy.linalg.norm(graph.nodes[n]["pos"] - graph.nodes[m]["pos"])
            graph.add_edge(n, m, key=str(n) + str(m), weight=weight)


class GraphLoader:
    graphs = get_available_graphs()

    @staticmethod
    def parse_header(header: str) -> Tuple[int, int, int, int]:
        header = header.split(" ")
        node_count = int(header[0])
        k = int(header[1])
        blue = int(header[2])
        red = int(header[3])
        return node_count, k, blue, red

    @staticmethod
    def parse_row(row: str) -> Tuple[float, float, str]:
        row = row.split(" ")
        x = float(row[0])
        y = float(row[1])
        colour = str(row[2]).replace("\n", "")
        return x, y, colour

    @staticmethod
    def get_json(graph_name: str):
        if graph_name not in GraphLoader.graphs:
            return None
        f = open(f"{os.path.dirname(__file__)}/dataset/{graph_name}.txt", "r")
        node_count, k, blue, red = GraphLoader.parse_header(f.readline())

        data = []
        for i in range(node_count):
            x, y, colour = GraphLoader.parse_row(f.readline())
            data.append({"x": x, "y": y, "colour": colour})
        f.close()

        json = {}
        json["k"] = k
        json["blue"] = blue
        json["red"] = red
        json["nodes"] = node_count
        json["data"] = data
        return json

    @staticmethod
    def get_graph(graph_name: str):
        if graph_name not in GraphLoader.graphs:
            return None
        f = open(f"{os.path.dirname(__file__)}/dataset/{graph_name}.txt", "r")
        node_count, k, blue, red = GraphLoader.parse_header(f.readline())

        G = nx.Graph()
        for i in range(node_count):
            x, y, colour = GraphLoader.parse_row(f.readline())
            G.add_node(i, pos=numpy.array((x, y)), colour=Colour[colour.upper()])

        calculate_edges(G)
        return G
