import random, math
from typing import Tuple, Dict, Set, Generator, List

import networkx as nx

from src.kcenter.constant.colour import Colour
from src.kcenter.solver.abstract_solver import AbstractSolver


class Neighbour:
    """
    Data structure to store a neighbour to a point and the distance to it.
    """

    def __init__(self, point: int, cost: float):
        self.point = point
        self.cost = cost

    def copy(self):
        return Neighbour(self.point, self.cost)

    def __eq__(self, other):
        if isinstance(other, Neighbour):
            return self.point == other.point and self.cost == other.cost
        return False

    def __str__(self):
        return "{" + f"point: {self.point}, cost: {round(self.cost, 3)}" + "}"

    def __repr__(self):
        return self.__str__()


class NearestCenters:
    """
    Data structure to store the nearest and second nearest centers to a given point
    """

    def __init__(self, nearest: Neighbour, second_nearest: Neighbour):
        self.nearest = nearest
        self.second_nearest = second_nearest

    def __eq__(self, other):
        if isinstance(other, NearestCenters):
            return self.nearest == other.nearest and self.second_nearest == other.second_nearest
        return False

    def __str__(self):
        return f'{{\'nearest_center\': {self.nearest}, \'second_nearest_center\': {self.second_nearest}}}'

    def __repr__(self):
        return self.__str__()


class Individual:
    """
    An individual in the population, storing centers that form a solution and the cost of the solution.
    """

    def __init__(self, centers: Set[int], cost=0, nearest_centers={}):
        self.centers = centers
        self.cost = cost
        self.nearest_centers = nearest_centers

    def init_nearest_centers(self, points, weights):
        """
        Calculates closest and second closest centers of every point for this individuals centers.
        :param graph: Graph in metric space containing weights between points
        """
        for point in points:
            nearest_center = None
            second_nearest_center = None
            for center in self.centers:
                if center == point:
                    continue
                cost = weights[(point, center)]
                if nearest_center is None:
                    nearest_center = Neighbour(point=center, cost=cost)
                elif cost <= nearest_center.cost:
                    second_nearest_center = nearest_center
                    nearest_center = Neighbour(point=center, cost=cost)
                elif second_nearest_center is None:
                    second_nearest_center = Neighbour(point=center, cost=cost)
                elif cost <= second_nearest_center.cost:
                    Neighbour(point=center, cost=cost)

            if point in self.centers:
                second_nearest_center = nearest_center
                nearest_center = Neighbour(point=point, cost=0)

            self.nearest_centers[point] = NearestCenters(nearest_center, second_nearest_center)
        furthest_point = max(points,
                             key=lambda x: 0
                             if self.nearest_centers[x].nearest is None
                             else self.nearest_centers[x].nearest.cost
                             )
        if self.nearest_centers[furthest_point].nearest is not None:
            self.cost = self.nearest_centers[furthest_point].nearest.cost

    def copy(self):
        return Individual(centers=self.centers, cost=self.cost, nearest_centers=self.nearest_centers)

    def __str__(self):
        return "{centers: " + str(
            list(self.centers)) + f", cost: {self.cost}, nearest_centers: {self.nearest_centers}" + "}"


