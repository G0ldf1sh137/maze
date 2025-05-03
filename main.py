from graphics import Window, Point, Line

from cell import Cell
from maze import Maze


def main():
    win = Window(1920, 1080)
    
    maze = Maze(10, 10, 21, 38, 50, 50, win)
    maze.solve()

    win.wait_for_close()




if __name__ == "__main__":
    main()