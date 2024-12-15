from Matrix import Matrix
import random

class GameBoard(Matrix):
    WALL = "🧱"
    COIN = "💰"
    EMPTY = "⬜"
    TRAP = "🕳"
    POWER_UP = "⚡"
    TREASURE = "🎁"

    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.coins = 0

    def load_board(self):
        while True:
            self.matrix = []
            self.coins = 0
            self.place_walls_and_coins()
            self.matrix[0][0] = "🤠"  # Initial player positions
            self.matrix[self.rows - 1][self.cols - 1] = "👩‍🚀"
            if self.coins >= 10:
                break

    def place_walls_and_coins(self):
        elements = [self.COIN, self.EMPTY, self.WALL, self.TRAP, self.POWER_UP, self.TREASURE]
        for r in range(self.rows):
            self.matrix.append([random.choice(elements) for _ in range(self.cols)])
            self.coins += self.matrix[r].count(self.COIN)
        self._scatter_coins()

    def _scatter_coins(self):
        for r in range(1, self.rows, 2):
            for c in range(1, self.cols, random.randint(1, 3)):
                if random.choice([True, False]):
                    self.matrix[r][c] = self.COIN
                    self.coins += 1

    def update_position(self, current_row, current_col, new_row, new_col, player):
        self.matrix[current_row][current_col] = self.EMPTY
        self.matrix[new_row][new_col] = player

    def is_valid_move(self, row, col, opponent):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.matrix[row][col] not in [self.WALL, opponent]
