import glob
from typing import Dict, List

import numpy as np

from benchmark.statistic.quade import quade_test, post_hoc_quade_test
from benchmark.statistic.wilcoxon import wilcoxon_test
from server.gow_graph_loader import GowGraphLoader
from server.graph_loader import GraphLoader
from server.orlib_graph_loader import ORLIBGraphLoader

problem_list = {
    "GOWALLA": GowGraphLoader.get_problem_list(),
    "SYNTHETIC": GraphLoader.get_problem_list(),
    "ORLIB": ORLIBGraphLoader.get_problem_list()
}

loader = {
    "GOWALLA": GowGraphLoader,
    "SYNTHETIC": GraphLoader,
    "ORLIB": ORLIBGraphLoader
}

results_type = Dict[str, float]
instance_results_type = Dict[str, results_type]
summary_type = Dict[str, Dict[str, instance_results_type]]


def generate_latex_table(summaries: summary_type, dataset: List[str], type: str):
    print()
    DECIMAL_POINTS = 2
    algs = list(summaries.keys())

    header = "\\multicolumn{1}{c}{Instance}"
    for algorithm in algs:
        header += "& \\quad & \\multicolumn{4}{c}{" + algorithm + "}"
    header += "& \\quad & multicolumn{2}{c}{Statistics}"
    print(f"{header}\\\\")

    sub_underline = "\\cline{1-1}"
    COLUMN_WIDTH = 4
    for idx, algorithm in enumerate(algs):
        sub_underline += " \\cline{" + str(idx + 2 + COLUMN_WIDTH * idx) + "-" + str(idx + 4 + COLUMN_WIDTH * idx) + "}"

    print(f"{sub_underline}\\\\")

    sub_header = "name"
    for algorithm in algs:
        sub_header += f" && min & $\\mu$ & $\\sigma$ & mean time"
    sub_header += " && \%-gap (cost) & \%-gap (time)"

    print(f"{sub_header}\\\\")

    time_gaps = []
    cost_gaps = []
    costs = {alg:[] for alg in algs}
    times = {alg:[] for alg in algs}
    for problem in problem_list[dataset]:
        graph = loader[dataset].get_graph(problem)
        n = graph.graph["n"]
        k = graph.graph["k"]
        min_blue = graph.graph["min_blue"]
        min_red = graph.graph["min_red"]

        row = f"{problem}"
        for algorithm in algs:
            minimum = '{:.2f}'.format(round(summaries[algorithm][problem][type]["min"], DECIMAL_POINTS))
            mean = '{:.2f}'.format(round(summaries[algorithm][problem][type]["mean"], DECIMAL_POINTS))
            std = '{:.2f}'.format(round(summaries[algorithm][problem][type]["std"], DECIMAL_POINTS))
            mean_time = '{:.2f}'.format(round(summaries[algorithm][problem]["time"]["mean"], DECIMAL_POINTS))
            row += f" && {minimum} & {mean} & {std} & {mean_time}"

            times[algorithm].append(summaries[algorithm][problem]["time"]["mean"])
            costs[algorithm].append(summaries[algorithm][problem]["cost"]["mean"])

        cost_gap = ((summaries[algs[1]][problem]["cost"]["mean"] / summaries[algs[0]][problem]["cost"][
            "mean"]) - 1) * 100
        cost_gap_rounded = '{:.2f}'.format(round(cost_gap, DECIMAL_POINTS))
        time_gap = ((summaries[algs[1]][problem]["time"]["mean"] / summaries[algs[0]][problem]["time"][
            "mean"]) - 1) * 100
        time_gap_rounded = '{:.2f}'.format(round(time_gap, DECIMAL_POINTS))
        row += f" && {cost_gap_rounded} & {time_gap_rounded}"

        time_gaps.append(time_gap)
        cost_gaps.append(cost_gap)

        print(f"{row}\\\\")

    footer = "\\multicolumn{1}{c}{Average}"
    for algorithm in algs:
        mean_time = '{:.2f}'.format(round(sum(times[algorithm])/len(times[algorithm]),DECIMAL_POINTS))
        mean_cost = '{:.2f}'.format(round(sum(costs[algorithm])/len(costs[algorithm]), DECIMAL_POINTS))
        footer += f" &&& {mean_cost} && {mean_time}"
    footer += f" && {np.mean(cost_gaps)} & {np.mean(time_gaps)}"
    print(f"{footer}\\\\")
    print()


