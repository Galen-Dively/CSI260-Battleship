

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, value):
        return "Hit" if self.x == value.x and self.y == value.y else "Miss"