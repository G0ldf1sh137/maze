
from graphics import Window, Point, Line



class Cell:
    """
    A class representing a cell in a grid.
    """

    def __init__(
        self, 
        win: Window,
        left_wall: bool = True,
        right_wall: bool = True,
        top_wall: bool = True,
        bottom_wall: bool = True,
    ):
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall

        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
    
    
    def draw(self, x1, y1, x2, y2):
        """
        Draws the cell on the given window.
        """
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        if self.has_top_wall:
            top = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top)
        
        if self.has_right_wall:
            right = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right)
        
        if self.has_bottom_wall:
            bottom = Line(Point(x2, y2), Point(x1, y2))
            self._win.draw_line(bottom)
        
        if self.has_left_wall:
            left = Line(Point(x1, y2), Point(x1, y1))
            self._win.draw_line(left)
        

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"