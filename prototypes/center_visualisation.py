import matplotlib as matplotlib
import matplotlib.pyplot as plt

from kcenter.pbs.similarity import CompareSolution
from server.graph_loader import GraphLoader

colors = ["#00000040", "#00FF0080", "#FF000080"]

#graph = GraphLoader.get_graph("medium")
graph = GraphLoader.get_graph("large")

x = [graph.nodes()[i]["pos"][0] for i in graph.nodes()]
y = [graph.nodes()[i]["pos"][1] for i in graph.nodes()]
color_indices = [0 for i in range(len(x))]

# expected_population = [
#     {8, 1, 12, 21},
#     {16, 3, 4, 23},
#     {9, 10, 3, 15},
#     {0, 9, 4, 21},
#     {17, 19, 14, 23},
#     {10, 3, 14, 23},
#     {18, 23, 21, 15},
#     {0, 18, 3, 13}
# ]

expected_population = [
    {103, 106, 12, 15, 91},
    {106, 108, 51, 60, 29},
    {106, 44, 108, 49, 56},
    {97, 106, 46, 113, 50},
    {64, 108, 22, 60, 29},
    {106, 44, 52, 89, 92},
    {106, 16, 22, 27, 29},
    {70, 42, 106, 45, 24}
]

first_individual = 1
x += [graph.nodes()[i]["pos"][0] for i in expected_population[first_individual]]
y += [graph.nodes()[i]["pos"][1] for i in expected_population[first_individual]]
color_indices += [1 for x in range(5)]

second_individual = 0
x += [graph.nodes()[i]["pos"][0] for i in expected_population[second_individual]]
y += [graph.nodes()[i]["pos"][1] for i in expected_population[second_individual]]
color_indices += [2 for x in range(5)]

# PLOT
colormap = matplotlib.colors.ListedColormap(colors)
plt.scatter(x, y, c=color_indices, cmap=colormap)
plt.show()

# Similarity

MIN = (34.78753471028318, 42.83698613479884)
MAX = (196.61095005621613, 178.77089875665393)
comp = CompareSolution(graph, min_value=MIN, max_value=MAX)

print(comp.sim(expected_population[first_individual], expected_population[second_individual]))
print(comp.sim(expected_population[second_individual], expected_population[first_individual]))
