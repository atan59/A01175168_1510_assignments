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


def combat_round(character, monster):
    """
    Run a single round of combat.

    :param character: a dictionary
    :param monster: a dictionary
    :precondition: character must be a correctly formatted dictionary
    :precondition: monster must be a correctly formatted dictionary
    :postcondition: run a round of combat until someone dies
    """
    while check_if_alive(character) and check_if_alive(monster):
        if check_first_attack() == 1:
            print(character['Name'] + " attacks first!")
            attack(character, monster)
        elif check_first_attack() == 2:
            print(monster['Name'] + " attacks first!")
            attack(monster, character)


def check_first_attack():
    """
    Check which opponent attacks first.

    :return: an int
    """
    opponent_one = 0
    opponent_two = 0
    while opponent_one == opponent_two:
        opponent_one = roll_die(1, 3)
        opponent_two = roll_die(1, 3)
    if opponent_one > opponent_two:
        result = 1
    else:
        result = 2
    return result


def attack(attacker, victim):
    """
    Attack another character.

    :param attacker: a dictionary
    :param victim: a dictionary
    :precondition: attacker must be a correctly formatted dictionary
    :precondition:  victim must be a correctly formatted dictionary
    :postcondition: attacker attacks victim
    """
    hit_points = roll_die(1, 6)
    victim['HP'][1] = victim['HP'][1] - hit_points
    print("\n" + attacker['Name'] + " dealt " + str(hit_points) + " damage!")
    if victim['HP'][1] < 0:
        victim['HP'][1] = 0
    print(victim['Name'] + " has " + str(victim['HP'][1]) + " HP left.")


def check_if_alive(character):
    """
    Check if character is alive.

    :param character: a dictionary
    :precondition: character must be a correctly formatted dictionary
    :postcondition: check if character is alive
    :return: a boolean
    """
    if character['HP'][1] == 0:
        print("\n" + character['Name'] + " is dead!")
        result = False
    else:
        print("\n" + character['Name'] + " is alive!")
        result = True
    return result




if __name__ == "__main__":
    doctest.testmod()
    main()
