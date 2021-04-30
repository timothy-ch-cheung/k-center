import subprocess
import sys

import matplotlib.pyplot as plt

from benchmark.tools.benchmark.benchmark_gowalla import calc_timeout
from src.server.gow_graph_loader import GowGraphLoader


def plot_graph(y1, y2):
    x1 = [x * INTERVAL for x in range(len(y1))]
    x2 = [x * INTERVAL for x in range(len(y2))]

    fig, ax = plt.subplots()
    ax.plot(x1, y1, label="alg_1", color="blue")
    ax.plot(x2, y2, label="alg_2", color="red")

    plt.xlabel("Time (seconds)")
    plt.ylabel("Memory Usage (MiB)")
    plt.title("Memory usage comparison")

    plt.show()


if __name__ == "__main__":
    INTERVAL = 0.001
    GRAPH_NAME = "solved_gow41"
    graph = GowGraphLoader.get_graph(GRAPH_NAME)
    TIMEOUT = calc_timeout(graph.graph["n"], graph.graph["k"])

    y1_str = subprocess.run([sys.executable, "profile/colourful_pbs.py", str(INTERVAL), str(TIMEOUT), GRAPH_NAME],
                            stdout=subprocess.PIPE).stdout.decode('utf-8')
    y1 = [float(y) for y in y1_str.replace("[", "").replace("]", "").split(",")]

    y2_str = subprocess.run([sys.executable, "profile/constant_colourful.py", str(INTERVAL), str(TIMEOUT), GRAPH_NAME],
                            stdout=subprocess.PIPE).stdout.decode('utf-8')
    y2 = [float(y) for y in y2_str.replace("[", "").replace("]", "").split(",")]

    plot_graph(y1, y2)
