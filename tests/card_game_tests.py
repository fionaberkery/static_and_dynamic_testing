import unittest 

from src.card import *
from src.card_game import *

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Hearts", 7)
        self.card2 = Card("Diamonds", 10)
        self.card3 = Card("Spades", 1)
        self.card4 = Card("Clubs", 4)
        self.cards1 = [self.card1, self.card2]
        self.cards2 = [self.card1, self.card3, self.card4]

    def test_suit_is_not_ace(self):
        self.assertEqual(False, CardGame.check_for_ace(self, self.card1))

    def test_suit_is_ace(self):
        self.assertEqual(True,CardGame.check_for_ace(self, self.card3))

    def test_can_return_highest_card(self):
        self.assertEqual(self.card2, CardGame.highest_card(self, self.card1, self.card2))

    def test_can_get_total_of_two_cards(self):
        result = CardGame.cards_total(self, self.cards1)
        self.assertEqual("You have a total of 17", result)

    def test_can_get_total_of_three_cards(self):
        result = CardGame.cards_total(self, self.cards2)
        self.assertEqual("You have a total of 12", result)   




            
