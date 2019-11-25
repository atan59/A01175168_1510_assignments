"""Find all prime numbers in a range from 0 to an integer given by the user."""


def eratosthenes(upper_bound: int) -> list:
    number_list = list(range(0, upper_bound + 1))
    number_list = remove_zero_and_one(number_list)
    return number_list


def check_if_zero_or_one(number: int) -> bool:
    return 0 <= number <= 1


def check_if_prime(number: int) -> bool:
    pass


def check_if_multiple(number: int) -> bool:
    pass


def remove_multiples(number: int, number_list: list) -> list:
    number_list = [number for number in number_list if not check_if_zero_or_one(number)]
    return number_list


def remove_zero_and_one(number_list: list) -> list:
    number_list = [number for number in number_list if not check_if_zero_or_one(number)]
    return number_list


eratosthenes(5)
