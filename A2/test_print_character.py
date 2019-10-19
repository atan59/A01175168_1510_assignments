from unittest import TestCase
from unittest.mock import patch
import io
from A2.dungeonsanddragons import print_character


class TestPrint_character(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_hit_die_six(self, mock_stdout):
        expected = "\n*~~~~~~~~~~Character Sheet~~~~~~~~~~*\n" + \
                   "Name: test\n" + \
                   "Race: Human\n" + \
                   "Class: Wizard\n" + \
                   "HP: 6/6\n" + \
                   "XP: 0\n" + \
                   "*~~~~~~~~~~~~~~~Stats~~~~~~~~~~~~~~~*\n" + \
                   "Strength: 6\n" + \
                   "Dexterity: 6\n" + \
                   "Constitution: 6\n" + \
                   "Intelligence: 6\n" + \
                   "Wisdom: 6\n" + \
                   "Charisma: 6\n" + \
                   "*~~~~~~~~~~~~~Inventory~~~~~~~~~~~~~*\n" + \
                   "Nothing...\n\n"
        print_character({'Name': 'test', 'Race': 'human', 'Class': 'wizard', 'HP': [6, 6], 'Strength': 6,
                         'Dexterity': 6, 'Constitution': 6, 'Intelligence': 6, 'Wisdom': 6, 'Charisma': 6,
                         'Inventory': [], 'XP': 0})
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_hit_die_eight(self, mock_stdout):
        expected = "\n*~~~~~~~~~~Character Sheet~~~~~~~~~~*\n" + \
                   "Name: test\n" + \
                   "Race: Human\n" + \
                   "Class: Bard\n" + \
                   "HP: 8/8\n" + \
                   "XP: 0\n" + \
                   "*~~~~~~~~~~~~~~~Stats~~~~~~~~~~~~~~~*\n" + \
                   "Strength: 6\n" + \
                   "Dexterity: 6\n" + \
                   "Constitution: 6\n" + \
                   "Intelligence: 6\n" + \
                   "Wisdom: 6\n" + \
                   "Charisma: 6\n" + \
                   "*~~~~~~~~~~~~~Inventory~~~~~~~~~~~~~*\n" + \
                   "Nothing...\n\n"
        print_character({'Name': 'test', 'Race': 'human', 'Class': 'bard', 'HP': [8, 8], 'Strength': 6,
                         'Dexterity': 6, 'Constitution': 6, 'Intelligence': 6, 'Wisdom': 6, 'Charisma': 6,
                         'Inventory': [], 'XP': 0})
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_hit_die_ten(self, mock_stdout):
        expected = "\n*~~~~~~~~~~Character Sheet~~~~~~~~~~*\n" + \
                   "Name: test\n" + \
                   "Race: Human\n" + \
                   "Class: Fighter\n" + \
                   "HP: 10/10\n" + \
                   "XP: 0\n" + \
                   "*~~~~~~~~~~~~~~~Stats~~~~~~~~~~~~~~~*\n" + \
                   "Strength: 6\n" + \
                   "Dexterity: 6\n" + \
                   "Constitution: 6\n" + \
                   "Intelligence: 6\n" + \
                   "Wisdom: 6\n" + \
                   "Charisma: 6\n" + \
                   "*~~~~~~~~~~~~~Inventory~~~~~~~~~~~~~*\n" + \
                   "Nothing...\n\n"
        print_character({'Name': 'test', 'Race': 'human', 'Class': 'fighter', 'HP': [10, 10], 'Strength': 6,
                         'Dexterity': 6, 'Constitution': 6, 'Intelligence': 6, 'Wisdom': 6, 'Charisma': 6,
                         'Inventory': [], 'XP': 0})
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_hit_die_twelve(self, mock_stdout):
        expected = "\n*~~~~~~~~~~Character Sheet~~~~~~~~~~*\n" + \
                   "Name: test\n" + \
                   "Race: Human\n" + \
                   "Class: Barbarian\n" + \
                   "HP: 12/12\n" + \
                   "XP: 0\n" + \
                   "*~~~~~~~~~~~~~~~Stats~~~~~~~~~~~~~~~*\n" + \
                   "Strength: 6\n" + \
                   "Dexterity: 6\n" + \
                   "Constitution: 6\n" + \
                   "Intelligence: 6\n" + \
                   "Wisdom: 6\n" + \
                   "Charisma: 6\n" + \
                   "*~~~~~~~~~~~~~Inventory~~~~~~~~~~~~~*\n" + \
                   "Nothing...\n\n"
        print_character({'Name': 'test', 'Race': 'human', 'Class': 'barbarian', 'HP': [12, 12], 'Strength': 6,
                         'Dexterity': 6, 'Constitution': 6, 'Intelligence': 6, 'Wisdom': 6, 'Charisma': 6,
                         'Inventory': [], 'XP': 0})
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)
