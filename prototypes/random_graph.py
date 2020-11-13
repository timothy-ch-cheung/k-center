import random
import numpy as np

graph_space = 100

def get_random_point(opt, point):
    length = np.sqrt(np.random.uniform(0, opt))
    angle = np.pi * np.random.uniform(0, 2)

    x = length * np.cos(angle)
    y = length * np.sin(angle)
    point[0] += x
    point[1] += y
    return point

def generate_graph(n, r, b, num_centers, num_outliers, opt, name):
    centers = set()
    points = set()
    for i in range(num_centers):
        center_coord = (random.uniform(0, graph_space), random.uniform(0, graph_space))
        while center_coord in centers:
            # need to randomise colour
            center_coord = (random.uniform(0, graph_space), random.uniform(0, graph_space))
        centers.add(center_coord)

    num_cluster_nodes = n - num_centers - num_outliers
    for i in range(num_cluster_nodes):
        # gaussian distribute points length max opt around centers
        get_random_point(opt, )

    f = open(f"{name}.txt", "w")
    f.write(f"{n} {num_centers} {b} {r} {b} {r}")



print(random.gauss(1, 2))