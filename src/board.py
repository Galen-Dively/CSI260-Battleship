from coordinate import Coordinate


class Board:
    def __init__(self):
        rows, cols = (10, 10)
        arr = [['.' for _ in range(cols)] for _ in range(rows)]
        self.grid = arr
        self.ships = []

    def __str__(self):
        """to str method to print board"""
        ret_str = '   ' + '  '.join(str(i + 1) for i in range(10)) + '\n'
        for i, row in enumerate(self.grid):
            row_label = chr(ord('A') + i)
            ret_str += f'{row_label} ' + ' '.join(f' {cell}' for cell in row) + '\n'
        return ret_str

    def __len__(self):
        return len(self.ships)

    def __getitem__(self, coord: Coordinate):
        """returns item at coordinate"""
        return self.grid[coord.row][coord.col]

    def __setitem__(self, coord: Coordinate, value):
        self.grid[coord.row][coord.col] = value


# board = Board()
#
# board[Coordinate.from_string('B4')] = 'X'
# board[Coordinate.from_string('C3')] = 'O'
# board[Coordinate.from_string('C5')] = 'X'
#
# print(board)
#
# print(board[Coordinate.from_string('C5')])
