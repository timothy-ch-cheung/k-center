from src.server.gow_graph_loader import GowGraphLoader


def test_load_gow_graph():
    graph = GowGraphLoader.get_graph("gow01")

    assert len(graph.nodes()) == 100
    assert len(graph.edges()) == 5050


def test_get_header():
    header = GowGraphLoader.get_header("gow01")
    assert header == (100, 18, 82, 5, 13, 61)
