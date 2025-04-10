from src.player import Player
from src.board import Board
from src.coordinate import Coordinate



class Game:
    def __init__(self, player, ai):
        self.player  = player
        self.ai = ai
        self.players = [self.player, self.ai]
        self._game_over = False
        self.current_player = self.player
        self.opponent = self.ai

    def _switch_turns(self):
        self.current_player, self.opponent = self.opponent, self.current_player

    def play(self):
        """
        Turns and game over
        :return:
        """
        print("------- BATTLESHIP -> STARTING GAME -------")

        #How to set up the boards?

        #Start Playing
        while not self._game_over:
            self.round_info()
            attack_coord = self.current_player.get_move(self.opponent.board)
            result = self.current_player.make_move(Coordinate.from_string(attack_coord))

            if result == "miss":
                print(f"You missed!")
            elif result == "hit":
                print(f"You got a hit!")
            elif result == "sunk":
                print(f"You sunk my battleship!")

            print("-----------------------------------------")

            #Game over?
            if self.opponent.has_ships == True:
                self.game_over = True
                print (f"{self.current_player.name} HAS SUNK ALL SHIPS!")
                print(f"{self.current_player.name} WINS!")
                self.opponent.print_full_board()
                break

            #switch turns
            self._switch_turns()

    def round_info(self):
        print(f"{self.current_player.name}'s turn!")

        self.opponent.print_board()





