from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import generate_vowel


class TestGenerateVowel(TestCase):
    @patch('random.randint', return_value=0)
    def test_generate_vowel_min(self, mock_randint):
        actual = generate_vowel()
        expected = 'a'
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_generate_vowel_mid(self, mock_randint):
        actual = generate_vowel()
        expected = 'o'
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=5)
    def test_generate_vowel_max(self, mock_randint):
        actual = generate_vowel()
        expected = 'y'
        self.assertEqual(expected, actual)
