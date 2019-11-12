"""Module for functions for monsters."""
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


def create_monster():
    """
    Create a monster.

    :return: a dictionary
    """
    names = ['The Netherling', 'The Deadly Brute', 'The Horned Blaze Boar', 'The Grisly Venom Rat', 'The Jagged Howler']
    name_choice = random.randint(0, 4)
    monster_stats = {'Name': names[name_choice], 'HP': [6, 6]}

    return monster_stats


def check_monster_encounter_chance():
    """
    Check if a monster is encountered.

    :return: a boolean
    """
    result = random.randint(0, 4)
    if result == 0:
        result = True
    else:
        result = False
    return result


def check_flee_chance():
    """
    Check if character successfully flees or not.

    :return: a boolean
    """
    result = random.randint(0, 11)
    if result == 0:
        result = False
    else:
        result = True
    return result


def flee_attack(attacker, victim):
    """
    Attack another character.

    :param attacker: a dictionary
    :param victim: a dictionary
    :precondition: attacker must be a correctly formatted dictionary
    :precondition:  victim must be a correctly formatted dictionary
    :postcondition: attacker attacks victim
    """
    hit_points = random.randint(1, 5)

    victim['HP'][1] = victim['HP'][1] - hit_points
    print("\n" + "The monster dealt " + str(hit_points) + " damage!")
    if victim['HP'][1] < 0:
        victim['HP'][1] = 0
    print(victim['Name'] + " has " + str(victim['HP'][1]) + " HP left.")


if __name__ == "__main__":
    doctest.testmod()
