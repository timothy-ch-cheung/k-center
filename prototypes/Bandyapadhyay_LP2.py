import pyomo.environ as pyo
from tests.kcenter.util.create_test_graph import basic_graph, basic_graph_with_outlier, Colour

graph = basic_graph_with_outlier()

# clusters (no outliers)
#potential_clusters = {4: {3, 4}, 2: {0, 1, 2}}

# clusters (outliers)
potential_clusters = {4: {3, 4}, 2: {2}, 1: {0, 1}}
potential_cluster_centers = potential_clusters.keys()
n = len(potential_cluster_centers)
b = 2
r = 2
k = 2

model = pyo.ConcreteModel()

model.N = pyo.Set(initialize=potential_cluster_centers)

# Decision variable (should the point be a center?)
model.x = pyo.Var(model.N, within=pyo.Reals, bounds=(0, 1))

model.red_coverage = pyo.Param(initialize=r, within=pyo.PositiveIntegers)
model.blue_coverage = pyo.Param(initialize=b, within=pyo.PositiveIntegers)
model.k = pyo.Param(initialize=k, within=pyo.PositiveIntegers)


def calculate_colour_coverage(point: int, colour: Colour):
    coverage = 0
    cluster = potential_clusters[point]
    for node in cluster:
        if graph.nodes()[node]["colour"] == colour:
            coverage += 1
    return coverage


def objective_func(mdl):
    return sum(calculate_colour_coverage(x, Colour.RED) * mdl.x[x] for x in mdl.N)


model.objective = pyo.Objective(rule=objective_func, sense=pyo.maximize)


def rule_sufficient_blue(mdl):
    bixi = sum(calculate_colour_coverage(x, Colour.BLUE) * mdl.x[x] for x in mdl.N)
    return bixi >= mdl.blue_coverage


model.const1 = pyo.Constraint(model.N, rule=rule_sufficient_blue)


def rule_less_than_k(mdl):
    return sum(mdl.x[i] for i in mdl.x) <= mdl.k


model.const2 = pyo.Constraint(rule=rule_less_than_k)

solver = pyo.SolverFactory('glpk')
result = solver.solve(model, tee=False)
print("Number of solutions:", len(model.solutions))

List = list(model.x.keys())
for i in List:
    print(i, 'x:', model.x[i]())
