
class Board:
    def __init__(self):
        rows, cols = (10, 10)
        arr = [['.'] * cols] * rows
        self.grid = arr

    def __str__(self):
        ret_str = ''

        for row in self.grid:
            for space in row:
                ret_str += ' '+space + ' '
            ret_str +='\n'
        return(ret_str)



board = Board()

print (board)