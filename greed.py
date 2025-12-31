import random
from grid import * 

GREED_CURSOR = -1

# Create new Greed grid 
def new_Greed() -> IntGrid:
    # Make blank IntGrid 
    rows, cols = 22, 79
    grid = new_grid(rows, cols, 0)
    # Randomize grid digits 
    per_digit = 193 
    digits: list[int] = [GREED_CURSOR]
    for i in range(1, 10):
        digits.extend([i] * per_digit)
    random.shuffle(digits)
    for idx, digit in enumerate(digits):
        row, col = index_to_coords(idx, cols)
        grid[row][col] = digit 
    return grid

# Display Greed grid 
def display_Greed(grid: IntGrid):
    table: dict[int, str] = {
        0: "%2s" % ".", # empty cell
        GREED_CURSOR: "%2s" % "@", # cursor cell
    }
    def to_string(cell: int) -> str:
        if cell not in table:
            return "%2d" % cell 
        return table[cell]
    display_grid(grid, to_string)
