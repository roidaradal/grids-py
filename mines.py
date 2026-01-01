from grid import IntGrid, Callable
from utils import random_numbers

# Easy      9x9     10
# Medium    16x16   40
# Hard      30x16   99

class Mines(IntGrid):
    bomb = -1 

    def __init__(self, rows: int, cols: int, mines: int):
        # Make blank IntGrid 
        super().__init__(rows, cols, 0)
        # Randomly place bombs 
        for idx in random_numbers(rows*cols, mines):
            row, col = self.index_to_coords(idx)
            self.cells[row][col] = self.bomb 
        is_bomb: Callable[[int], bool] = lambda cell: cell == self.bomb 
        # Count neighbor mines 
        for row, line in enumerate(self.cells):
            for col, cell in enumerate(line):
                if cell == self.bomb: continue 
                self.cells[row][col] = self.count_neighbors((row,col), is_bomb)

    def to_string(self, cell: int) -> str:
        bomb_cell = "%3s" % "X"
        num_cell = "%3d" % cell 
        return bomb_cell if cell == self.bomb else num_cell
