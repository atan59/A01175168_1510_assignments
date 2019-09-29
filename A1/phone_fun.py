"""Translate letters in a phone number into numbers."""
import doctest


def check_if_letter(digit):
    """
    Check if digit is a letter.

    :param digit: a string
    :precondition: digit must be a string
    :postcondition: return True or False based on whether the digit is a letter or not
    :return: a boolean
    >>> check_if_letter("A")
    True
    >>> check_if_letter("0")
    False
    """
    if 65 <= ord(digit) <= 90:
        result = True
    else:
        result = False
    return result


def convert_to_number(letter):
    """
    Convert a letter into a number.

    :param letter: a string
    :precondition: letter must be a one character string
    :postcondition: convert letter into a number
    :return: a string
    >>> convert_to_number("A")
    '2'
    >>> convert_to_number("D")
    '3'
    """
    if 65 <= ord(letter) <= 67:
        digit = "2"
    elif 68 <= ord(letter) <= 70:
        digit = "3"
    elif 71 <= ord(letter) <= 73:
        digit = "4"
    elif 74 <= ord(letter) <= 76:
        digit = "5"
    elif 77 <= ord(letter) <= 79:
        digit = "6"
    elif 80 <= ord(letter) <= 83:
        digit = "7"
    elif 84 <= ord(letter) <= 86:
        digit = "8"
    elif 87 <= ord(letter) <= 90:
        digit = "9"
    return digit


def check_digit(phone_number, digit):
    """
    Check if digit in phone number is letter.

    :param phone_number: a string
    :param digit: an int
    :return: an int
    >>> check_digit("123-456-7890", 0)
    '1'
    >>> check_digit("123-456-ABCD", 8)
    '2'
    """
    if check_if_letter(phone_number[digit]):
        number = convert_to_number(phone_number[digit])
    else:
        number = phone_number[digit]
    return number


def number_translator():
    phone_number = input("Enter a 10-character phone number (XXX-XXX-XXXX): ")
    new_number = ""

    new_number = new_number + check_digit(phone_number, 0) + check_digit(phone_number, 1) + \
        check_digit(phone_number, 2) + "-" + check_digit(phone_number, 4) + check_digit(phone_number, 5) + \
        check_digit(phone_number, 6) + "-" + check_digit(phone_number, 8) + check_digit(phone_number, 9) + \
        check_digit(phone_number, 10) + check_digit(phone_number, 11)

    print("The translated phone number:", new_number)


if __name__ == "__main__":
    doctest.testmod()
