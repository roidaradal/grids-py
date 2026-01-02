import random
from grid import IntGrid
from utils import Color

class Greed(IntGrid):
    cursor = -1 
    cellColor = {
        1: Color.green,
        2: Color.cyan,
        3: Color.yellow,
        4: Color.magenta,
        5: Color.blue,
        6: Color.magenta,
        7: Color.yellow,
        8: Color.cyan,
        9: Color.green,
    }

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
                return "%6s" % Color.white(".")
            case self.cursor:
                return "%6s" % Color.redOnWhite("@")
            case _:
                return "%6s" % self.cellColor[cell](str(cell))
