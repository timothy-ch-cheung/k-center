from server.gow_graph_loader import GowGraphLoader
from server.graph_loader import GraphLoader

loader = {
    "GOWALLA": GowGraphLoader,
    "SYNTHETIC": GraphLoader
}

def print_latex_dataset_table(dataset: str):
    problem_list = loader[dataset].get_problem_list()
    for problem in problem_list:
        if dataset == "SYNTHETIC":
            problem = dataset + "/" + problem
        header = loader[dataset].get_header(problem)

        line = f"{problem.replace('SYNTHETIC/', '')}"
        for i in range(6):
            if i == 3:
                line += " &"
            line += f" & {header[i]}"

        if dataset == "SYNTHETIC":
            outliers = header[6]
            opt = "{:.2f}".format(header[7])
            line += f" & & {outliers} & {opt}"
        line += "\\\\"
        print(line)
    print()

if __name__ == "__main__":
    print_latex_dataset_table("GOWALLA")
    print_latex_dataset_table("SYNTHETIC")