from g2048 import *
from greed import *

# Game constants
GAME_2048 = "2048"
GAME_CONWAY = "conway"
GAME_GREED = "greed"
GAME_MINES = "mines"

def main():
    option = GAME_GREED
    if option == GAME_2048:
        grid = new_2048()
        display_2048(grid)
    elif option == GAME_GREED:
        grid = new_Greed()
        display_Greed(grid)
    else:
        print('Unknown option:', option)


if __name__ == '__main__':
    main()