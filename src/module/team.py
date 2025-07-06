class Team:
    def __init__(self, players):
        if len(players) != 2:
            raise ValueError("A team must have exactly 2 players.")
        self.players = players
        self.melds = []  # A list of melds
        self.score = 0

    def add_meld(self, meld):
        """Add a new meld to the team's melds."""
        self.melds.append(meld)

    def has_canasta(self):
        """Check if the team has at least one complete canasta."""
        # Example: canasta = meld with 7+ cards of the same rank
        for meld in self.melds:
            if len(meld) >= 7:
                return True
        return False

    def __str__(self):
        return f"Team({', '.join(player.name for player in self.players)})"
