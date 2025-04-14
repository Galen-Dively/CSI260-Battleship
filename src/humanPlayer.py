from player import Player
from coordinate import Coordinate


class HumanPlayer(Player):
    """human player subclass of player that checks for user input"""
    def get_move(self, other_grid) -> Coordinate:
        rows = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        cols = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        while True:
            move = input(f"{self.name}, please enter your move (i.e: A4): ")
            if len(move) < 2:
                print("Invalid move format")
                continue

            coord = Coordinate.from_string(move)

            if other_grid[coord] != '.':
                print("Must hit empty space")
            elif move[0].lower() not in rows:
                print("Invalid row")
            elif not move[1:].isdigit() or int(move[1:]) not in cols:
                print("Invalid column")
            else:
                return move

        while True:
            move = input(f"{self.name}, please enter your move (e.g., A4): ").strip().lower()
            if len(move) < 2:
                print("Invalid format.")
                continue
            row_char = move[0]
            col_str = move[1:]

            if row_char not in rows or col_str not in cols:
                print("Invalid row or column.")
                continue

            row = rows.index(row_char)
            col = int(col_str) - 1
            return Coordinate(row, col)