def generate_latex_table_known_opt(summaries: summary_type, dataset: List[str]):
    print()
    DECIMAL_POINTS = 2
    algs = list(summaries.keys())

    time_gaps = []
    cost_gaps = []

    header = "\\multicolumn{2}{c}{Instance}"
    for algorithm in algs:
        header += "& \\quad & \\multicolumn{5}{c}{" + algorithm + "}"
    header += "& \\quad & \\multicolumn{2}{c}{Statistics}"
    print(f"{header}\\\\")

    sub_underline = "\\cline{1-1}"
    COLUMN_WIDTH = 4
    for idx, algorithm in enumerate(algs):
        sub_underline += " \\cline{" + str(idx + 2 + COLUMN_WIDTH * idx) + "-" + str(idx + 4 + COLUMN_WIDTH * idx) + "}"

    print(f"{sub_underline}\\\\")

    above_opt = {alg: [] for alg in algs}
    times = {alg: [] for alg in algs}
    costs = {alg: [] for alg in algs}
    for problem in problem_list[dataset]:
        if dataset == "SYNTHETIC":
            graph = loader[dataset].get_graph(f"SYNTHETIC/{problem}")
        else:
            graph = loader[dataset].get_graph(f"{problem}")

        opt = round(graph.graph["opt"], 2)
        optimal_cost = '{:.2f}'.format(round(graph.graph["opt"], 2))

        row = f"{problem} & {optimal_cost}"
        for algorithm in algs:
            minimum = '{:.2f}'.format(round(summaries[algorithm][problem]["cost"]["min"], DECIMAL_POINTS))
            mean = '{:.2f}'.format(round(summaries[algorithm][problem]["cost"]["mean"], DECIMAL_POINTS))
            std = '{:.2f}'.format(round(summaries[algorithm][problem]["cost"]["std"], DECIMAL_POINTS))
            mean_time = '{:.2f}'.format(round(summaries[algorithm][problem]["time"]["mean"], DECIMAL_POINTS))
            percentage_above_opt = ((summaries[algorithm][problem]["cost"]["mean"] / opt) - 1) * 100

            above_opt[algorithm].append(percentage_above_opt)
            times[algorithm].append(summaries[algorithm][problem]["time"]["mean"])
            costs[algorithm].append(summaries[algorithm][problem]["cost"]["mean"])

            percentage_above_opt = '{:.2f}'.format(round(percentage_above_opt), DECIMAL_POINTS)
            row += f" && {minimum} & {mean} & {std} & {percentage_above_opt} & {mean_time}"

        cost_gap = ((summaries[algs[1]][problem]["cost"]["mean"] / summaries[algs[0]][problem]["cost"][
            "mean"]) - 1) * 100
        cost_gap_rounded = '{:.2f}'.format(round(cost_gap, DECIMAL_POINTS))
        time_gap = ((summaries[algs[1]][problem]["time"]["mean"] / summaries[algs[0]][problem]["time"][
            "mean"]) - 1) * 100
        time_gap_rounded = '{:.2f}'.format(round(time_gap, DECIMAL_POINTS))
        row += f" && {cost_gap_rounded} & {time_gap_rounded}"

        time_gaps.append(time_gap)
        cost_gaps.append(cost_gap)

        print(f"{row}\\\\")

    footer = "\\multicolumn{2}{c}{Average}"
    for algorithm in algs:
        mean = '{:.2f}'.format(round(sum(costs[algorithm]) / len(costs[algorithm]), DECIMAL_POINTS))
        mean_time = '{:.2f}'.format(round(sum(times[algorithm]) / len(times[algorithm]), DECIMAL_POINTS))
        mean_above_opt = '{:.2f}'.format(round(sum(above_opt[algorithm]) / len(above_opt[algorithm]), DECIMAL_POINTS))
        footer += f" &&&&& {mean_above_opt} & {mean_time}"
    footer += f" && {np.mean(cost_gaps)} & {np.mean(time_gaps)}"
    print(f"{footer}\\\\")
    print()


