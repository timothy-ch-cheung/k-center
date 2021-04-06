from server.orlib_graph_loader import ORLIBGraphLoader


def test_list_problems():
    problems = ORLIBGraphLoader.get_problem_list()
    assert problems == ['pmed1', 'pmed10', 'pmed11', 'pmed12', 'pmed13', 'pmed14', 'pmed15', 'pmed16', 'pmed17',
                        'pmed18', 'pmed19', 'pmed2', 'pmed20', 'pmed21', 'pmed22', 'pmed23', 'pmed24', 'pmed25',
                        'pmed26', 'pmed27', 'pmed28', 'pmed29', 'pmed3', 'pmed30', 'pmed31', 'pmed32', 'pmed33',
                        'pmed34', 'pmed35', 'pmed36', 'pmed37', 'pmed38', 'pmed39', 'pmed4', 'pmed40', 'pmed5',
                        'pmed6', 'pmed7', 'pmed8', 'pmed9']
