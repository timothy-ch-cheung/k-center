import random
from typing import Optional, Dict

import networkx as nx

from src.kcenter.colourful_pbs.alternative_architecture.abstract_genetic_colourful_pbs import \
    AbstractGeneticColourfulPBS
from src.kcenter.constant.colour import Colour


class TournamentColourfulPBS(AbstractGeneticColourfulPBS):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int], mating_pool_size: Optional[int] = None):
        if mating_pool_size is None:
            super().__init__(graph, k, constraints)
        else:
            super().__init__(graph, k, constraints, mating_pool_size=mating_pool_size)

    def selection(self):
        """Perform tournament selection

        :return: list of individuals
        """
        mating_pool = []
        fitness = [x.cost for x in self.population]
        population_pool = list(self.population)
        for i in range(self.MATING_POOL_SIZE):
            pos = random.sample(set([x for x in range(len(population_pool))]), 2)
            contestant_1, contestant_2 = population_pool[pos[0]], population_pool[pos[1]]
            if contestant_1.cost < contestant_2.cost:
                mating_pool.append(contestant_1)
                del population_pool[pos[0]], fitness[pos[0]]
            else:
                mating_pool.append(contestant_2)
                del population_pool[pos[1]], fitness[pos[1]]
        return mating_pool
