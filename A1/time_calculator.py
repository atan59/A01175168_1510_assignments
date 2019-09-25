""""Convert seconds into days, hours, and minutes"""


def calculate_days(time):
    """
    Calculate number of days with time given in seconds.

    :param time: an int
    :precondition: time must be a positive int
    :postcondition: Calculate number of days
    :return: an int
    """
    return int(time / 86400)


def calculate_seconds_in_days(days):
    """
    Calculate number of seconds in number of days.

    :param days: an int
    :precondition: days must be a positive int
    :postcondition: Calculate number of seconds
    :return: an int
    """
    return int(days * 86400)


def calculate_hours(time):
    """
    Calculate number of hours with time given in seconds.

    :param time: an int
    :precondition: time must be a positive int
    :postcondition: Calculate number of hours
    :return: an int
    """
    return int(time / 3600)


def calculate_seconds_in_hours(hours):
    """
    Calculate number of seconds in number of hours.

    :param hours: an int
    :precondition: hours must be a positive int
    :postcondition: Calculate number of seconds
    :return: an int
    """
    return int(hours * 3600)


def calculate_minutes(time):
    """
    Calculate number of minutes given the time in seconds.

    :param time: an int
    :precondition: time must be a positive int
    :postcondition: Calculate number of minutes
    :return: an int
    """
    return int(time / 60)


def calculate_seconds_in_minutes(minutes):
    """
    Calculate number of seconds in number of seconds.

    :param minutes: an int
    :precondition: minutes must be positive int
    :postcondition: Calculate number of seconds
    :return: an int
    """
    return int(minutes * 60)


def concatenate_two_strings(string_1, string_2):
    """
    Combine two strings into one string

    :param string_1: a string
    :param string_2: a string
    :precondition: string_1 must not be an empty string
    :precondition: string_2 must not be an empty string
    :postcondition: Combine the two strings into one string
    :return: a string
    """
    return str(string_1), str(string_2)


def concatenate_three_strings(string_1, string_2, string_3):
    """
    Combine three strings into one string.

    :param string_1: a string
    :param string_2: a string
    :param string_3: a string
    :precondition: string_1 must not be an empty string
    :precondition: string_2 must not be an empty string
    :precondition: string_3 must not be an empty string
    :postcondition: Combine the three strings into one string
    :return: a string
    """
    return str(string_1), str(string_2), str(string_3)


def concatenate_four_strings(string_1, string_2, string_3, string_4):
    """
    Combine four strings into one string.

    :param string_1: a string
    :param string_2: a string
    :param string_3: a string
    :param string_4: a string
    :precondition: string_1 must not be an empty string
    :precondition: string_2 must not be an empty string
    :precondition: string_3 must not be an empty string
    :precondition: string_4 must not be an empty string
    :postcondition: Combine the four strings into one string
    :return: a string
    """
    return str(string_1), str(string_2), str(string_3), str(string_4)


def time_calculator(seconds):
    """
    Calculate days, hours, minutes, and seconds with a given amount of seconds.

    :param seconds: an int
    :precondition: seconds must be a positive int
    :postcondition: Calculate days, hours, minutes, and seconds
    """
    if seconds >= 86400:
        days = calculate_days(seconds)
        seconds = seconds - calculate_seconds_in_days(days)

        hours = calculate_hours(seconds)
        seconds = seconds - calculate_seconds_in_hours(hours)

        minutes = calculate_minutes(seconds)
        seconds = seconds - calculate_seconds_in_minutes(minutes)

        total_time = concatenate_four_strings(days, hours, minutes, seconds)

        print(total_time)
    elif 86400 > seconds >= 3600:
        hours = calculate_hours(seconds)
        seconds = seconds - calculate_seconds_in_hours(hours)

        minutes = calculate_minutes(seconds)
        seconds = seconds - calculate_seconds_in_minutes(minutes)

        total_time = concatenate_four_strings(hours, minutes, seconds)

        print(total_time)
    elif 3600 > seconds >= 60:
        minutes = calculate_minutes(seconds)
        seconds = seconds - calculate_seconds_in_minutes(minutes)

        total_time = concatenate_four_strings(minutes, seconds)

        print(total_time)
