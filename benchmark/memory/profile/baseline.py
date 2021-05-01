from functools import partial

from memory_profiler import memory_usage

from benchmark.memory.profile.util import parse_args
from server.gow_graph_loader import GowGraphLoader

if __name__ == "__main__":
    INTERVAL, TIMEOUT, GRAPH_NAME = parse_args()
    fun = partial(GowGraphLoader.get_graph, GRAPH_NAME)
    baseline = memory_usage(fun, interval=INTERVAL)
    print(baseline)