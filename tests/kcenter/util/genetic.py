from src.kcenter.constant.colour import Colour
from src.kcenter.pbs.pbs import Individual, PBS
from tests.kcenter.util.create_test_graph import basic_graph


def generate_test_population_basic_graph():
    graph = basic_graph()
    instance = PBS(graph, 2, {Colour.BLUE: 2, Colour.RED: 2})
    one = Individual({0, 1})
    two = Individual({1, 2})
    three = Individual({2, 3})
    four = Individual({3, 4})
    population = [one, two, three, four]
    for individual in population:
        individual.init_nearest_centers(instance.points, instance.weights)

    return population + population
