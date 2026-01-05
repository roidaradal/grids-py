import sys
from g2048 import G2048
from greed import Greed
from mines import Mines
from conway import Conway

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print('Usage: python main.py <2048|conway|greed|mines>')
        return 
    
    option = args[0]
    match option:
        case "2048":
            grid = G2048()
            print(grid)
        case "conway":
            grid = Conway.random(50, 250, 1500)
            grid.loop(100)
        case "greed":
            grid = Greed()
            grid.play()
        case "mines":
            grid = Mines(9, 9, 10)
            print(grid)
        case _:
            print('Unknown option:', option)


if __name__ == '__main__':
    main()