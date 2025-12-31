from g2048 import *

# Game constants
GAME_2048 = "2048"
GAME_CONWAY = "conway"
GAME_GREED = "greed"
GAME_MINES = "mines"

def main():
    option = GAME_2048 
    if option == GAME_2048:
        grid = new_2048()
        display_2048(grid)
    else:
        print('Unknown option:', option)


if __name__ == '__main__':
    main()