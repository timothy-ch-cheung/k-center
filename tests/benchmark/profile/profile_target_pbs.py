import cProfile
import pstats

from kcenter.pbs.target_pbs import TargetPBS
from kcenter.verify.verify import verify_k_center_solution
from server.orlib_graph_loader import ORLIBGraphLoader

optimal = ORLIBGraphLoader.get_opt()

problem_instance = "pmed3"

graph = ORLIBGraphLoader.get_graph(problem_instance)
k = graph.graph["k"]
target = optimal[problem_instance]

instance = TargetPBS(graph, k, {})

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
