import math
import os
import time
from pathlib import Path

from benchmark.tools.benchmark.benchmark_orlib import get_latest_log, get_last_valid_result
from src.kcenter.constant.colour import Colour
from src.kcenter.verify.verify import verify_solution
from src.server.graph_loader import GraphLoader
from src.server.routes import k_center_algorithms
from src.util.logger import LogEntry


def calc_timeout(n, k):
    return math.ceil(0.15 * n + 0.5 * k)


def benchmark(problem_name: str, trials: int, algorithm: str, problem_set: str, timeout: int):
    graph = GraphLoader.get_graph(f"{problem_set}/{problem_name}")
    n = graph.graph["n"]
    k = graph.graph["k"]
    min_blue = graph.graph["min_blue"]
    min_red = graph.graph["min_red"]
    optimal_cost = graph.graph["opt"]
    constraints = {Colour.BLUE: min_blue, Colour.RED: min_red}
    solver = k_center_algorithms[algorithm](graph, k, constraints, name=algorithm)
    if timeout == -1:
        timeout = calc_timeout(n, k)

    results = []
    for i in range(trials):
        if "pbs" in algorithm:
            clusters, outliers, radius = solver.target_solve(timeout=timeout, log=True, target_cost=optimal_cost)
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

    with open(f"SYNTHETIC/{algorithm}/{problem_name}_results.txt", "w") as f:
        for result in results:
            f.write(f"{result.cost}, {result.time}\n")
        f.flush()
        os.fsync(f)


def run_synthetic_suite(algorithm, trials, timeout):
    PROBLEM_SET = "SYNTHETIC"
    problem_list = GraphLoader.get_problem_list(PROBLEM_SET)
    Path(f"{PROBLEM_SET}/{algorithm}").mkdir(parents=True, exist_ok=True)
    start_time = time.time()

    for problem in problem_list:
        my_file = Path(f"{algorithm}/{problem}_results.txt")
        if my_file.is_file():
            continue

        benchmark(problem, trials, algorithm, PROBLEM_SET, timeout)
        print(f"Benchmarked {algorithm} algorithm on {problem} with {trials} trials")

    print(f"total time: {time.time() - start_time}")


if __name__ == "__main__":
    run_synthetic_suite("colourful_pbs", 10, -1)
