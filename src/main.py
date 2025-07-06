from module.game import Game

game = Game(["Ruud", "Mariska", "Menno", "Lobke"])

# Play 3 rounds (just to test)
for round_num in range(3):
    print(f"\n=== Round {round_num + 1} ===")
    game.play_round()
    game.show_game_state()
