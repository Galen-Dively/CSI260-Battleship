import random
from src.player import Player
from src.coordinate import Coordinate


class AIPlayer(Player):
    """ai subclass of player, uses basic algorithm to search for random places and then investigate locally around hits"""
    def __init__(self, name: str):
        super().__init__(name)
        self.target_stack = []
        self.tried = set()

    def get_move(self, other_board) -> str:
        """get move to play from AI"""
        # update target stack
        self._update_targets_from_board(other_board)

        # Choose from target stack
        while self.target_stack:
            coord = self.target_stack.pop()
            if (coord.row, coord.col) not in self.tried:
                self.tried.add((coord.row, coord.col))
                return self._coord_to_str(coord)

        # choose random untried coordinate
        while True:
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            if (row, col) not in self.tried:
                self.tried.add((row, col))
                return self._coord_to_str(Coordinate(row, col))

    def _update_targets_from_board(self, board):
        """look for new hits and update the stack"""

        for r in range(10):
            for c in range(10):
                if board.grid[r][c] == "X":
                    self._add_adjacent_targets(Coordinate(r, c))

    def _add_adjacent_targets(self, coord):
        """adds adjacent targets to the stack"""
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            new_r, new_c = coord.row + dr, coord.col + dc
            new_coord = Coordinate(new_r, new_c)

            if self._is_valid(new_coord) and (new_r, new_c) not in self.tried:
                self.target_stack.append(new_coord)

    def _is_valid(self, coord) -> bool:
        return 0 <= coord.row < 10 and 0 <= coord.col < 10

    def _coord_to_str(self, coord) -> str:
        return f"{chr(ord('A') + coord.row)}{coord.col + 1}"
