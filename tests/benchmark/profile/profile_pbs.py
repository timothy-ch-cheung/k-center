import cProfile
import pstats

from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import PBS
from src.server.graph_loader import GraphLoader

graph = GraphLoader.get_graph("k_center")
instance = PBS(graph, 5, {Colour.BLUE: 0, Colour.RED: 20})

# graph = GraphLoader.get_graph("large")
# instance = PBS(graph, 10, {Colour.BLUE: 50, Colour.RED: 50})

# graph = GraphLoader.get_graph("thousand")
# instance = PBS(graph, 50, {Colour.BLUE: 500, Colour.RED: 500})

profiler = cProfile.Profile()
profiler.enable()
clusters, outliers, radius = instance.solve()
profiler.disable()
stats = pstats.Stats(profiler).sort_stats('cumtime')
stats.print_stats()
stats = pstats.Stats(profiler).sort_stats('tottime')
stats.print_stats()

print("cost", radius)
