import cProfile
import pstats

from src.server.graph_loader import GraphLoader

profiler = cProfile.Profile()
profiler.enable()
graph = GraphLoader.get_graph("thousand")
profiler.disable()
stats = pstats.Stats(profiler).sort_stats('cumtime')
stats.print_stats()