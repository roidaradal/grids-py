from grid import * 
from utils import random_numbers

# Easy      9x9     10
# Medium    16x16   40
# Hard      30x16   99

bomb = -1

# Create new Minesweeper grid 
def new_Mines(rows: int, cols: int, mines: int) -> IntGrid:
    # Make blank IntGrid 
    grid = new_IntGrid(rows, cols)
    # Randomly place bombs 
    for idx in random_numbers(rows*cols, mines):
        row, col = index_to_coords(idx, cols)
        grid[row][col] = bomb 
    is_bomb: Callable[[int],bool] = lambda cell: cell == bomb 
    # Count neighbor mines 
    for row, line in enumerate(grid):
        for col, cell in enumerate(line):
            if cell == bomb: continue 
            grid[row][col] = count_neighbors(grid, (row,col), is_bomb)
    return grid

# Display Minesweeper grid 
def display_Mines(grid: IntGrid):
    bomb_cell = "%3s" % "X"
    def to_string(cell: int) -> str:
        normal_cell = "%3d" % cell
        return bomb_cell if cell == bomb else normal_cell
    display_grid(grid, to_string)