class PBS(AbstractSolver):
    """
    Implementation based on the algorithm by W. Pullan from
    'A Memetic Genetic Algorithm for the Vertex p-center Problem (2008)'
    """
    POPULATION_SIZE = 8
    GENERATIONS = 3

    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int]):
        self.points = set(graph.nodes())
        self.weights = {}
        self.population = []
        self.no_update_count = 0
        for i in self.points:
            for j in self.points:
                if i == j:
                    graph.add_edge(i, j, weight=0)
                self.weights[(i, j)] = graph[i][j]["weight"]
        self.MAX_WEIGHT = max(nx.get_edge_attributes(graph, "weight").values())
        super().__init__(graph, k, constraints)
        PBS.order_edges(self.graph)

    @staticmethod
    def order_edges(graph: nx.Graph):
        """For each point in the graph, store every adjacent point in order of closest to furthest away.
        """
        points = list(graph.nodes())
        for point in points:
            neighbours = [adj for (_, adj) in graph.edges(point)]
            neighbours = sorted(neighbours, key=lambda x: graph[point][x]["weight"])
            graph.nodes()[point]["neighbours"] = neighbours

    @staticmethod
    def linear_search(array: List[int], target: int):
        """
        :param array: Array to search of items for
        :param target: target item to find
        :return: If item is found, return the index. Return -1 if not found.
        """
        for i in range(len(array)):
            if array[i] == target:
                return i
        return -1

    @staticmethod
    def get_nwk(graph: nx.Graph, w: int, k: int, nw=None) -> List[int]:
        """Get a sublist of k edges from a point w

        :param w: point to get neighbours from
        :param k: number of points to return
        :return: k neighbours from point w
        """
        if nw is None:
            nw = graph.nodes()[w]["neighbours"]
        return nw[:k]

    def add_center(self, center: int, individual: Individual):
        """Add a center to the individual and update neighbours

        :param center: Center to add
        :param individual: Individual in population
        """
        max_center_cost = 0
        individual.centers.add(center)

        for p in self.points:
            cost = self.weights[(center, p)]
            nearest_centers = individual.nearest_centers[p]
            if nearest_centers.nearest is None or cost < nearest_centers.nearest.cost:
                nearest_centers.second_nearest = nearest_centers.nearest
                nearest_centers.nearest = Neighbour(point=center, cost=cost)
            elif nearest_centers.second_nearest is None or cost < nearest_centers.second_nearest.cost:
                nearest_centers.second_nearest = Neighbour(point=center, cost=cost)

            if nearest_centers.nearest.cost > max_center_cost:
                max_center_cost = nearest_centers.nearest.cost

        individual.cost = max_center_cost

    def find_next(self, point: int, individual: Individual):
        """Find second nearest center

        :param point: Point to find second nearest center to
        :param individual: Individual in population
        :return: Second nearest neighbouring center to a point
        """
        closest = individual.nearest_centers[point].nearest.point
        min_center_cost = float("inf")
        min_center = None

        for center in individual.centers:
            if center == closest:
                continue
            cost = self.weights[(point, center)]
            if min_center_cost > cost:
                min_center_cost = cost
                min_center = center
        if min_center is None:
            return None
        else:
            return Neighbour(min_center, min_center_cost)

    def remove_center(self, center: int, individual: Individual):
        """Remove a center to the individual and update neighbours

        :param center: Center to remove
        :param individual: Individual in population
        """
        max_center_cost = 0
        individual.centers.remove(center)

        for p in self.points:
            nearest_centers = individual.nearest_centers[p]
            if nearest_centers.nearest.point == center:
                nearest_centers.nearest = nearest_centers.second_nearest
                nearest_centers.second_nearest = self.find_next(p, individual)
            elif nearest_centers.second_nearest is None or nearest_centers.second_nearest.point == center:
                nearest_centers.second_nearest = self.find_next(p, individual)

            if nearest_centers.nearest.cost > max_center_cost:
                max_center_cost = nearest_centers.nearest.cost

        individual.cost = max_center_cost

    def find_pair(self, w: int, individual: Individual) -> Tuple[int, int]:
        """Find the optimal center and vertex pair to swap to reduce cost

        :param w: point to get neighbours from
        :param individual: Individual in population
        :return: (center, vertex) pair to swap
        """
        C = self.MAX_WEIGHT
        L = set()
        furthest_point_facility = individual.nearest_centers[w].nearest
        neighbours = self.graph.nodes()[w]["neighbours"]
        k = PBS.linear_search(neighbours, furthest_point_facility.point)
        nwk = PBS.get_nwk(self.graph, w, k, neighbours)
        for i in nwk:
            if i in individual.centers:
                continue

            self.add_center(i, individual)
            M = {}
            for center in individual.centers:
                M[center] = 0

            for point in self.points:
                if i == point:
                    continue

                second_nearest = individual.nearest_centers[point].second_nearest
                nearest = individual.nearest_centers[point].nearest

                min_dist = min(self.weights[(point, i)], second_nearest.cost)
                if min_dist > M[nearest.point]:
                    M[nearest.point] = min_dist

            for center in individual.centers:
                if center == i:
                    continue
                if M[center] == C:
                    L.add((center, i))
                elif M[center] < C:
                    L = {(center, i)}
                    C = M[center]
            self.remove_center(i, individual)
        return random.choice(tuple(L))

    def get_furthest_point(self, individual: Individual):
        """Get point furthest from its nearest center

        :param individual: Individual in population
        :return: The point which is furthest from its nearest center
        """
        max_cost = 0
        max_point = 0
        for p in self.points:
            nearest = individual.nearest_centers[p].nearest
            if nearest is not None:
                if max_cost < nearest.cost:
                    max_point = p
                    max_cost = nearest.cost
                if nearest.cost == individual.cost:
                    return p
        return max_point

    def initilise_local_search(self, individual: Individual):
        while len(individual.centers) < self.k:
            furthest_point = self.get_furthest_point(individual)
            furthest_point_facility = individual.nearest_centers[furthest_point].nearest
            if furthest_point_facility is None:
                nwk = list(self.graph.nodes())
            else:
                k = PBS.linear_search(self.graph.nodes()[furthest_point]["neighbours"], furthest_point_facility.point)
                nwk = PBS.get_nwk(self.graph, furthest_point, k)
            new_center = random.choice(nwk)
            self.add_center(new_center, individual)

    def local_search(self, individual: Individual, generation: int):
        """Local search on an individual in the population to find the locally optimise solution

        :param individual: Individual in population
        :param generation: Current generation number
        :return: A new individual with optimised solution
        """
        self.initilise_local_search(individual)
        termination_iterations_cost = math.floor(0.1 * generation * self.graph.number_of_nodes())
        termination_iterations_count = 2 * self.graph.number_of_nodes()
        iteration = 0
        stale_iterations = 0
        optimised_individual = individual.copy()
        swapped = set()
        while stale_iterations < termination_iterations_cost and iteration < termination_iterations_count:
            prev_cost = optimised_individual.cost
            furthest_point = self.get_furthest_point(optimised_individual)
            point_to_remove, point_to_add = self.find_pair(furthest_point, optimised_individual)
            if (point_to_remove, point_to_add) not in swapped:
                self.remove_center(point_to_remove, optimised_individual)
                self.add_center(point_to_add, optimised_individual)
                swapped.add((point_to_remove, point_to_add))

            iteration += 1
            if optimised_individual.cost >= prev_cost:
                stale_iterations += 1

        furthest_point = self.get_furthest_point(individual)
        optimised_individual.cost = optimised_individual.nearest_centers[furthest_point].nearest.cost
        return optimised_individual

    def mutation_random(self, individual: Individual):
        """Randomly select a subset n of centers from an individual. To make up k centers again, select (k-n) centers from
        the set of vertices.

        :param individual: Individual in population
        :return: The mutated solution
        """
        q = random.randint(self.k // 2, self.k)
        other_points = self.points.difference(individual.centers)
        retained_centers = random.sample(individual.centers, q)
        new_centers = random.sample(other_points, self.k - q)
        child_solution = Individual(centers=set(retained_centers + new_centers))
        child_solution.init_nearest_centers(self.points, self.weights)
        return child_solution

    def mutation_directed(self, individual: Individual):
        """The two closest centers are deleted from the solution.

        :param individual: Individual in population
        :return: The mutated solution with the two closest centers deleted
        """
        closest_centers = None
        closest_distance = float("inf")
        for center in individual.centers:
            for other_center in individual.centers.difference({center}):
                weight = self.weights[(center, other_center)]
                if weight < closest_distance:
                    closest_distance = weight
                    closest_centers = (center, other_center)
        new_centers = individual.centers
        if closest_centers:
            new_centers = new_centers.difference(closest_centers)
        child_solution = Individual(centers=new_centers)
        child_solution.init_nearest_centers(self.points, self.weights)
        return child_solution

    def crossover_random(self, first_parent: Individual, second_parent: Individual):
        """Crossover two parents by randomly selecting centers from both parents.

        :param first_parent: An individual from the population
        :param second_parent: An individual from the population
        :return: A single child solution
        """
        new_centers = set(random.sample(first_parent.centers.union(second_parent.centers), self.k))
        child_solution = Individual(centers=new_centers)
        child_solution.init_nearest_centers(self.points, self.weights)
        return child_solution

    def crossover_directed(self, first_parent: Individual, second_parent: Individual):
        """Crossover two parents by selecting two random points and splitting the centers of the parents by calculating
        the ratio of distance between those points and the centers.

        More specifically:
        A random number q is generated [0.1, ..., 0.9]
        two random points p1 and p2
        distance between two points d[a][b]
        For first child solution:
            - All centers from parent 1 where d[center][p1]/d[center][p2] <= q
            - All centers from parent 2 where d[center][p1]/d[center][p2] > q
        For second child solution:
            - All centers from parent 1 where d[center][p1]/d[center][p2] > q
            - All centers from parent 2 where d[center][p1]/d[center][p2] <= q

        :param first_parent: An individual from the population
        :param second_parent: An individual from the population
        :return: Two child solutions
        """

        def generate_child(pbs: PBS, centers: Set[int]):
            child = Individual(centers=centers)
            if len(child.centers) > pbs.k:
                child.centers = set(random.sample(child.centers, pbs.k))
                child.init_nearest_centers(pbs.points, pbs.weights)
            else:
                child.init_nearest_centers(pbs.points, pbs.weights)
            return child

        INTERVAL_START = 0.1
        INTERVAL_END = 0.9
        first_user = random.choice(tuple(self.points))
        second_user = random.choice(tuple(self.points))
        q = random.uniform(INTERVAL_START, INTERVAL_END)
        first_child_centers = set()
        second_child_centers = set()
        for center in first_parent.centers:
            if center == second_user:
                continue
            d1 = self.weights[(center, first_user)]
            d2 = self.weights[(center, second_user)]
            if d1 / d2 <= q:
                first_child_centers.add(center)
            else:
                second_child_centers.add(center)
        for center in second_parent.centers:
            if center == second_user:
                continue
            if d1 / d2 <= q:
                second_child_centers.add(center)
            else:
                first_child_centers.add(center)

        first_child = generate_child(self, first_child_centers)
        second_child = generate_child(self, second_child_centers)
        return first_child, second_child

    def update_population(self, candidate: Individual):
        """Add the candidate to the solution if the candidate improves the population

        W. Pullan stated: "To maintain diversity in the population, no new p-center solution S is added (+) to P if it
        is close (in cost or facilities) to any Pi in P"

        We define diversity as follows:
        - 75% of centers are the same any centers in P
        - the cost is within 1% of any cost in P

        :param candidate: potential individual to add to the population
        """

        def is_between(lower_bound: float, upper_bound: float, value: float):
            return lower_bound <= value <= upper_bound

        CENTER_THRESHHOLD = 0.75
        COST_THRESHHOLD = 0.01
        is_diverse = True
        for individual in self.population:
            if len(candidate.centers.intersection(individual.centers)) > len(individual.centers) * CENTER_THRESHHOLD:
                is_diverse = False
                break

            lower = candidate.cost * (1 - COST_THRESHHOLD)
            upper = candidate.cost * (1 + COST_THRESHHOLD)
            if is_between(lower, upper, individual.cost):
                is_diverse = False
                break
        if is_diverse:
            index_max = max(range(len(self.population)), key=lambda x: self.population[x].cost)
            self.population[index_max] = candidate
            self.no_update_count = 0
        else:
            self.no_update_count += 1

        return self.population

    def generate_population(self) -> List[Individual]:
        population = []
        for i in range(PBS.POPULATION_SIZE):
            init_center = {random.choice(tuple(self.points))}
            individual = Individual(init_center)
            individual.init_nearest_centers(self.points, self.weights)
            population.append(self.local_search(individual, 0))
        return population

    def generator(self) -> Generator[Tuple[Dict[int, Set[int]], int, str], None, None]:
        pass

    def evolve(self):
        self.population = self.generate_population()
        self.no_update_count = 0

        for generation in range(1, PBS.GENERATIONS + 1):
            for i, individual in enumerate(self.population):
                for j, sibling in enumerate(self.population):
                    if i == j:
                        continue
                    self.update_population(self.local_search(self.mutation_random(individual), generation))
                    self.update_population(
                        self.local_search(self.mutation_directed(self.crossover_random(individual, sibling)),
                                          generation))

                    first_child, second_child = self.crossover_directed(individual, sibling)
                    self.update_population(self.local_search(self.mutation_directed(first_child), generation))
                    self.update_population(self.local_search(self.mutation_directed(second_child), generation))

    def solve(self) -> Tuple[Dict[int, Set[int]], Set[int], float]:
        """Solves the K-Center problem using the genetic algorithm created by W. Pullan.

        Uses two mutation operators, two crossover operators and a local search.
        """
        self.evolve()
        clusters = {}

        fittest_individual = min(self.population, key=lambda x: x.cost)
        for center in fittest_individual.centers:
            points_in_cluster = set()
            for point in self.points:
                if self.graph[center][point]["weight"] <= fittest_individual.cost:
                    points_in_cluster.add(point)
            clusters[center] = points_in_cluster
        return clusters, set(), fittest_individual.cost
