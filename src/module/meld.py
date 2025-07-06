class Meld:
    def __init__(self, cards):
        if not cards:
            raise ValueError("Meld cannot be empty.")
        self.cards = cards
        self.rank = self._determine_rank()

    def _determine_rank(self):
        # Get the rank of the first non-wild card, or 'Wild' if all wilds
        for card in self.cards:
            if not card.is_wild():
                return card.rank
        return 'Wild'

    def add_card(self, card):
        """Adds a card to the meld (without validation for now)."""
        self.cards.append(card)

    def __str__(self):
        return f"Meld({self.rank}): " + ', '.join(str(c) for c in self.cards)

    def __repr__(self):
        return f"Meld(rank='{self.rank}', cards={self.cards})"
