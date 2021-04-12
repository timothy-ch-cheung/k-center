import itertools
import math
import random
from functools import reduce
from typing import Dict, Set, Tuple, List, Optional

import networkx as nx

from src.kcenter.constant.colour import Colour
from src.kcenter.constant.solver_state import SolverState
from src.kcenter.pbs.pbs import PBS, Individual
from src.kcenter.solver.abstract_generator import Solution
from src.kcenter.verify.verify import cluster


class PBSSteps:
    DECIMAL_PLACES = 3

    @staticmethod
    def round_coord(coord: Tuple[float, float]):
        return round(coord[0], PBSSteps.DECIMAL_PLACES), round(coord[1], PBSSteps.DECIMAL_PLACES)

    @staticmethod
    def nodes_to_coords(graph: nx.Graph, centers: Set[int]) -> Set[Tuple[float, float]]:
        coordinates = set()
        for center in centers:
            coord = tuple(graph.nodes()[center]["pos"])
            coordinates.add(PBSSteps.round_coord(coord))
        return coordinates

    @staticmethod
    def node_to_coord(graph: nx.Graph, center: int):
        return PBSSteps.round_coord(tuple(graph.nodes()[center]["pos"]))

    @staticmethod
    def inspect_header(generation):
        if generation == 0:
            return "POPULATION GENERATION: "
        else:
            return f"INSPECT GENERATION {generation}: "

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
        return "The initial population is generated, the evolution phase can now be started"

    @staticmethod
    def end_of_generation(solutions):
        best_individual, min_cost = PBSSteps.get_best_individual(solutions)
        return f"The best individual in this generation is {best_individual} with a cost of {round(min_cost, PBSSteps.DECIMAL_PLACES)}"

    @staticmethod
    def finished_evolving(num_generations, solutions):
        best_individual, min_cost = PBSSteps.get_best_individual(solutions)
        return f"{num_generations} generations were completed. The fittest individual was {best_individual} with a cost of {round(min_cost, PBSSteps.DECIMAL_PLACES)}"

    @staticmethod
    def inspect_initialise_local_search(centers: Set[Tuple[float, float]], k: int, generation: int):
        header = PBSSteps.inspect_header(generation)
        return header + f"The current individual {centers} has less than {k} centers, {k - len(centers)} more needs to be added"

    @staticmethod
    def inspect_initialise_local_search_add(new_center: Tuple[float, float], cost: float, generation: int):
        header = PBSSteps.inspect_header(generation)
        return header + f"The point furthest away from its nearest center, the point at {new_center}, is added to the solution, the new cost is {round(cost, PBSSteps.DECIMAL_PLACES)}"

    @staticmethod
    def inspect_end_initialise_local_search(centers: Set[Tuple[float, float]], generation: int):
        header = PBSSteps.inspect_header(generation)
        return header + f"At the end of local search initialisation, the set of centers is {centers}"

    @staticmethod
    def inspect_begin_local_search(generation: int):
        return PBSSteps.inspect_header(
            generation) + "We now enter a phase where we make swaps between points and centers."

    @staticmethod
    def inspect_best_pair_swapped(old_center: Tuple[float, float], new_center: Tuple[float, float], cost: float,
                                  generation: int):
        return PBSSteps.inspect_header(
            generation) + f"""{old_center} is removed from the set of centers and it is replaced with {new_center}, the new cost is {round(cost, PBSSteps.DECIMAL_PLACES)}"""

    @staticmethod
    def inspect_best_pair_not_swapped(old_center: Tuple[float, float], new_center: Tuple[float, float],
                                      generation: int):
        return PBSSteps.inspect_header(
            generation) + f"""{old_center} and {new_center} we identified as the best center and point pair to swap, 
            but the swap was not made as they have already been swapped before in this invocation of local search"""

    @staticmethod
    def inspect_local_search_end(centers: Set[Tuple[float, float]], cost: float, iterations: int, generation: int):
        header = PBSSteps.inspect_header(generation)
        return header + f"""The local search ended after {iterations} iterations, the new cost of the solution (with 
        centers {centers}) is {round(cost, PBSSteps.DECIMAL_PLACES)}"""

    @staticmethod
    def inspect_population_updated(centers: Set[Tuple[float, float]], generation: int):
        header = PBSSteps.inspect_header(generation)
        return header + f"{centers} will improve the population; it replaces the lowest ranked individual in the population"

    @staticmethod
    def inspect_population_not_updated(centers: Set[Tuple[float, float]], generation: int):
        header = PBSSteps.inspect_header(generation)
        return header + f"{centers} will not improve the population so it is not added"

    @staticmethod
    def inspect_mutation_random(old_centers: Set[Tuple[float, float]], new_centers: Set[Tuple[float, float]],
                                generation: int):
        header = PBSSteps.inspect_header(generation)
        return header + f"""A random mutation operator is applied to the set of centers {old_centers}, where a subset of the original centers is combined with points sampled random to get the new center set {new_centers}"""

    @staticmethod
    def inspect_mutation_directed(old_centers: Set[Tuple[float, float]], new_centers: Set[Tuple[float, float]],
                                  generation: int):
        header = PBSSteps.inspect_header(generation)
        return header + f"""A directed mutation operator is applied to the set of centers {old_centers}, where the two 
        closest centers {old_centers.difference(new_centers)} are deleted from the solution, resulting in the set of 
        centers {new_centers}"""

    @staticmethod
    def inspect_crossover_random(first_parent_centers: Set[Tuple[float, float]],
                                 second_parent_centers: Set[Tuple[float, float]],
                                 child_centers: Set[Tuple[float, float]],
                                 k: int, generation: int):
        header = PBSSteps.inspect_header(generation)
        return header + f"""A random crossover operator is applied to the two parents {first_parent_centers} and 
        {second_parent_centers}, by randomly sampling {k} centers from them - the resulting child center set is 
        {child_centers}"""

    @staticmethod
    def inspect_crossover_directed(first_parent_centers: Set[Tuple[float, float]],
                                   second_parent_centers: Set[Tuple[float, float]],
                                   first_child_centers: Set[Tuple[float, float]],
                                   second_child_centers: Set[Tuple[float, float]], generation: int):
        header = PBSSteps.inspect_header(generation)
        return header + f"""A directed crossover operator is applied to the two parents {first_parent_centers} and 
        {second_parent_centers}, two children are created by mixing centers from the parents - the resulting children 
        are {first_child_centers} and {second_child_centers}"""

    @staticmethod
    def inspect_local_search_start(name: str, generation: int):
        header = PBSSteps.inspect_header(generation)
        return header + f"Local search is ran on the {name} solution"

    @staticmethod
    def inspect_mutation_directed_start(name: str, generation: int):
        header = PBSSteps.inspect_header(generation)
        return header + f"After the {name} solution has been locally optimised, it is passed through a directed mutation operator"

    @staticmethod
    def inspect_generate_candidate(intial_point: Tuple[float, float], k: int, generation: int):
        header = PBSSteps.inspect_header(generation)
        return header + f"""To generate a candidate, an initial point {intial_point} is randomly selected - local 
        search is invoked on it to create a solution with {k} centers"""

    @staticmethod
    def inspect_add_generated_candidate(candidate_centers: Set[Tuple[float, float]], generation: int):
        header = PBSSteps.inspect_header(generation)
        return header + f"""The centers {candidate_centers} are added to the population"""


