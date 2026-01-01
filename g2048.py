from grid import IntGrid
from utils import random_numbers

# 2048: 4x4 grid, adds "2" randomly at empty space, small chance of "4"

class G2048(IntGrid): 
    def __init__(self):
        # Make blank IntGrid
        rows, cols = 4, 4 
        super().__init__(rows, cols, 0)
        # Randomly place 2x 2 tiles 
        for idx in random_numbers(rows*cols, 2):
            row, col = self.index_to_coords(idx)
            self.cells[row][col] = 2 
    
    def to_string(self, cell: int) -> str:
        blank = "%5s" % "."
        num = "%5d" % cell 
        return blank if cell == 0 else num
