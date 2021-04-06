import glob
import os
import re
from typing import Tuple, Dict, List

import networkx as nx


class ORLIBGraphLoader:
    @staticmethod
    def parse_header(header: str) -> Tuple[int, int, int]:
        """Header format: vertices, number of edges, p

        :param header: header from the ORLIB problem instance
        :return: number of vertices, number of edges, k
        """
        header = header.strip().split(" ")
        num_vertices = int(header[0])
        num_edges = int(header[1])
        k = int(header[2])
        return num_vertices, num_edges, k

    @staticmethod
    def parse_edge(edge: str) -> Tuple[int, int, float]:
        """Header format: start vertex, end vertex, cost

        :param header: edge line from the ORLIB problem instance
        :return: start vertex, end vertex, cost
        """
        edge = edge.strip().split(" ")
        start_vertex = int(edge[0])
        end_vertex = int(edge[1])
        cost = float(edge[2])
        return start_vertex, end_vertex, cost

    @staticmethod
    def get_graph(graph_name: str) -> nx.Graph:
        G = nx.Graph()
        with open(f"{os.path.dirname(__file__)}/dataset/ORLIB/{graph_name}.txt", "r") as f:
            num_vertices, num_edges, k = ORLIBGraphLoader.parse_header(f.readline())
            G.graph["k"] = k

            for vertex in range(1, num_vertices + 1):
                G.add_node(vertex)

            for line in f.readlines():
                start_vertex, end_vertex, cost = ORLIBGraphLoader.parse_edge(line)
                G.add_edge(start_vertex, end_vertex, key=str(start_vertex) + str(end_vertex), weight=cost)
                G.add_edge(end_vertex, start_vertex, key=str(end_vertex) + str(start_vertex), weight=cost)

        shortest_paths = nx.algorithms.shortest_paths.floyd_warshall(G)

        for start_vertex, neighbours in shortest_paths.items():
            for end_vertex, cost in neighbours.items():
                G.add_edge(start_vertex, end_vertex, key=str(start_vertex) + str(end_vertex), weight=cost)
        return G

    @staticmethod
    def get_opt() -> Dict[str, float]:
        opt = dict()
        with open(f"{os.path.dirname(__file__)}/dataset/ORLIB/kcenteropt.txt", "r") as f:
            for line in f.readlines():
                line = line.strip().split(" ")
                problem_instance = line[0]
                optimal = float(line[1])
                opt[problem_instance] = optimal
        return opt

    @staticmethod
    def get_problem_list():
        problems = glob.glob(f"{os.path.dirname(__file__)}/dataset/ORLIB/pmed*.txt")
        problem_names: List[str] = []
        reg = re.compile("(?<=ORLIB\\\\).*(?=.txt)")
        for path in problems:
            result = reg.search(path)
            name = result.group(0)
            problem_names.append(name)

        return problem_names
