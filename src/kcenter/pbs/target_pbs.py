import math
from itertools import chain
from typing import Dict, Tuple, Set, Generator, Optional, List

import networkx as nx

from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import PBS, Individual


class TargetPBS(PBS):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        super().__init__(graph, k, constraints)

    def generate_population(self) -> Generator[Optional[Individual], None, None]:
        self.population = []
        MAX_FAIL_COUNT = 8
        num_fail = 0
        while len(self.population) < PBS.POPULATION_SIZE:
            candidate = self.generate_candidate()
            if self.is_diverse(candidate) or num_fail >= MAX_FAIL_COUNT:
                self.population.append(candidate)
                num_fail = 0
                yield candidate
            else:
                num_fail += 1
                yield None

    def evolve(self) -> Generator[Optional[Individual], None, None]:
        """Solves the K-Center problem using the genetic algorithm created by W. Pullan.

        Uses two mutation operators, two crossover operators and a local search.
        """

        target_reached = False
        generation = 1
        while not target_reached:
            for individual in self.population:
                for sibling in self.population:
                    if individual == sibling:
                        continue
                    candidate = self.local_search(self.mutation_random(individual), generation)
                    yield candidate if self.update_population(candidate) else None

                    child = self.local_search(self.crossover_random(individual, sibling), generation)
                    yield child if self.update_population(child) else None
                    candidate = self.local_search(self.mutation_directed(child), generation)
                    yield candidate if self.update_population(candidate) else None

                    first_child, second_child = self.crossover_directed(individual, sibling)

                    first_child = self.local_search(first_child, generation)
                    yield first_child if self.update_population(first_child) else None
                    candidate = self.local_search(self.mutation_directed(first_child), generation)
                    yield candidate if self.update_population(candidate) else None

                    second_child = self.local_search(second_child, generation)
                    yield second_child if self.update_population(second_child) else None
                    candidate = self.local_search(self.mutation_directed(second_child), generation)
                    yield candidate if self.update_population(candidate) else None
            generation += 1

    def target_solve(self, target_cost: float) -> Tuple[Dict[int, Set[int]], Set[int], float]:
        generator = chain(self.generate_population(), self.evolve())
        solution = None
        for candidate in generator:
            if candidate is not None and (math.isclose(candidate.cost, target_cost) or candidate.cost < target_cost):
                solution = candidate
                break

        clusters = {center: set() for center in solution.centers}
        outliers = set()

        for point in self.points:
            min_dist = float("inf")
            nearest_center = None
            for center in solution.centers:
                if point == center:
                    nearest_center = center
                    break
                cost = self.weights[(point, center)]
                if cost <= min_dist and cost <= solution.cost:
                    min_dist = cost
                    nearest_center = center
            if nearest_center is not None:
                clusters[nearest_center].add(point)
            else:
                outliers.add(point)

        return clusters, outliers, solution.cost
