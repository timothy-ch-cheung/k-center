import matplotlib.pyplot as plt
import numpy as np

orlib_comparisons = {
    'Gon': {'GRASP': 15, 'PBS': 4},
    'GRASP': {'Gon': 25, 'PBS': 6},
    'PBS': {'Gon': 36, 'GRASP': 34}
}

orlib_comparisons = {
    'gon': {'GRASP': 11, 'PBS': 2},
    'grasp': {'Gon': 23, 'PBS': 3},
    'pbs': {'Gon': 34, 'GRASP': 31}
}

colours = {
    'Gon': 'red',
    'GRASP': 'blue',
    'PBS': 'green'
}

y_labels = list(orlib_comparisons.keys())

first_group = [list(x.values())[0] for x in orlib_comparisons.values()]
first_group_labels = [list(x.keys())[0] for x in orlib_comparisons.values()]
first_colour_group = [colours[x] for x in first_group_labels]

second_group = [list(x.values())[1] for x in orlib_comparisons.values()]
second_group_labels = [list(x.keys())[1] for x in orlib_comparisons.values()]
second_colour_group = [colours[x] for x in second_group_labels]

ind = np.arange(len(y_labels))
width = 0.4

fig, ax = plt.subplots()
rects1 = ax.barh(ind, first_group, width, color=first_colour_group)
rects2 = ax.barh(ind + width, second_group, width, color=second_colour_group)

ax.set(xlabel='Number of problem instances with lower μ cost',
       title='Pairwise comparison of k-center algorithms')

ax.set(yticks=ind + 0.5 * width, yticklabels=y_labels, ylim=[2 * width - 1, len(y_labels)])

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

plt.show()
