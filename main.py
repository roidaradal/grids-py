from g2048 import new_2048, display_2048
from greed import new_Greed, display_Greed
from mines import new_Mines, display_Mines

# Game constants
GAME_2048 = "2048"
GAME_CONWAY = "conway"
GAME_GREED = "greed"
GAME_MINES = "mines"

def main():
    option = GAME_MINES
    if option == GAME_2048:
        grid = new_2048()
        display_2048(grid)
    elif option == GAME_GREED:
        grid = new_Greed()
        display_Greed(grid)
    elif option == GAME_MINES:
        grid = new_Mines(9, 9, 10)
        display_Mines(grid)
    else:
        print('Unknown option:', option)


if __name__ == '__main__':
    main()