from module.match import Match

match = Match(["Ruud", "Mariska", "Menno", "Lobke"])

match.start_new_game()  # Start a new game
game = match.games[0]  # Assuming the first game is the one we want to play

# Play 3 rounds (just to test)
for round_num in range(3):
    print(f"\n=== Round {round_num + 1} ===")
    game.play_round()
    game.show_game_state()
