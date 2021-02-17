import random

from kcenter.constant.colour import Colour
from kcenter.pbs.pbs import PBS, Individual
from server.graph_loader import GraphLoader
from server.orlib_graph_loader import ORLIBGraphLoader

random.seed(0)

graph = ORLIBGraphLoader.get_graph("pmed3")
constraints = {}
k = 10

instance = PBS(graph, k, constraints)

sol1 = Individual({32, 36, 77, 48, 81, 18, 82, 49, 52, 87})
instance.init_individual(sol1)

sol2 = Individual({32, 36, 77, 48, 17, 82, 51, 52, 55, 87})
instance.init_individual(sol2)

for i in range(20):
    sol1 = instance.local_search(instance.mutation_random(sol1), 20)

print()
