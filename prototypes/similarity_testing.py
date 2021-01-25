from kcenter.pbs.similarity import CompareSolution
from server.graph_loader import GraphLoader

graph = GraphLoader.get_graph("medium")
MIN = (34.78753471028318, 42.83698613479884)
MAX = (196.61095005621613, 178.77089875665393)
comp = CompareSolution(graph, min_value=MIN, max_value=MAX)

print(comp.sim({4, 7, 15, 17}, {5, 6, 16, 18}))