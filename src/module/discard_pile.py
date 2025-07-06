class DiscardPile:
    def __init__(self):
        """Creates an empty discard pile."""
        self.cards = []
        self.is_frozen = False  # Optional: whether the pile is frozen (wilds or jokers on top)

    def add_card(self, card):
        """Adds a card to the top of the discard pile and updates frozen status."""
        self.cards.append(card)
        if card.is_wild() or card.is_red_three():
            self.freeze()

    def top_card(self):
        """Returns the top card of the discard pile without removing it."""
        if not self.cards:
            return None
        return self.cards[-1]

    def take_pile(self):
        """Removes and returns all cards from the pile (used when picking up the pile)."""
        taken_cards = list(self.cards)
        self.cards.clear()
        self.unfreeze()
        return taken_cards

    def freeze(self):
        """Freezes the pile, making it harder to pick up (as per Canasta rules)."""
        self.is_frozen = True

    def unfreeze(self):
        """Unfreezes the pile."""
        self.is_frozen = False

    def is_empty(self):
        return len(self.cards) == 0

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        top = self.top_card()
        return f"DiscardPile(top={top}, frozen={self.is_frozen}, size={len(self.cards)})"

    def __repr__(self):
        return f"DiscardPile(cards={self.cards})"
