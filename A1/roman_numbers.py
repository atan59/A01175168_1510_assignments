"""Convert a positive integer into a roman numeral."""
import doctest


def check_four(digit):
    """
    Check if digit is equal to four.

    :param digit: an int
    :precondition: digit must be an int
    :postcondition: return True or False based on whether digit is equal to four
    :return: a boolean
    >>> check_four(4)
    True
    >>> check_four(3)
    False
    """
    if digit == 4:
        result = True
    else:
        result = False
    return result


def check_five(digit):
    """
        Check if digit is equal to five.

        :param digit: an int
        :precondition: digit must be an int
        :postcondition: return True or False based on whether digit is equal to five
        :return: a boolean
        >>> check_five(5)
        True
        >>> check_five(3)
        False
    """
    if digit == 5:
        result = True
    else:
        result = False
    return result


def check_nine(digit):
    """
    Check if digit is equal to nine.

    :param digit: an int
    :precondition: digit must be an int
    :postcondition: return True or False based on whether digit is equal to nine
    :return: a boolean
    >>> check_nine(9)
    True
    >>> check_nine(3)
    False
    """
    if digit == 9:
        result = True
    else:
        result = False
    return result


def check_one_digit(number):
    """
    Convert a one digit number into roman numeral.

    :param number: an int
    :precondition: number must be an int
    :postcondition: convert number into a roman numeral
    :return: a string
    >>> check_one_digit(1)
    'I'
    >>> check_one_digit(4)
    'IV'
    >>> check_one_digit(8)
    'VIII'
    """
    if number == 0:
        roman_numeral = ""
    elif check_four(number):
        roman_numeral = "IV"
    elif check_five(number):
        roman_numeral = "V"
    elif check_nine(number):
        roman_numeral = "IX"
    elif number < 4:
        roman_numeral = "I" * int(number)
    elif 4 < number < 9:
        roman_numeral = "V" + "I" * (number - 5)
    return roman_numeral


def check_two_digits(number):
    """
    Convert a two digit number into roman numeral.

    :param number: an int
    :precondition: number must be an int
    :postcondition: convert number into a roman numeral
    :return: a string
    >>> check_two_digits(10)
    'X'
    >>> check_two_digits(33)
    'XXXIII'
    >>> check_two_digits(99)
    'XCIX'
    """
    tens = int(number / 10)
    ones = number - tens * 10

    if number == 0:
        roman_numeral = ""
    elif 0 < number < 10:
        roman_numeral = check_one_digit(number)
    elif 10 <= number < 20:
        tens = "X"
        ones = check_one_digit(ones)

        roman_numeral = tens + ones
    elif 20 <= number < 40:
        tens = "X" * tens
        ones = check_one_digit(ones)

        roman_numeral = tens + ones
    elif 40 <= number < 50:
        tens = "XL"
        ones = check_one_digit(ones)

        roman_numeral = tens + ones
    elif 50 <= number < 60:
        tens = "L"
        ones = check_one_digit(ones)

        roman_numeral = tens + ones
    elif 60 <= number < 90:
        tens = "L" + "X" * (tens - 5)
        ones = check_one_digit(ones)

        roman_numeral = tens + ones
    elif 90 <= number < 100:
        tens = "XC"
        ones = check_one_digit(ones)

        roman_numeral = tens + ones
    return roman_numeral


def check_three_digits(number):
    """
    Convert a three digit number into roman numeral.

    :param number: an int
    :precondition: number must be an int
    :postcondition: convert number into a roman numeral
    :return: a string
    >>> check_three_digits(100)
    'C'
    >>> check_three_digits(505)
    'DV'
    >>> check_three_digits(999)
    'CMXCIX'
    """
    hundreds = int(number / 100)
    tens = int((number - hundreds * 100) / 10)
    ones = number - hundreds * 100 - tens * 10

    if number == 0:
        roman_numeral = ""
    elif 0 < number < 10:
        roman_numeral = check_one_digit(number)
    elif 10 <= number < 100:
        roman_numeral = check_two_digits(number)
    elif 100 <= number < 200:
        hundreds = "C"
        tens_and_ones = check_two_digits(tens * 10 + ones)

        roman_numeral = hundreds + tens_and_ones
    elif 200 <= number < 400:
        hundreds = "C" * hundreds
        tens_and_ones = check_two_digits(tens * 10 + ones)

        roman_numeral = hundreds + tens_and_ones
    elif 400 <= number < 500:
        hundreds = "CD"
        tens_and_ones = check_two_digits(tens * 10 + ones)

        roman_numeral = hundreds + tens_and_ones
    elif 500 <= number < 600:
        hundreds = "D"
        tens_and_ones = check_two_digits(tens * 10 + ones)

        roman_numeral = hundreds + tens_and_ones
    elif 600 <= number < 900:
        hundreds = "D" + "C" * (hundreds - 5)
        tens_and_ones = check_two_digits(tens * 10 + ones)

        roman_numeral = hundreds + tens_and_ones
    elif 900 <= number < 1000:
        hundreds = "CM"
        tens_and_ones = check_two_digits(tens * 10 + ones)

        roman_numeral = hundreds + tens_and_ones
    return roman_numeral


def check_four_digits(number):
    """
    Convert a four digit number into roman numeral.

    :param number: an int
    :precondition: number must be an int
    :postcondition: convert number into a roman numeral
    :return: a string
    >>> check_four_digits(1000)
    'M'
    >>> check_four_digits(5050)
    'MMMMML'
    >>> check_four_digits(9999)
    'MMMMMMMMMCMXCIX'
    """
    thousands = int(number / 1000)
    hundreds = int((number - thousands * 1000) / 100)
    tens = int((number - thousands * 1000 - hundreds * 100) / 10)
    ones = number - thousands * 1000 - hundreds * 100 - tens * 10

    thousands = "M" * thousands
    hundreds_tens_and_ones = check_three_digits(hundreds * 100 + tens * 10 + ones)

    roman_numeral = thousands + hundreds_tens_and_ones
    return roman_numeral


def convert_to_roman_numeral(positive_int):
    """
    Convert a positive int to a roman numeral.

    :param positive_int: an int
    :precondition: positive_int must be a positive int
    :postcondition: Convert positive_int into a roman numeral
    :return: a string
    >>> convert_to_roman_numeral(1)
    'I'
    >>> convert_to_roman_numeral(10)
    'X'
    >>> convert_to_roman_numeral(100)
    'C'
    >>> convert_to_roman_numeral(1000)
    'M'
    """
    if len(str(positive_int)) == 5:
        converted_number = "MMMMMMMMMM"
    elif len(str(positive_int)) == 4:
        converted_number = check_four_digits(positive_int)
    elif len(str(positive_int)) == 3:
        converted_number = check_three_digits(positive_int)
    elif len(str(positive_int)) == 2:
        converted_number = check_two_digits(positive_int)
    elif len(str(positive_int)) == 1:
        converted_number = check_one_digit(positive_int)
    else:
        print("The number is out of range.")
    return converted_number


if __name__ == "__main__":
    doctest.testmod()


"""
First I used decomposition to break the function into separate sections and then even smaller sections within those
sections. This was done to reduce the size of each function and make sure that they only do one thing. After I
decomposed the main function, I used pattern matching to find blocks of code that are repeated and made those into
helper functions. I then used automation to execute the main function in organized steps.
"""
