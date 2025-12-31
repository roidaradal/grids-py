from typing import Callable

# Grid types
type Grid[T] = list[list[T]]
Coords = tuple[int,int]
IntGrid = Grid[int]
BoolGrid = Grid[bool]

# Create new blank grid 
def new_grid[T](rows: int, cols: int, initial: T) -> Grid[T]:
    return [[initial for _ in range(cols)] for _ in range(rows)]

# Convert index to coords 
def index_to_coords(idx: int, width: int) -> Coords:
    return (idx // width, idx % width)

# Display grid using the to_string function 
def display_grid[T](grid: Grid[T], to_string: Callable[[T], str]):
    for line in grid:
        out = [to_string(cell) for cell in line]
        print (''.join(out))

# Return num_rows, num_cols of grid 
def shape[T](grid: Grid[T]) -> tuple[int, int]:
    return (len(grid), len(grid[0]))

# Check if (y,x) coords is outside of (rows,cols) grid 
def not_inside_bounds(y: int, x: int, rows: int, cols: int) -> bool:
    return y < 0 or x < 0 or y >= rows or x >= cols

# Count the neighbors of grid cell at <coords> using the ok function
def count_neighbors[T](grid: Grid[T], coords: Coords, ok: Callable[[T], bool]) -> int:
    rows, cols = shape(grid)
    y, x = coords 
    count = 0 
    deltas = (-1, 0, 1)
    for dy in deltas:
        for dx in deltas:
            if dy == 0 and dx == 0: continue 
            ny, nx = y+dy, x+dx 
            if not_inside_bounds(ny, nx, rows, cols): continue 
            if ok(grid[ny][nx]):
                count += 1
    return count