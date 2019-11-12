from unittest import TestCase
from A3.character import validate_move


class TestValidateMove(TestCase):
    def test_validate_move_possible(self):
        actual = validate_move([(0, 0), (0, 1), (1, 0), (1, 1)], {"Current Position": (0, 0)}, "2")
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_impossible(self):
        actual = validate_move([(0, 0), (0, 1), (1, 0), (1, 1)], {"Current Position": (0, 0)}, "1")
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_possible_type(self):
        actual = type(validate_move([(0, 0), (0, 1), (1, 0), (1, 1)], {"Current Position": (0, 0)}, "2"))
        expected = type(True)
        self.assertEqual(expected, actual)

    def test_validate_move_impossible_type(self):
        actual = type(validate_move([(0, 0), (0, 1), (1, 0), (1, 1)], {"Current Position": (0, 0)}, "1"))
        expected = type(False)
        self.assertEqual(expected, actual)
