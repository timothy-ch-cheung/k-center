from kcenter.constant.colour import Colour
from kcenter.verify.verify import verify_k_center_solution
from server.graph_loader import GraphLoader

graph = GraphLoader.get_graph("large")

centers = {4, 68, 72, 11, 76, 34, 108, 111, 113, 61}
cost = 34.182478925582565
constraints = {Colour.BLUE: 50, Colour.RED: 50}
k = 10

print(verify_k_center_solution(graph, centers, k, cost))
