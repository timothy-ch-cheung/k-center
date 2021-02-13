import random

from kcenter.pbs.target_pbs import TargetPBS
from server.orlib_graph_loader import ORLIBGraphLoader


# TODO: Key error: fix this
def test_target_pbs_pmed1():
    random.seed(120)
    graph = ORLIBGraphLoader.get_graph("pmed1")
    target = 127.0
    instance = TargetPBS(graph, graph.graph["k"], {})

    clusters, outliers, radius = instance.target_solve(target)

# TODO: Does not  terminate - fix this
def test_target_pbs_pmed1():
    random.seed(135)
    graph = ORLIBGraphLoader.get_graph("pmed1")
    target = 127.0
    instance = TargetPBS(graph, graph.graph["k"], {})

    clusters, outliers, radius = instance.target_solve(target)
