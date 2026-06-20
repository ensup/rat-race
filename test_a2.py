import unittest

from a2 import DOWN, HALL, LEFT, Maze, RAT_1_CHAR, RAT_2_CHAR, Rat, RIGHT, SPROUT, UP, WALL


class TestMazeMove(unittest.TestCase):
    def _make_maze(self, grid, r1_row=1, r1_col=1, r2_row=1, r2_col=2):
        rat_1 = Rat(RAT_1_CHAR, r1_row, r1_col)
        rat_2 = Rat(RAT_2_CHAR, r2_row, r2_col)
        return Maze([list(row) for row in grid], rat_1, rat_2)

    def test_move_updates_row_and_col(self):
        maze = self._make_maze([
            '###',
            '#..',
            '###',
        ])

        moved = maze.move(maze.rat_1, UP + DOWN, RIGHT)

        self.assertTrue(moved)
        self.assertEqual(1, maze.rat_1.row)
        self.assertEqual(2, maze.rat_1.col)

    def test_move_into_wall_returns_false(self):
        maze = self._make_maze([
            '###',
            '#.#',
            '###',
        ])

        moved = maze.move(maze.rat_1, UP + DOWN, RIGHT)

        self.assertFalse(moved)
        self.assertEqual(1, maze.rat_1.row)
        self.assertEqual(1, maze.rat_1.col)

    def test_move_to_sprout_eats_and_clears_cell(self):
        maze = self._make_maze([
            '#####',
            '#.@.#',
            '#####',
        ])

        moved = maze.move(maze.rat_1, UP + DOWN, RIGHT)

        self.assertTrue(moved)
        self.assertEqual(1, maze.rat_1.num_sprouts_eaten)
        self.assertEqual(0, maze.num_sprouts_left)
        self.assertEqual(HALL, maze.maze[1][2])

    def test_move_out_of_bounds_returns_false(self):
        maze = self._make_maze([
            '..',
            '..',
        ], r1_row=0, r1_col=0)

        moved = maze.move(maze.rat_1, UP, LEFT)

        self.assertFalse(moved)
        self.assertEqual(0, maze.rat_1.row)
        self.assertEqual(0, maze.rat_1.col)


if __name__ == '__main__':
    unittest.main()
