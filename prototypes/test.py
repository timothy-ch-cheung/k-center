import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

orlib_comparisons = {
    'Gon': {'Gon': 0, 'GRASP': 15, 'PBS': 4},
    'GRASP': {'Gon': 25, 'GRASP': 0, 'PBS': 6},
    'PBS': {'Gon': 36, 'GRASP': 34, 'PBS': 0}
}

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
