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


def choose_inventory(inventory):
    """
    Buy items from a shop.

    :param inventory: a list
    :precondition: inventory must be a populated list
    :postcondition: allow player to buy items from a shop inventory
    :return: a sorted list
    """
    purchased = []
    choice = 0
    purchases_made = 0

    print("*~~~~~~~~~~Welcome to " + inventory[0] + "!~~~~~~~~~~*\n" +
          "To buy an item, type the number of the item.\n" +
          "If you are finished and would like to exit the shop, type -1.\n")

    while (len(inventory) - 1) > choice > 0:
        print("\nHere is the list of the items we sell:\n" + "*~~~~~~~~~~~~~~~Items~~~~~~~~~~~~~~~*")
        for i in range(1, len(inventory)):
            print(str(i) + ". " + inventory[i])

        choice = int(input("\nWhat would you like you buy? (-1 to exit): "))

        if choice > 0:
            purchased.append(inventory[choice])
            print("\nYou have purchased one " + inventory[choice] + ".")

            purchases_made += 1
            print("You have purchased a total of " + str(purchases_made) + " items from the shop.\n")

    return sorted(purchased)


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


def select_race():
    """
    Select a race for the character.

    :return: a string
    """
    races = ['dragonborn', 'dwarf', 'elf', 'gnome', 'half-elf', 'halfling', 'half-orc', 'human', 'tiefling']
    print("\n*~~~~~Choose Your Race~~~~~*\n" +
          "Here's a list of races you can choose from.\n" +
          "Please type the number of the race you would like to pick. (e.g. 1)\n" +
          "1. Dragonborn\n" + "2. Dwarf\n" + "3. Elf\n" + "4. Gnome\n" + "5. Half-Elf\n" + "6. Halfling\n" +
          "7. Half-Orc\n" + "8. Human\n" + "9. Tiefling\n")

    choice = int(input("Your Race Choice: "))

    while choice < 1 or choice > 9:
        print("You have entered an invalid choice.\n" + "Please choose again.\n" +
              "Here's the list of valid choices.\n" +
              "Please type the number of the class you would like to pick. (e.g. 1)\n" +
              "1. Dragonborn\n" + "2. Dwarf\n" + "3. Elf\n" + "4. Gnome\n" + "5. Half-Elf\n" +
              "6. Halfling\n" + "7. Half-Orc\n" + "8. Human\n" + "9. Tiefling\n")
        choice = int(input("Your Race Choice: "))

    return races[choice - 1]


def select_class():
    """
    Select a class for the character.

    :return: a list
    """
    player_class =['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rouge', 'sorcerer',
                   'warlock', 'wizard']
    print("\n*~~~~~Choose Your Class~~~~~*\n" +
          "Here's a list of classes you can choose from.\n" +
          "Please type the number of the class you would like to pick. (e.g. 1)\n" +
          "1. Barbarian\n" + "2. Bard\n" + "3. Cleric\n" + "4. Druid\n" + "5. Fighter\n" + "6. Monk\n" +
          "7. Paladin\n" + "8. Ranger\n" + "9. Rouge\n" + "10. Sorcerer\n" + "11. Warlock\n" + "12. Wizard\n")

    choice = int(input("Your Class Choice: "))

    while choice < 1 or choice > 12:
        print("You have entered an invalid choice.\n" + "Please choose again.\n" +
              "Here's the list of valid choices.\n" +
              "Please type the number of the class you would like to pick. (e.g. 1)\n" +
              "1. Barbarian\n" + "2. Bard\n" + "3. Cleric\n" + "4. Druid\n" + "5. Fighter\n" + "6. Monk\n" +
              "7. Paladin\n" + "8. Ranger\n" + "9. Rouge\n" + "10. Sorcerer\n" + "11. Warlock\n" + "12. Wizard\n")

    return player_class[choice - 1]


