import time

from kcenter.brute_force.brute_force_colourful_k_center import BruteForceColourfulKCenter
from kcenter.constant.colour import Colour
from server.gow_graph_loader import GowGraphLoader

graph = GowGraphLoader.get_graph("gow41")
print()
k = graph.graph["k"]
min_blue = graph.graph["min_blue"]
min_red = graph.graph["min_red"]

start_time = time.time()
solver = BruteForceColourfulKCenter(graph, k, {Colour.BLUE: min_blue, Colour.RED: min_red})
print(f"Brute forcing will take approximately {solver.predict_time()} seconds")
clusters, outliers, radius = solver.solve()
end_time = time.time()
time_taken = end_time - start_time

print(f"time taken: {time_taken}")
print(f"optimal cost: {radius}")

with open("gow41_opt.txt", "w") as f:
    f.write(f"opt={radius}\n")
    f.write(f"centers={list(clusters.keys())}\n")
    f.write(f"outliers={list(outliers)}\n")
    f.write(f"time_taken={time_taken}\n")
