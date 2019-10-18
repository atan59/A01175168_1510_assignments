from unittest import TestCase
from unittest.mock import patch
import io
from A2.dungeonsanddragons import check_if_alive


class TestCheckIfAlive(TestCase):
    def test_check_if_alive_is_alive(self):
        expected = True
        actual = check_if_alive({'Name': "test", 'Race': "test", 'Class': "test", 'HP': [1, 1], 'Strength': 1,
                                 'Dexterity': 1, 'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1,
                                 'XP': 0, 'Inventory': []})
        self.assertEqual(expected, actual)

    def test_check_if_alive_is_dead(self):
        expected = False
        actual = check_if_alive({'Name': "test", 'Race': "test", 'Class': "test", 'HP': [1, 0], 'Strength': 1,
                                 'Dexterity': 1, 'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1,
                                 'XP': 0, 'Inventory': []})
        self.assertEqual(expected, actual)

    def test_check_if_alive_is_alive_is_bool(self):
        actual = check_if_alive({'Name': "test", 'Race': "test", 'Class': "test", 'HP': [1, 1], 'Strength': 1,
                                 'Dexterity': 1, 'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1,
                                 'XP': 0, 'Inventory': []})
        self.assertIs(type(actual), bool)

    def test_check_if_alive_is_dead_is_bool(self):
        actual = check_if_alive({'Name': "test", 'Race': "test", 'Class': "test", 'HP': [1, 0], 'Strength': 1,
                                 'Dexterity': 1, 'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1,
                                 'XP': 0, 'Inventory': []})
        self.assertIs(type(actual), bool)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_check_if_alive_is_alive_print(self, mock_stdout):
        expected = '\ntest is alive!\n'
        check_if_alive({'Name': "test", 'Race': "test", 'Class': "test", 'HP': [1, 1], 'Strength': 1, 'Dexterity': 1,
                        'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []})
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_check_if_alive_is_dead_print(self, mock_stdout):
        expected = '\ntest is dead!\n'
        check_if_alive({'Name': "test", 'Race': "test", 'Class': "test", 'HP': [1, 0], 'Strength': 1, 'Dexterity': 1,
                        'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []})
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)
