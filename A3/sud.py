"""Driver of game"""
from A3.character import *
from A3.monsters import *


def print_backstory():
    """
    Print the backstory of the game.
    """
    print("*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "Welcome young adventurer!\n" +
          "The city has been overrun by 5 despicable creatures from the dark realms and we need someone to save us!\n" +
          "You must come and defeat theses monsters before it's too late!\n" + "*~~~~~~~~~~*\n")


def make_board():
    """
    Create a 5x5 game board.

    :return: a list
    """
    board = []
    for i in range(0, 5):
        for j in range(0, 5):
            board.append((i, j))
    return board


def print_board(character_stats):
    """
    Print the map.

    :param character_stats: a dictionary
    """
    printed_board = []
    for i in range(0, 5):
        for j in range(0, 5):
            if (i, j) == character_stats['Current Position']:
                printed_board.append("▣")
            else:
                printed_board.append("◻")
        printed_board.append("\n")
    print("*~~~~~~~~~~MAP~~~~~~~~~~*\n")
    print("".join(printed_board))




if __name__ == "__main__":
    doctest.testmod()
    main()
