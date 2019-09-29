"""Mix two primary colours to make one secondary colour."""
import doctest


def check_valid(colour):
    """
    Check if colour is a primary colour.

    :param colour: a string
    :precondition: colour must be a string
    :postcondition: return True or False based on whether choice is valid or not
    :return: a boolean
    >>> check_valid("red")
    True
    >>> check_valid("yellow")
    True
    >>> check_valid("blue")
    True
    >>> check_valid("green")
    False
    """
    if colour == "red":
        result = True
    elif colour == "yellow":
        result = True
    elif colour == "blue":
        result = True
    else:
        result = False
    return result


def check_repeat(colour_1, colour_2):
    """
    Check if colours are the same.

    :param colour_1: a string
    :param colour_2: a string
    :precondition: colour_1 must be a string
    :precondition: colour_2 must be a string
    :postcondition: return True or False based on whether the colours are the same or not
    :return: a boolean
    >>> check_repeat("red", "red")
    True
    >>> check_repeat("red", "blue")
    False
    """
    if colour_1 == colour_2:
        result = True
    else:
        result = False
    return result


def mix_colours(colour_1, colour_2):
    """
    Mix two primary colours together.

    :param colour_1: a string
    :param colour_2: a string
    :precondition: must be a string
    :precondition: must be a string
    :postcondition: mix colour_1 and colour_2 together
    :return: a string
    >>> mix_colours("red", "yellow")
    'Orange'
    >>> mix_colours("yellow", "blue")
    'Green'
    >>> mix_colours("red", "blue")
    'Purple'
    """
    if (colour_1 == "red" and colour_2 == "yellow") or (colour_1 == "yellow" and colour_2 == "red"):
        mixed_colour = "Orange"
    elif (colour_1 == "yellow" and colour_2 == "blue") or (colour_1 == "blue" and colour_2 == "yellow"):
        mixed_colour = "Green"
    elif (colour_1 == "red" and colour_2 == "blue") or (colour_1 == "blue" and colour_2 == "red"):
        mixed_colour = "Purple"
    return mixed_colour


def colour_mixer():
    """
    Mix two primary colours to make one secondary colour.
    """
    colour_1 = (input("Enter one primary colour: ")).lower()

    if not check_valid(colour_1):
        print("You have entered an invalid colour.")

    colour_2 = (input("Enter one primary colour: ")).lower()

    if not check_valid(colour_2):
        print("You have entered an invalid colour.")

    if check_repeat(colour_1, colour_2):
        print("You have entered two of the same colour.")

    print("You have created:", mix_colours(colour_1, colour_2))


if __name__ == "__main__":
    doctest.testmod()
