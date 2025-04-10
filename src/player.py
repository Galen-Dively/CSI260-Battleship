from board import Board
from coordinate import Coordinate


class Player:
    def __init__(self, name: str):
        self.name = name
        self.board = Board()
    
    def get_board(self) -> Board:
        return self.board
    
    @property
    def has_ships(self) -> bool:
        return len(self.board) > 0
    
    def get_move(self, other_grid):
        rows = ["a","b","c","d","e","f","g","h","i","j"]
        cols = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        while True:
            move = input("Please enter your move (i.e: A4): ")
            if move[0].lower() not in rows:
                print("Invalid move")
            elif int(move[1:]) not in cols:
                print("Invalid move")
            else:
                return move
    
    def make_move(self, coord: Coordinate) -> str:
        """
        Returns "hit", "miss", or "sunk" based on the result.
        """
        # Check for a hit
        hit_ship = None
        for ship in self.board.ships:
            if ship.hit_at(coord):
                hit_ship = ship
                break
        
        if hit_ship:
            if hit_ship.is_sunk:
                # Update grid to mark sunken ship
                for ship_coord in hit_ship.coordinates:
                    self.board[ship_coord] = "S"
                return "sunk"
            else:
                # Mark as hit
                self.board[coord] = "X"
                return "hit"
        else:
            # Mark as miss
            self.board[coord] = "O"
            return "miss"
    
    def print_board(self) -> None:
        """Print the board without revealing unhit ships."""
        print(f"{self.name}'s Board:")
        print(self.board)
    
    def print_full_board(self) -> None:
        """Print the board including all ships, hit or not."""
        print(f"{self.name}'s Full Board:")
        
        # Create a temporary copy of the grid
        temp_grid = [row[:] for row in self.board.grid]
        
        # Add all ships to the grid
        for ship in self.board.ships:
            for i, coord in enumerate(ship.coordinates):
                # Only overwrite if not already hit or sunk
                if temp_grid[coord.row][coord.col] not in ["X", "S"]:
                    temp_grid[coord.row][coord.col] = "#"
        
        # Print the board
        header = '   ' + '  '.join(str(i + 1) for i in range(10))
        print(header)
        
        for i, row in enumerate(temp_grid):
            row_str = f"{chr(ord('A') + i)}  " + "  ".join(row)
            print(row_str)