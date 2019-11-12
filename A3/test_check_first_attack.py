from unittest import TestCase
from unittest.mock import patch
from A3.sud import check_first_attack


class TestCheckFirstAttack(TestCase):
    @patch('random.randint', side_effect=[2, 1])
    def test_check_first_attack_opponent_one(self, mock_randint):
        expected = 1
        actual = check_first_attack()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 2])
    def test_check_first_attack_opponent_two(self, mock_randint):
        expected = 2
        actual = check_first_attack()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[2, 1])
    def test_check_first_attack_opponent_one_type(self, mock_randint):
        expected = type(1)
        actual = type(check_first_attack())
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 2])
    def test_check_first_attack_opponent_two_type(self, mock_randint):
        expected = type(2)
        actual = type(check_first_attack())
        self.assertEqual(expected, actual)
