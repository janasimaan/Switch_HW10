class Directions:
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    @staticmethod
    def get(direction):
        try:
            return getattr(Directions, direction.upper())
        except AttributeError:
            raise ValueError(f"Invalid direction: {direction}")