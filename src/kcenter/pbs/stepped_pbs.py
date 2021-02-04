from typing import Dict

import networkx as nx

from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import PBS


class PBSSteps:
    DECIMAL_PLACES = 3

    @staticmethod
    def get_best_individual(solutions):
        best_individual = -1
        min_cost = float("inf")
        for i, individual in enumerate(solutions):
            if individual["radius"] < min_cost:
                best_individual = i
                min_cost = individual["radius"]
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
            centers = [{"x": pos[0], "y": pos[1]} for pos in [self.graph.nodes()[i]["pos"] for i in individual.centers]]
            solutions.append({
                "k": len(centers), "centers": centers, "radius": individual.cost, "outliers": 0, "timeTaken": 0
            })
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

        fittest_individual = min(self.population, key=lambda x: x.cost)
        clusters = {center: set() for center in fittest_individual.centers}
        outliers = set()

        for point in self.points:
            min_dist = float("inf")
            nearest_center = None
            for center in fittest_individual.centers:
                if point == center:
                    nearest_center = center
                    break
                cost = self.weights[(point, center)]
                if cost <= min_dist and cost <= fittest_individual.cost:
                    min_dist = cost
                    nearest_center = center
            if nearest_center is not None:
                clusters[nearest_center].add(point)
            else:
                outliers.add(point)

        solutions = self.yield_population()
        yield solutions, PBSSteps.finished_evolving(PBS.GENERATIONS, solutions), False
