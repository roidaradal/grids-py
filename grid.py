import os, time
from typing import Callable, Self

Coords = tuple[int,int]
Delta = tuple[int,int]

class Grid[T]:
    Up: Delta = (-1, 0)
    Down: Delta = (1, 0)
    Left: Delta = (0, -1)
    Right: Delta = (0, 1)

    @classmethod 
    def new(cls, rows: int, cols: int, initial: T) -> list[list[T]]:
        return [[initial for _ in range(cols)] for _ in range(rows)]
    
    def __init__(self, rows: int, cols: int, initial: T):
        self.cells = self.new(rows, cols, initial)
        
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
        
    # Play grid game 
    # Overridden by child grids
    def play(self):
        print("Grid is not playable")

IntGrid = Grid[int]
BoolGrid = Grid[bool]

# Clear screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

