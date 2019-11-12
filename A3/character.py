"""Module with functions for the player's character."""
import random
import doctest


def roll_die(number_of_rolls, number_of_sides):
    """
    Roll a die with a specific number of sides a certain number of times.

    :param number_of_rolls: a positive int
    :param number_of_sides: a positive int
    :precondition: number_of_rolls must be an int greater than 0
    :precondition: number_of_sides must be an int greater than 0
    :postcondition: calculate total number after a certain number of rolls.
    :return: an int
    """
    if (number_of_rolls <= 0) or (number_of_sides <= 0):
        total = 0
    else:
        total = 0
        for rolls in range(number_of_rolls):
            total += random.randint(1, number_of_sides + 1)
    return total


def generate_name():
    """
    Ask user to input a name.

    :return: a string
    """
    name = input("What would you like your name to be?: ")
    while len(name) <= 0:
        print("That's an invalid name!")
        name = input("What would you like your name to be?: ")
    return name


def create_character():
    """
    Create a character.

    :return: a dictionary
    """
    name = generate_name()
    character_stats = {'Name': name, 'HP': [10, 10], 'Current Position': (0, 0)}

    return character_stats


def get_user_choice():
    """
    Get user choice.

    :return: a string
    """
    choice = input("*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "Which direction would you like to go?\n" +
                   "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "1. North\n" + "2. East\n" + "3. South\n" +
                   "4. West\n" + "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "Please type number from 1 - 4\n" +
                   "If you would like to quit, type \"q\"\n" + "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" +
                   "Choice: ")
    while choice not in ['1', '2', '3', '4', 'q']:
        print("*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "That's not a valid choice!\n" +
              "Please input your choice again.\n" + "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n")
        choice = input("*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "Which direction would you like to go?\n" +
                       "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "1. North\n" + "2. East\n" + "3. South\n" +
                       "4. West\n" + "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" +
                       "Please type number from 1 - 4\n" + "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "Choice: ")
    return choice


def validate_move(board, character, direction):
    """
    Check if move is valid.

    :param board: a list
    :param character: a dictionary
    :param direction: a string
    :precondition: board must be a list of tuples
    :precondition: character must be a dictionary with a key "Current Position"
    :precondition: direction must be a string
    :postcondition: check if move is valid within the board
    :return: a boolean

    >>> validate_move([(0, 0), (0, 1), (1, 0), (1, 1)], {"Current Position": (0, 0)}, "2")
    True
    >>> validate_move([(0, 0), (0, 1), (1, 0), (1, 1)], {"Current Position": (0, 0)}, "1")
    False
    """
    if direction == "1":
        move = (character["Current Position"][0] - 1, character["Current Position"][1])
    elif direction == "2":
        move = (character["Current Position"][0], character["Current Position"][1] + 1)
    elif direction == "3":
        move = (character["Current Position"][0] + 1, character["Current Position"][1])
    elif direction == "4":
        move = (character["Current Position"][0], character["Current Position"][1] - 1)
    if move in board:
        result = True
    else:
        result = False
    return result


def move_character(character, direction):
    """
    Move a character one step.

    :param character: a dictionary
    :param direction: a string
    :precondition: character must be a dictionary with a key "Current Position"
    :precondition: direction must be a string
    :postcondition: move character one step in specified direction
    """
    if direction == "1":
        character["Current Position"] = (character["Current Position"][0] - 1, character["Current Position"][1])
    elif direction == "2":
        character["Current Position"] = (character["Current Position"][0], character["Current Position"][1] + 1)
    elif direction == "3":
        character["Current Position"] = (character["Current Position"][0] + 1, character["Current Position"][1])
    elif direction == "4":
        character["Current Position"] = (character["Current Position"][0], character["Current Position"][1] - 1)


if __name__ == "__main__":
    doctest.testmod()
