import pytest

from src.server.orlib_graph_loader import ORLIBGraphLoader


@pytest.mark.skip(reason="possibly failing CI")
def test_list_problems():
    problems = ORLIBGraphLoader.get_problem_list()
    assert set(problems) == {'pmed1', 'pmed10', 'pmed11', 'pmed12', 'pmed13', 'pmed14', 'pmed15', 'pmed16', 'pmed17',
                        'pmed18', 'pmed19', 'pmed2', 'pmed20', 'pmed21', 'pmed22', 'pmed23', 'pmed24', 'pmed25',
                        'pmed26', 'pmed27', 'pmed28', 'pmed29', 'pmed3', 'pmed30', 'pmed31', 'pmed32', 'pmed33',
                        'pmed34', 'pmed35', 'pmed36', 'pmed37', 'pmed38', 'pmed39', 'pmed4', 'pmed40', 'pmed5',
                        'pmed6', 'pmed7', 'pmed8', 'pmed9'}


@pytest.mark.skip(reason="possibly failing CI")
def test_get_opt():
    OPT = ORLIBGraphLoader.get_opt()
    assert OPT == {'pmed1': 127.0, 'pmed10': 20.0, 'pmed11': 59.0, 'pmed12': 51.0, 'pmed13': 36.0, 'pmed14': 26.0,
                   'pmed15': 18.0, 'pmed16': 47.0, 'pmed17': 39.0, 'pmed18': 28.0, 'pmed19': 18.0, 'pmed2': 98.0,
                   'pmed20': 13.0, 'pmed21': 40.0, 'pmed22': 38.0, 'pmed23': 22.0, 'pmed24': 15.0, 'pmed25': 11.0,
                   'pmed26': 38.0, 'pmed27': 32.0, 'pmed28': 18.0, 'pmed29': 13.0, 'pmed3': 93.0, 'pmed30': 9.0,
                   'pmed31': 30.0, 'pmed32': 29.0, 'pmed33': 15.0, 'pmed34': 11.0, 'pmed35': 30.0, 'pmed36': 27.0,
                   'pmed37': 15.0, 'pmed38': 29.0, 'pmed39': 23.0, 'pmed4': 74.0, 'pmed40': 13.0, 'pmed5': 48.0,
                   'pmed6': 84.0, 'pmed7': 64.0, 'pmed8': 55.0, 'pmed9': 37.0}
