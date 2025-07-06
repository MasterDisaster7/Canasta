from .card import Card

class Hand:
    def __init__(self):
        """Creates an empty hand."""
        self.cards = []

    def add_cards(self, new_cards):
        """Adds one or more cards to the hand."""
        if isinstance(new_cards, Card):
            self.cards.append(new_cards)
        else:
            self.cards.extend(new_cards)

    def remove_card(self, card):
        """Removes a specific card from the hand."""
        if card in self.cards:
            self.cards.remove(card)
            return card
        else:
            raise ValueError(f"Card {card} not found in hand")

    def discard_card(self, card):
        """Alias for remove_card; could later trigger discard pile logic."""
        return self.remove_card(card)

    def has_card(self, rank, suit=None):
        """Checks if the hand contains a card by rank (and optionally suit)."""
        return any(c.rank == rank and (suit is None or c.suit == suit) for c in self.cards)

    def get_all_cards(self):
        """Returns a copy of all cards in the hand."""
        return list(self.cards)

    def sort_hand(self):
        """Sorts the hand using the Card class's comparison operators."""
        self.cards.sort()

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

    def __repr__(self):
        return f"Hand({self.cards})"
