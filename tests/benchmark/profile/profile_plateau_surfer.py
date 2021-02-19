import cProfile
import random

from kcenter.plateau_surfer.plateau_surfer import PlateauSurfer
from server.orlib_graph_loader import ORLIBGraphLoader

#random.seed(2)
graph = ORLIBGraphLoader.get_graph("pmed2")
constraints = {}
k = graph.graph["k"]

instance = PlateauSurfer(graph, k, constraints)

profiler = cProfile.Profile()
profiler.enable()
clusters, outliers, radius = instance.solve()
profiler.disable()
