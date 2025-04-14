from board import Board
from coordinate import Coordinate
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name: str):
        self.name = name
        self.board = Board()
        self.lives = 5
    
    def get_board(self) -> Board:
        return self.board
    
    @property
    def has_ships(self) -> bool:
        return len(self.board.ships) > 0
    
    def get_move(self):
        pass
    
    def make_move(self, coord: Coordinate, opponent_board) -> str:
        """Returns "hit", "miss", or "sunk" based on the result."""
        if not opponent_board:
            raise ValueError("No opponent board set. Call get_move() first.")
            
        hit_ship = None
        for ship in opponent_board.ships:
            # Check if the coordinate is in ship's coordinates (which are tuples)
            for ship_coord in ship.coordinates:
                if isinstance(ship_coord, tuple) and (coord.row, coord.col) == ship_coord:
                    hit_ship = ship
                    break
            if hit_ship:
                break
        
        if hit_ship:
            opponent_board[coord] = "X"
            
            all_hit = True
            for ship_coord in hit_ship.coordinates:
                row, col = ship_coord if isinstance(ship_coord, tuple) else (ship_coord.row, ship_coord.col)
                ship_coordinate = Coordinate(row, col)
                if opponent_board[ship_coordinate] != "X":
                    all_hit = False
                    break
                    
            if all_hit:
                for ship_coord in hit_ship.coordinates:
                    row, col = ship_coord if isinstance(ship_coord, tuple) else (ship_coord.row, ship_coord.col)
                    ship_coordinate = Coordinate(row, col)
                    opponent_board[ship_coordinate] = "S"
                return "sunk"
            else:
                return "hit"
        else:
            opponent_board[coord] = "O"
            return "miss"
    
    def print_board(self) -> None:
        print(f"{self.name}'s Board:")
        print(self.board)
    
    def print_full_board(self) -> None:
        print(f"{self.name}'s Full Board:")
        
        temp_grid = [row[:] for row in self.board.grid]
        
        for ship in self.board.ships:
            for coord in ship.coordinates:
                # Handle tuple coordinates from ship class
                row, col = coord if isinstance(coord, tuple) else (coord.row, coord.col)
                if temp_grid[row][col] not in ["X", "S"]:
                    temp_grid[row][col] = "#"
        
        header = '   ' + '  '.join(str(i + 1) for i in range(10))
        print(header)
        
        for i, row in enumerate(temp_grid):
            row_str = f"{chr(ord('A') + i)}  " + "  ".join(row)
            print(row_str)