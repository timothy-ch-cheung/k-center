import random

from kcenter.constant.colour import Colour
from kcenter.pbs.pbs import PBS, Individual
from server.graph_loader import GraphLoader

random.seed(0)

graph = GraphLoader.get_graph("large")
constraints = {Colour.BLUE: 50, Colour.RED: 50}
k = 5

instance = PBS(graph, k, constraints)

sol1 = Individual({106, 12, 81, 89, 92})
instance.init_individual(sol1)

sol2 = Individual({106, 12, 45, 86, 92})
instance.init_individual(sol2)

opt1 = instance.local_search(sol1, 2)

opt2 = instance.local_search(sol2, 2)

print()
