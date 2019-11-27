"""Decompose an amount of money into the smallest amount of bills and coins possible."""
import doctest
import math


def cash_money(amount: float) -> dict:
    """
    Split amount of money in CAD into the smallest amount of bills and coins.

    :param amount: a float
    :precondition: amount must be a positive float
    :postcondition: Split amount of money into bills and coins in the form of a dictionary
    :return: a dictionary

    >>> cash_money(188.41)
    {100: 1, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1, 1: 1, 0.25: 1, 0.1: 1, 0.05: 1, 0.01: 1}
    >>> cash_money(100.01)
    {100: 1, 0.01: 1}
    >>> cash_money(54.23)
    {50: 1, 2: 2, 0.1: 2, 0.01: 3}
    """
    money_count = {}
    currency_list = [100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05, 0.01]

    try:
        if amount < 0 or type(amount) != float:
            raise ValueError("This is not a valid amount!")
    except (ValueError, TypeError) as e:
        print("Error: " + str(e))
    else:
        while amount != 0:
            for currency in currency_list:
                if math.floor(amount / currency) != 0:
                    money_count[currency] = math.floor(amount / currency)
                    amount = round(amount - money_count[currency] * currency, 2)
        return money_count


if __name__ == "__main__":
    doctest.testmod()
