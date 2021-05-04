import glob
import math
import os
import time
from pathlib import Path

from src.kcenter.constant.colour import Colour
from src.kcenter.solver.abstract_target_solver import AbstractTargetSolver
from src.server.orlib_graph_loader import ORLIBGraphLoader
from src.server.routes import k_center_algorithms
from src.util.logger import LogEntry, log_filename

OPT = ORLIBGraphLoader.get_opt()
problem_list = ORLIBGraphLoader.get_problem_list()


def calc_timeout(n, k):
    return math.ceil(0.1 * n + 0.5 * k)


def get_latest_log(algorithm: str, n: int, k: int):
    logs = glob.glob(f"{log_filename(algorithm, n, k)}_*")
    latest_log = max(logs, key=os.path.getctime)
    return latest_log


def get_last_valid_result(log_name: str, timeout: int):
    last_valid = None
    with open(log_name, "r") as f:
        for line in f.readlines():
            line = line.strip().split(" ")
            cost = float(line[0])
            sol_time = float(line[1])

            if sol_time > timeout:
                break

            last_valid = LogEntry(cost=cost, time=sol_time)
    return last_valid


def benchmark(problem_name: str, trials: int, algorithm: str, timeout: int):
    graph = ORLIBGraphLoader.get_graph(problem_name)
    n = graph.graph["n"]
    k = graph.graph["k"]
    solver = k_center_algorithms[algorithm](graph, k, {Colour.BLUE: n, Colour.RED: 0}, name=algorithm)
    optimal_cost = OPT[problem_name]
    if timeout == -1:
        timeout = calc_timeout(n, k)

    results = []
    for i in range(trials):
        if algorithm == "grasp_ps" or "target" in algorithm:
            clusters, outliers, radius = solver.target_solve(target_cost=optimal_cost, timeout=timeout, log=True)
            log = get_latest_log(algorithm, n, k)
            entry = get_last_valid_result(log, timeout)
            results.append(entry)
            if os.path.isfile(log):
                os.remove(log)
        else:
            start_time = time.time()
            clusters, outliers, radius = solver.solve()
            end_time = time.time()
            results.append(LogEntry(cost=radius, time=end_time - start_time))

    with open(f"ORLIB/{algorithm}/{problem_name}_results.txt", "w") as f:
        for result in results:
            f.write(f"{result.cost}, {result.time}\n")
        f.flush()
        os.fsync(f)


def run_orlib_suite(algorithm, trials, timeout):
    Path(f"ORLIB/{algorithm}").mkdir(parents=True, exist_ok=True)
    start_time = time.time()

    for problem in problem_list:
        my_file = Path(f"{algorithm}/{problem}_results.txt")
        if my_file.is_file():
            continue

        benchmark(problem, trials, algorithm, timeout)
        print(f"Benchmarked {algorithm} algorithm on {problem} with {trials} trials")

    print(f"total time: {time.time() - start_time}")


if __name__ == "__main__":
    run_orlib_suite("grasp_ps", 10, -1)
