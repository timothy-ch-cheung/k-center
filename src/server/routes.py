from flask import render_template, request, jsonify, Blueprint

from src.kcenter.bandyapadhyay.solver import ConstantColourfulKCenterSolver
from src.kcenter.constant.colour import Colour
from src.kcenter.greedy.greedy import GreedySolver
from src.kcenter.greedy.greedy_reduce import GreedyReduceSolver
from src.server.graphs import graphs
from tests.kcenter.util.create_test_graph import basic_graph, basic_graph_with_outlier

main = Blueprint('main', __name__)


@main.route("/")
def index():
    return render_template('index.html')


@main.route('/api/v1/graph/<name>', methods=["GET"])
def get_graph(name):
    return graphs[name]


def determine_graph(name):
    if name == "basic":
        return basic_graph()
    elif name == "basic_with_outlier":
        return basic_graph_with_outlier()


def repackage_solution(graph, clusters, outliers, radius):
    def to_colour(colour: Colour):
        colours = {
            1: "blue",
            2: "red"
        }
        return colours[colour]

    json = {"centerRadius": radius}
    data = []
    nodes = list(graph.nodes())
    for node in nodes:
        point_data = {}
        if node in clusters:
            point_data["center"] = True
        position = graph.nodes()[node]["pos"]
        point_data["x"] = position[0]
        point_data["y"] = position[1]
        point_data["colour"] = to_colour(graph.nodes()[node]["colour"])
        data.append(point_data)
    json["data"] = data
    return json


@main.route('/api/v1/solve', methods=["POST"])
def solve():
    request_data = request.get_json()
    k = request_data['k']

    blue = request_data['blue']
    red = request_data['red']
    constraints = {Colour.BLUE: blue, Colour.RED: red}

    graph = determine_graph(request_data['graph'])
    algorithm = request_data['algorithm']

    instance = None
    if algorithm == "greedy":
        instance = GreedySolver(graph, k, constraints)
    elif algorithm == "greedy_reduce":
        instance = GreedyReduceSolver(graph, k, constraints)
    elif algorithm == "colourful_bandyapadhyay":
        instance = ConstantColourfulKCenterSolver(graph, k, constraints)

    clusters, outliers, radius = instance.solve()
    return jsonify(repackage_solution(graph, clusters, outliers, radius))
