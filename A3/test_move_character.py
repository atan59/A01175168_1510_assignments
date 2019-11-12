from unittest import TestCase
from A3.character import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_north(self):
        character = {"Current Position": (1, 0)}
        move_character(character, "1")
        actual = character["Current Position"]
        expected = (0, 0)
        self.assertEqual(expected, actual)

    def test_move_character_east(self):
        character = {"Current Position": (0, 0)}
        move_character(character, "2")
        actual = character["Current Position"]
        expected = (0, 1)
        self.assertEqual(expected, actual)

    def test_move_character_south(self):
        character = {"Current Position": (0, 0)}
        move_character(character, "3")
        actual = character["Current Position"]
        expected = (1, 0)
        self.assertEqual(expected, actual)

    def test_move_character_west(self):
        character = {"Current Position": (0, 1)}
        move_character(character, "4")
        actual = character["Current Position"]
        expected = (0, 0)
        self.assertEqual(expected, actual)
