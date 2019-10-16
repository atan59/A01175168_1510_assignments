from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import generate_name


class TestGenerate_name(TestCase):
    @patch('random.randint', return_value=1)
    def test_generate_vowel_zero(self, mock_randint):
        actual = generate_name(0)
        expected = ''
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[0, 1])
    def test_generate_vowel_one(self, mock_randint):
        actual = generate_name(1)
        expected = 'Be'
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[0, 1, 2, 3])
    def test_generate_vowel_positive(self, mock_randint):
        actual = generate_name(2)
        expected = 'Bedo'
        self.assertEqual(expected, actual)
