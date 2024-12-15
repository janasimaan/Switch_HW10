from game import GoldRush

def play_game():
    print("Welcome to Gold Rush!")
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    game = GoldRush(rows, cols)
    game.board.load_board()
    game.board.print_matrix()

    skip_opponent_turn = None
    player_turn = 0

    while not game.winner:
        current_player = game.player1 if player_turn == 0 else game.player2
        next_player = game.player2 if player_turn == 0 else game.player1

        if skip_opponent_turn == current_player:
            print(f"{current_player.symbol}'s turn is skipped! ⏸️")
            skip_opponent_turn = None
            player_turn = 1 - player_turn
            continue

        direction = input(f"{current_player.symbol}, enter your move (up, down, left, right): ").strip().lower()
        game.move_player(current_player, direction)
        game.board.print_matrix()

        if game.winner:
            print(f"{current_player.symbol} wins! 🎉")
            return

        if hasattr(game, 'extra_turn_player') and game.extra_turn_player == current_player:
            print(f"{current_player.symbol} gets an extra turn! 🎉")
            game.extra_turn_player = None  # Reset extra turn flag
            continue

        player_turn = 1 - player_turn  # Switch turns

        if hasattr(game, 'skip_opponent_turn') and game.skip_opponent_turn == current_player:
            print(f"{current_player.symbol} can skip the opponent's next turn! 🛑")
            skip_opponent_turn = next_player  # Set opponent's turn to be skipped

if __name__ == "__main__":
    play_game()
