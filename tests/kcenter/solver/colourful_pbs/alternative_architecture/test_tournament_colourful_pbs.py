import pytest

from src.kcenter.colourful_pbs.alternative_architecture.tournament_colourful_pbs import TournamentColourfulPBS
from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import Individual
from tests.kcenter.util.create_test_graph import basic_graph_with_outlier
from tests.kcenter.util.genetic import generate_test_population_basic_graph


@pytest.fixture
def instance():
    constraints = {Colour.BLUE: 2, Colour.RED: 2}
    k = 2
    graph = basic_graph_with_outlier()
    instance = TournamentColourfulPBS(graph, k, constraints)
    instance.population = generate_test_population_basic_graph()
    return instance


def test_tournament_selection(seed_random, instance):
    mating_pool = instance.selection()
    assert len(mating_pool) == 4
    assert mating_pool == [Individual({3, 2}), Individual({0, 1}), Individual({1, 2}), Individual({0, 1})]
