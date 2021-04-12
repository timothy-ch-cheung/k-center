from typing import Dict, Tuple

import numpy as np

from benchmark.statistic.quade import quade_test, post_hoc_quade_test
from benchmark.tools.compare_genetic_architecture.compare_genetic_architecture import algorithms
from server.graph_loader import GraphLoader

problems = GraphLoader.get_problem_list("TRAIN_COLOURFUL")


def summarise_file(algorithm: str, problem: str) -> Tuple[float, float, float]:
    costs = []
    with open(f"{algorithm}/{problem}_results.txt", "r") as f:
        for line in f.readlines():
            line = line.strip().split(" ")
            cost = float(line[0])
            costs.append(cost)

    minimum = min(costs)
    mean = float(np.mean(costs))
    std = float(np.std(costs))
    return minimum, mean, std


def format_float(num: float):
    return "{:.4f}".format(num)


def summarise(algorithm: str) -> Dict[str, float]:
    summary = dict()
    with open(f"{algorithm}_summary.txt", "w") as f:
        f.write("PROBLEM\tMIN\tMEAN\tSTD\n")
        for problem in problems:
            minimum, mean, std = summarise_file(algorithm, problem)

            summary[problem] = {"min": minimum, "mean": mean, "std": std}
            f.write(f"{problem} {format_float(minimum)} {format_float(mean)} {format_float(std)}\n")
    return summary


def analyse(summaries: Dict[str, Dict[str, float]]) -> Tuple[float, Dict[Tuple[str, str], float]]:
    algorithm_labels = [x.replace("target_", "") for x in summaries.keys()]
    problem_labels = list(next(iter(summaries.values())).keys())

    measurements = tuple()
    for alg in algorithms:
        alg_measurements = []
        for problem in problem_labels:
            alg_measurements.append(summaries[alg][problem]["mean"])
        measurements = measurements + tuple([alg_measurements])
    problem_labels = [x.replace("train_col_", "") for x in problem_labels]

    p_value = quade_test(algorithm_labels, problem_labels, measurements)
    pairwise_p_values = post_hoc_quade_test(algorithm_labels, problem_labels, measurements)

    with open(f"ANOVA.txt", "w") as f:
        f.write(f"p-value={p_value}\n")
        f.write(f"pairwise p-values={pairwise_p_values}\n")

    return p_value, pairwise_p_values


if __name__ == "__main__":
    summaries = dict()
    for alg in algorithms:
        summaries[alg] = summarise(alg)

    p_value, pairwise_p_values = analyse(summaries)
    print(f"Quade omnibus test p-value: {p_value}")
    print(f"Pairwise post-hoc Quade test p-values: {pairwise_p_values}")
