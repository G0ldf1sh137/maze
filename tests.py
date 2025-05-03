import unittest

from maze import Maze


class Tests(unittest.TestCase):

    def setUp(self):
        self.num_cols = 12
        self.num_rows = 10
        self.m1 = Maze(0, 0, self.num_rows, self.num_cols, 10, 10)

    def test_maze_create_cells(self):
        self.assertEqual(
            len(self.m1._cells[0]),
            self.num_rows,
        )

    def test_maze_entrance(self):
        entrance = self.m1._cells[0][0]
        self.assertTrue(entrance.has_left_wall, "Unexpected entrance wall broken")
        self.assertFalse(entrance.has_top_wall, "Entrance wall not broken")

    def test_maze_exit(self):
        exit = self.m1._cells[self.num_cols - 1][self.num_rows - 1]
        self.assertTrue(exit.has_right_wall, "Unexpected exit wall broken")
        self.assertFalse(exit.has_bottom_wall, "Exit wall not broken")

    def test_maze_init_visited_reset(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                cell = self.m1._cells[i][j]
                self.assertFalse(cell.visited, f"Cell ({i}, {j}) should not be visited")

    def test_maze_solve(self):
        self.assertTrue(self.m1.solve(), "Maze should be solvable")


if __name__ == "__main__":
    unittest.main()
