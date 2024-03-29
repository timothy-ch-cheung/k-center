import glob
import os
import re
from typing import Tuple, Dict, List

import networkx as nx
from haversine import haversine

from src.kcenter.constant.colour import Colour


class GowGraphLoader:
    @staticmethod
    def parse_header(header: str) -> Tuple[int, int, int, int, float, int, int]:
        """Header format: nodes, blue, red, k, mean consumption, min_blue, min_red

        :param header: header from the Gowalla problem instance
        :return: number of vertices, number of edges, k
        """
        header = header.strip().split(" ")
        num_vertices = int(header[0])
        num_blue = int(header[1])
        num_red = int(header[2])
        k = int(header[3])
        mean_consumption = float(header[4])
        min_blue = int(header[5])
        min_red = int(header[6])
        return num_vertices, num_blue, num_red, k, mean_consumption, min_blue, min_red

    @staticmethod
    def parse_edge(node: str) -> Tuple[int, float, float, int]:
        """Node format: location_id, latitude, longitude, visits

        :param header: edge line from the ORLIB problem instance
        :return: location_id, latitude, longitude, visits
        """
        node = node.strip().split(" ")
        location_id = int(node[0])
        latitude = float(node[1])
        longitude = float(node[2])
        visits = int(node[3])
        return location_id, latitude, longitude, visits

    @staticmethod
    def get_header(graph_name: str):
        with open(f"{os.path.dirname(__file__)}/dataset/GOWALLA/{graph_name}.txt", "r") as f:
            num_vertices, num_blue, num_red, k, mean_consumption, min_blue, min_red =  GowGraphLoader.parse_header(f.readline())
            return num_vertices, num_blue, num_red, k, min_blue, min_red

    @staticmethod
    def get_graph(graph_name: str) -> nx.Graph:
        G = nx.Graph()
        with open(f"{os.path.dirname(__file__)}/dataset/GOWALLA/{graph_name}.txt", "r") as f:
            num_vertices, num_blue, num_red, k, mean_consumption, min_blue, min_red = GowGraphLoader.parse_header(f.readline())
            G.graph["n"] = num_vertices
            G.graph["k"] = k
            G.graph["min_blue"] = min_blue
            G.graph["min_red"] = min_red

            for idx, line in enumerate(f.readlines()):
                location_id, latitude, longitude, visits = GowGraphLoader.parse_edge(line)
                col = Colour.BLUE if visits > mean_consumption else Colour.RED
                G.add_node(idx, lat=latitude, lon=longitude, colour=col, loc_id=location_id)

        for i in G.nodes():
            for j in G.nodes():
                point_a = (G.nodes()[i]["lat"], G.nodes()[i]["lon"])
                point_b = (G.nodes()[j]["lat"], G.nodes()[j]["lon"])
                distance = haversine(point_a, point_b)
                G.add_edge(i, j, key=str(i) + str(j), weight=distance)
                G.add_edge(j, i, key=str(j) + str(i), weight=distance)

        return G

    @staticmethod
    def get_problem_list():
        problems = glob.glob(f"{os.path.dirname(__file__)}/dataset/GOWALLA/gow*.txt")
        folder_name = f"GOWALLA{os.path.sep}"
        problems = [x[x.index(folder_name) + len(folder_name):] for x in problems]
        problem_names: List[str] = []
        reg = re.compile(f".*(?=.txt)")
        for path in problems:
            result = reg.search(path)
            name = result.group(0)
            problem_names.append(name)

        return problem_names
