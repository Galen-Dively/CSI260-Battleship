
class Board:
    def __init__(self):
        rows, cols = (10, 10)
        arr = [['.' for _ in range(cols)] for _ in range(rows)]
        self.grid = arr
        self.ships = []
        self.letter_convert = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}
        self.num_convert = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7:'h', 8: 'i', 9: 'j'}

    def __str__(self):
        ret_str = '   1  2  3  4  5  6  7  8  9  10\n'
        counter = 0
        for row in self.grid:
            ret_str += f'{self.num_convert[counter].upper()} '
            counter += 1
            for space in row:

                ret_str += ' '+space + ' '
            ret_str +='\n'
        return ret_str

    def __getitem__(self, coords):
        """returns """
        x, y = coords
        x = x.lower()
        x = self.letter_convert[x]
        return self.grid[x][y-1]

    def __setitem__(self, coords, item):
        x, y = coords
        x = x.lower()
        x = self.letter_convert[x]
        self.grid[x][y-1] = item



board = Board()

board['B', 4] = 'X'
board['C', 3] = 'O'
board['C', 5] = 'X'

print(board)

print('print', board['B', 4])