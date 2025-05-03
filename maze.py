from __future__ import annotations

import time

from cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ) -> Maze:
        self._x1 = x1 # x coordinate of the top-left corner of the maze
        self._y1 = y1 # y coordinate of the top-left corner of the maze
        self._num_rows = num_rows # number of rows in the maze
        self._num_cols = num_cols # number of columns in the maze
        self._cell_size_x = cell_size_x # width of each cell
        self._cell_size_y = cell_size_y # height of each cell
        self._win = win # window to draw the maze on

        self._create_cells()


    # Create cells in the maze
    def _create_cells(self) -> None:
        # List of all cells in the maze
        self._cells = []
        
        # loop through columns
        for col in range(self._num_cols):
            # List of cells in the current column
            col_cells = []
            # loop through rows
            for row in range(self._num_rows):
                # add a new cell to the list of cells in col_cells
                col_cells.append(Cell(self._win))
            # add the new column to _cells
            self._cells.append(col_cells)
            
        
        # Draw the cells in the maze
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)

    
    
    def _draw_cell(self, i: int, j: int) -> None:
        
        # For testing, return from this function if the window is None
        if self._win is None:
            return
        
        # Calculate the coordinates of the cell
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        
        # draw the cell at position
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    
    def _animate(self) -> None:
        # For testing, return from this function if the window is None
        if self._win is None:
            return
        
        # Redraw the window to show the changes and sleep until next frame
        self._win.redraw()
        time.sleep(0.05)