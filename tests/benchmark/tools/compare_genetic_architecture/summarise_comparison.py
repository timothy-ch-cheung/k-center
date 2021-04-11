import numpy as np

from server.graph_loader import GraphLoader

problems = GraphLoader.get_problem_list("TRAIN_COLOURFUL")


def summarise_file(algorithm: str, problem: str):
    costs = []
    with open(f"{algorithm}/{problem}_results.txt", "r") as f:
        for line in f.readlines():
            line = line.strip().split(" ")
            cost = float(line[0])
            costs.append(cost)

    minimum = min(costs)
    mean = np.mean(costs)
    std = np.std(costs)
    return minimum, mean, std


def summarise(algorithm: str):
    with open(f"{algorithm}_summary.txt", "w") as f:
        f.write("PROBLEM\tMIN\tMEAN\tSTD\n")
        for problem in problems:
            minimum, mean, std = sum(algorithm, problem)
            f.write(f"{problem} {minimum} {mean} {std}\n")

if __name__ == "__main__":
    summarise("")
