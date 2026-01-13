import random
from grid import IntGrid 
from utils import center

class Memory(IntGrid):
    def __init__(self):
        # Make blank IntGrid 
        rows, cols = 5, 8 
        super().__init__(rows, cols, 0)
        # Randomize grid digits 
        per_digit = 4 
        digits: list[int] = []
        for i in range(10):
            digits.extend([i] * per_digit)
        random.shuffle(digits)
        
        
        for idx, digit in enumerate(digits):
            row, col = self.index_to_coords(idx)
            self.cells[row][col] = digit 
    
    def to_string(self, cell: int) -> str:
        return center(str(cell), 5)
