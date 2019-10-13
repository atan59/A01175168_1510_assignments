"""Dungeons and Dragons mini game program."""
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


def choose_inventory(inventory, selection):
    """
    Choose a certain number of items in an inventory.

    :param inventory: a list
    :param selection: a positive int
    :precondition: inventory must be a populated list
    :precondition: selection must be a positive int
    :postcondition: make a list with randomly selected items from the inventory
    :return: a list
    """
    if (inventory == []) and (selection == 0):
        result = []
    elif (inventory != []) and (selection == 0):
        result = []
    elif selection < 0:
        print("You can't make a negative selection!")
        result = []
    elif selection > len(inventory):
        print("Your selection is greater than the amount of items in the inventory.")
        result = sorted(inventory)
    elif selection == len(inventory):
        result = sorted(inventory)
    else:
        result = random.choices(inventory, None, k=selection)
        result = sorted(result)
    return result


def generate_vowel():
    """
    Generate a random vowel.

    :return: a string
    """
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']

    vowel = vowel_list[random.randint(0, len(vowel_list) - 1)]
    return vowel


def generate_consonant():
    """
    Generate a random consonant.

    :return: a string
    """
    consonant_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x',
                      'y', 'z']

    consonant = consonant_list[random.randint(0, len(consonant_list) - 1)]
    return consonant


def generate_syllable():
    """
    Generate a random syllable.

    :return: a string
    """
    return generate_consonant() + generate_vowel()


def generate_name(syllables):
    """
    Generate a name with a certain number of syllables.

    :param syllables: an int
    :precondition: must be a positive int
    :postcondition: Generate a name with a certain number of syllables.
    :return: a string
    """
    name = ''

    for i in range(0, syllables):
        name += generate_syllable()
    return name.capitalize()


def create_character(name_length):
    """
    Create a character with a name and six attributes.

    :param name_length: an int
    :precondition: name_length must be an int greater than 0
    :postcondition: create a list with a name and six mini-lists with attributes
    :return: a list
    """
    if name_length < 0:
        print("This is an invalid name length.")
    else:
        character_stats = []
        attribute_names = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']

        character_stats.append(generate_name(name_length))

        for i in range(0, 6):
            attribute = [attribute_names[i], roll_die(3, 6)]
            character_stats.append(attribute)
        return character_stats


def print_character(character):
    """
    Print character information.

    :param character: a list
    :precondition: character must be a populated list
    :postcondition: print character information

    >>> print_character(["Name", ['Strength', 3], ['Dexterity', 4], ['Constitution', 5], ['Intelligence', 6], \
    ['Wisdom', 7], ['Charisma', 8]])
    *~~~~~~~~~~Character Sheet~~~~~~~~~~*
    Name: Name
    *~~~~~~~~~~~~~~~Stats~~~~~~~~~~~~~~~*
    Strength: 3
    Dexterity: 4
    Constitution: 5
    Intelligence: 6
    Wisdom: 7
    Charisma: 8
    >>> print_character(["Name", ['Strength', 3], ['Dexterity', 4], ['Constitution', 5], ['Intelligence', 6], \
    ['Wisdom', 7], ['Charisma', 8],['Shield', 'Sword']])
    *~~~~~~~~~~Character Sheet~~~~~~~~~~*
    Name: Name
    *~~~~~~~~~~~~~~~Stats~~~~~~~~~~~~~~~*
    Strength: 3
    Dexterity: 4
    Constitution: 5
    Intelligence: 6
    Wisdom: 7
    Charisma: 8
    *~~~~~~~~~~Inventory~~~~~~~~~~*
    1. Shield
    2. Sword
    """
    result = "*~~~~~~~~~~Character Sheet~~~~~~~~~~*" + "\n" + \
             "Name: " + character[0] + "\n" + \
             "*~~~~~~~~~~~~~~~Stats~~~~~~~~~~~~~~~*" + "\n"

    for i in range(1, 7):
        if len(character) == 8:
            result += character[i][0] + ": " + str(character[i][1]) + "\n"
        else:
            if i == 6:
                result += character[i][0] + ": " + str(character[i][1])
            else:
                result += character[i][0] + ": " + str(character[i][1]) + "\n"

    if len(character) == 8:
        result += "*~~~~~~~~~~Inventory~~~~~~~~~~*" + "\n"
        for i in range(0, len(character[7])):
            if i == len(character[7]) - 1:
                result += str(i + 1) + ". " + character[7][i]
            else:
                result += str(i + 1) + ". " + character[7][i] + "\n"
    print(result)


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
