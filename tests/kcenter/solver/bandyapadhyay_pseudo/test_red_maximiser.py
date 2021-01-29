from src.kcenter.bandyapadhyay_pseudo.red_maximiser import RedMaximiser
from tests.kcenter.util.create_test_graph import basic_graph, basic_graph_with_outlier


def test_red_maximiser_basic_graph():
    graph = basic_graph()
    # Output of Bandyapadhyay et al. clustering algorithm for basic graph
    clusters = {4: {3, 4}, 2: {0, 1, 2}}

    maximiser = RedMaximiser(graph, clusters, min_blue_coverage=3)
    solution = maximiser.solve(k=2)

    assert solution[2] == 1.0
    assert solution[4] == 1.0


def test_red_maximiser_basic_graph_with_outlier():
    graph = basic_graph_with_outlier()
    # Output of Bandyapadhyay et al. clustering algorithm for basic graph
    clusters = {4: {3, 4}, 2: {2}, 1: {0, 1}}

    maximiser = RedMaximiser(graph, clusters, min_blue_coverage=2)
    solution = maximiser.solve(k=2)

    assert solution[1] == 1.0
    assert solution[2] == 0.0
    assert solution[4] == 1.0
