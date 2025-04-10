import player
import game
import board

def main():
    player1 = player.Player("test player 1")
    player2 = player.Player("test player 2")
    my_game = game.Game(player1, player2)
    my_game.play()

if __name__ == '__main__':
    main()