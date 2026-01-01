import os, time
from typing import Callable, Self

Coords = tuple[int,int]

class Grid[T]:
    def __init__(self, rows: int, cols: int, initial: T):
        self.cells = [[initial for _ in range(cols)] for _ in range(rows)]
        
    def __repr__(self) -> str:
        out = []
        for line in self.cells:
            out.append(''.join(self.to_string(cell) for cell in line))
        return '\n'.join(out)
    
    # Overridden by child grids
    def to_string(self, cell: T) -> str:
        return ""
    
    # Overriden by child grids
    def next(self) -> Self:
        return self

    @property 
    def shape(self) -> tuple[int,int]:
        return (len(self.cells), len(self.cells[0]))
    
    # Check if coords is inside grid bounds
    def inside_bounds(self, pt: Coords) -> bool:
        (y, x), (rows, cols) = pt, self.shape
        return y >= 0 and x >= 0 and y < rows and x < cols 
    
    # Convert index to Coords
    def index_to_coords(self, idx: int) -> Coords:
        _, cols = self.shape 
        return (idx // cols, idx % cols)
    
    # Count neighbors of grid cell at <coords> using the ok function
    def count_neighbors(self, coords: Coords, ok: Callable[[T], bool]) -> int:
        (y, x) = coords
        deltas = (-1, 0, 1)
        count = 0
        for dy in deltas:
            for dx in deltas:
                if dy == 0 and dx == 0: continue 
                ny, nx = y+dy, x+dx 
                if not self.inside_bounds((ny, nx)): continue 
                if ok(self.cells[ny][nx]): count += 1
        return count
    
    # Run loop 
    def loop(self, delay_ms: int):
        grid = self
        while True:
            clear_screen()
            print(grid)
            if delay_ms > 0:
                time.sleep(delay_ms / 1000.0)
            grid = grid.next()

IntGrid = Grid[int]
BoolGrid = Grid[bool]

# Clear screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

