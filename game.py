from game_board import GameBoard
from player import Player
from directions import Directions
import random

class GoldRush:
    PLAYER1 = "🤠"
    PLAYER2 = "👩‍🚀"

    def __init__(self, rows, cols):
        self.board = GameBoard(rows, cols)  # Initialize the board
        self.player1 = Player(self.PLAYER1)
        self.player2 = Player(self.PLAYER2)
        self.winner = None

    def start_game(self):
        self.board.load_board()  # Correct method to load the board

    def move_player(self, player, direction):
        current_row, current_col = self.find_player(player)
        self._move(current_row, current_col, player, direction)

    def find_player(self, player):
        for i, row in enumerate(self.board.matrix):
            for j, value in enumerate(row):
                if value == player.symbol:
                    return i, j
        raise ValueError(f"{player.symbol} not found on the board!")

    def _move(self, current_row, current_col, player, direction):
        try:
            delta_row, delta_col = Directions.get(direction)
        except ValueError as e:
            print(e)
            return

        new_row, new_col = current_row + delta_row, current_col + delta_col
        opponent = self.player2 if player == self.player1 else self.player1

        if self.board.is_valid_move(new_row, new_col, opponent.symbol):
            cell = self.board.matrix[new_row][new_col]
            actions = {
                GameBoard.COIN: lambda: player.add_points(10),
                GameBoard.TRAP: lambda: player.penalize(),
                GameBoard.POWER_UP: lambda: player.power_up(),
                GameBoard.TREASURE: lambda: self._treasure(player)
            }

            actions.get(cell, lambda: None)()

            print(f"{player.symbol} fell into a {cell}!")
            print(f"Scores: {self.player1.symbol} - {self.player1.score}, {self.player2.symbol} - {self.player2.score}")
            self.board.update_position(current_row, current_col, new_row, new_col, player.symbol)

        self._check_win()

    def _treasure(self, player):
        reward = random.choice([5, 10, 15, 20, 30])
        player.add_points(reward)
        print(f"{player.symbol} discovered a treasure chest! 🎁 Reward: {reward} points")

    def _check_win(self):
        if self.player1.score >= 100:
            self.winner = self.player1
            print(f"{self.player1.symbol} wins the game! 🏆")
        elif self.player2.score >= 100:
            self.winner = self.player2
            print(f"{self.player2.symbol} wins the game! 🏆")
