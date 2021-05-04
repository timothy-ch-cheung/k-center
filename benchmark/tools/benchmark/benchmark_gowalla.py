import math
import os
import time
from pathlib import Path
from typing import Optional

from benchmark.tools.benchmark.benchmark_orlib import get_latest_log, get_last_valid_result
from src.kcenter.constant.colour import Colour
from src.kcenter.verify.verify import verify_solution
from src.server.gow_graph_loader import GowGraphLoader
from src.server.routes import k_center_algorithms
from src.util.logger import LogEntry

problem_list = GowGraphLoader.get_problem_list()


def calc_timeout(n, k):
    return math.ceil(0.15 * n + 0.5 * k)


def benchmark(problem_name: str, trials: int, algorithm: str, timeout: int):
    graph = GowGraphLoader.get_graph(problem_name)
    n = graph.graph["n"]
    k = graph.graph["k"]
    min_blue = graph.graph["min_blue"]
    min_red = graph.graph["min_red"]
    constraints = {Colour.BLUE: min_blue, Colour.RED: min_red}
    solver = k_center_algorithms[algorithm](graph, k, constraints, name=algorithm)
    if timeout == -1:
        timeout = calc_timeout(n, k)

    results = []
    for i in range(trials):
        if "pbs" in algorithm:
            clusters, outliers, radius = solver.target_solve(timeout=timeout, log=True)
            log = get_latest_log(algorithm, n, k)
            entry = get_last_valid_result(log, timeout)
            if os.path.isfile(log):
                os.remove(log)
        else:
            start_time = time.time()
            clusters, outliers, radius = solver.solve()
            end_time = time.time()
            entry = LogEntry(cost=radius, time=end_time - start_time)

        assert verify_solution(graph, constraints, k, radius, set(clusters.keys()))
        results.append(entry)

    with open(f"GOWALLA/{algorithm}/{problem_name}_results.txt", "w") as f:
        for result in results:
            f.write(f"{result.cost}, {result.time}\n")
        f.flush()
        os.fsync(f)


def run_gowalla_suite(algorithm, trials, timeout):
    Path(f"GOWALLA/{algorithm}").mkdir(parents=True, exist_ok=True)
    start_time = time.time()

    print()
    for problem in problem_list:
        my_file = Path(f"{algorithm}/{problem}_results.txt")
        if my_file.is_file():
            continue

        benchmark(problem, trials, algorithm, timeout)
        print(f"Benchmarked {algorithm} algorithm on {problem} with {trials} trials")

    print(f"\ntotal time: {time.time() - start_time}")


if __name__ == "__main__":
    run_gowalla_suite("colourful_pbs", 10, -1)
