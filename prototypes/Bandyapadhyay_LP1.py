import pyomo.environ as pyo
from math import sqrt

# Quote from Sayan Bandyapadhyay et al. from "A Constant Approximation for Colorful k-Center"
# It is easy to see that an optimal solution satisfies all the constraints when the guess ρ is correct (i.e., when ρ ≥ OP T).
# Therefore, henceforth, we assume that ρ = OPT

# We use this LP to determine a valid "guess" of the OPT

points = [
    [1.3, 2.6],
    [1.2, 2.1],
    [0.5, 2.3],
    [5.9, 5.2],
    [6.4, 4.7]
]

colours = [
    "B",
    "B",
    "B",
    "R",
    "R"
]

n = len(points)
b = 3
r = 2
k = 2
opt_guess = 1


def euclidean_distance(p1, p2):
    return sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))


def generate_cost_matrix(data_points):
    matrix = []
    for i in data_points:
        row = []
        for j in data_points:
            row.append(euclidean_distance(i, j))
        matrix.append(row)
    return matrix


cost_matrix = generate_cost_matrix(points)
model = pyo.ConcreteModel()

print("cost_matrix:")
for row in cost_matrix:
    print([round(x, 2) for x in row])
print()
# data point cost indexes
model.N = pyo.RangeSet(n)
model.M = pyo.RangeSet(n)
model.U = pyo.RangeSet(1)

# Decision variable (should the point be a center?)
model.x = pyo.Var(model.N, within=pyo.Reals, bounds=(0, 1))
model.z = pyo.Var(model.N, within=pyo.Reals, bounds=(0, 1))

model.cost = pyo.Param(model.N, model.M, initialize=lambda model, i, j: cost_matrix[i - 1][j - 1], within=pyo.Reals)
model.colours = pyo.Param(model.N, initialize=lambda model, i: colours[i - 1], within=pyo.Any)
model.red_coverage = pyo.Param(model.U, initialize={1: r}, within=pyo.PositiveIntegers)
model.blue_coverage = pyo.Param(model.U, initialize={1: b}, within=pyo.PositiveIntegers)
model.opt_guess = pyo.Param(model.U, initialize={1: opt_guess}, within=pyo.PositiveReals)


def get_surrounding_points(i, n_points, cost, opt):
    surr_points = []
    for j in n_points:
        if cost[i, j] <= opt:
            surr_points.append(j)
    return surr_points


# We use a constant objective function as the algorithm only requires a feasible solution
def objective_func(mdl):
    return 0


model.objective = pyo.Objective(rule=objective_func, sense=pyo.minimize)


def rule_surrounding_points(mdl, N):
    surr_points = get_surrounding_points(N, mdl.N, model.cost, mdl.opt_guess[1])

    xi_sum = sum(mdl.x[j] for j in surr_points)
    zj = mdl.z[N]

    return zj <= xi_sum


model.const1 = pyo.Constraint(model.N, rule=rule_surrounding_points)


def rule_less_than_k(mdl):
    return sum(mdl.x[i] for i in mdl.x) <= k


model.const2 = pyo.Constraint(rule=rule_less_than_k)


def rule_sufficient_red(mdl, N):
    if (mdl.colours[N] != "R"):
        return pyo.Constraint.Skip
    zj = sum(mdl.z[j] for j in mdl.N if mdl.colours[j] == "R")
    return zj >= mdl.red_coverage[1]


model.const3 = pyo.Constraint(model.N, rule=rule_sufficient_red)


def rule_sufficient_blue(mdl, N):
    if (mdl.colours[N] != "B"):
        return pyo.Constraint.Skip
    zj = sum(mdl.z[j] for j in mdl.N if mdl.colours[j] == "B")
    return zj >= mdl.blue_coverage[1]


model.const4 = pyo.Constraint(model.N, rule=rule_sufficient_blue)

solver = pyo.SolverFactory('glpk')
result = solver.solve(model, tee=False)
print("Number of solutions:", len(model.solutions))

List = list(model.x.keys())
for i in List:
    print(i, 'x:', model.x[i](), 'z:', model.z[i]())
