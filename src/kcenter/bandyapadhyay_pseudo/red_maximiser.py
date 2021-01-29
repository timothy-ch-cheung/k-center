from functools import partial
from typing import Dict, Set, Optional

import networkx as nx
import pyomo.environ as pyo

from src.kcenter.constant.colour import Colour


class RedMaximiser:
    """LP program which maximises the amount of red points covered by the centers.

    Constrained by using at most k centers and covering b blue points. If the LP finds a solution, it is guaranteed
    to meet the blue coverage requirement of the Colourful K-Center problem but it may not cover enough red points.
    """

    def __init__(self, graph: nx.Graph, clusters: Dict[int, Set[int]], min_blue_coverage: int):
        self.graph = graph
        self.clusters = clusters
        self.min_blue_coverage = min_blue_coverage
        self.model = None

    @staticmethod
    def calculate_colour_coverage(point: int, colour: Colour, graph: nx.Graph, clusters: Dict[int, Set[int]]) -> int:
        """Given a potential center, sum the number of points with a given colour that it would cover.

        :param point: potential center
        :param colour: colour to count
        :param clusters: Dictionary of centers as keys which index a set of values that belong to that cluster
        """
        coverage = 0
        cluster = clusters[point]
        for node in cluster:
            if graph.nodes()[node]["colour"] == colour:
                coverage += 1
        return coverage

    @staticmethod
    def rule_sufficient_blue(mdl: pyo.Model, N, graph: nx.Graph, clusters: Dict[int, Set[int]]) -> bool:
        """Ensures that a minimum amount of blue points are covered by the centers

        :param clusters: Dictionary of centers as keys which index a set of values that belong to that cluster
        """
        bixi = sum(RedMaximiser.calculate_colour_coverage(x, Colour.BLUE, graph, clusters) * mdl.x[x] for x in mdl.N)
        return bixi >= mdl.blue_coverage

    @staticmethod
    def rule_k_centers(mdl: pyo.Model) -> bool:
        """Ensures that no more than K centers will be chosen
        """
        return sum(mdl.x[i] for i in mdl.x) <= mdl.k

    @staticmethod
    def objective_func(mdl, graph: nx.Graph, clusters: Dict[int, Set[int]]) -> float:
        """Calculates the number of red points covered by the centers

        :param clusters: Dictionary of centers as keys which index a set of values that belong to that cluster
        """
        return sum(RedMaximiser.calculate_colour_coverage(x, Colour.RED, graph, clusters) * mdl.x[x] for x in mdl.N)

    def initialise_model(self, k: int):
        self.model = pyo.ConcreteModel()
        self.model.N = pyo.Set(initialize=self.clusters.keys())

        # Decision variable: how much this point is fractionally opened as a center
        self.model.x = pyo.Var(self.model.N, within=pyo.Reals, bounds=(0, 1))

        # constraint constants
        self.model.blue_coverage = pyo.Param(initialize=self.min_blue_coverage, within=pyo.PositiveIntegers)
        self.model.k = pyo.Param(initialize=k, within=pyo.PositiveIntegers)

        # set constraints
        min_blue = partial(RedMaximiser.rule_sufficient_blue, graph=self.graph, clusters=self.clusters)
        self.model.rule_min_blue = pyo.Constraint(rule=min_blue)
        self.model.const2 = pyo.Constraint(rule=RedMaximiser.rule_k_centers)

        objective_func = partial(RedMaximiser.objective_func, graph=self.graph, clusters=self.clusters)
        self.model.objective = pyo.Objective(rule=objective_func, sense=pyo.maximize)

    def solve(self, k: int, solver="glpk") -> Optional[Dict[int, float]]:
        """Finds centers which maximise the amount of red points covered

        :return: A Dictionary of centers (with the degree that they are fractionally opened)
        """
        self.initialise_model(k)

        solver = pyo.SolverFactory(solver)
        solver.solve(self.model, tee=False)

        solution = {}
        for point in self.model.x.keys():
            solution[point] = self.model.x[point]()
        return solution
