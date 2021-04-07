import pyomo.environ as pyo
from scipy.optimize import linprog

# Maximise         z = 2x + 3y
# Subject to       2x + 3y <= 9
#                  x, y >= 0

# SciPy method #

objective = [-2, -3]
constraint_lhs = [[2, 3]]
constraint_rhs = [9]
x_bounds = (0, None)
y_bounds = (0, None)

scipy_solution = linprog(objective, constraint_lhs, constraint_rhs, bounds=[x_bounds, y_bounds])
print(f'SciPy linprog: {scipy_solution.x[0]}, y: {scipy_solution.x[1]}')


# Pyomo method #

def objective_func(mdl):
    return 2 * mdl.x + 3 * mdl.y


def constraint(mdl):
    return 2 * mdl.x + 3 * mdl.y <= 9


model = pyo.ConcreteModel()
model.x = pyo.Var(within=pyo.NonNegativeReals)
model.y = pyo.Var(within=pyo.NonNegativeReals)

model.constraint = pyo.Constraint(rule=constraint)
model.objective = pyo.Objective(rule=objective_func, sense=pyo.maximize)
solver = pyo.SolverFactory('glpk')
pyomo_solution = solver.solve(model)
print(f'Pyomo x: {model.x.value}, y: {model.y.value}')
