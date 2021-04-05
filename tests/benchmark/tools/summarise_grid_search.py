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

    with open(f"summary.txt", "a+") as f:
        for ab_pair, percentages in summary.items():
            f.write(f"{ab_pair[0]} {ab_pair[1]} {sum(percentages) / len(percentages)}\n")


if __name__ == "__main__":
    summarise()
