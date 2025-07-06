class Card:
    SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades', 'Joker']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace', 'Joker']

    def __init__(self, rank, suit):
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        if suit == 'Joker':
            if rank != 'Joker':
                raise ValueError("Joker suit must have Joker rank")
        elif rank not in self.RANKS[:-1]:
            raise ValueError(f"Invalid rank: {rank}")
        
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "Joker" if self.suit == 'Joker' else f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"Card(rank='{self.rank}', suit='{self.suit}')"

    def __eq__(self, other):
        return isinstance(other, Card) and self.rank == other.rank and self.suit == other.suit

    def __hash__(self):
        return hash((self.rank, self.suit))

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        suit_order = self.SUITS
        rank_order = self.RANKS
        if self.suit != other.suit:
            return suit_order.index(self.suit) < suit_order.index(other.suit)
        return rank_order.index(self.rank) < rank_order.index(other.rank)

    def is_wild(self):
        """Returns True if the card is a Joker or a 2 (wild cards in Canasta)."""
        return self.suit == 'Joker' or self.rank == '2'

    def is_red_three(self):
        """Returns True if the card is a red 3 (Diamonds or Hearts)."""
        return self.rank == '3' and self.suit in ['Hearts', 'Diamonds']

    def is_black_three(self):
        """Returns True if the card is a black 3 (Spades or Clubs)."""
        return self.rank == '3' and self.suit in ['Spades', 'Clubs']