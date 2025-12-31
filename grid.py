from typing import Callable

# Grid types
Coords = tuple[int,int]
IntGrid = list[list[int]]

# Create new blank grid 
def new_IntGrid(rows: int, cols: int) -> IntGrid:
    return [[0 for _ in range(cols)] for _ in range(rows)]

# Convert index to coords 
def index_to_coords(idx: int, width: int) -> Coords:
    return (idx // width, idx % width)

# Display grid using the to_string function 
def display_grid[T](grid: list[list[T]], to_string: Callable[[T], str]):
    for line in grid:
        out = [to_string(cell) for cell in line]
        print (''.join(out))