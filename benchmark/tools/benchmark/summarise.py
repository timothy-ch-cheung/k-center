import glob
from typing import Dict, List

import numpy as np

from server.gow_graph_loader import GowGraphLoader

problem_list = {
    "GOWALLA": GowGraphLoader.get_problem_list()
}

loader = {
    "GOWALLA": GowGraphLoader
}

results_type = Dict[str, float]
instance_results_type = Dict[str, results_type]
summary_type = Dict[str, Dict[str, instance_results_type]]

def generate_latex_table(summaries: summary_type, dataset: List[str], type: str):
    print()
    DECIMAL_POINTS = 2
    algs = list(summaries.keys())

    header = "\\multicolumn{5}{c}{Instance}"
    for algorithm in algs:
        header += "& \\quad & \\multicolumn{4}{c}{" + algorithm + "}"
    print(f"{header}\\\\")

    sub_underline = "\\cline{1-5}"
    COLUMN_WIDTH = 4
    for idx,algorithm in enumerate(algs):
        sub_underline += " \\cline{" + str(idx + 2 + COLUMN_WIDTH * idx) + "-" + str(idx + 4 + COLUMN_WIDTH * idx) + "}"

    print(f"{sub_underline}\\\\")

    sub_header = "Name & n & k & b & r"
    for algorithm in algs:
        sub_header += f" && min & $\\mu$ & $\\sigma$ & mean time"

    print(f"{sub_header}\\\\")

    for problem in problem_list[dataset]:
        graph = loader[dataset].get_graph(problem)
        n = graph.graph["n"]
        k = graph.graph["k"]
        min_blue = graph.graph["min_blue"]
        min_red = graph.graph["min_red"]

        row = f"{problem} & {n} & {k} & {min_blue} & {min_red}"
        for algorithm in algs:
            minimum = '{:.2f}'.format(round(summaries[algorithm][problem][type]["min"], DECIMAL_POINTS))
            mean = '{:.2f}'.format(round(summaries[algorithm][problem][type]["mean"], DECIMAL_POINTS))
            std = '{:.2f}'.format(round(summaries[algorithm][problem][type]["std"], DECIMAL_POINTS))
            mean_time = '{:.2f}'.format(round(summaries[algorithm][problem]["cost"]["mean"], DECIMAL_POINTS))
            row += f" && {minimum} & {mean} & {std} & {mean_time}"

        print(f"{row}\\\\")
    print()


def generate_latex_table_known_opt(summaries: summary_type, dataset: List[str], type: str):
    print()
    DECIMAL_POINTS = 2
    algs = list(summaries.keys())
    percentage_above_opt = {alg: [] for alg in algs}

    header = "\\multicolumn{6}{c}{Instance}"
    for algorithm in algs:
        header += "& \\quad & \\multicolumn{3}{c}{" + algorithm + "}"
    print(f"{header}\\")

    for problem in problem_list[dataset]:
        graph = loader[dataset].get_graph(problem)
        n = graph.graph["n"]
        k = graph.graph["k"]
        min_blue = graph.graph["min_blue"]
        min_red = graph.graph["min_red"]
        optimal_cost = '{:.2f}'.format(round(graph.graph["opt"], 2))

        row = f"{problem} & {n} & {k} & {min_blue} & {min_red} & {optimal_cost}"
        for algorithm in algs:
            minimum = '{:.2f}'.format(round(summaries[algorithm][problem]["min"], DECIMAL_POINTS))
            mean = '{:.2f}'.format(round(summaries[algorithm][problem]["mean"], DECIMAL_POINTS))
            std = '{:.2f}'.format(round(summaries[algorithm][problem]["std"], DECIMAL_POINTS))
            row += f" && {minimum} & {mean} & {std}"

            percentage_above_opt[algorithm].append(summaries[algorithm][problem][type]["mean"] / float(optimal_cost))
        print(f"{row}\\\\")

    footer = "\\multicolumn{6}{c}{Average \% cost above opt}"
    for algorithm in algs:
        above_opt = percentage_above_opt[algorithm]
        footer += " && \multicolumn{3}{c}{"
        footer += f"{'{:.2f}'.format((sum(above_opt) / len(above_opt) - 1) * 100)}\%"
        footer += "}"

    print(f"{footer}\\\\")
    print()


def calc_stats(results: List[float]) -> Dict[str, float]:
    minimum = min(results)
    mean = float(np.mean(results))
    std = float(np.std(results))
    return {"min": minimum, "mean": mean, "std": std}


def summarise(dataset: str):
    results_path = "../../../results/"
    dataset_path = f"{results_path}{dataset}_RESULTS"
    algorithms = glob.glob(f"{dataset_path}/*")
    algorithms = [x.replace(f"{dataset_path}\\", "") for x in algorithms]

    summaries: summary_type = {alg: dict() for alg in algorithms}
    for alg in algorithms:
        for problem in problem_list[dataset]:
            summaries[alg][problem] = dict()
            costs = []
            durations = []
            with open(f"{dataset_path}/{alg}/{problem}_results.txt", "r") as f:
                for line in f.readlines():
                    line = line.strip().split(" ")
                    cost = float(line[0])
                    time = float(line[1])
                    costs.append(cost)
                    durations.append(time)

            summaries[alg][problem]["cost"] = calc_stats(costs)
            summaries[alg][problem]["time"] = calc_stats(durations)
    return summaries


if __name__ == "__main__":
    dataset = "GOWALLA"
    summaries = summarise(f"{dataset}")

    generate_latex_table(summaries, dataset, "cost")
    # generate_latex_table(summaries, dataset, "time")
