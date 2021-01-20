from kcenter.constant.colour import Colour
from kcenter.verify.verify import verify_k_center_solution
from server.graph_loader import GraphLoader

graph = GraphLoader.get_graph("large")

centers = {97, 99, 101, 106, 111, 50, 54, 56, 28, 61}
cost = 36.18065589367729

constraints = {Colour.BLUE: 50, Colour.RED: 50}
k = 10

print(verify_k_center_solution(graph, centers, k, cost))
