import random
from grid import IntGrid

class Greed(IntGrid):
    cursor = -1 

    def __init__(self):
        # Make blank IntGrid 
        rows, cols = 22, 79
        super().__init__(rows, cols, 0)
        # Randomize grid digits 
        per_digit = 193 
        digits: list[int] = [self.cursor]
        for i in range(1, 10):
            digits.extend([i]* per_digit)
        random.shuffle(digits)
        for idx, digit in enumerate(digits):
            row, col = self.index_to_coords(idx)
            self.cells[row][col] = digit 

    def to_string(self, cell: int) -> str:
        match cell:
            case 0:
                return "%2s" % "."
            case self.cursor:
                return "%2s" % "@"
            case _:
                return "%2d" % cell

