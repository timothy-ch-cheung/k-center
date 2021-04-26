import glob
import os
import re
from pathlib import Path
from typing import Set, Tuple, List, Dict

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
    nodes = set(graph.nodes())
    for n in graph.nodes():
        for m in nodes:
            if n == m:
                continue
            weight = numpy.linalg.norm(graph.nodes[n]["pos"] - graph.nodes[m]["pos"])
            graph.add_edge(n, m, key=str(n) + str(m), weight=weight)
            graph.add_edge(m, n, key=str(m) + str(n), weight=weight)
        nodes.remove(n)


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
        graph_file = Path(f"{os.path.dirname(__file__)}/dataset/{graph_name}.txt")
        if not graph_file.is_file():
            return None
        f = open(f"{os.path.dirname(__file__)}/dataset/{graph_name}.txt", "r")
        node_count, k, blue, red, min_blue, min_red, opt, outliers = GraphLoader.parse_header(f.readline())

        G = nx.Graph()
        G.graph["n"] = node_count
        G.graph["k"] = k
        G.graph["min_blue"] = min_blue
        G.graph["min_red"] = min_red
        G.graph["opt"] = opt

        for i in range(node_count):
            x, y, colour = GraphLoader.parse_row(f.readline())
            G.add_node(i, pos=numpy.array((x, y)), colour=Colour[colour.upper()])
        f.close()

        calculate_edges(G)
        return G

    @staticmethod
    def get_problem_list(dataset_name: str = "SYNTHETIC"):
        problems = glob.glob(f"{os.path.dirname(__file__)}/dataset/{dataset_name}/*.txt")
        folder_name = f"{dataset_name}{os.path.sep}"
        problems = [x[x.index(folder_name) + len(folder_name):] for x in problems]
        problem_names: List[str] = []
        reg = re.compile(f".*(?=.txt)")
        for path in problems:
            result = reg.search(path)
            name = result.group(0)
            problem_names.append(name)

        return problem_names

    @staticmethod
    def get_opt(dataset_name: str = "SYNTHETIC") -> Dict[str, float]:
        optimal_costs = dict()
        for problem in GraphLoader.get_problem_list():
            f = open(f"{os.path.dirname(__file__)}/dataset/{dataset_name}/{problem}.txt", "r")
            node_count, k, blue, red, min_blue, min_red, opt, outliers = GraphLoader.parse_header(f.readline())
            optimal_costs[problem] = opt
        return optimal_costs