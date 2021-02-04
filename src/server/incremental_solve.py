import time

from flask import request, Blueprint, jsonify

from src.kcenter.pbs.stepped_pbs import SteppedPBS
from src.kcenter.bandyapadhyay.stepped_solver import SteppedConstantColourful
from src.kcenter.bandyapadhyay.stepped_pseudo_solver import SteppedConstantPseudoColourful
from src.kcenter.greedy.stepped_greedy import SteppedGreedy
from src.kcenter.greedy.stepped_greedy_reduce import SteppedGreedyReduce
from src.kcenter.constant.colour import Colour
from src.server.graph_loader import GraphLoader
from src.server.routes import repackage_solution

step = Blueprint('step', __name__)

problem_instances = {}

stepped_algorithms = {
    "greedy": SteppedGreedy,
    "greedy_reduce": SteppedGreedyReduce,
    "colourful_bandyapadhyay_pseudo": SteppedConstantPseudoColourful,
    "colourful_bandyapadhyay": SteppedConstantColourful,
    "pbs": SteppedPBS
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


def process_standard(graph, graph_name, step, time_elapsed):
    solutions, label, is_active = step

    data = []
    nodes = list(graph.nodes())
    for node in nodes:
        position = graph.nodes()[node]["pos"]
        point_data = {"x": position[0], "y": position[1], "colour": graph.nodes()[node]["colour"].name.lower()}
        data.append(point_data)

    solutions_json = []
    for solution in solutions:
        solutions_json.append({**solution.to_json(graph), **{"timeTaken": time_elapsed}})

    solution = {"data": data,
                "solutions": solutions_json,
                "step": {"label": label, "active": is_active},
                **GraphLoader.get_json_meta_data(graph_name)
                }
    return solution, is_active


def process_genetic(graph, graph_name, step):
    solutions, label, is_active = step
    data = []
    nodes = list(graph.nodes())
    for node in nodes:
        position = graph.nodes()[node]["pos"]
        point_data = {"x": position[0], "y": position[1], "colour": graph.nodes()[node]["colour"].name.lower()}
        data.append(point_data)
    solution = {"data": data, "solutions": solutions, "step": {"label": label, "active": is_active}}
    solution = {**solution, **GraphLoader.get_json_meta_data(graph_name)}
    return solution, is_active


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
    step = next(generator)
    end = time.time()
    time_elapsed = end - start

    if len(step) == 3:
        solution, is_active = process_standard(graph, graph_name, step, time_elapsed)
    else:
        solution, is_active = process_genetic(graph, graph_name, step)

    if not is_active:
        del problem_instances[id]

    return jsonify(solution)