def get_class_hit_die(character_class):
    """
    Get the number of sides of the character's hit die based on their class.

    :param character_class: a string
    :precondition: character_class must be a string with a valid class
    :postcondition: Get the number of sides of the die for the character's class
    :return: an int

    >>> get_class_hit_die('wizard')
    6
    >>> get_class_hit_die('bard')
    8
    >>> get_class_hit_die('fighter')
    10
    >>> get_class_hit_die('barbarian')
    12
    """
    six_side = ['sorcerer', 'wizard']
    eight_side = ['bard', 'cleric', 'druid', 'monk', 'rouge', 'warlock']
    ten_side = ['fighter', 'paladin', 'ranger']
    twelve_side = ['barbarian']

    side = 0

    if character_class in six_side:
        side = 6
    elif character_class in eight_side:
        side = 8
    elif character_class in ten_side:
        side = 10
    elif character_class in twelve_side:
        side = 12
    return side


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
        character_stats = {}
        attribute_names = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']

        character_stats['Name'] = generate_name(name_length)
        character_stats['Race'] = select_race()

        character_stats['Class'] = select_class()

        hp = roll_die(1, get_class_hit_die(character_stats['Class']))
        character_stats['HP'] = [hp, hp]

        for i in range(0, 6):
            character_stats[attribute_names[i]] = roll_die(3, 6)

        character_stats['XP'] = 0
        character_stats['Inventory'] = []
        return character_stats


def print_character(character):
    """
    Print a character sheet with all character information.

    :param character: a dictionary
    :precondition: character must be a correctly formatted dictionary
    :postcondition: print a filled out character sheet
    """
    result = "\n*~~~~~~~~~~Character Sheet~~~~~~~~~~*\n" + \
             "Name: " + character['Name'] + "\n" + \
             "Race: " + character['Race'].capitalize() + "\n" + \
             "Class: " + character['Class'].capitalize() + "\n" + \
             "HP: " + str(character['HP'][0]) + "/" + str(character['HP'][1]) + "\n" + \
             "XP: " + str(character['XP']) + "\n" + \
             "*~~~~~~~~~~~~~~~Stats~~~~~~~~~~~~~~~*\n" + \
             "Strength: " + str(character['Strength']) + "\n" + \
             "Dexterity: " + str(character['Dexterity']) + "\n" + \
             "Constitution: " + str(character['Constitution']) + "\n" + \
             "Intelligence: " + str(character['Intelligence']) + "\n" + \
             "Wisdom: " + str(character['Wisdom']) + "\n" + \
             "Charisma: " + str(character['Charisma']) + "\n" + \
             "*~~~~~~~~~~~~~Inventory~~~~~~~~~~~~~*\n"

    if not character['Inventory']:
        result += "Nothing...\n"
    else:
        for i in range(0, len(character['Inventory'])):
            result += str(i + 1) + ". " + character['Inventory'][i] + "\n"

    print(result)


def combat_round(opponent_one, opponent_two):
    """
    Run a single round of combat.

    :param opponent_one: a dictionary
    :param opponent_two: a dictionary
    :precondition: opponent_one must be a correctly formatted dictionary
    :precondition: opponent_two must be a correctly formatted dictionary
    :postcondition: run a single round of combat
    """
    if check_first_attack() == 1:
        print(opponent_one['Name'] + " rolled a higher number so they get to attack first.")
        if check_dex_roll(opponent_one, opponent_two):
            attack(opponent_one, opponent_two)
            if check_if_alive(opponent_two):
                print("\nNow it is " + opponent_two['Name'] + "'s turn to attack!")
                if check_dex_roll(opponent_two, opponent_one):
                    attack(opponent_two, opponent_one)
                    check_if_alive(opponent_one)
        else:
            print("\nNow it is " + opponent_two['Name'] + "'s turn to attack!")
            if check_dex_roll(opponent_two, opponent_one):
                attack(opponent_two, opponent_one)
                check_if_alive(opponent_one)

    else:
        print(opponent_two['Name'] + " rolled a higher number so they get to attack first.")
        if check_dex_roll(opponent_two, opponent_one):
            attack(opponent_two, opponent_one)
            if check_if_alive(opponent_one):
                print("\nNow it is " + opponent_one['Name'] + "'s turn to attack!")
                if check_dex_roll(opponent_one, opponent_two):
                    attack(opponent_one, opponent_two)
                    check_if_alive(opponent_two)
        else:
            print("\nNow it is " + opponent_one['Name'] + "'s turn to attack!")
            if check_dex_roll(opponent_one, opponent_two):
                attack(opponent_one, opponent_two)
                check_if_alive(opponent_two)


