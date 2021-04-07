import random
import time

import numpy as np

from kcenter.pbs.target_pbs import TargetPBS
from server.orlib_graph_loader import ORLIBGraphLoader


def benchmark(problem_instance: str, target: float, verbose: bool = False):
    graph = ORLIBGraphLoader.get_graph(problem_instance)
    instance = TargetPBS(graph, graph.graph["k"], {})

    TRIALS = 100
    costs = []
    durations = []

    for i in range(TRIALS):
        random.seed(i)
        start = time.time()
        clusters, outliers, radius = instance.target_solve(target_cost=target)
        duration = time.time() - start
        costs.append(radius)
        durations.append(duration)
        if verbose:
            print(i, round(radius, 3), round(duration, 3))

    cost_stats = f"COST[mean={np.mean(costs)}, std={np.std(costs)}]"
    time_stats = f"TIME[mean={np.mean(durations)}, std={np.std(durations)}]"
    print(f"{problem_instance}: {cost_stats} {time_stats}")

optimal_costs = ORLIBGraphLoader.get_opt()

for i in range(1, 41):
    problem = f"pmed{i}"
    benchmark(problem, optimal_costs[problem])
