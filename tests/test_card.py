import unittest
from src.module.card import Card

class TestCard(unittest.TestCase):

    def test_valid_card_creation(self):
        card = Card('Ace', 'Hearts')
        self.assertEqual(card.rank, 'Ace')
        self.assertEqual(card.suit, 'Hearts')

    def test_invalid_suit_raises(self):
        with self.assertRaises(ValueError):
            Card('Ace', 'Flowers')

    def test_joker_validation(self):
        card = Card('Joker', 'Joker')
        self.assertEqual(str(card), 'Joker')

        with self.assertRaises(ValueError):
            Card('Ace', 'Joker')

    def test_equality_and_hash(self):
        card1 = Card('5', 'Diamonds')
        card2 = Card('5', 'Diamonds')
        self.assertEqual(card1, card2)
        self.assertEqual(hash(card1), hash(card2))

if __name__ == '__main__':
    unittest.main()
