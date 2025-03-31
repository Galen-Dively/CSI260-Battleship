from typing import override



class Player:
    def __init__(self, board):
        self.board = board
    
    def get_board(self):
        return self.board
    
    def get_move(self):
        print(self.board)
        move = input("Enter your move: ")
        return move
    
    @property
    def has_ships(self):
        pass

class AI(Player):
    def __init__(self, board):
        super().__init__(board)

    @override
    def get_move(self):
        pass
    


