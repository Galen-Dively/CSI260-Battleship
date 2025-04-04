
from dataclasses import dataclass


@dataclass
class Coordinate:
    x: int
    y: int

    def __eq__(self, value):
        return "Hit" if self.x == value.x and self.y == value.y else "Miss"