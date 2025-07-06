import unittest
from src.module.card import Card
from src.module.game import Game

class TestCanastaGameState(unittest.TestCase):
    def setUp(self):
        """Set up the game state for testing."""

        # Setup game with the player and discard pile
        self.game = Game(player_names=['Player1', 'Player2', 'Player3', 'Player4'])
        self.player = self.game.current_player()  # Get the first player
        self.discard_pile = self.game.discard_pile

        # Utility function to set up the discard pile with a specific list of cards
        def set_discard_pile(cards):
            # Remove all cards from the discard pile
            self.discard_pile.cards.clear()
            # Add the specified cards
            for card in cards:
                self.discard_pile.add_card(card)

        self.set_discard_pile = set_discard_pile

        # Utility function to set the player's hand to a specific list of cards
        def set_player_hand(cards):
            # Remove all cards from the player's hand
            while self.player.hand.get_all_cards():
                remove_card = self.player.hand.get_all_cards()[0]
                self.player.hand.remove_card(remove_card)
            # Add the specified cards
            self.player.hand.add_cards(cards)

        self.set_player_hand = set_player_hand

    def test_player_can_grab_discard_pile_with_doubles(self):
        # Add some cards to the discard pile for initial setup
        self.set_discard_pile([
            Card('4', 'Hearts'),
            Card('5', 'Hearts'),
            Card('6', 'Hearts'),
            Card('7', 'Hearts')   # This will be the top card
        ])

        # Set up the player's hand for this test
        self.set_player_hand([Card('4', 'Hearts'), Card('7', 'Clubs'), Card('7', 'Clubs')])

        # Check if player can legally pick up the discard pile
        can_grab = self.player.can_pick_up_discard(self.discard_pile)
        self.assertTrue(can_grab, "Player should be allowed to grab the discard pile")

        # Simulate player grabbing the discard pile
        self.player.pick_up_discard_pile(self.discard_pile)

        # Verify the discard pile is now empty
        self.assertEqual(len(self.game.discard_pile.cards), 0, "Discard pile should be empty after grabbing")

        # Verify the player’s hand includes old hand + discard pile cards
        expected_hand = [
            Card('4', 'Hearts'),
            Card('7', 'Clubs'),
            Card('7', 'Clubs'),
            Card('4', 'Hearts'),
            Card('5', 'Hearts'),
            Card('6', 'Hearts'),
            Card('7', 'Hearts'),
        ]
        self.assertCountEqual(self.player.hand.get_all_cards(), expected_hand, "Player's hand should include all discard pile cards")
    
    def test_player_can_grab_discard_pile_with_wildcard(self):
        # Add some cards to the discard pile for initial setup
        self.set_discard_pile([
            Card('4', 'Hearts'),
            Card('5', 'Hearts'),
            Card('6', 'Hearts'),
            Card('7', 'Hearts')   # This will be the top card
        ])

        # Set up the player's hand for this test
        self.set_player_hand([Card('4', 'Hearts'), Card('7', 'Clubs'), Card('2', 'Clubs')])

        # Check if player can legally pick up the discard pile
        can_grab = self.player.can_pick_up_discard(self.discard_pile)
        self.assertTrue(can_grab, "Player should be allowed to grab the discard pile")

    def test_player_can_grab_frozen_discard_pile_with_doubles(self):
        # Add some cards to the discard pile for initial setup
        self.set_discard_pile([
            Card('4', 'Hearts'),
            Card('5', 'Hearts'),
            Card('6', 'Hearts'),
            Card('2', 'Hearts'),  # This card will be used to freeze the discard pile
            Card('7', 'Hearts')   # This will be the top card
        ])

        # Set up the player's hand for this test
        self.set_player_hand([Card('4', 'Hearts'), Card('7', 'Clubs'), Card('7', 'Clubs')])

        # Check if player can legally pick up the discard pile
        can_grab = self.player.can_pick_up_discard(self.discard_pile)
        self.assertTrue(can_grab, "Player should be allowed to grab the discard pile")

        # Simulate player grabbing the discard pile
        self.player.pick_up_discard_pile(self.discard_pile)

        # Verify the discard pile is now empty
        self.assertEqual(len(self.game.discard_pile.cards), 0, "Discard pile should be empty after grabbing")

        # Verify the player’s hand includes old hand + discard pile cards
        expected_hand = [
            Card('4', 'Hearts'),
            Card('7', 'Clubs'),
            Card('7', 'Clubs'),
            Card('4', 'Hearts'),
            Card('5', 'Hearts'),
            Card('6', 'Hearts'),
            Card('2', 'Hearts'),
            Card('7', 'Hearts'),
        ]
        self.assertCountEqual(self.player.hand.get_all_cards(), expected_hand, "Player's hand should include all discard pile cards")
    
    def test_player_cant_grab_frozen_discard_pile_with_wildcard(self):
        # Add some cards to the discard pile for initial setup
        self.set_discard_pile([
            Card('4', 'Hearts'),
            Card('5', 'Hearts'),
            Card('6', 'Hearts'),
            Card('2', 'Hearts'),  # This card will be used to freeze the discard pile
            Card('7', 'Hearts')   # This will be the top card
        ])

        # Set up the player's hand for this test
        self.set_player_hand([Card('4', 'Hearts'), Card('7', 'Clubs'), Card('2', 'Clubs')])

        # Check if player can legally pick up the discard pile
        can_grab = self.player.can_pick_up_discard(self.discard_pile)
        self.assertFalse(can_grab, "Player should not be allowed to grab the discard pile")

if __name__ == '__main__':
    unittest.main()
