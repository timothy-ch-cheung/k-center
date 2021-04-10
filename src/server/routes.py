import time

import networkx as nx
from flask import render_template, request, jsonify, Blueprint

from src.kcenter.pbs.target_pbs import TargetPBS
from src.kcenter.plateau_surfer.plateau_surfer import PlateauSurfer
from src.kcenter.bandyapadhyay.pseudo_solver import ConstantPseudoColourful
from src.kcenter.bandyapadhyay.solver import ConstantColourful
from src.kcenter.brute_force.brute_force_colourful_k_center import BruteForceColourfulKCenter
from src.kcenter.brute_force.brute_force_k_center import BruteForceKCenter
from src.kcenter.colourful_pbs.colourful_pbs import ColourfulPBS
from src.kcenter.constant.colour import Colour
from src.kcenter.greedy.greedy import Greedy
from src.kcenter.greedy.greedy_reduce import GreedyReduce
from src.kcenter.pbs.pbs import PBS
from src.server.graph_loader import GraphLoader
from src.util.time_converter import seconds_to_string

main = Blueprint('main', __name__)
k_center_algorithms = {
    "greedy": Greedy,
    "greedy_reduce": GreedyReduce,
    "colourful_bandyapadhyay_pseudo": ConstantPseudoColourful,
    "colourful_bandyapadhyay": ConstantColourful,
    "pbs": PBS,
    "target_pbs": TargetPBS,
    "colourful_pbs": ColourfulPBS,
    "brute_force_k_center": BruteForceKCenter,
    "brute_force_colourful_k_center": BruteForceColourfulKCenter,
    "grasp": PlateauSurfer
}


class ResponseTypes:
    PREDICTED_TIME = "predicted_time"


@main.route("/")
@main.route("/solve")
@main.route("/steps")
def index():
    return render_template('index.html')


@main.route('/api/v1/graph/<name>', methods=["GET"])
def get_graph(name):
    return GraphLoader.get_json(name)


def get_point_list(graph: nx.Graph):
    data = []
    nodes = list(graph.nodes())
    for node in nodes:
        position = graph.nodes()[node]["pos"]
        point_data = {"x": position[0], "y": position[1], "colour": graph.nodes()[node]["colour"].name.lower()}
        data.append(point_data)
    return data


def repackage_solution(graph: nx.Graph, clusters, outliers, radius, time_elapsed):
    """Reformat the clusters, outliers and radius to be in a format that the front-end can process
    """
    data = get_point_list(graph)

    centers = [{"x": pos[0], "y": pos[1]} for pos in [graph.nodes()[i]["pos"] for i in clusters.keys()]]
    solution = {
        "k": len(centers),
        "radius": radius,
        "outliers": len(outliers),
        "timeTaken": time_elapsed,
        "centers": centers
    }
    return {"data": data, "solutions": [solution]}


def repackage_notice(graph: nx.Graph, alert: str, algorithm: str):
    data = get_point_list(graph)
    alert = {"message": alert, "type": f"{algorithm}_{ResponseTypes.PREDICTED_TIME}"}
    return {"data": data, "alert": alert}


@main.route('/api/v1/solve', methods=["POST"])
def solve():
    request_data = request.get_json()
    k, blue, red = request_data['k'], request_data['blue'], request_data['red']
    constraints = {Colour.BLUE: blue, Colour.RED: red}

    graph_name = request_data['graph']
    graph = GraphLoader.get_graph(graph_name)
    algorithm = request_data['algorithm']

    instance = k_center_algorithms[algorithm](graph, k, constraints)

    if algorithm.startswith("brute_force") and len(graph.nodes()) > 50:
        estimated_time = instance.predict_time()
        message = f"Solving was not attempted, on this server, it would take {seconds_to_string(estimated_time)} to solve"
        sol_data = repackage_notice(graph, message, algorithm)
    else:
        start = time.time()
        clusters, outliers, radius = instance.solve()
        end = time.time()
        time_elapsed = end - start
        sol_data = repackage_solution(graph, clusters, outliers, radius, time_elapsed)

    solution = {**sol_data, **GraphLoader.get_json_meta_data(graph_name)}

    return jsonify(solution)
