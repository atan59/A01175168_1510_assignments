from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import select_class


class TestSelectClass(TestCase):
    @patch('builtins.input', return_value=1)
    def test_select_class_min(self, mock_input):
        expected = 'barbarian'
        actual = select_class()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value=12)
    def test_select_class_max(self, mock_input):
        expected = 'wizard'
        actual = select_class()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value=1)
    def test_select_class_is_string_min(self, mock_input):
        actual = select_class()
        self.assertEqual(type(actual), str)

    @patch('builtins.input', return_value=12)
    def test_select_class_is_string_max(self, mock_input):
        actual = select_class()
        self.assertEqual(type(actual), str)
