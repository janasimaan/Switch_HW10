import random

class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.score = 0

    def penalize(self):
        self.score = max(0, self.score - 10)

    def add_points(self, points):
        self.score += points

    def power_up(self):
        power_up_type = random.choice(["Points Boost", "Extra Turn", "Skip Opponent's Turn"])
        if power_up_type == "Points Boost":
            bonus_points = random.choice([10, 20, 30])
            self.add_points(bonus_points)
            print(f"{self.symbol} gets a Points Boost! +{bonus_points} points!")
        elif power_up_type == "Extra Turn":
            print(f"{self.symbol} gets an extra turn!")
        elif power_up_type == "Skip Opponent's Turn":
            print(f"{self.symbol} skips the opponent's turn!")
