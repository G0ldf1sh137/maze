from graphics import Window, Point, Line

from cell import Cell
from maze import Maze

X_OFFSET = 40
Y_OFFSET = 20
NUM_ROWS = 26
NUM_COLS = 46
CELL_WIDTH = 40
CELL_HEIGHT = 40

def main():
    win = Window(1920, 1080)

    maze = Maze(
        X_OFFSET, 
        Y_OFFSET, 
        NUM_ROWS, 
        NUM_COLS, 
        CELL_WIDTH, 
        CELL_HEIGHT, 
        win
    )
    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
