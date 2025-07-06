from .hand import Hand
from .meld import Meld

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

    def can_pick_up_discard(self, discard_pile):
        """Checks if the player can pick up the discard pile."""
        top_card = discard_pile.top_card()
        if not top_card:
            return False

        # Find cards in hand matching the top card's rank
        matching_cards = [card for card in self.hand.get_all_cards() if card.rank == top_card.rank]

        if discard_pile.is_frozen:
            return len(matching_cards) >= 2 # Rule: When frozen, must have 2 or more matching cards in hand
        else:
            # Rule: When not frozen, must have at least 1 matching card and 1 wild, or two matching cards in hand
            wild_cards = [card for card in self.hand.get_all_cards() if card.is_wild()]
            return (len(matching_cards) >= 2) or (len(matching_cards) >= 1 and len(wild_cards) >= 1)

    def pick_up_discard_pile(self, discard_pile):
        """Adds the entire discard pile to the hand."""
        pile_cards = discard_pile.take_pile()
        self.hand.add_cards(pile_cards)
        # TODO force meld after picking up discard

    def discard(self, card, discard_pile):
        """Discard a card from hand to the discard pile."""
        discarded = self.hand.discard_card(card)
        discard_pile.add_card(discarded)
        return discarded

    def form_meld(self, cards):
        """Creates a meld from cards in the hand (no rules checked yet)."""
        for card in cards:
            self.hand.remove_card(card)
        new_meld = Meld(cards)
        self.melds.append(new_meld)
        print(f"{self.name} formed a meld: {new_meld}")

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
