"""A collection of functions to calculate compound interest."""
import doctest


def add(number_1, number_2):
    """
    Add two numbers together.

    :param number_1: an int or float
    :param number_2: an int or float
    :precondition: number_1 must ba an int or a float
    :precondition: number_2 must be an int or a float
    :postcondition: add number_1 and number_2 together
    :return: an int or float
    >>> add(0, 0)
    0
    >>> add(1, 1)
    2
    >>> add(-1, 3)
    2
    >>> add(30.5, 2)
    32.5
    >>> add(-2.5, 5)
    2.5
    >>> add(-1, -2)
    -3
    >>> add(-2.4, -6.4)
    -8.8
    """
    return number_1 + number_2


def multiply(number_1, number_2):
    """
    Multiply two numbers together.

    :param number_1: an int or a float
    :param number_2: an int or a float
    :precondition: number_1 must be an int or a float
    :precondition: number_2 must be an int or a float
    :postcondition: Multiply number_1 and number_2 together
    :return: an int or a float
    >>> multiply(0, 0)
    0
    >>> multiply(1, 1)
    1
    >>> multiply(0.1, 0.3)
    0.03
    >>> multiply(2, 0.5)
    1.0
    >>> multiply(-1, 1)
    -1
    >>> multiply(-1, -1)
    1
    >>> multiply(-1.5, 2)
    -3.0
    >>> multiply(-2.4, -1.2)
    2.88
    """
    return number_1 * number_2


def divide(dividend, divisor):
    """
    Divide dividend by divisor.

    :param dividend: an int or a float
    :param divisor: an int or a float
    :precondition: dividend must be an int or a float
    :precondition: divisor must be an int or a float not equal to 0
    :postcondition: divide dividend by divisor
    :return: a float
    >>> divide(0, 1)
    0.0
    >>> divide(1, 1)
    1.0
    >>> divide(2, 0.5)
    4.0
    >>> divide(1.2, 0.3)
    4.0
    >>> divide(-1, 1.0)
    -1.0
    >>> divide(-2, -0.5)
    4.0
    """
    return dividend / divisor


def exponent(base, exponent_value):
    """
    Calculate base raised to power of exponent_value.

    :param base: an int or float
    :param exponent_value: an int or float
    :precondition: base must be an int or a float
    :precondition: exponent_value must ba an int or a float
    :postcondition: Calculate base raised to the power of exponent_value
    :return: an int or float
    >>> exponent(1, 1)
    1
    >>> exponent(2, 1.0)
    2.0
    >>> exponent(0, 0)
    1
    >>> exponent(-2, 1)
    -2
    >>> exponent(-4, -1)
    -0.25
    >>> exponent(-1, -1)
    -1.0
    """
    return base ** exponent_value


def compound_interest(principal, interest_rate, times_compounded, years):
    """
    Calculate compound interest amount.

    :param principal: a positive float
    :param interest_rate: a positive float
    :param times_compounded: a positive int
    :param years: a positive int
    :precondition: principal must be a positive float
    :precondition: interest_rate must be a positive float
    :precondition: times_compound must a positive int greater than 0
    :precondition: years must be a positive int
    :postcondition: calculate compound interest amount
    :return: a float rounded to two decimal places
    >>> compound_interest(0, 0.0, 1, 0)
    0.0
    >>> compound_interest(10, 0.10, 1, 10)
    25.94
    >>> compound_interest(25, 0.05, 2, 10)
    40.97
    >>> compound_interest(10, 0.15, 4, 20)
    190.13
    """
    amount = multiply(principal,
                      exponent(add(1, divide(interest_rate, times_compounded)), multiply(times_compounded, years)))
    return round(amount, 2)


if __name__ == "__main__":
    doctest.testmod()
