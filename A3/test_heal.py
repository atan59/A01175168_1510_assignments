from unittest import TestCase
from A3.sud import heal


class TestHeal(TestCase):
    def test_heal_plus_two(self):
        character = {'Name': 'Test', 'HP': [1, 10]}
        expected = 3
        heal(character)
        actual = character['HP'][0]
        self.assertEqual(expected, actual)

    def test_heal_plus_two_to_full(self):
        character = {'Name': 'Test', 'HP': [9, 10]}
        expected = 10
        heal(character)
        actual = character['HP'][0]
        self.assertEqual(expected, actual)

    def test_heal_full(self):
        character = {'Name': 'Test', 'HP': [10, 10]}
        expected = 10
        heal(character)
        actual = character['HP'][0]
        self.assertEqual(expected, actual)

    def test_heal_plus_two_type(self):
        character = {'Name': 'Test', 'HP': [1, 10]}
        expected = type(3)
        heal(character)
        actual = type(character['HP'][0])
        self.assertEqual(expected, actual)

    def test_heal_plus_two_to_full_type(self):
        character = {'Name': 'Test', 'HP': [9, 10]}
        expected = type(10)
        heal(character)
        actual = type(character['HP'][0])
        self.assertEqual(expected, actual)

    def test_heal_full_type(self):
        character = {'Name': 'Test', 'HP': [10, 10]}
        expected = type(10)
        heal(character)
        actual = type(character['HP'][0])
        self.assertEqual(expected, actual)
