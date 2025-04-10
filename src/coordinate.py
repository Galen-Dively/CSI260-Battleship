
class Coordinate:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    @classmethod
    def from_string(cls, s: str):
        """returns coord obj from string input 'A3 -> (0,2)'"""
        row_letter = s[0].upper()
        col_number = int(s[1:]) - 1
        row_number = ord(row_letter) - ord('A')
        return cls(row_number, col_number)

    def __str__(self):
        """to string method, takes coord obj and prints string representation (2,3)->'C4'"""
        row_letter = chr(self.col + ord('A'))
        return f"{row_letter}{self.row + 1}"

    def __eq__(self, other):
        """checks if two coords are equal"""
        if isinstance(other, Coordinate):
            return self.row == other.row and self.col == other.col
        return False
