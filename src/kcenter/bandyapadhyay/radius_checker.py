import pyomo.environ as pyo

# Quote from Sayan Bandyapadhyay et al. from "A Constant Approximation for Colorful k-Center"
# It is easy to see that an optimal solution satisfies all the constraints when the guess ρ is correct
# (i.e., when ρ ≥ OP T). Therefore, henceforth, we assume that ρ = OPT

class Radius 