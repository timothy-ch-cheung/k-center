import time

import networkx as nx

from kcenter.plateau_surfer.plateau_surfer import PlateauSurfer
from server.tsplib_graph_loader import TSPLIBGraphLoader

"""
Grid Optimisation to calculate Alpha and Beta values for the Greedy Randomised Build algorithm for GRASP Plateau
Surfer (Ferone et. al. 2017)

Data Set for training are TSPLIB instances, optimal costs from Pullan 2008
"""

TRIALS = 5


def grid_search(problem: str, graph: nx.graph, k):
    with open(f"{problem}_{k}.txt", "a+") as result_file:
        alpha_beta_count = dict()
        # file format: "alpha beta cost"
        result_file.seek(0, 0)
        for line in result_file.readlines():
            line = line.strip().split(" ")
            alpha = line[0]
            beta = line[1]
            cost = float(line[2])

            if (alpha, beta) not in alpha_beta_count:
                alpha_beta_count[(alpha, beta)] = 1
            else:
                alpha_beta_count[(alpha, beta)] += 1

        candidates = []
        for alpha in [x / 10 for x in range(0, 10 + 1)]:
            for beta in [x / 10 for x in range(0, 10 + 1)]:
                pair = (str(round(alpha, 1)), str(round(beta, 1)))
                if pair not in alpha_beta_count or alpha_beta_count[pair] < 5:
                    candidates.append(pair)

        for candidate in candidates:
            alpha = float(candidate[0])
            beta = float(candidate[1])

            solver = PlateauSurfer(graph, k, alpha=alpha, beta=beta)

            for i in range(TRIALS):
                cluster, outliers, cost = solver.solve(iterations=5)
                result_file.write(f"{candidate[0]} {candidate[1]} {cost}\n")
                result_file.flush()


if __name__ == "__main__":
    OPT = TSPLIBGraphLoader.get_opt()
    results = dict()

    with open("duration.txt", "a") as f:
        for problem_instance in OPT.keys():
            for k, optimal_cost in OPT[problem_instance].items():
                graph = TSPLIBGraphLoader.get_graph(problem_instance)

                start_time = time.time()
                grid_search(problem_instance, graph, k)
                end_time = time.time()
                log_time = f"{problem_instance} k={k} time={round(end_time - start_time, 3)}\n"
                f.write(log_time)
                print(log_time)
