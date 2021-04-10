from src.server.gow_graph_loader import GowGraphLoader


def test_list_problems():
    problems = GowGraphLoader.get_problem_list()
    assert problems == ['gow01', 'gow02', 'gow03', 'gow04', 'gow05', 'gow06', 'gow07', 'gow08', 'gow09', 'gow10',
                        'gow11', 'gow12', 'gow13', 'gow14', 'gow15', 'gow16', 'gow17', 'gow18', 'gow19', 'gow20',
                        'gow21', 'gow22', 'gow23', 'gow24', 'gow25', 'gow26', 'gow27', 'gow28', 'gow29', 'gow30',
                        'gow31', 'gow32', 'gow33', 'gow34', 'gow35', 'gow36', 'gow37', 'gow38', 'gow39', 'gow40']
