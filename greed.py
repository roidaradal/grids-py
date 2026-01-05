import random
from grid import Grid, Delta, Coords, IntGrid, clear_screen
from utils import Color, Keyboard

class Greed(IntGrid):
    cursor = -1 
    cellColor = {
        1: Color.green,
        2: Color.cyan,
        3: Color.yellow,
        4: Color.magenta,
        5: Color.blue,
        6: Color.magenta,
        7: Color.yellow,
        8: Color.cyan,
        9: Color.green,
    }

    def __init__(self):
        # Make blank IntGrid 
        rows, cols = 22, 79
        super().__init__(rows, cols, 0)
        # Randomize grid digits 
        per_digit = 193 
        digits: list[int] = [self.cursor]
        for i in range(1, 10):
            digits.extend([i]* per_digit)
        random.shuffle(digits)

        self.score: int = 0
        self.cursor_position: Coords = (0, 0)
        for idx, digit in enumerate(digits):
            row, col = self.index_to_coords(idx)
            self.cells[row][col] = digit 
            if digit == self.cursor:
                self.cursor_position = (row,col)

    def to_string(self, cell: int) -> str:
        match cell:
            case 0:
                return "%6s" % Color.white(".")
            case self.cursor:
                return "%6s" % Color.redOnWhite("@")
            case _:
                return "%6s" % self.cellColor[cell](str(cell))

    def play(self):
        while True:
            clear_screen()
            print('Score:', self.score)
            print(self)
            k = Keyboard.get_char().lower()
            ok = True
            match k:
                case 'q':
                    break 
                case 'w':
                    ok = self.move_cursor(Grid.Up) 
                case 's':
                    ok = self.move_cursor(Grid.Down)
                case 'a':
                    ok = self.move_cursor(Grid.Left)
                case 'd':
                    ok = self.move_cursor(Grid.Right)

            if not ok:
                print('Game over! You have fallen out of the grid')
                break
            
            # TODO: check if current position still has available moves
    
    def move_cursor(self, delta: Delta) -> bool:
        (y, x), (dy, dx) = self.cursor_position, delta 
        ny, nx = y+dy, x+dx 
        if not self.inside_bounds((ny, nx)):
            return False
        
        steps = self.cells[ny][nx]
        if steps == 0: return True 

        # Clear current cursor
        self.cells[y][x] = 0

        for _ in range(steps):
            y, x = y+dy, x+dx 
            if not self.inside_bounds((y, x)):
                return False
            self.score += self.cells[y][x]
            self.cells[y][x] = 0

        
        self.cursor_position = (y, x)
        self.cells[y][x] = self.cursor
        return True
