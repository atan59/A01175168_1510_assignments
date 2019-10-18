from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import check_first_attack


class TestCheckFirstAttack(TestCase):
    @patch('random.randint', side_effect=[20, 1])
    def test_check_first_attack_opponent_one_greater(self, mock_randint):
        expected = 1
        actual = check_first_attack()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 20])
    def test_check_first_attack_opponent_two_greater(self, mock_randint):
        expected = 2
        actual = check_first_attack()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[20, 1])
    def test_check_first_attack_opponent_one_greater_is_int(self, mock_randint):
        actual = check_first_attack()
        self.assertEqual(type(actual), int)

    @patch('random.randint', side_effect=[1, 20])
    def test_check_first_attack_opponent_two_greater_is_int(self, mock_randint):
        actual = check_first_attack()
        self.assertEqual(type(actual), int)
