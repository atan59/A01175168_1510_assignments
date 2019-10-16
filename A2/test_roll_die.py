from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import roll_die


class TestRollDie(TestCase):
    @patch('random.randint', return_value=1)
    def test_roll_die_negative_rolls(self, mock_randint):
        actual = roll_die(-1, 6)
        expected = 0
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_roll_die_negative_sides(self, mock_randint):
        actual = roll_die(3, -1)
        expected = 0
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_roll_die_zero_rolls(self, mock_randint):
        actual = roll_die(0, 6)
        expected = 0
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_roll_die_zero_sides(self, mock_randint):
        actual = roll_die(3, 0)
        expected = 0
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_roll_die_one_roll(self, mock_randint):
        actual = roll_die(1, 6)
        expected = 1
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_roll_die_one_side(self, mock_randint):
        actual = roll_die(3, 1)
        expected = 3
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_roll_die_one_roll_one_side(self, mock_randint):
        actual = roll_die(1, 1)
        expected = 1
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_roll_die_positive_rolls_positive_sides(self, mock_randint):
        actual = roll_die(3, 6)
        expected = 3
        self.assertEqual(expected, actual)
