from typing import Dict

import matplotlib.patheffects as PathEffects
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.patches import Rectangle

orlib_comparisons = {
    'Gon': {'Gon': 0, 'GRASP': 15, 'PBS': 4},
    'GRASP': {'Gon': 25, 'GRASP': 0, 'PBS': 6},
    'PBS': {'Gon': 36, 'GRASP': 34, 'PBS': 0}
}

orlib_comparisons_two_sigma = {
    'Gon': {'Gon': 0, 'GRASP': 11, 'PBS': 2},
    'GRASP': {'Gon': 23, 'GRASP': 0, 'PBS': 3},
    'PBS': {'Gon': 34, 'GRASP': 31, 'PBS': 0}
}


def plot_stacked_bar(orlib_comparisons: Dict[str, Dict[str, int]]):
    algorithms = list(orlib_comparisons.keys())
    gon = [x['Gon'] for x in [orlib_comparisons[y] for y in algorithms]]
    grasp = [x['GRASP'] for x in [orlib_comparisons[y] for y in algorithms]]
    pbs = [x['PBS'] for x in [orlib_comparisons[y] for y in algorithms]]

    fig, ax = plt.subplots()

    rects1 = ax.barh(algorithms, gon, color="#eaca52", label='Gon')
    rects2 = ax.barh(algorithms, grasp, left=gon, color="#4c5a72", label='GRASP')
    rects3 = ax.barh(algorithms, pbs, left=[x + y for x, y in zip(gon, grasp)], color="#c46335", label='PBS')
    ax.set_xlim([0, 80])

    plt.xlabel('Number of problem instances with a lower μ cost')
    plt.ylabel('Algorithm')
    plt.title('Comparison of Gon, GRASP and PBS')
    ax.legend()

    for p in ax.get_children()[:-1]:  # skip the last patch as it is the background
        if isinstance(p, Rectangle):
            x, y = p.get_xy()
            w, h = p.get_width(), p.get_height()
            if w > 0:  # anything that have a height of 0 will not be annotated
                ax.text(x + 0.5 * w, y + 0.5 * h, w, va='center', ha='center')

    plt.show()


def plot_confusion_matrix(orlib_comparisons: Dict[str, Dict[str, int]]):
    PROBLEM_NUM = 40
    algs = list(orlib_comparisons.keys())
    NUM_ALGS = len(algs)
    results = [[(orlib_comparisons[x][y] / PROBLEM_NUM) * 100 for x in algs] for y in algs]

    fig, ax = plt.subplots()
    fig = plt.gcf()
    fig.set_size_inches(9.5, 9.5)
    im = ax.imshow(results, cmap=cm.Purples)

    ax.set_xticks(np.arange(NUM_ALGS))
    ax.set_yticks(np.arange(NUM_ALGS))
    ax.set_xticklabels(algs, fontsize=16)
    ax.set_yticklabels(algs, fontsize=16)

    plt.xlabel("Algorithm X", fontsize=18)
    plt.ylabel("Algorithm Y", fontsize=18)

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    plt.rcParams.update({'font.size': 14})
    for i in range(NUM_ALGS):
        for j in range(NUM_ALGS):
            text = ax.text(j, i, f"{round(results[i][j], 1)}%",
                           ha="center", va="center", color="w", fontsize=28)
            text.set_path_effects([PathEffects.withStroke(linewidth=2, foreground='black')])

    plt.rcParams.update({'font.size': 16})
    ax.set_title("Comparison of Gon, GRASP and PBS")
    plt.show()


if __name__ == "__main__":
    plot_stacked_bar(orlib_comparisons)
    plot_confusion_matrix(orlib_comparisons)
