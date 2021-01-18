from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import PBS
from src.server.graph_loader import GraphLoader

graph = GraphLoader.get_graph("large")
instance = PBS(graph, 4, {Colour.BLUE: 10, Colour.RED: 10})
clusters, outliers, radius = instance.solve()
print(clusters)
print(f'cost: {radius}')
