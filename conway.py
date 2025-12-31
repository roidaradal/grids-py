from grid import *
from utils import random_numbers

# Create new random Conway's Game of Life grid
def random_Conway(rows: int, cols: int, cells: int) -> BoolGrid:
    grid = new_grid(rows, cols, False)
    for idx in random_numbers(rows*cols, cells):
        row, col = index_to_coords(idx, cols)
        grid[row][col] = True
    return grid

# Compute the next Conway's Game of Life grid
def next_Conway(grid: BoolGrid) -> BoolGrid:
    grid2: BoolGrid = []
    is_alive: Callable[[bool], bool] = lambda alive: alive 
    for row, line in enumerate(grid):
        line2: list[bool] = []
        for col, curr_alive in enumerate(line):
            count = count_neighbors(grid, (row,col), is_alive)
            next_alive = False 
            if curr_alive and (count == 2 or count == 3):
                next_alive = True 
            elif not curr_alive and count == 3:
                next_alive = True 
            line2.append(next_alive)
        grid2.append(line2)
    return grid2

# Display Conway's Game of Life grid 
def display_Conway(grid: BoolGrid):
    def to_string(alive: bool) -> str:
        return "\u25A0" if alive else " "
    display_grid(grid, to_string)