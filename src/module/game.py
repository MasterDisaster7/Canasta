from .deck import Deck
from .discard_pile import DiscardPile
from .player import Player

class Game:
    def __init__(self, player_names):
        """Initializes the game with 4 players (two teams)."""
        if len(player_names) != 4:
            raise ValueError("Canasta requires exactly 4 players.")

        # Create players
        self.players = [Player(name) for name in player_names]

        # Divide players into two teams
        self.teams = {
            "Team A": [self.players[0], self.players[2]],
            "Team B": [self.players[1], self.players[3]]
        }

        # Create deck and discard pile
        self.deck = Deck()
        self.discard_pile = DiscardPile()

        # Deal initial hands
        self.deal_initial_hands()

        # Track whose turn it is
        self.current_player_index = 0

    def deal_initial_hands(self, cards_per_player=11):
        """Deals the starting hand to all players."""
        for player in self.players:
            player.draw_from_deck(self.deck, cards_per_player)

    def next_player(self):
        """Advances to the next player's turn."""
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def current_player(self):
        """Returns the player whose turn it is."""
        return self.players[self.current_player_index]

    def play_turn(self):
        player = self.current_player()
        print(f"\n--- {player.name}'s turn ---")

        # 1. Draw a card
        drawn_card = self.deck.draw()
        player.hand.add_cards(drawn_card)
        print(f"{player.name} drew {drawn_card}")

        # 2. Try to form a meld if possible
        rank_counts = {}
        for card in player.hand.get_all_cards():
            rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1

        # If there are 3+ of a rank, form a meld
        for rank, count in rank_counts.items():
            if count >= 3:
                meld_cards = [card for card in player.hand.get_all_cards() if card.rank == rank][:count]
                player.form_meld(meld_cards)
                break  # Meld only once per turn (for simplicity)

        # 3. Discard a card (the first one for now)
        if player.hand.get_all_cards():
            discard_card = player.hand.get_all_cards()[0]
            player.discard(discard_card, self.discard_pile)
            print(f"{player.name} discarded {discard_card}")

        self.next_player()

    def play_round(self):
        """Plays one full round (each player takes one turn)."""
        for _ in self.players:
            self.play_turn()

    def show_game_state(self):
        """Prints a summary of the current game state."""
        print("\n=== Game State ===")
        for player in self.players:
            print(f"{player.name}: {player.show_hand()}")
        print(self.discard_pile)

    def is_game_over(self):
        """Checks if any player has gone out (simplified end condition)."""
        return any(player.has_gone_out for player in self.players)
