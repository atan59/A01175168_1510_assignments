from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import generate_syllable


class TestGenerateSyllable(TestCase):
    @patch('random.randint', side_effect=[0, 0])
    def test_generate_syllable_min_consonant_and_vowel(self, mock_randint):
        actual = generate_syllable()
        expected = 'ba'
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[10, 3])
    def test_generate_syllable_mid_consonant_and_vowel(self, mock_randint):
        actual = generate_syllable()
        expected = 'no'
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[20, 5])
    def test_generate_syllable_max_consonant_and_vowel(self, mock_randint):
        actual = generate_syllable()
        expected = 'zy'
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 1])
    def test_generate_syllable_positive_consonant_and_vowel(self, mock_randint):
        actual = generate_syllable()
        expected = 'ce'
        self.assertEqual(expected, actual)
