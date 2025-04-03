from typing import override
from random import randint

class Player:
    def __init__(self, board):
        self.board = board
    
    def get_board(self):
        return self.board
    
    def get_move(self, other_board):
        # convert ascii to number in alphabet
        print(self.board)
        move = input("Enter your move 'C3': ")

        for col in self.board:
            for row in col:
                if self.board 

        return move
    
    @property
    def has_ships(self):
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
    

print(Player(1).get_move())

class Board:
    def __init__(self):
        rows, cols = (10, 10)
        arr = [['.'] * cols] * rows
        self.grid = arr

    def __str__(self):
        ret_str = ''

        for row in self.grid:
            for space in row:
                ret_str += ' '+space + ' '
            ret_str +='\n'
        return(ret_str)



board = Board()

print (board.grid)