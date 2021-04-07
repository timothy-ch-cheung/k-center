import networkx as nx

from kcenter.constant.colour import Colour
from kcenter.plateau_surfer.plateau_surfer import PlateauSurfer
from server.tsplib_graph_loader import TSPLIBGraphLoader

"""
Grid Optimisation to calculate Alpha and Beta values for the Greedy Randomised Build algorithm for GRASP Plateau
Surfer (Ferone et. al. 2017)

Data Set for training are TSPLIB instances, optimal costs from Pullan 2008
"""


def grid_search(graph: nx.graph, k, opt_cost):
    for alpha in [x / 10.0 for x in range(0, 10, 1)]:
        for beta in [x / 10.0 for x in range(0, 10, 1)]:
            solver = PlateauSurfer(graph, k, alpha=alpha, beta=beta)
            print("start")
            solution = solver.solve(iterations=1)
            print(solution)


OPT = TSPLIBGraphLoader.get_opt()
results = dict()

for problem_instance in OPT.keys():
    for k, optimal_cost in OPT[problem_instance].items():
        graph = TSPLIBGraphLoader.get_graph(problem_instance)
        grid_search(graph, k, optimal_cost)
