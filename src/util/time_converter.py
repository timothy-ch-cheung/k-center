def from_seconds(seconds: float):
    years, seconds = divmod(seconds, 365 * 24 * 60 * 60)
    weeks, seconds = divmod(seconds, 7 * 24 * 60 * 60)
    days, seconds = divmod(seconds, 24 * 60 * 60)
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)
    return years, weeks, days, hours, minutes, seconds


def seconds_to_string(seconds: float):
    years, weeks, days, hours, minutes, seconds = from_seconds(seconds)
    string = ""
    string += "" if years == 0 else f"{int(years)} years,"
    string += "" if weeks == 0 else f"{int(weeks)} weeks,"
    string += "" if days == 0 else f"{int(days)} days,"
    string += "" if hours == 0 else f"{int(hours)} hours,"
    string += "" if minutes == 0 else f"{int(minutes)} minutes,"
    string += f"{round(seconds, 3)} seconds"
    return string
