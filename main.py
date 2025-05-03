from graphics import Window, Point, Line

from cell import Cell


def main():
    win = Window(800, 600)
    
    c1 = Cell(win, bottom_wall=False)
    c1.draw(100, 100, 200, 200)
    
    c2 = Cell(win, top_wall=False, right_wall=False)
    c2.draw(100, 200, 200, 300)

    win.wait_for_close()




if __name__ == "__main__":
    main()