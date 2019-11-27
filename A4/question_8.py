"""Get time/s that need the most bars to display."""
import doctest


def get_bars_total(hours: int, minutes_left: int, minutes_right: int) -> int:
    """
    Calculate total bars needed to display time.

    :param hours: an int
    :param minutes_left: an int
    :param minutes_right: an int
    :precondition: hours must be a positive int between 0 and 12
    :precondition: minutes_left must be a positive int between 0 and 12
    :precondition: minutes_right must be a positive int between 0 and 12
    :postcondition: calculate total amount of bars needed to display time
    :return: an int

    >>> get_bars_total(1, 1, 1)
    6
    >>> get_bars_total(12, 5, 9)
    18
    >>> get_bars_total(1, 0, 0)
    14
    """
    bars_in_numbers = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6, 10: 8, 11: 4, 12: 7}
    return bars_in_numbers[hours] + bars_in_numbers[minutes_left] + bars_in_numbers[minutes_right]


def check_if_higher(times: dict, bars_total: int) -> list:
    """
    Check if given bars_total is higher than the bars totals in the dictionary.

    :param times: a dictionary
    :param bars_total: an int
    :precondition: times must be a dictionary with times and bar totals
    :precondition: bars_totals must be a positive int
    :postcondition: Check if given bars_total is higher than the bars totals in the dictionary.
    :return: a list

    >>> check_if_higher({"0:00": 0}, 14)
    ['0:00']
    >>> check_if_higher({"0:00": 0, "1:10": 10}, 14)
    ['0:00', '1:10']
    >>> check_if_higher({"1:00": 14}, 6)
    []
    """
    lower_times = []
    for key, value in times.items():
        if bars_total >= value:
            lower_times.append(key)
    return lower_times


def im_not_sleepy() -> str:
    """
    Finds the time that needs the most bars to display.

    :return: a string
    """
    times = {"0:00": 0}
    for i in range(1, 13):
        for j in range(6):
            for k in range(10):
                time = str(i) + ":" + str(j) + str(k)
                bars_total = get_bars_total(i, j, k)
                lower_times = check_if_higher(times, bars_total)
                if lower_times:
                    times[time] = bars_total
                    for item in lower_times:
                        del times[item]
    for key, value in times.items():
        return key + " requires the most bars. It requires: " + str(value) + " bars to display."


if __name__ == "__main__":
    doctest.testmod()
