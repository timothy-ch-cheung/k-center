from kcenter.constant.colour import Colour
from kcenter.pbs.pbs import PBS
from server.graph_loader import GraphLoader


def test_generate_population_medium_graph(seed_random):
    graph = GraphLoader.get_graph("medium")
    instance = PBS(graph, 4, {Colour.BLUE: 10, Colour.RED: 10})
    population = instance.generate_population()

    expected_population = [
        {8, 1, 12, 21},
        {16, 3, 4, 23},
        {9, 10, 3, 15},
        {0, 9, 4, 21},
        {17, 19, 14, 23},
        {10, 3, 14, 23},
        {18, 23, 21, 15},
        {0, 18, 3, 13}
    ]
    for i, individual in enumerate(population):
        assert individual.centers == expected_population[i]
