import cProfile
import pstats

from kcenter.colourful_pbs.alternative_architecture.roulette_colourful_pbs import RouletteColourfulPBS
from kcenter.colourful_pbs.target_colourful_pbs import TargetColourfulPBS
from kcenter.verify.verify import verify_solution
from src.kcenter.constant.colour import Colour
from src.server.graph_loader import GraphLoader

problem_name = "train_col_n100_k10"
graph = GraphLoader.get_graph(f"TRAIN_COLOURFUL/{problem_name}")
k = graph.graph["k"]
min_blue = graph.graph["min_blue"]
min_red = graph.graph["min_red"]
optimal_cost = graph.graph["opt"]
constraints = {Colour.BLUE: min_blue, Colour.RED: min_red}

# instance = TargetColourfulPBS(graph, k, constraints)
instance = RouletteColourfulPBS(graph, k, constraints)

profiler = cProfile.Profile()
profiler.enable()
clusters, outliers, radius = instance.target_solve(target_cost=optimal_cost, timeout=40, log=True)
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
