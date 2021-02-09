import pytest

from src.util.time_converter import from_seconds, seconds_to_string

test_data = [
    (20, "20 seconds"),
    (145, "2 minutes,25 seconds"),
    (3750, "1 hours,2 minutes,30 seconds"),
    (262955, "3 days,1 hours,2 minutes,35 seconds"),
    (1558950, "2 weeks,4 days,1 hours,2 minutes,30 seconds"),
    (33094950, "1 years,2 weeks,4 days,1 hours,2 minutes,30 seconds"),
    (33094950000000000000000, "1.05E+15 years,41 weeks,5 days,18 hours,40 minutes,0 seconds")
]


@pytest.mark.parametrize("seconds, expected_string", test_data)
def test_convert_seconds_to_string(seconds, expected_string):
    assert seconds_to_string(seconds) == expected_string


def test_convert_seconds():
    years, weeks, days, hours, minutes, seconds = from_seconds(33019506)
    assert years == 1
    assert weeks == 2
    assert days == 3
    assert hours == 4
    assert minutes == 5
    assert seconds == 6