class SteppedPBS(PBS):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int], name: Optional[str] = None):
        if name is None:
            super().__init__(graph, k, constraints)
        else:
            super().__init__(graph, k, constraints, name=name)

    def yield_population(self):
        solutions = []

        for individual in self.population:
            clustered_points = cluster(self.graph, individual.centers, individual.cost)
            outliers = self.points.difference(reduce((lambda x, y: x.union(y)), clustered_points.values()))
            solutions.append(Solution(clusters=clustered_points, outliers=outliers, cost=individual.cost))
        return solutions

    def yield_candidate(self, individual: Individual):
        cost = self.find_cost(individual)
        clustered_points = cluster(self.graph, individual.centers, cost)
        outliers = self.points.difference(reduce((lambda x, y: x.union(y)), clustered_points.values()))
        return [Solution(clusters=clustered_points, outliers=outliers, cost=cost)]

    def initilise_local_search(self, individual: Individual):
        if len(individual.centers) < self.k:
            center_coords = PBSSteps.nodes_to_coords(self.graph, individual.centers)
            label = PBSSteps.inspect_initialise_local_search(center_coords, self.k, self.current_generation)
            yield self.yield_candidate(individual), label, SolverState.ACTIVE_SUB
        while len(individual.centers) < self.k:
            new_center_point = self.get_next_point(individual)
            furthest_point_facility = individual.nearest_centers[new_center_point].nearest
            if furthest_point_facility is None:
                nwk = list(self.points.difference(individual.centers))
            else:
                k = PBS.linear_search(self.graph.nodes()[new_center_point]["neighbours"], furthest_point_facility.point)
                nwk = list(set(PBS.get_nwk(self.graph, new_center_point, k)).difference(individual.centers))
            new_center = random.choice(nwk)
            self.add_center(new_center, individual)
            label = PBSSteps.inspect_initialise_local_search_add(PBSSteps.node_to_coord(self.graph, new_center),
                                                                 individual.cost,
                                                                 self.current_generation)
            yield self.yield_candidate(individual), label, SolverState.ACTIVE_SUB
        self.find_cost(individual)
        center_coords = PBSSteps.nodes_to_coords(self.graph, individual.centers)
        label = PBSSteps.inspect_end_initialise_local_search(center_coords, self.current_generation)
        yield self.yield_candidate(individual), label, SolverState.ACTIVE_SUB

    def local_search(self, individual: Individual, generation: int):
        """Local search on an individual in the population to find the locally optimise solution

        :param individual: Individual in population
        :param generation: Current generation number
        :return: A new individual with optimised solution
        """
        initialise_local_search = self.initilise_local_search(individual)
        for step in initialise_local_search:
            yield step
        termination_iterations_cost = math.floor(0.1 * (generation + 1) * self.graph.number_of_nodes())
        termination_iterations_count = 2 * self.graph.number_of_nodes()
        iteration = 0
        stale_iterations = 0
        optimised_individual = individual.copy()
        swapped = set()
        yield self.yield_candidate(optimised_individual), PBSSteps.inspect_begin_local_search(
            self.current_generation), SolverState.ACTIVE_SUB
        while stale_iterations < termination_iterations_cost and iteration < termination_iterations_count:
            prev_cost = optimised_individual.cost
            furthest_point = self.get_furthest_point(optimised_individual)
            point_to_remove, point_to_add = self.find_pair(furthest_point, optimised_individual)
            old_center_coords = self.graph.nodes()[point_to_remove]["pos"]
            new_center_coords = self.graph.nodes()[point_to_add]["pos"]
            if (point_to_remove, point_to_add) not in swapped:
                self.remove_center(point_to_remove, optimised_individual)
                self.add_center(point_to_add, optimised_individual)
                swapped.add((point_to_remove, point_to_add))
                label = PBSSteps.inspect_best_pair_swapped(old_center_coords, new_center_coords,
                                                           optimised_individual.cost, self.current_generation)
                yield self.yield_candidate(optimised_individual), label, SolverState.ACTIVE_SUB
            else:
                label = PBSSteps.inspect_best_pair_not_swapped(old_center_coords, new_center_coords,
                                                               self.current_generation)
                yield self.yield_candidate(optimised_individual), label, SolverState.ACTIVE_SUB

            iteration += 1
            if optimised_individual.cost >= prev_cost:
                stale_iterations += 1

        center_coords = PBSSteps.nodes_to_coords(self.graph, optimised_individual.centers)
        label = PBSSteps.inspect_local_search_end(center_coords, optimised_individual.cost, iteration, generation)
        yield self.yield_candidate(optimised_individual), label, SolverState.ACTIVE_SUB

    def update_population(self, candidate: Individual):
        center_coords = PBSSteps.nodes_to_coords(self.graph, candidate.centers)
        if super().update_population(candidate):
            yield self.yield_candidate(candidate), PBSSteps.inspect_population_updated(center_coords,
                                                                                       self.current_generation), SolverState.ACTIVE_SUB
        else:
            yield self.yield_candidate(candidate), PBSSteps.inspect_population_not_updated(center_coords,
                                                                                           self.current_generation), SolverState.ACTIVE_SUB

    def mutation_random_step(self, individual: Individual, generation: int):
        old_center_coords = PBSSteps.nodes_to_coords(self.graph, individual.centers)
        individual = self.mutation_random(individual)
        new_center_coords = PBSSteps.nodes_to_coords(self.graph, individual.centers)
        label = PBSSteps.inspect_mutation_random(old_center_coords, new_center_coords, generation)
        yield self.yield_candidate(individual), label, SolverState.ACTIVE_SUB

        yield self.yield_candidate(individual), PBSSteps.inspect_local_search_start("randomly mutated",
                                                                                    generation), SolverState.ACTIVE_SUB
        local_search_steps = self.local_search(individual, generation)
        for step in local_search_steps:
            yield step

        yield next(self.update_population(individual))

    def mutation_directed_step(self, individual: Individual, generation: int):
        old_center_coords = PBSSteps.nodes_to_coords(self.graph, individual.centers)
        individual = self.mutation_random(individual)
        new_center_coords = PBSSteps.nodes_to_coords(self.graph, individual.centers)
        label = PBSSteps.inspect_mutation_directed(old_center_coords, new_center_coords, generation)
        yield self.yield_candidate(individual), label, SolverState.ACTIVE_SUB

        yield self.yield_candidate(individual), PBSSteps.inspect_local_search_start("directed mutated",
                                                                                    generation), SolverState.ACTIVE_SUB
        local_search_steps = self.local_search(individual, generation)
        for step in local_search_steps:
            yield step

        yield next(self.update_population(individual))

    def crossover_random_steps(self, first_parent: Individual, second_parent: Individual, generation: int):
        first_parent_center_coords = PBSSteps.nodes_to_coords(self.graph, first_parent.centers)
        second_parent_center_coords = PBSSteps.nodes_to_coords(self.graph, second_parent.centers)
        child = self.crossover_random(first_parent, second_parent)
        child_center_coords = PBSSteps.nodes_to_coords(self.graph, child.centers)
        label = PBSSteps.inspect_crossover_random(first_parent_center_coords, second_parent_center_coords,
                                                  child_center_coords, self.k, generation)
        yield self.yield_candidate(child), label, SolverState.ACTIVE_SUB

        yield self.yield_candidate(child), PBSSteps.inspect_local_search_start("child",
                                                                               generation), SolverState.ACTIVE_SUB
        local_search_steps = self.local_search(child, generation)
        for step in local_search_steps:
            yield step

        yield next(self.update_population(child))
        yield self.yield_candidate(child), PBSSteps.inspect_mutation_directed_start("child",
                                                                                    generation), SolverState.ACTIVE_SUB
        mutation_directed_steps = self.mutation_directed_step(child, generation)
        for step in mutation_directed_steps:
            yield step

    def crossover_directed_step(self, first_parent: Individual, second_parent: Individual, generation: int):
        first_parent_center_coords = PBSSteps.nodes_to_coords(self.graph, first_parent.centers)
        second_parent_center_coords = PBSSteps.nodes_to_coords(self.graph, second_parent.centers)
        first_child, second_child = self.crossover_directed(first_parent, second_parent)
        first_child_coords = PBSSteps.nodes_to_coords(self.graph, first_child.centers)
        second_child_coords = PBSSteps.nodes_to_coords(self.graph, second_child.centers)
        label = PBSSteps.inspect_crossover_directed(first_parent_center_coords, second_parent_center_coords,
                                                    first_child_coords, second_child_coords, generation)
        yield self.yield_candidate(first_child), label, SolverState.ACTIVE_SUB

        yield self.yield_candidate(first_child), PBSSteps.inspect_local_search_start("first child",
                                                                                     generation), SolverState.ACTIVE_SUB
        local_search_steps = self.local_search(first_child, generation)
        for step in local_search_steps:
            yield step

        yield next(self.update_population(first_child))
        yield self.yield_candidate(first_child), PBSSteps.inspect_mutation_directed_start("first child",
                                                                                          generation), SolverState.ACTIVE_SUB
        mutation_directed_steps = self.mutation_directed_step(first_child, generation)
        for step in mutation_directed_steps:
            yield step

        yield self.yield_candidate(second_parent), PBSSteps.inspect_local_search_start("second child",
                                                                                       generation), SolverState.ACTIVE_SUB
        local_search_steps = self.local_search(second_child, generation)
        for step in local_search_steps:
            yield step

        yield next(self.update_population(second_child))
        yield self.yield_candidate(second_child), PBSSteps.inspect_mutation_directed_start("second child",
                                                                                           generation), SolverState.ACTIVE_SUB
        mutation_directed_steps = self.mutation_directed_step(second_child, generation)
        for step in mutation_directed_steps:
            yield step

    def generate_population(self, seed_population : Optional[List[Individual]] = None) -> List[Individual]:
        def generate_candidate(self: PBS):
            init_center = random.choice(tuple(self.points))
            candidate = Individual({init_center})
            self.init_individual(candidate)
            return candidate, init_center

        while len(self.population) < PBS.POPULATION_SIZE:
            candidate, init_center = generate_candidate(self)
            init_center_coord = PBSSteps.node_to_coord(self.graph, init_center)
            label = PBSSteps.inspect_generate_candidate(init_center_coord, self.k, self.current_generation)
            self.yield_population(), label, SolverState.ACTIVE_SUB
            local_search_steps = self.local_search(candidate, self.current_generation)
            for step in local_search_steps:
                yield step
            self.population.append(candidate)
            candidate_center_coords = PBSSteps.nodes_to_coords(self.graph, candidate.centers)
            yield self.yield_candidate(candidate), PBSSteps.inspect_add_generated_candidate(candidate_center_coords,
                                                                                            self.current_generation), SolverState.ACTIVE_SUB

    def generator(self):
        self.population = []
        generate_population_steps = self.generate_population()
        for step in generate_population_steps:
            yield step
        self.no_update_count = 0
        yield self.yield_population(), PBSSteps.initial_population(), SolverState.ACTIVE_MAIN

        for generation in range(1, PBS.GENERATIONS + 1):
            self.current_generation = generation
            for individual in self.population:
                for sibling in self.population:
                    if individual == sibling:
                        continue
                    mutation_random_steps = self.mutation_random_step(sibling, generation)
                    crossover_random_steps = self.crossover_random_steps(individual, sibling, generation)
                    crossover_directed_steps = self.crossover_directed_step(individual, sibling, generation)
                    generation_steps = itertools.chain(mutation_random_steps,
                                                       crossover_random_steps,
                                                       crossover_directed_steps)
                    for step in generation_steps:
                        yield step
            solutions = self.yield_population()
            yield solutions, PBSSteps.end_of_generation(solutions), SolverState.ACTIVE_MAIN

        solutions = self.yield_population()
        yield solutions, PBSSteps.finished_evolving(PBS.GENERATIONS, solutions), SolverState.INACTIVE
