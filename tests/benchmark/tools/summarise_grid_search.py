import math
from typing import Dict, Tuple

import matplotlib.patheffects as PathEffects
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

from server.tsplib_graph_loader import TSPLIBGraphLoader

"""
Calculate mean percentage above optimal cost for each alpha-beta parameter combination
"""


def read_results(problem: str, k: int):
    results = dict()
    with open(f"{problem}_{k}.txt", "r") as f:
        for line in f.readlines():
            line = line.strip().split(" ")
            cost = float(line[2])
            ab_pair = (line[0], line[1])
            if ab_pair not in results:
                results[ab_pair] = [cost]
            else:
                results[ab_pair].append(cost)
    return results


def summarise():
    OPT = TSPLIBGraphLoader.get_opt()
    summary = dict()

    for problem_instance in OPT.keys():
        for k, optimal_cost in OPT[problem_instance].items():
            results = read_results(problem_instance, k)
            for ab_pair, costs in results.items():
                mean_cost = sum(costs) / len(costs)
                percentage_over_opt = (mean_cost / optimal_cost) - 1
                if ab_pair not in summary:
                    summary[ab_pair] = [percentage_over_opt]
                else:
                    summary[ab_pair].append(percentage_over_opt)

    mean_summary = {key: (sum(percentages) / len(percentages)) for key, percentages in summary.items()}
    with open(f"summary.txt", "w") as f:
        for ab_pair, mean_percentage in mean_summary.items():
            f.write(f"{ab_pair[0]} {ab_pair[1]} {mean_percentage}\n")

    return mean_summary


def plot_heat_map(results, alphas, betas):
    results = results[::-1]
    alphas = alphas[::-1]
    fig, ax = plt.subplots()
    fig = plt.gcf()
    fig.set_size_inches(10.0, 10.0)
    im = ax.imshow(results, cmap=cm.inferno.reversed())

    ax.set_xticks(np.arange(len(alphas)))
    ax.set_yticks(np.arange(len(betas)))
    ax.set_xticklabels(betas, fontsize=14)
    ax.set_yticklabels(alphas, fontsize=14)

    plt.xlabel("Beta value", fontsize=16)
    plt.ylabel("Alpha value", fontsize=16)

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    plt.rcParams.update({'font.size': 14})
    for i in range(len(alphas)):
        for j in range(len(betas)):
            text = ax.text(j, i, round(results[(i, j)], 1),
                           ha="center", va="center", color="w")
            text.set_path_effects([PathEffects.withStroke(linewidth=1, foreground='dimgrey')])

    plt.rcParams.update({'font.size': 16})
    ax.set_title("% Above optimal cost (GRASP Plateau Surfer)")
    plt.show()


def plot_quadrant_stats(results, alphas, betas):
    def mean(arr):
        return sum(arr) / len(arr)

    def calc_quandrant(results):
        n = len(results)
        half_n = math.ceil(n / 2)
        m = len(results[0])
        half_m = math.ceil(m / 2)
        top_left = [results[i][j] for i in range(0, half_n) for j in range(0, half_m)]
        top_right = [results[i][j] for i in range(0, half_n) for j in range(half_m, m)]
        bot_left = [results[i][j] for i in range(half_n, n) for j in range(0, half_m)]
        bot_right = [results[i][j] for i in range(half_n, n) for j in range(half_m, m)]

        quandrants = [[mean(bot_left), mean(bot_right)],
                      [mean(top_left), mean(top_right)]
                      ]

        y_bounds = [f"alpha=[{alphas[half_n]}-{alphas[n - 1]}]", f"alpha=[{alphas[0]}-{alphas[half_n - 1]}]"]
        x_bounds = [f"beta=[{betas[0]}-{betas[half_m - 1]}]", f"beta=[{betas[half_m]}-{alphas[m - 1]}]"]

        return quandrants, x_bounds, y_bounds

    quandrants, x_bounds, y_bounds = calc_quandrant(results)

    fig, ax = plt.subplots()
    fig = plt.gcf()
    fig.set_size_inches(6.0, 6.0)
    im = ax.imshow(quandrants, cmap=cm.Greys)

    ax.set_xticks(np.arange(2))
    ax.set_yticks(np.arange(2))
    ax.set_xticklabels(x_bounds, fontsize=12)
    ax.set_yticklabels(y_bounds, fontsize=12, rotation='vertical', va="center")

    plt.rcParams.update({'font.size': 20})
    for i in range(2):
        for j in range(2):
            text = ax.text(j, i, round(quandrants[i][j], 2),
                           ha="center", va="center", color="w")
            text.set_path_effects([PathEffects.withStroke(linewidth=2, foreground='dimgrey')])

    ax.set_title("% Above optimal cost (GRASP Plateau Surfer)\nQuandrant averages", fontsize=14)
    plt.show()


def plot(summary: Dict[Tuple[str, str], float]):
    results = []
    alphas = sorted(list(set([ab_pair[0] for ab_pair in summary.keys()])))
    betas = sorted(list(set([ab_pair[1] for ab_pair in summary.keys()])))

    for alpha in alphas:
        row = []
        for beta in betas:
            row.append(summary[(alpha, beta)] * 100)
        results.append(row)

    results = np.array(results)
    plot_heat_map(results, alphas, betas)
    plot_quadrant_stats(results, alphas, betas)


if __name__ == "__main__":
    summary = summarise()
    plot(summary)
