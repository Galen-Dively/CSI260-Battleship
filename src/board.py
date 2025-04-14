from coordinate import Coordinate
from ship import Ship
import random


class Board:
    def __init__(self):
        rows, cols = (10, 10)
        arr = [['.' for _ in range(cols)] for _ in range(rows)]
        self.grid = arr
        self.ships = []
        self.generate_ships()

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


    def generate_ships(self):
        gen_ships = [5,4,3,3,2]

        for length in gen_ships:

            placed = False
            while not placed:

                # 0 is vertical, 1 is horizontal
                orientation = random.choice(['horizontal', 'vertical'])

                if orientation == 'vertical':  # vertical
                    origin_row = random.randint(0, 10 - length)
                    origin_col = random.randint(0, 9)
                else:  # horizontal
                    origin_row = random.randint(0, 9)
                    origin_col = random.randint(0, 10 - length)

                new_ship = Ship(length, orientation, (origin_row, origin_col) )
                new_coords = new_ship.get_coordinates()

                overlap = False
                for ship in self.ships:
                    if set(new_coords) & set(ship.get_coordinates()):
                        overlap = True
                        break

                if not overlap:
                    print(f'placed ship {length}')
                    placed = True
                    self.ships.append(new_ship)

# board = Board()
#
# board[Coordinate.from_string('B4')] = 'X'
# board[Coordinate.from_string('C3')] = 'O'
# board[Coordinate.from_string('C5')] = 'X'
#
# print(board)
#
# print(board[Coordinate.from_string('C5')])
