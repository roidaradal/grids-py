from grid import *
from utils import random_numbers

# 2048: 4x4 grid, adds "2" randomly at empty space, small chance of "4"

# Create new 2048 grid 
def new_2048() -> IntGrid:
    # Make blank IntGrid
    rows, cols = 4, 4 
    grid = new_IntGrid(rows, cols)
    # Randomly place 2x 2 tiles 
    for idx in random_numbers(rows*cols, 2):
        row, col = index_to_coords(idx, cols)
        grid[row][col] = 2
    return grid

# Display 2048 grid 
def display_2048(grid: IntGrid):
    blank = "%5s" % "."
    def to_string(cell: int) -> str:
        num = "%5d" % cell 
        return blank if cell == 0 else num
    display_grid(grid, to_string)
