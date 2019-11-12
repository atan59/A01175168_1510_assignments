from unittest import TestCase
from unittest.mock import patch
from A3.monsters import check_flee_chance


class TestCheckFleeChance(TestCase):
    @patch('random.randint', return_value=1)
    def test_check_flee_chance_true(self, mock_randint):
        expected = True
        actual = check_flee_chance()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=0)
    def test_check_flee_chance_false(self, mock_randint):
        expected = False
        actual = check_flee_chance()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_check_flee_chance_true_type(self, mock_randint):
        expected = type(True)
        actual = type(check_flee_chance())
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=0)
    def test_check_flee_chance_false_type(self, mock_randint):
        expected = type(False)
        actual = type(check_flee_chance())
        self.assertEqual(expected, actual)
