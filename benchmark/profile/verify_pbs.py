from kcenter.constant.colour import Colour
from kcenter.verify.verify import verify_k_center_solution, verify_solution
from server.graph_loader import GraphLoader

graph = GraphLoader.get_graph("large")

centers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
cost = 12.5

constraints = {Colour.BLUE: 50, Colour.RED: 50}
k = 10

print(verify_solution(graph, constraints, k, cost, centers))
