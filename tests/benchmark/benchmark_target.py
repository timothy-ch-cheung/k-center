import random
import time

import numpy as np

from kcenter.pbs.target_pbs import TargetPBS
from server.orlib_graph_loader import ORLIBGraphLoader
from src.kcenter.constant.colour import Colour

graph = ORLIBGraphLoader.get_graph("pmed1")
k = graph.graph["k"]
constraints = {Colour.BLUE: 100, Colour.RED: 0}
target = 127
instance = TargetPBS(graph, k, constraints)

TRIALS = 100
costs = []
durations = []

print("COST TIME")
for i in range(TRIALS):
    start = time.time()
    random.seed(i)
    clusters, outliers, radius = instance.target_solve(target_cost=target)
    duration = time.time() - start
    costs.append(radius)
    durations.append(duration)
    print(i, round(radius, 3), round(duration, 3))

print(f"COST: mean={np.mean(costs)} std={np.std(costs)}")
print(f"TIME: mean={np.mean(durations)} std={np.std(durations)}")
