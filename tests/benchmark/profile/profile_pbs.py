import cProfile, pstats

from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import PBS
from src.server.graph_loader import GraphLoader
from tests.kcenter.solver.pbs.test_pbs import STRICT_CONSTRAINTS, K
from tests.kcenter.util.create_test_graph import medium_graph

# graph = medium_graph()
graph = GraphLoader.get_graph("k_center")
#instance = PBS(graph, 5, {Colour.BLUE: 0, Colour.RED: 20})
instance = PBS(graph, 5, {Colour.BLUE: 0, Colour.RED: 20})

profiler = cProfile.Profile()
profiler.enable()
clusters, outliers, radius = instance.solve()
profiler.disable()
stats = pstats.Stats(profiler).sort_stats('cumtime')
stats.print_stats()

print("cost", radius)
