from src.player import Player, AI
from src.board import Board


class Game:
    def __init__(self):
        self.player  = Player()
        self.ai = AI()