def check_first_attack():
    """
    Check which opponent attacks first.

    :return: an int
    """
    opponent_one = 0
    opponent_two = 0

    while opponent_one == opponent_two:
        opponent_one = roll_die(1, 20)
        opponent_two = roll_die(1, 20)

    if opponent_one > opponent_two:
        result = 1
    else:
        result = 2

    return result


def check_dex_roll(attacker, victim):
    """
    Check if attacker's roll is greater than victim's dexterity.

    :param attacker: a dictionary
    :param victim: a dictionary
    :precondition: attacker must be a correctly formatted dictionary
    :precondition: victim must be a correctly formatted dictionary
    :postcondition: check if attacker's roll is greater than victim's dexterity
    :return: a boolean
    """
    dex_roll = roll_die(1, 20)
    print("\n" + attacker['Name'] + " rolled a " + str(dex_roll) + ".")
    print(victim['Name'] + " has a dexterity of " + str(victim['Dexterity']) + ".")

    if dex_roll > victim['Dexterity']:
        print("\n" + attacker['Name'] + " successfully attacked!")
        result = True
    else:
        print("\n" + attacker['Name'] + " unsuccessfully attacked!")
        result = False

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
    hit_points = roll_die(1, get_class_hit_die(attacker['Class']))

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
    """
    if character['HP'][1] == 0:
        print("\n" + character['Name'] + " is dead!")
        result = False
    else:
        print("\n" + character['Name'] + " is alive!")
        result = True
    return result


def main():
    """
    Run a demo for the game.
    """
    shop_inventory = ['The Fantastic Plane Tradepost', 'Adamantine Armor', 'Demon Armor', 'Dwarven Plate',
                      'Mariner\'s Armor', 'Sentinel Shield', 'Spellguard Shield', 'Sun Blade',
                      'Wand of Enemy Destruction', 'Javelin of Lightning']

    end_demo = "n"
    while end_demo == "n":
        print("\n*~~~~~~~~~~Dungeons and Dragons Demo~~~~~~~~~~*\n")
        print("Welcome to the demo!\n" + "Let's start off by creating your character!\n")

        name_length_1 = int(input("How many syllables do you want in your name?: "))

        character = create_character(name_length_1)

        print("\nHere's your character's stats!")
        print_character(character)

        print("Now let's create an opponent!\n")

        name_length_2 = int(input("How many syllables do you want in your opponent's name?: "))

        opponent = create_character(name_length_2)

        print("\nHere's your opponent's stats!")
        print_character(opponent)

        enter_shop = (input("Would you like to go into the shop? (\"y\" or \"n\"): ")).lower()

        if enter_shop == "y":
            character['Inventory'] = choose_inventory(shop_inventory)

            print("\nHere's your updated character stats!")
            print("\nThe items you've purchased are now in your inventory!")
            print_character(character)

        print("\nNow let's have a short combat round!")
        print("\n*~~~~~~~~~~Combat Round~~~~~~~~~~*")
        combat_round(character, opponent)
        print("\nThat's the end of the combat round!")

        end_demo = (input("Would you like to end the demo? (\"y\" or \"n\"): ")).lower()

    print("*~~~~~~~~~~~~~~~~~~~~The End~~~~~~~~~~~~~~~~~~~~*")

    doctest.testmod()


if __name__ == "__main__":
    main()
