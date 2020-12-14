import cProfile, pstats

from kcenter.pbs.pbs import PBS
from tests.kcenter.solver.pbs.test_pbs import STRICT_CONSTRAINTS, K
from tests.kcenter.util.create_test_graph import medium_graph

graph = medium_graph()
instance = PBS(graph, K, STRICT_CONSTRAINTS)

profiler = cProfile.Profile()
profiler.enable()
clusters, outliers, radius = instance.solve()
profiler.disable()
stats = pstats.Stats(profiler).sort_stats('cumtime')
stats.print_stats()