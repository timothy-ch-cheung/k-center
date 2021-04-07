import cProfile
import pstats

from kcenter.plateau_surfer.plateau_surfer import PlateauSurfer
from kcenter.verify.verify import verify_solution
from server.tsplib_graph_loader import TSPLIBGraphLoader
from src.kcenter.constant.colour import Colour

# graph = GraphLoader.get_graph("k_center")
# constraints = {Colour.BLUE: 0, Colour.RED: 20}
# k = 5

# graph = GraphLoader.get_graph("large")
# constraints = {Colour.BLUE: 50, Colour.RED: 50}
# k = 5

graph = TSPLIBGraphLoader.get_graph("pr226")
constraints = {Colour.BLUE: 226, Colour.RED: 0}
k = 40

# graph = GraphLoader.get_graph("medium")
# constraints = {Colour.BLUE: 10, Colour.RED: 10}
# k = 4

# graph = GraphLoader.get_graph("basic")
# constraints = {Colour.BLUE: 2, Colour.RED: 2}
# k = 2

# graph = GraphLoader.get_graph("thousand")
# constraints = {Colour.BLUE: 500, Colour.RED: 500}
# k = 50

# instance = TargetPBS(graph, k, constraints)
instance = PlateauSurfer(graph, k, constraints)
# instance = PlateauSurferList(graph, k, constraints, alpha=0, beta=0)

profiler = cProfile.Profile()
profiler.enable()
# clusters, outliers, radius = instance.solve(iterations=1)
clusters, outliers, radius = instance.target_solve(target_cost=650, timeout=5, log=True)
profiler.disable()
stats = pstats.Stats(profiler).sort_stats('cumtime')
stats.print_stats()
# stats = pstats.Stats(profiler).sort_stats('tottime')
# stats.print_stats()

print("cost", radius)
print("centers", set(clusters.keys()))
print("clusters", clusters)
print("outliers", outliers)

print(verify_solution(graph, constraints, k, radius, set(clusters.keys())))
