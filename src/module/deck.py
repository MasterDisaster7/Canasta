import random
from .card import Card

class Deck:
    def __init__(self, num_decks=2):
        """Creates the draw pile with num_decks of standard 54-card decks (including Jokers)."""
        self.cards = []
        for _ in range(num_decks):
            for suit in Card.SUITS:
                if suit == 'Joker':
                    # Add Jokers: two per deck
                    self.cards.append(Card(rank='Joker', suit='Joker'))
                    self.cards.append(Card(rank='Joker', suit='Joker'))
                else:
                    for rank in Card.RANKS[:-1]:  # Exclude the Joker rank here
                        self.cards.append(Card(rank=rank, suit=suit))
        self.shuffle()

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self.cards)

    def draw(self, count=1):
        """Draws one or more cards from the top of the deck."""
        if count > len(self.cards):
            raise ValueError("Not enough cards left to draw")
        drawn = self.cards[:count]
        self.cards = self.cards[count:]
        return drawn if count > 1 else drawn[0]

    def add_cards(self, cards):
        """Adds cards back into the deck (e.g., when reshuffling discard pile)."""
        if isinstance(cards, Card):
            self.cards.append(cards)
        else:
            self.cards.extend(cards)

    def is_empty(self):
        """Returns True if the deck is empty."""
        return len(self.cards) == 0

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return f"Deck with {len(self.cards)} cards"

    def __repr__(self):
        return f"Deck({self.cards})"
