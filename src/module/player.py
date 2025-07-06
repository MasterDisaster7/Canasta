from .hand import Hand

class Player:
    def __init__(self, name):
        """Creates a player with a name and an empty hand."""
        self.name = name
        self.hand = Hand()
        self.melds = []  # List of lists of Cards (each meld is a list of cards)
        self.has_gone_out = False

    def draw_from_deck(self, deck, count=1):
        """Draw cards from the deck and add them to the hand."""
        drawn = deck.draw(count)
        self.hand.add_cards(drawn)

    def discard(self, card, discard_pile):
        """Discard a card from hand to the discard pile."""
        discarded = self.hand.discard_card(card)
        discard_pile.add_card(discarded)
        return discarded

    def form_meld(self, cards):
        """Forms a meld from specified cards in the hand."""
        # Remove the cards from the hand
        for card in cards:
            self.hand.remove_card(card)
        self.melds.append(cards)

    def show_hand(self):
        """Returns the cards in the hand as a string."""
        return str(self.hand)

    def show_melds(self):
        """Returns a string representation of the player's melds."""
        return [', '.join(str(card) for card in meld) for meld in self.melds]

    def go_out(self):
        """Marks the player as having gone out."""
        self.has_gone_out = True

    def __str__(self):
        return f"Player {self.name}"

    def __repr__(self):
        return f"Player(name='{self.name}')"
