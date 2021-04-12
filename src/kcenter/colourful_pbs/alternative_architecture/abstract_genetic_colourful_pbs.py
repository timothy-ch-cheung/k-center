from abc import abstractmethod
from itertools import chain
from typing import Dict, Generator, Optional, List

import networkx as nx

from src.kcenter.colourful_pbs.target_colourful_pbs import TargetColourfulPBS
from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import Individual, PBS


def calculate_offspring_size(population_size):
    div = 4
    offspring_div = [population_size // div + (1 if x < population_size % div else 0) for x in range(div)]
    num_x1, num_x2, num_m1, num_m2 = offspring_div[0], offspring_div[1], offspring_div[2], offspring_div[3]
    return num_x1, num_x2, num_m1, num_m2


class AbstractGeneticColourfulPBS(TargetColourfulPBS):

    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int], mating_pool_size: int = 4,
                 name: Optional[str] = None):
        super().__init__(graph, k, constraints, name=name)
        self.MATING_POOL_SIZE = mating_pool_size

    @abstractmethod
    def selection(self):
        pass

    def gen_offspring_crossover_1(self, mating_pool: List[Individual], num_offspring: int, generation: int):
        offspring_count = 0
        k = 0
        while offspring_count < num_offspring:
            if k + 1 >= len(mating_pool):
                k = 0
            first_parent = mating_pool[k]
            second_parent = mating_pool[k + 1]
            k += 1

            child = self.local_search(self.crossover_random(first_parent, second_parent), generation)
            offspring_count += 1
            yield child

    def gen_offspring_crossover_2(self, mating_pool: List[Individual], num_offspring: int, generation: int):
        offspring_count = 0
        k = len(mating_pool) - 1
        while offspring_count < num_offspring:
            if k - 1 <= 0:
                k = len(mating_pool) - 1
            first_parent = mating_pool[k]
            second_parent = mating_pool[k - 1]
            k -= 1

            first_child, second_child = self.crossover_directed(first_parent, second_parent)

            first_child = self.local_search(first_child, generation)
            offspring_count += 1
            yield first_child

            if offspring_count < num_offspring:
                second_child = self.local_search(second_child, generation)
                offspring_count += 1
                yield second_child

    def gen_offspring_mutation_1(self, mating_pool: List[Individual], num_offspring: int, generation: int):
        offspring_count = 0
        while offspring_count < num_offspring:
            for k in range(len(mating_pool)):
                if offspring_count >= num_offspring:
                    break

                parent = mating_pool[k]
                child = self.local_search(self.mutation_random(parent), generation)
                offspring_count += 1
                yield child

    def gen_offspring_mutation_2(self, mating_pool: List[Individual], num_offspring: int, generation: int):
        offspring_count = 0
        while offspring_count < num_offspring:
            for k in range(len(mating_pool) - 1, -1, -1):
                if offspring_count >= num_offspring:
                    break

                parent = mating_pool[k]
                child = self.local_search(self.mutation_directed(parent), generation)
                offspring_count += 1
                yield child

    def evolve(self) -> Generator[Optional[Individual], None, None]:
        """Solves the K-Center problem using the genetic algorithm created by W. Pullan.

        Uses two mutation operators, two crossover operators and a local search.
        """

        target_reached = False
        generation = 1

        while not target_reached:
            mating_pool = self.selection()
            new_population = []

            # Create new population with [25% crossover 1][25% crossover 2][25% mutation 1][25% mutation 2]
            num_x1, num_x2, num_m1, num_m2 = calculate_offspring_size(PBS.POPULATION_SIZE)

            crossover_1 = self.gen_offspring_crossover_1(mating_pool, num_x1, generation)
            crossover_2 = self.gen_offspring_crossover_2(mating_pool, num_x2, generation)
            mutation_1 = self.gen_offspring_mutation_1(mating_pool, num_m1, generation)
            mutation_2 = self.gen_offspring_mutation_2(mating_pool, num_m2, generation)

            generator = chain(crossover_1, crossover_2, mutation_1, mutation_2)
            for individual in generator:
                new_population.append(individual)
                yield individual

            self.population = new_population
            generation += 1
