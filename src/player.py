from typing import override
from random import randint
from coordinate import Coordinate

class Player:
    def __init__(self, board):
        self.board = board
    
    def get_board(self):
        return self.board
    
    @property
    def has_ships(self):
        if self.board.ships > 1:
            return False
        return True
    
    def get_move(self, other_grid):
        """
        Returns the coord
        """
        # convert ascii to number in alphabet
        print(self.board)
        move = input("Enter your move 'C3': ")
        match move[0].upper():
            case "A":
                y = 1
            case "B":
                y = 2
            case "C":
                y = 3
            case "D":
                y = 4
            case "E":
                y = 5
            case "F":
                y = 6
            case "G":
                y = 7
            case "H":
                y = 8
        coord = Coordinate(int(y), int(move[1]))
        return coord
    
    def make_move(self, coord):
        pass

    def print_board(self):
        pass

    def print_full_board(self):
        # includes ships not hit
        pass

class AI(Player):
    def __init__(self, board):
        super().__init__(board)

    @override
    def get_move(self):
        x = randint(1, 10)
        y = randint(1, 10)
        return str(x) + str(y)
    

print(Player(1).get_move(AI(1).board()))