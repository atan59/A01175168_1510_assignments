from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import generate_consonant


class TestGenerateConsonant(TestCase):
    @patch('random.randint', return_value=0)
    def test_generate_consonant_min(self, mock_randint):
        actual = generate_consonant()
        expected = 'b'
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=10)
    def test_generate_consonant_mid(self, mock_randint):
        actual = generate_consonant()
        expected = 'n'
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=20)
    def test_generate_consonant_max(self, mock_randint):
        actual = generate_consonant()
        expected = 'z'
        self.assertEqual(expected, actual)
