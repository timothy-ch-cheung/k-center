import random
from typing import Optional, Dict

import networkx as nx

from src.kcenter.colourful_pbs.alternative_architecture.abstract_genetic_colourful_pbs import \
    AbstractGeneticColourfulPBS
from src.kcenter.constant.colour import Colour


class RouletteColourfulPBS(AbstractGeneticColourfulPBS):
    def __init__(self, graph: nx.Graph, k: int, constraints: Dict[Colour, int], mating_pool_size: Optional[int] = None,
                 name: Optional[str] = None):
        if mating_pool_size is None:
            super().__init__(graph, k, constraints, name=name)
        else:
            super().__init__(graph, k, constraints, mating_pool_size=mating_pool_size, name=name)

    def selection(self):
        """Perform roulette selection

        :return: list of individuals
        """
        mating_pool = []
        fitness = [x.cost for x in self.population]
        population_pool = list(self.population)
        for i in range(self.MATING_POOL_SIZE):
            pos = random.choices(
                range(len(population_pool)),
                fitness,
                k=1
            )[0]
            mating_pool.append(population_pool[pos])
            del population_pool[pos], fitness[pos]
        return mating_pool
