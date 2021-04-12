from src.kcenter.colourful_pbs.target_colourful_pbs import TargetColourfulPBS
from tests.kcenter.solver.pbs.test_pbs import K, RELAXED_CONSTRAINTS
from tests.kcenter.util.create_test_graph import basic_graph_with_outlier


def test_set_name():
    graph = basic_graph_with_outlier()
    instance = TargetColourfulPBS(graph, K, RELAXED_CONSTRAINTS, name="test_name")
    assert instance.name == "test_name"