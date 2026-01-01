from grid import BoolGrid, Callable
from utils import random_numbers

class Conway(BoolGrid):
    @classmethod 
    def random(cls, rows: int, cols: int, cells: int) -> "Conway":
        grid = Conway(rows, cols, False)
        for idx in random_numbers(rows*cols, cells):
            row, col = grid.index_to_coords(idx)
            grid.cells[row][col] = True
        return grid
    
    def to_string(self, cell: bool) -> str:
        alive = cell 
        return "\u25A0" if alive else " "
    
    # Compute next grid
    def next(self) -> "Conway":
        rows, cols = self.shape
        grid = Conway(rows, cols, False)
        is_alive: Callable[[bool], bool] = lambda alive: alive 
        for row, line in enumerate(self.cells):
            line2: list[bool] = []
            for col, curr_alive in enumerate(line):
                count = self.count_neighbors((row, col), is_alive)
                next_alive = False 
                if curr_alive and (count == 2 or count == 3):
                    next_alive = True 
                elif not curr_alive and count == 3:
                    next_alive = True 
                line2.append(next_alive)
            grid.cells[row] = line2
        return grid