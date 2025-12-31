import os, random, time
from grid import Grid, Callable

# Generate <count> random numbers from [0, limit)
def random_numbers(limit: int, count: int) -> list[int]:
    numbers: set[int] = set()
    while len(numbers) != count:
        numbers.add(random.randrange(limit))
    return list(numbers)

# Run loop 
def run_loop[T](grid: Grid[T], display: Callable[[Grid[T]], None], get_next: Callable[[Grid[T]], Grid[T]], delay_ms: int):
    while True:
        clear_screen()
        display(grid)
        if delay_ms > 0:
            time.sleep(delay_ms / 1000.0)
        grid = get_next(grid)

# Clear screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
