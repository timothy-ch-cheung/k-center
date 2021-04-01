import os
from typing import Tuple, Dict

import networkx as nx
import numpy

from server.graph_loader import calculate_edges


class TSPLIBGraphLoader:

    @staticmethod
    def parse_node(node: str) -> Tuple[int, int, float]:
        """Header format: id, x coordinate, y coordinate

        :param header: node line from the TSPLIB problem instance
        :return: id, x_coord, y_coord
        """
        node = node.strip().split(" ")
        id = int(node[0])
        x_coord = int(node[1])
        y_coord = float(node[2])
        return id, x_coord, y_coord

    @staticmethod
    def get_graph(graph_name: str) -> nx.Graph:
        G = nx.Graph()
        with open(f"{os.path.dirname(__file__)}/dataset/TSPLIB/{graph_name}.tsp", "r") as f:

            for line in f.readlines()[6:-1]:
                node, x_coordinate, y_coordinate = TSPLIBGraphLoader.parse_node(line)
                G.add_node(node, pos=numpy.array((x_coordinate, y_coordinate)))

        calculate_edges(G)
        return G

    @staticmethod
    def get_opt() -> Dict[str, Dict[int,float]]:
        opt = dict()
        with open(f"{os.path.dirname(__file__)}/dataset/TSPLIB/opt.txt", "r") as f:
            for line in f.readlines():
                line = line.strip().split(" ")
                name = line[0]
                k = int(line[1])
                optimal_cost = float(line[2])
                if name not in opt:
                    opt[name] = dict()

                opt[name][k] = optimal_cost
        return opt