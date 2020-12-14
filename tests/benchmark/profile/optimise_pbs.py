from kcenter.constant.colour import Colour
from kcenter.pbs.pbs import PBS
from server.graph_loader import GraphLoader

graph = GraphLoader.get_graph("large")
instance = PBS(graph, 4, {Colour.BLUE: 10, Colour.RED: 10})
clusters, outliers, radius = instance.solve()
print(clusters)
print(f'cost: {radius}')
