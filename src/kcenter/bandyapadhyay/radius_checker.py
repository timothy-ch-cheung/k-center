from functools import partial
from typing import List, Optional, Dict

import networkx as nx
import pyomo.environ as pyo

from src.kcenter.constant.colour import Colour
import logging


class RadiusChecker:
    """LP program which checks if a given radius can solve the Colourful K-Center problem for a given graph

    Quote from Sayan Bandyapadhyay et al. from "A Constant Approximation for Colorful k-Center"
    It is easy to see that an optimal solution satisfies all the constraints when the guess ρ is correct
    (i.e., when ρ ≥ OP T). Therefore, henceforth, we assume that ρ = OPT.
    """

    def __init__(self, graph: nx.Graph, k: int, min_red_coverage: int, min_blue_coverage: int):
        logging.getLogger('pyomo.core').setLevel(logging.ERROR)
        self.graph = graph
        self.k = k
        self.min_red_coverage = min_red_coverage
        self.min_blue_coverage = min_blue_coverage
        self.model = None

    @staticmethod
    def get_surrounding_points(point: int, mdl: pyo.Model, graph: nx.graph) -> List[int]:
        """Gets all points within radius mdl.opt of the supplied point

        Calculates B(j, ρ) described in LP1 Bandyapadhyay et al. (2019)
        """
        surr_points = [point]
        for j in mdl.N:
            if point != j and graph[point][j]["weight"] <= mdl.opt.value:
                surr_points.append(j)
        return surr_points

    @staticmethod
    def rule_sparse_centers(mdl: pyo.Model, n: int, graph: nx.Graph) -> bool:
        """Ensures that all points are not within mdl.opt distance of too many fractionally opened centers. Which causes
        the centers to distanced from each other.

        :param n: current point to check
        """
        surr_points = RadiusChecker.get_surrounding_points(n, mdl, graph)
        xi_sum = sum(mdl.x[j] for j in surr_points)
        zj = mdl.z[n]

        return zj <= xi_sum

    @staticmethod
    def rule_k_centers(mdl: pyo.Model) -> bool:
        """Ensures that no more than K centers will be chosen
        """
        return sum(mdl.x[i] for i in mdl.x) <= mdl.k

    @staticmethod
    def rule_colour_min_coverage(mdl: pyo.Model, graph: nx.Graph, colour: Colour, coverage: int):
        """Ensures that a colour has a minimum coverage by the centers

        :param colour: colour constraint is placed on
        :param coverage: minimum number to cover
        """
        zj = sum(mdl.z[j] for j in mdl.N if graph.nodes()[j]["colour"] == colour)
        return zj >= coverage

    @staticmethod
    def objective_func(mdl: pyo.Model) -> float:
        """
        Constant objective function as the algorithm only requires a feasible solution
        """
        return 0

    def initialise_model(self, opt: float):
        self.model = pyo.ConcreteModel()

        nodes = list(self.graph.nodes())
        self.model.N = pyo.Set(initialize=nodes)

        # Decision variable: how much this point is fractionally opened as a center
        self.model.x = pyo.Var(self.model.N, within=pyo.Reals, bounds=(0, 1))
        # Decision variable: how much this point is covered by its surrounding centers
        self.model.z = pyo.Var(self.model.N, within=pyo.Reals, bounds=(0, 1))

        # constraint constants
        self.model.opt = pyo.Param(initialize=opt, within=pyo.PositiveReals)
        self.model.red_coverage = pyo.Param(initialize=self.min_red_coverage, within=pyo.PositiveIntegers)
        self.model.blue_coverage = pyo.Param(initialize=self.min_blue_coverage, within=pyo.PositiveIntegers)
        self.model.k = pyo.Param(initialize=self.k, within=pyo.PositiveIntegers)

        # set constraints
        sparse_centers = partial(RadiusChecker.rule_sparse_centers, graph=self.graph)
        self.model.rule_sparse_centers = pyo.Constraint(self.model.N, rule=sparse_centers)

        self.model.rule_k_centers = pyo.Constraint(rule=RadiusChecker.rule_k_centers)

        self.model.rule_red_coverage = pyo.Constraint(
            expr=RadiusChecker.rule_colour_min_coverage(self.model, graph=self.graph, colour=Colour.RED,
                                                        coverage=self.model.red_coverage))

        self.model.rule_blue_coverage = pyo.Constraint(
            expr=RadiusChecker.rule_colour_min_coverage(self.model, graph=self.graph, colour=Colour.BLUE,
                                                        coverage=self.model.blue_coverage))

        self.model.objective = pyo.Objective(rule=RadiusChecker.objective_func, sense=pyo.minimize)

    def verify(self, radius_guess: float, solver="glpk") -> Optional[Dict[int, Dict[str, float]]]:
        """Verifies whether a given guess at the length of the optimal radius can solve the Colourful K-Center problem
        for this graph.

        :param radius_guess: Guess of the optimal radius for the graph
        :param solver: LP solver to use
        :return: If there is a solution, a dictionary of points and their corresponding x and z values. If there isn't
        a solution None is returned.
        """
        self.initialise_model(radius_guess)

        solver = pyo.SolverFactory(solver)
        solver.solve(self.model, tee=False)

        if len(self.model.solutions) > 0:
            solution = {}
            for point in self.model.x.keys():
                solution[point] = {"x": self.model.x[point](), "z": self.model.z[point]()}
            return solution
        else:
            return None
