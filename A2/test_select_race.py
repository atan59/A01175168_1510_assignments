from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import select_race


class TestSelectRace(TestCase):
    @patch('builtins.input', return_value=1)
    def test_select_race_min(self, mock_input):
        expected = 'dragonborn'
        actual = select_race()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value=9)
    def test_select_race_max(self, mock_input):
        expected = 'tiefling'
        actual = select_race()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value=1)
    def test_select_race_is_string_min(self, mock_input):
        actual = select_race()
        self.assertIs(type(actual), str)

    @patch('builtins.input', return_value=9)
    def test_select_race_is_string_max(self, mock_input):
        actual = select_race()
        self.assertIs(type(actual), str)
