import cProfile
import pstats

from kcenter.pbs.target_pbs import TargetPBS
from kcenter.verify.verify import verify_k_center_solution
from server.orlib_graph_loader import ORLIBGraphLoader
from src.kcenter.constant.colour import Colour

# graph = GraphLoader.get_graph("k_center")
# constraints = {Colour.BLUE: 0, Colour.RED: 20}
# k = 5
# target = 5.0

# graph = GraphLoader.get_graph("large")
# constraints = {Colour.BLUE: 50, Colour.RED: 50}
# k = 5
# target = 45.406651436823594

# graph = GraphLoader.get_graph("medium")
# constraints = {Colour.BLUE: 10, Colour.RED: 10}
# k = 4
# target = 45.40201898472788

# graph = GraphLoader.get_graph("basic")
# constraints = {Colour.BLUE: 2, Colour.RED: 2}
# k = 2
# target = 0.7280109889280517

# graph = GraphLoader.get_graph("thousand")
# constraints = {Colour.BLUE: 500, Colour.RED: 500}
# k = 50

graph = ORLIBGraphLoader.get_graph("pmed1")
constraints = {Colour.BLUE: 100, Colour.RED: 0}
k = graph.graph["k"]
target = 127

instance = TargetPBS(graph, k, constraints)

profiler = cProfile.Profile()
profiler.enable()
clusters, outliers, radius = instance.target_solve(target_cost=target)
profiler.disable()
stats = pstats.Stats(profiler).sort_stats('cumtime')
stats.print_stats()
# stats = pstats.Stats(profiler).sort_stats('tottime')
# stats.print_stats()

print("cost", radius)
print("centers", set(clusters.keys()))
print("clusters", clusters)
print("outliers", outliers)

print(verify_k_center_solution(graph, set(clusters.keys()), k, radius))
