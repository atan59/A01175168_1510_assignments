"""A collection of functions to calculate compound interest."""
import doctest


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
    amount = principal * ((1 + (interest_rate / times_compounded)) ** (times_compounded * years))
    return round(amount, 2)


if __name__ == "__main__":
    doctest.testmod()


"""
I used abstraction to ignore any details that would cause the function to have an error when it is run. I then used
automation to organize the main function into well-defined steps to execute the task.
"""
