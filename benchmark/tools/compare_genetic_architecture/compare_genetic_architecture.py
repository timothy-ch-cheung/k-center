import math
import os
import time
from pathlib import Path

from benchmark.tools.benchmark.benchmark_orlib import get_latest_log, get_last_valid_result
from kcenter.colourful_pbs.alternative_architecture.roulette_colourful_pbs import RouletteColourfulPBS
from kcenter.colourful_pbs.alternative_architecture.tournament_colourful_pbs import TournamentColourfulPBS
from kcenter.colourful_pbs.target_colourful_pbs import TargetColourfulPBS
from kcenter.constant.colour import Colour
from kcenter.verify.verify import verify_solution
from server.graph_loader import GraphLoader

algorithms = {
    "target_pbs_original": TargetColourfulPBS,
    "target_pbs_roulette": RouletteColourfulPBS,
    "target_pbs_tournament": TournamentColourfulPBS
}


def calc_timeout(n, k):
    return math.ceil(0.15 * n + 0.5 * k)


def benchmark(problem_name: str, trials: int, algorithm: str, problem_set: str):
    graph = GraphLoader.get_graph(f"{problem_set}/{problem_name}")
    n = graph.graph["n"]
    k = graph.graph["k"]
    min_blue = graph.graph["min_blue"]
    min_red = graph.graph["min_red"]
    optimal_cost = graph.graph["opt"]
    constraints = {Colour.BLUE: min_blue, Colour.RED: min_red}
    solver = algorithms[algorithm](graph, k, constraints, name=algorithm)
    timeout = calc_timeout(n, k)

    results = []
    for i in range(trials):
        clusters, outliers, radius = solver.target_solve(target_cost=optimal_cost, timeout=timeout, log=True)
        log = get_latest_log(algorithm, n, k)
        entry = get_last_valid_result(log, timeout)
        results.append(entry)
        if os.path.isfile(log):
            os.remove(log)

        verify_solution(graph, constraints, k, radius, set(clusters.keys()))

    with open(f"{algorithm}/{problem_name}_results.txt", "w") as f:
        for result in results:
            f.write(f"{result.cost} {result.time}\n")
        f.flush()
        os.fsync(f)


def run_suite(ALGORITHM):
    PROBLEM_SET = "TRAIN_COLOURFUL"
    problem_list = GraphLoader.get_problem_list(PROBLEM_SET)
    TRIALS = 50
    Path(f"{ALGORITHM}").mkdir(parents=True, exist_ok=True)
    start_time = time.time()

    for problem in problem_list:
        my_file = Path(f"{ALGORITHM}/{problem}_results_2.txt")
        if my_file.is_file():
            continue

        benchmark(problem, TRIALS, ALGORITHM, PROBLEM_SET)
        print(f"Benchmarked {ALGORITHM} algorithm on {problem} with {TRIALS} trials")

    print(f"total time: {time.time() - start_time}")


if __name__ == "__main__":
    for alg in algorithms.keys():
        run_suite(alg)