def generate_latex_table_known_opt_no_stats(summaries: summary_type, dataset: List[str]):
    print()
    DECIMAL_POINTS = 2
    algs = list(summaries.keys())

    header = "\\multicolumn{2}{c}{Instance}"
    for algorithm in algs:
        header += "& \\quad & \\multicolumn{4}{c}{" + algorithm + "}"
    print(f"{header}\\\\")

    sub_underline = "\\cline{1-1}"
    COLUMN_WIDTH = 4
    for idx, algorithm in enumerate(algs):
        sub_underline += " \\cline{" + str(idx + 2 + COLUMN_WIDTH * idx) + "-" + str(idx + 4 + COLUMN_WIDTH * idx) + "}"

    print(f"{sub_underline}\\\\")

    above_opt = {alg: [] for alg in algs}
    for problem in problem_list[dataset]:
        if dataset == "ORLIB":
            opt = ORLIBGraphLoader.get_opt()[problem]
        else:
            problem_path = problem
            if dataset == "SYNTHETIC":
                problem_path = problem_path + "/" + problem

            graph = loader[dataset].get_graph(problem_path)
            opt = graph.graph["opt"]

        optimal_cost = '{:.2f}'.format(round(opt, DECIMAL_POINTS))

        row = f"{problem} & {optimal_cost}"
        for algorithm in algs:
            minimum = '{:.2f}'.format(round(summaries[algorithm][problem]["cost"]["min"], DECIMAL_POINTS))
            mean = '{:.2f}'.format(round(summaries[algorithm][problem]["cost"]["mean"], DECIMAL_POINTS))
            std = '{:.2f}'.format(round(summaries[algorithm][problem]["cost"]["std"], DECIMAL_POINTS))
            percentage_above_opt = ((summaries[algorithm][problem]["cost"]["mean"] / opt) - 1) * 100

            above_opt[algorithm].append(percentage_above_opt)

            percentage_above_opt = '{:.2f}'.format(round(percentage_above_opt), DECIMAL_POINTS)
            row += f" && {minimum} & {mean} & {std} & {percentage_above_opt}"

        print(f"{row}\\\\")

    footer = "\\multicolumn{2}{c}{Average}"
    for algorithm in algs:
        mean_above_opt = sum(above_opt[algorithm]) / len(above_opt[algorithm])
        mean_above_opt = '{:.2f}'.format(round(mean_above_opt, DECIMAL_POINTS))
        footer += f"&&&&& {mean_above_opt}"
    print(f"{footer}\\\\")
    print()


def analyse(summaries: summary_type):
    algs = list(summaries.keys())
    measurements = [[] for algorithm in algs]
    for problem in problem_list[dataset]:
        for idx, algorithm in enumerate(algs):
            measurements[idx].append(summaries[algorithm][problem]["cost"]["mean"])

    if len(algs) == 2:
        p_value = wilcoxon_test(measurements[0], measurements[1])
    else:
        p_value = quade_test(algs, problem_list[dataset], measurements)

    print(f"p-value={p_value}")

    if len(algs) > 2 and p_value <= 0.05:
        pairwise_p_values = post_hoc_quade_test(algs, problem_list[dataset], measurements)
        print(pairwise_p_values)


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

    analyse(summaries)
    generate_latex_table(summaries, dataset, "cost")
    # generate_latex_table_known_opt(summaries, dataset)
    # generate_latex_table_known_opt_no_stats(summaries, dataset)
