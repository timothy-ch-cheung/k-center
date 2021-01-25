from kcenter.constant.colour import Colour
from kcenter.pbs.pbs import PBS
from server.graph_loader import GraphLoader
import time
import numpy as np

graph = GraphLoader.get_graph("large")
instance = PBS(graph, 10, {Colour.BLUE: 50, Colour.RED: 50})

TRIALS = 100
costs = []
durations = []

print("COST TIME")
for i in range(TRIALS):
    start = time.time()
    clusters, outliers, radius = instance.solve()
    duration = time.time() - start
    costs.append(radius)
    durations.append(durations)
    print(round(radius, 3), round(duration, 3))

print(f"COST: mean={np.mean(costs)} std={np.std(costs)}")
print(f"TIME: mean={np.mean(durations)} std={np.std(durations)}")
