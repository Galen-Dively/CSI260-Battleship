from board import Board
from coordinate import Coordinate


class Player:
    def __init__(self, name: str):
        self.name = name
        self.board = Board()
        self.opponent_board = None
    
    def get_board(self) -> Board:
        return self.board
    
    @property
    def has_ships(self) -> bool:
        return len(self.board) > 0
    
    def get_move(self, opponent_board):
        self.opponent_board = opponent_board
        rows = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        cols = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        while True:
            move = input(f"{self.name}, please enter your move (i.e: A4): ")
            if len(move) < 2:
                print("Invalid move format")
                continue
                
            if move[0].lower() not in rows:
                print("Invalid row")
            elif not move[1:].isdigit() or int(move[1:]) not in cols:
                print("Invalid column")
            else:
                return move
    
    def make_move(self, coord: Coordinate) -> str:
        """Returns "hit", "miss", or "sunk" based on the result."""
        if not self.opponent_board:
            raise ValueError("No opponent board set. Call get_move() first.")
            
        hit_ship = None
        for ship in self.opponent_board.ships:
            # Check if the coordinate is in ship's coordinates (which are tuples)
            for ship_coord in ship.coordinates:
                if isinstance(ship_coord, tuple) and (coord.row, coord.col) == ship_coord:
                    hit_ship = ship
                    break
            if hit_ship:
                break
        
        if hit_ship:
            self.opponent_board[coord] = "X"
            
            all_hit = True
            for ship_coord in hit_ship.coordinates:
                row, col = ship_coord if isinstance(ship_coord, tuple) else (ship_coord.row, ship_coord.col)
                ship_coordinate = Coordinate(row, col)
                if self.opponent_board[ship_coordinate] != "X":
                    all_hit = False
                    break
                    
            if all_hit:
                for ship_coord in hit_ship.coordinates:
                    row, col = ship_coord if isinstance(ship_coord, tuple) else (ship_coord.row, ship_coord.col)
                    ship_coordinate = Coordinate(row, col)
                    self.opponent_board[ship_coordinate] = "S"
                return "sunk"
            else:
                return "hit"
        else:
            self.opponent_board[coord] = "O"
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