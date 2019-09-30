""""Convert seconds into days, hours, and minutes"""
import doctest


def calculate_days(time):
    """
    Calculate number of days with time given in seconds.

    :param time: an int
    :precondition: time must be a positive int
    :postcondition: Calculate number of days
    :return: an int
    >>> calculate_days(86400)
    1
    >>> calculate_days(172800)
    2
    """
    return int(time / 86400)


def calculate_seconds_in_days(days):
    """
    Calculate number of seconds in number of days.

    :param days: an int
    :precondition: days must be a positive int
    :postcondition: Calculate number of seconds
    :return: an int
    >>> calculate_seconds_in_days(1)
    86400
    >>> calculate_seconds_in_days(2)
    172800
    """
    return int(days * 86400)


def calculate_hours(time):
    """
    Calculate number of hours with time given in seconds.

    :param time: an int
    :precondition: time must be a positive int
    :postcondition: Calculate number of hours
    :return: an int
    >>> calculate_hours(3600)
    1
    >>> calculate_hours(7200)
    2
    """
    return int(time / 3600)


def calculate_seconds_in_hours(hours):
    """
    Calculate number of seconds in number of hours.

    :param hours: an int
    :precondition: hours must be a positive int
    :postcondition: Calculate number of seconds
    :return: an int
    >>> calculate_seconds_in_hours(1)
    3600
    >>> calculate_seconds_in_hours(2)
    7200
    """
    return int(hours * 3600)


def calculate_minutes(time):
    """
    Calculate number of minutes given the time in seconds.

    :param time: an int
    :precondition: time must be a positive int
    :postcondition: Calculate number of minutes
    :return: an int
    >>> calculate_minutes(60)
    1
    >>> calculate_minutes(120)
    2
    """
    return int(time / 60)


def calculate_seconds_in_minutes(minutes):
    """
    Calculate number of seconds in number of seconds.

    :param minutes: an int
    :precondition: minutes must be positive int
    :postcondition: Calculate number of seconds
    :return: an int
    >>> calculate_seconds_in_minutes(1)
    60
    >>> calculate_seconds_in_minutes(2)
    120
    """
    return int(minutes * 60)


def time_calculator(seconds):
    """
    Calculate days, hours, minutes, and seconds with a given amount of seconds.

    :param seconds: an int
    :precondition: seconds must be a positive int
    :postcondition: Calculate days, hours, minutes, and seconds
    >>> time_calculator(1)
    0 Day/s 0 Hour/s 0 Minute/s 1 Second/s
    >>> time_calculator(61)
    0 Day/s 0 Hour/s 1 Minute/s 1 Second/s
    >>> time_calculator(3601)
    0 Day/s 1 Hour/s 0 Minute/s 1 Second/s
    >>> time_calculator(86461)
    1 Day/s 0 Hour/s 1 Minute/s 1 Second/s
    """

    days = calculate_days(seconds)
    seconds = seconds - calculate_seconds_in_days(days)

    hours = calculate_hours(seconds)
    seconds = seconds - calculate_seconds_in_hours(hours)

    minutes = calculate_minutes(seconds)
    seconds = seconds - calculate_seconds_in_minutes(minutes)

    total_time = "%d Day/s %d Hour/s %d Minute/s %d Second/s" % (days, hours, minutes, seconds)

    print(total_time)


if __name__ == "__main__":
    doctest.testmod()


"""
I took the main function and decomposed it into multiple steps. Then I used automation to organize my functions into
an organized way to execute the task.
"""
