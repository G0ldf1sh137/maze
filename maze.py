from __future__ import annotations

from typing import List

import time
import random

from cell import Cell

SOLVE_SPEED = 0.01
BACKTRACK_SPEED = 0.02

class Maze:
    """
    A class representing a maze using a grid of cells.
    """
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ) -> Maze:
        self._x1 = x1  # x coordinate of the top-left corner of the maze
        self._y1 = y1  # y coordinate of the top-left corner of the maze
        self._num_rows = num_rows  # number of rows in the maze
        self._num_cols = num_cols  # number of columns in the maze
        self._cell_size_x = cell_size_x  # width of each cell
        self._cell_size_y = cell_size_y  # height of each cell
        self._win = win  # window to draw the maze on

        # If no seed provided, get a random seed so we get a different maze each time
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


    def _create_cells(self) -> None:
        self._cells: List[List[Cell]] = []
        for col in range(self._num_cols):
            # List of cells in the current column
            col_cells: List[Cell] = []
            for row in range(self._num_rows):
                col_cells.append(Cell(self._win))
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

    def _animate(self, t: float = 0.001) -> None:
        # For testing, return from this function if the window is None
        if self._win is None:
            return

        # Redraw the window to show the changes and sleep until next frame
        self._win.redraw()
        time.sleep(t)

    def _break_entrance_and_exit(self) -> None:
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        # Redraw the entrance and exit cells
        self._draw_cell(0, 0)
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j) -> None:
        self._cells[i][j].visited = True

        # Get the neighbors of the cell
        # Neighbors must be inside the loop to be updated after each wall break
        # or else when we return to the function we might re-visit the same cell
        while True:
            neighbors = []

            # Check Top
            if j > 0 and not self._cells[i][j - 1].visited:
                neighbors.append((i, j - 1))
            # Check Right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                neighbors.append((i + 1, j))
            # Check Bottom
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                neighbors.append((i, j + 1))
            # Check Left
            if i > 0 and not self._cells[i - 1][j].visited:
                neighbors.append((i - 1, j))

            # If there are no neighbors, draw current cell and return to break the loop
            if len(neighbors) == 0:
                self._draw_cell(i, j)
                return

            # Pick a random neighbor
            rand = random.randint(0, len(neighbors) - 1)

            # Knock down walls between the current cell and the chosen neighbor
            ni, nj = neighbors[rand]

            # Neighbor is the cell to the top
            if ni == i and nj == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[ni][nj].has_bottom_wall = False
            # Neighbor is the cell to the right
            elif ni == i + 1 and nj == j:
                self._cells[i][j].has_right_wall = False
                self._cells[ni][nj].has_left_wall = False
            # Neighbor is the cell to the bottom
            elif ni == i and nj == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[ni][nj].has_top_wall = False
            # Neighbor is the cell to the left
            elif ni == i - 1 and nj == j:
                self._cells[i][j].has_left_wall = False
                self._cells[ni][nj].has_right_wall = False

            # recursively call the function to break walls of the chosen neighbor
            self._break_walls_r(ni, nj)

    def _reset_cells_visited(self) -> None:
        # Reset the visited status of all cells
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self) -> bool:
        return self._solve_r(0, 0)

    def _solve_r(self, i: int, j: int) -> bool:
        # Return true if we reached the exit
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        self._animate(SOLVE_SPEED) # run animate faster when solving
        current = self._cells[i][j]
        current.visited = True

        # Check top
        if j > 0 and not current.has_top_wall and not self._cells[i][j - 1].visited:
            top = self._cells[i][j - 1]
            current.draw_move(top)
            if self._solve_r(i, j - 1):
                return True
            self._animate(BACKTRACK_SPEED) # run animate slower when backtracking
            current.draw_move(top, undo=True)

        # Check right
        if (
            i < self._num_cols - 1
            and not current.has_right_wall
            and not self._cells[i + 1][j].visited
        ):
            right = self._cells[i + 1][j]
            current.draw_move(right)
            if self._solve_r(i + 1, j):
                return True
            self._animate(BACKTRACK_SPEED)
            current.draw_move(right, undo=True)
        # Check bottom
        if (
            j < self._num_rows - 1
            and not current.has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            bottom = self._cells[i][j + 1]
            current.draw_move(bottom)
            if self._solve_r(i, j + 1):
                return True
            self._animate(BACKTRACK_SPEED)
            current.draw_move(bottom, undo=True)

        # Check left
        if i > 0 and not current.has_left_wall and not self._cells[i - 1][j].visited:
            left = self._cells[i - 1][j]
            current.draw_move(left)
            if self._solve_r(i - 1, j):
                return True
            self._animate(BACKTRACK_SPEED)
            current.draw_move(left, undo=True)

        return False
