from unittest import TestCase
from A3.sud import make_board


class TestMakeBoard(TestCase):
    def test_make_board_correct_tuples(self):
        actual = make_board()
        expected = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                    (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                    (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                    (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                    (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        self.assertEqual(expected, actual)

    def test_make_board_type(self):
        actual = type(make_board())
        expected = type([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                         (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                         (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                         (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                         (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)])
        self.assertEqual(expected, actual)
