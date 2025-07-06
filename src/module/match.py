from .game import Game
from .team import Team
from .player import Player


class Match:
    def __init__(self, player_names):
        """Initializes the game with 4 players (two teams)."""

        if len(player_names) != 4:
            raise ValueError("Canasta requires exactly 4 players.")

        # Create players
        self.players = [Player(name) for name in player_names]

        # Divide players into two teams
        self.team1 = Team([self.players[0], self.players[2]])
        self.team2 = Team([self.players[1], self.players[3]])

        # Set the back-reference
        for player in self.team1.players:
            player.team = self.team1
        for player in self.team2.players:
            player.team = self.team2
        self.games = []
        self.winning_score = 5000
        self.winner = None

    def start_new_game(self):
        self.check_for_winner()
        self.team1.melds = []
        self.team2.melds = []  # Reset melds for new game
        new_game = Game(self.players)
        self.games.append(new_game)
        # new_game.play_round() TODO

    def check_for_winner(self):
        for team in [self.team1, self.team2]:
            if team.score >= self.winning_score:
                self.winner = team
                break  # TODO handle ties or multiple winners

    def is_finished(self):
        return self.winner is not None
