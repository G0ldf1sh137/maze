import unittest

from maze import Maze

class Tests(unittest.TestCase):
    
    def setUp(self):
        self.num_cols = 12
        self.num_rows = 10
        self.m1 = Maze(0, 0, self.num_rows, self.num_cols, 10, 10)
    
    def test_maze_create_cells(self):
        self.assertEqual(
            len(self.m1._cells[0]), self.num_rows,
        )
        
        
    def test_maze_entrance(self):
        
        self.assertTrue(
            self.m1._cells[0][0].has_left_wall,
            "Unexpected wall broken"
        )
        
        self.assertFalse(
            self.m1._cells[0][0].has_top_wall,
            "Entrance wall not broken"
        )
        
        
    def test_maze_exit(self):
        
        self.assertTrue(
            self.m1._cells[self.num_cols - 1][self.num_rows - 1].has_right_wall,
            "Unexpected wall broken"
        )
        
        self.assertFalse(
            self.m1._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall,
            "Exit wall not broken"
        )




if __name__ == "__main__":
    unittest.main()