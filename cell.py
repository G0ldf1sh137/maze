from __future__ import annotations

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
        visited: bool = False,
    ) -> Cell:
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall

        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.visited = visited
        self._win = win

    @property
    def center(self) -> Point:
        """
        Returns the center point of the cell.
        """
        return Point(
            self._x1 + (self._x2 - self._x1) / 2, self._y1 + (self._y2 - self._y1) / 2
        )

    def draw(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """
        Draws the cell on the given window.
        """
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        top = Line(Point(x1, y1), Point(x2, y1))
        right = Line(Point(x2, y1), Point(x2, y2))
        bottom = Line(Point(x2, y2), Point(x1, y2))
        left = Line(Point(x1, y2), Point(x1, y1))

        if self.has_top_wall:
            self._win.draw_line(top)
        else:
            self._win.draw_line(top, fill_color="#d9d9d9")

        if self.has_right_wall:
            self._win.draw_line(right)
        else:
            self._win.draw_line(right, fill_color="#d9d9d9")

        if self.has_bottom_wall:
            self._win.draw_line(bottom)
        else:
            self._win.draw_line(bottom, fill_color="#d9d9d9")

        if self.has_left_wall:
            self._win.draw_line(left)
        else:
            self._win.draw_line(left, fill_color="#d9d9d9")

    def draw_move(self, to_cell: Cell, undo=False) -> None:
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"
        line = Line(self.center, to_cell.center)
        self._win.draw_line(line, fill_color)
