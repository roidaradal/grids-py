import random, time
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
        self.steps: int = 0
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
            
    def display(self):
        clear_screen()
        print('Score: %d, Steps: %d' % (self.score, self.steps))
        print(self)

    def has_moves_left(self) -> bool:
        for dy, dx in [Grid.Up, Grid.Down, Grid.Left, Grid.Right]:
            y, x = self.cursor_position 
            ny, nx = y+dy, x+dx 
            if not self.inside_bounds((ny, nx)): continue 

            if self.cells[ny][nx] > 0: return True 
        return False

    def play(self):
        while True:
            self.display()

            # Check if has moves left
            if not self.has_moves_left():
                print('Game over! No moves available')
                break

            k = Keyboard.get_char().lower()
            ok = True
            last = ''
            match k:
                case 'q':
                    break 
                case 'w':
                    ok = self.move_cursor(Grid.Up) 
                    last = 'up'
                case 's':
                    ok = self.move_cursor(Grid.Down)
                    last = 'down'
                case 'a':
                    ok = self.move_cursor(Grid.Left)
                    last = 'left'
                case 'd':
                    ok = self.move_cursor(Grid.Right)
                    last = 'right'

            if not ok:
                print('Last move:', last)
                print('Game over! You have fallen off the grid')
                break
    
    def move_cursor(self, delta: Delta) -> bool:
        (y, x), (dy, dx) = self.cursor_position, delta 
        ny, nx = y+dy, x+dx 
        if not self.inside_bounds((ny, nx)):
            return False
        
        steps = self.cells[ny][nx]
        if steps == 0: return True 

        # Clear current cursor
        self.cells[y][x] = 0

        delay = 10 / 1000.0
        self.steps = steps
        for _ in range(steps):
            self.steps -= 1
            self.cells[y][x] = 0
            y, x = y+dy, x+dx 
            if not self.inside_bounds((y, x)): return False

            self.score += self.cells[y][x]
            self.cells[y][x] = self.cursor
            self.cursor_position = (y,x)

            self.display()
            time.sleep(delay)

        return True
