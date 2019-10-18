from unittest import TestCase
from unittest.mock import patch
import io
from A2.dungeonsanddragons import attack


class TestAttack(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=1)
    def test_attack_min_print(self, mock_randint, mock_stdout):
        expected = '\ntest dealt 1 damage!\ntest has 1 HP left.\n'
        attack({'Name': "test", 'Race': "test", 'Class': "wizard", 'HP': [1, 1], 'Strength': 1, 'Dexterity': 1,
                'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []},
               {'Name': "test", 'Race': "test", 'Class': "wizard", 'HP': [2, 2], 'Strength': 1, 'Dexterity': 1,
                'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []})
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=1)
    def test_attack_min_killed_print(self, mock_randint, mock_stdout):
        expected = '\ntest dealt 1 damage!\ntest has 0 HP left.\n'
        attack({'Name': "test", 'Race': "test", 'Class': "wizard", 'HP': [1, 1], 'Strength': 1, 'Dexterity': 1,
                'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []},
               {'Name': "test", 'Race': "test", 'Class': "wizard", 'HP': [1, 1], 'Strength': 1, 'Dexterity': 1,
                'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []})
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=6)
    def test_attack_max_print(self, mock_randint, mock_stdout):
        expected = '\ntest dealt 6 damage!\ntest has 1 HP left.\n'
        attack({'Name': "test", 'Race': "test", 'Class': "wizard", 'HP': [1, 1], 'Strength': 1, 'Dexterity': 1,
                'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []},
               {'Name': "test", 'Race': "test", 'Class': "wizard", 'HP': [7, 7], 'Strength': 1, 'Dexterity': 1,
                'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []})
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=6)
    def test_attack_max_killed_print(self, mock_randint, mock_stdout):
        expected = '\ntest dealt 6 damage!\ntest has 0 HP left.\n'
        attack({'Name': "test", 'Race': "test", 'Class': "wizard", 'HP': [1, 1], 'Strength': 1, 'Dexterity': 1,
                'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []},
               {'Name': "test", 'Race': "test", 'Class': "wizard", 'HP': [1, 1], 'Strength': 1, 'Dexterity': 1,
                'Constitution': 1, 'Intelligence': 1, 'Wisdom': 1, 'Charisma': 1, 'XP': 0, 'Inventory': []})
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)
