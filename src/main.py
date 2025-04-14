import humanPlayer
import AI
import game


def main():
    player1 = humanPlayer.HumanPlayer("Test Player 1")
    player2 = AI.AIPlayer("Bot Player")
    my_game = game.Game(player1, player2)
    my_game.play()

if __name__ == '__main__':
    main()