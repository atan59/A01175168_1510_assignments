from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import combat_round


class TestCombat_round(TestCase):
    @patch('random.randint', side_effect=[])
    def test_combat_round_opponent_one_first_and_wins(self):
        pass

    @patch('random.randint', side_effect=[])
    def test_combat_round_opponent_one_first_and_loses(self):
        pass

    @patch('random.randint', side_effect=[])
    def test_combat_round_opponent_two_first_and_wins(self):
        pass

    @patch('random.randint', side_effect=[])
    def test_combat_round_opponent_two_first_and_loses(self):
        pass
