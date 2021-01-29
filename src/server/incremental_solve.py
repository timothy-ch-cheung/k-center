import time

from flask import request, Blueprint, jsonify

from src.kcenter.greedy.stepped_greedy import SteppedGreedy
from src.kcenter.greedy.stepped_greedy_reduce import SteppedGreedyReduce
from src.kcenter.constant.colour import Colour
from src.server.graph_loader import GraphLoader
from src.server.routes import repackage_solution

step = Blueprint('step', __name__)

problem_instances = {}

stepped_algorithms = {
    "greedy": SteppedGreedy,
    "greedy_reduce": SteppedGreedyReduce
}


@step.route('/api/v1/step/start', methods=["POST"])
def start():
    request_data = request.get_json()
    id = request_data["id"]

    k, blue, red = request_data['k'], request_data['blue'], request_data['red']
    constraints = {Colour.BLUE: blue, Colour.RED: red}

    graph_name = request_data['graph']
    graph = GraphLoader.get_graph(graph_name)
    algorithm = request_data['algorithm']

    instance = stepped_algorithms[algorithm](graph, k, constraints)
    generator = instance.generator()
    problem_instances[id] = {"instance": instance, "generator": generator, "name": graph_name}
    return '', 204


@step.route('/api/v1/step/next', methods=["POST"])
def next_step():
    request_data = request.get_json()
    id = request_data["id"]

    if id not in problem_instances:
        return jsonify({"message": f"{id} is not an active problem instance"}), 404

    problem_instance = problem_instances[id]
    generator = problem_instance["generator"]
    graph = problem_instance["instance"].graph
    graph_name = problem_instance["name"]

    start = time.time()
    clusters, outliers, radius, label, is_active = next(generator)
    end = time.time()
    time_elapsed = end - start
    solution = repackage_solution(graph, clusters, outliers, radius, time_elapsed)
    solution = {**solution, **GraphLoader.get_json_meta_data(graph_name)}
    solution["step"] = {"label": label, "active": is_active}

    if not is_active:
        del problem_instances[id]

    return jsonify(solution)
