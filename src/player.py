from typing import override
from random import randint
from coordinate import Coordinate

class Player:
    def __init__(self, board):
        self.board = board
    
    def get_board(self):
        return self.board
    
    def get_move(self):
        print(self.board)
        move = input("Enter your move (x, y): ")
        move = move.split(",")
        coord = Coordinate(int(move[0]), int(move[1]))
        return coord
    
    @property
    def has_ships(self):
        pass

class AI(Player):
    def __init__(self, board):
        super().__init__(board)

    @override
    def get_move(self):
        x = randint(1, 10)
        y = randint(1, 10)
        return str(x) + str(y)
    



print(Player(1).get_move())