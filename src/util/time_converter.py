from decimal import Decimal


def from_seconds(seconds: float):
    """Break down time in seconds into more units.

    param seconds: time in seconds
    return: seconds broken down into years, weeks, days, hours, minutes, and seconds
    """
    years, seconds = divmod(seconds, 365 * 24 * 60 * 60)
    weeks, seconds = divmod(seconds, 7 * 24 * 60 * 60)
    days, seconds = divmod(seconds, 24 * 60 * 60)
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)
    return years, weeks, days, hours, minutes, seconds


def seconds_to_string(seconds: float):
    """Return a string describing time in seconds in more units.

    param seconds: time in seconds
    return: string describing time in seconds, omitting units which have a value of 0 - e.g. will not return the 'years'
    component if there are 0 years
    """
    years, weeks, days, hours, minutes, seconds = from_seconds(seconds)
    string = ""
    if years != 0 and years > 10 ** 10:
        string += f"{'%.2E' % Decimal(years)} years,"
    elif years != 0:
        string += "" if years == 0 else f"{int(years)} years,"
    string += "" if weeks == 0 else f"{int(weeks)} weeks,"
    string += "" if days == 0 else f"{int(days)} days,"
    string += "" if hours == 0 else f"{int(hours)} hours,"
    string += "" if minutes == 0 else f"{int(minutes)} minutes,"
    string += f"{round(seconds, 3)} seconds"
    return string
