from server.orlib_graph_loader import ORLIBGraphLoader


def test_get_pmed3_undirected():
    graph = ORLIBGraphLoader.get_graph("pmed3")
    nodes = list(graph.nodes())
    for i in nodes:
        assert len(graph[i]) == 100
        for j in nodes:
            assert graph[i][j]["weight"] == graph[j][i]["weight"]