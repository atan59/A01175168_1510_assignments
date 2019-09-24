""""Convert seconds into days, hours, and minutes"""


def calculate_days(time):
    return int(time / 86400)


def calculate_seconds_in_days(days):
    return int(days * 86400)


def calculate_hours(time):
    return int(time / 3600)


def calculate_seconds_in_hours(hours):
    return int(hours * 3600)


def calculate_minutes(time):
    return int(time / 60)


def calculate_seconds_in_minutes(minutes):
    return int(minutes * 60)


def concatenate_two_strings(string_1, string_2):
    return str(string_1), str(string_2)


def concatenate_three_strings(string_1, string_2, string_3):
    return str(string_1), str(string_2), str(string_3)


def concatenate_four_strings(string_1, string_2, string_3, string_4):
    return str(string_1), str(string_2), str(string_3), str(string_4)


def time_calculator(seconds):
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