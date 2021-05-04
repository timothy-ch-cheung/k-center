import os
import subprocess
import sys

import matplotlib.pyplot as plt

from benchmark.tools.benchmark.benchmark_gowalla import calc_timeout
from src.server.gow_graph_loader import GowGraphLoader


def plot_graph(GRAPH_NAME, INTERVAL, y1, y2, TIMEOUT, first_algorithm, second_algorithm):
    ALGORITHM_DISPLAY = {
        "colourful_bandyapadhyay": "Ban algorithm",
        "target_colourful_pbs": "Colourful PBS",
        "grasp_ps": "GRASP-PS",
        "greedy": "Gon algorithm",
        "target_pbs": "PBS"
    }

    baseline_str = subprocess.run([sys.executable, "-m","benchmark.memory.profile.baseline", str(INTERVAL), str(TIMEOUT), GRAPH_NAME],
                                  stdout=subprocess.PIPE).stdout.decode('utf-8')
    baseline = [float(y) for y in baseline_str.replace("[", "").replace("]", "").split(",")]

    x0 = [x * INTERVAL for x in range(len(baseline))]
    x1 = [x * INTERVAL for x in range(len(y1))]
    x2 = [x * INTERVAL for x in range(len(y2))]

    fig, ax = plt.subplots()

    def draw_hline(y):
        maximum = max(y)
        plt.axhline(maximum, color="lightgray", linestyle="--")
        plt.text(0, maximum, "{:.2f}".format(maximum), ha="center", va="bottom", fontsize=9)

    draw_hline(baseline)
    draw_hline(y1)
    draw_hline(y2)

    ax.plot(x0, baseline, label="Load Graph", color="green")
    ax.plot(x1, y1, label=ALGORITHM_DISPLAY[first_algorithm], color="blue")
    ax.plot(x2, y2, label=ALGORITHM_DISPLAY[second_algorithm], color="red")
    ax.legend()
    ax.set_ylim([None, max(baseline + y1 + y2) * 1.05])

    plt.xlabel("Time (seconds)")
    plt.ylabel("Memory Usage (MiB)")
    plt.title("Memory usage comparison")

    plt.show()


def profile_mem(graph_name, first_algorithm, second_algorithm):
    INTERVAL = 0.001
    graph = GowGraphLoader.get_graph(graph_name)
    TIMEOUT = calc_timeout(graph.graph["n"], graph.graph["k"])

    # Two algorithms need to be run as a separate subprocess to get the correct memory usage reading
    y1_str = subprocess.run(
        [sys.executable,"-m", f"benchmark.memory.profile.{first_algorithm}", str(INTERVAL), str(TIMEOUT),
         graph_name],
        stdout=subprocess.PIPE).stdout.decode('utf-8')
    y1 = [float(y) for y in y1_str.replace("[", "").replace("]", "").split(",")]

    y2_str = subprocess.run(
        [sys.executable,"-m", f"benchmark.memory.profile.{second_algorithm}", str(INTERVAL), str(TIMEOUT),
         graph_name],
        stdout=subprocess.PIPE).stdout.decode('utf-8')
    y2 = [float(y) for y in y2_str.replace("[", "").replace("]", "").split(",")]

    plot_graph(graph_name, INTERVAL, y1, y2, TIMEOUT, first_algorithm, second_algorithm)


if __name__ == "__main__":
    INTERVAL = 0.001
    GRAPH_NAME = "solved_gow41"
    graph = GowGraphLoader.get_graph(GRAPH_NAME)
    TIMEOUT = calc_timeout(graph.graph["n"], graph.graph["k"])
    print(f"Timeout: {TIMEOUT}")

    y1_str = subprocess.run(
        [sys.executable, "profile/target_colourful_pbs.py", str(INTERVAL), str(TIMEOUT), GRAPH_NAME],
        stdout=subprocess.PIPE).stdout.decode('utf-8')
    y1 = [float(y) for y in y1_str.replace("[", "").replace("]", "").split(",")]

    y2_str = subprocess.run(
        [sys.executable, "profile/colourful_bandyapadhyay.py", str(INTERVAL), str(TIMEOUT), GRAPH_NAME],
        stdout=subprocess.PIPE).stdout.decode('utf-8')
    y2 = [float(y) for y in y2_str.replace("[", "").replace("]", "").split(",")]

    plot_graph(GRAPH_NAME, INTERVAL, y1, y2, TIMEOUT, "target_colourful_pbs", "colourful_bandyapadhyay")
