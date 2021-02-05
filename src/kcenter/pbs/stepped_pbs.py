from functools import reduce
from typing import Dict

import networkx as nx

from src.kcenter.solver.abstract_generator import Solution
from src.kcenter.verify.verify import cluster
from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import PBS


class PBSSteps:
    DECIMAL_PLACES = 3

    @staticmethod
    def get_best_individual(solutions):
        best_individual = -1
        min_cost = float("inf")
        for i, solution in enumerate(solutions):
            if solution.cost < min_cost:
                best_individual = i
                min_cost = solution.cost
        return best_individual, min_cost

    @staticmethod
    def initial_population():
        return "The initial population is generated."

    @staticmethod
    def end_of_generation(solutions):
        best_individual, min_cost = PBSSteps.get_best_individual(solutions)
        return f"The best individual in this generation is {best_individual} with a cost of {round(min_cost, PBSSteps.DECIMAL_PLACES)}"

    @staticmethod
    def finished_evolving(num_generations, solutions):
        best_individual, min_cost = PBSSteps.get_best_individual(solutions)
        return f"{num_generations} generations were completed. The fittest individual was {best_individual} with a cost of {round(min_cost, PBSSteps.DECIMAL_PLACES)}"


class SteppedPBS(PBS):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    def yield_population(self):
        solutions = []

        for individual in self.population:
            clustered_points = cluster(self.graph, individual.centers, individual.cost)
            outliers = self.points.difference(reduce((lambda x, y: x.union(y)), clustered_points.values()))
            solutions.append(Solution(clusters=clustered_points, outliers=outliers, cost=individual.cost))
        return solutions

    def generator(self):
        self.population = self.generate_population()
        self.no_update_count = 0
        yield self.yield_population(), PBSSteps.initial_population(), True

        for generation in range(1, PBS.GENERATIONS + 1):
            for individual in self.population:
                for sibling in self.population:
                    if individual == sibling:
                        continue
                    self.update_population(self.local_search(self.mutation_random(individual), generation))
                    self.update_population(
                        self.local_search(self.mutation_directed(self.crossover_random(individual, sibling)),
                                          generation))

                    first_child, second_child = self.crossover_directed(individual, sibling)
                    self.update_population(self.local_search(self.mutation_directed(first_child), generation))
                    self.update_population(self.local_search(self.mutation_directed(second_child), generation))
            solutions = self.yield_population()
            yield solutions, PBSSteps.end_of_generation(solutions), True

        solutions = self.yield_population()
        yield solutions, PBSSteps.finished_evolving(PBS.GENERATIONS, solutions), False
