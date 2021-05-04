from functools import partial

from memory_profiler import memory_usage

from benchmark.memory.profile.util import parse_args
from src.kcenter.pbs.pbs import PBS
from src.kcenter.constant.colour import Colour
from src.server.gow_graph_loader import GowGraphLoader


def profile_memory_approximation(graph_name: str):
    graph = GowGraphLoader.get_graph(graph_name)
    constraints = {Colour.BLUE: graph.graph["min_blue"], Colour.RED: graph.graph["min_red"]}
    k = graph.graph["k"]
    instance = PBS(graph, k, constraints)
    instance.solve()


if __name__ == "__main__":
    INTERVAL, TIMEOUT, GRAPH_NAME = parse_args()
    fun = partial(profile_memory_approximation, GRAPH_NAME)
    mem = memory_usage(fun, interval=INTERVAL, max_iterations=1)
    print(mem)
