from src.server.gow_graph_loader import GowGraphLoader


def test_load_gow_graph():
    graph = GowGraphLoader.get_graph("gow01")

    assert len(graph.nodes()) == 100
    assert len(graph.edges()) == 5050