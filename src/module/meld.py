class Meld:
    def __init__(self, cards):
        if not cards:
            raise ValueError("Meld cannot be empty.")
        self.cards = cards
        self.rank = self._determine_rank()
        if not self._is_valid_meld():
            raise ValueError("Invalid meld: majority of cards are wild cards.")

    def _determine_rank(self):
        # Get the rank of the first non-wild card
        for card in self.cards:
            if not card.is_wild():
                return card.rank
        return None  # All cards are wild, no rank found
   
    def _is_valid_meld(self):
        wild_count = sum(1 for card in self.cards if card.is_wild())
        total = len(self.cards)
        return wild_count <= total // 2  # No majority wilds

    def add_card(self, card):
        """Adds a card to the meld (without validation for now)."""
        self.cards.append(card)

    def __str__(self):
        return f"Meld({self.rank}): " + ", ".join(str(c) for c in self.cards)

    def __repr__(self):
        return f"Meld(rank='{self.rank}', cards={self.cards})"
