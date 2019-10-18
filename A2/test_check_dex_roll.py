from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import check_dex_roll


class TestCheckDexRoll(TestCase):
    @patch('random.randint', return_value=20)
    def test_check_dex_roll_attacker_greater(self, mock_randint):
        expected = True
        actual = check_dex_roll(
            {'Name': "test", 'Race': "test", 'Class': "test", 'HP': [1, 1], 'Strength': 1, 'Dexterity': 1,
             'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []},
            {'Name': "test2", 'Race': "test2", 'Class': "test2", 'HP': [1, 1], 'Strength': 1, 'Dexterity': 10,
             'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []})
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_check_dex_roll_attacker_less(self, mock_randint):
        expected = False
        actual = check_dex_roll(
            {'Name': "test", 'Race': "test", 'Class': "test", 'HP': [1, 1], 'Strength': 1, 'Dexterity': 1,
             'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []},
            {'Name': "test2", 'Race': "test2", 'Class': "test2", 'HP': [1, 1], 'Strength': 1, 'Dexterity': 10,
             'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []})
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=10)
    def test_check_dex_roll_attacker_equal(self, mock_randint):
        expected = False
        actual = check_dex_roll(
            {'Name': "test", 'Race': "test", 'Class': "test", 'HP': [1, 1], 'Strength': 1, 'Dexterity': 1,
             'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []},
            {'Name': "test2", 'Race': "test2", 'Class': "test2", 'HP': [1, 1], 'Strength': 1, 'Dexterity': 10,
             'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []})
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=20)
    def test_check_dex_roll_attacker_greater_is_bool(self, mock_randint):
        actual = check_dex_roll(
            {'Name': "test", 'Race': "test", 'Class': "test", 'HP': [1, 1], 'Strength': 1, 'Dexterity': 1,
             'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []},
            {'Name': "test2", 'Race': "test2", 'Class': "test2", 'HP': [1, 1], 'Strength': 1, 'Dexterity': 10,
             'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []})
        self.assertIs(type(actual), bool)

    @patch('random.randint', return_value=1)
    def test_check_dex_roll_attacker_less_is_bool(self, mock_randint):
        actual = check_dex_roll(
            {'Name': "test", 'Race': "test", 'Class': "test", 'HP': [1, 1], 'Strength': 1, 'Dexterity': 1,
             'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []},
            {'Name': "test2", 'Race': "test2", 'Class': "test2", 'HP': [1, 1], 'Strength': 1, 'Dexterity': 10,
             'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []})
        self.assertIs(type(actual), bool)

    @patch('random.randint', return_value=10)
    def test_check_dex_roll_attacker_equal_is_bool(self, mock_randint):
        actual = check_dex_roll(
            {'Name': "test", 'Race': "test", 'Class': "test", 'HP': [1, 1], 'Strength': 1, 'Dexterity': 1,
             'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []},
            {'Name': "test2", 'Race': "test2", 'Class': "test2", 'HP': [1, 1], 'Strength': 1, 'Dexterity': 10,
             'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []})
        self.assertIs(type(actual), bool)
