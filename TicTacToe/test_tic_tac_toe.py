""" Test Suite for the TicTacToe Game

created 24.05.2021
Last update 26.05.2021
@author Max Weise
"""

from unittest import TestCase, skip
from tic_tac_toe import Grid

class Test_Grid(TestCase):

    def test_detect_win(self):
        """ Detect wins horizontally, vertically and diagonally."""
        self.test_grid_one = Grid(
                                [
                                    [' ', 'x', ' '],
                                    [' ', 'x', ' '],
                                    [' ', 'x', ' '],
                                ]
                            )
        
        self.test_grid_two = Grid(
                                [
                                    [' ', ' ', ' '],
                                    ['x', 'x', 'x'],
                                    [' ', ' ', ' '],
                                ]
                            )

        self.test_grid_three = Grid(
                                [
                                    ['x', ' ', ' '],
                                    [' ', 'x', ' '],
                                    [' ', ' ', 'x'],
                                ]
                            )

        self.test_grid_four = Grid(
                                [
                                    [' ', ' ', 'x'],
                                    [' ', 'x', ' '],
                                    ['x', ' ', ' '],
                                ]
                            )

        self.assertTrue(self.test_grid_one.detect_win('x'))
        self.assertTrue(self.test_grid_two.detect_win('x'))
        self.assertTrue(self.test_grid_three.detect_win('x'))
        self.assertTrue(self.test_grid_four.detect_win('x'))

    def test_detect_win_edgecase_vertical(self):
        """ Test for an edgecase which caused the programm to
            detect a win (false-positive).
        """
        self.test_grid = Grid(
                                [
                                    ['o', 'x', 'o'],
                                    ['x', 'o', 'x'],
                                    [' ', 'o', 'x'],
                                ]
                            )
        
        self.assertFalse(self.test_grid.detect_win('o'))
        self.assertFalse(self.test_grid.detect_win('x'))

    def test_detect_win_edgecase_horizontal(self):
        """ Test for an edgecase which caused te programm to
            detect a win (false-positive)
        """
        self.test_grid = Grid(
                                [
                                    ['o', 'x', 'x'],
                                    ['x', 'o', 'o'],
                                    [' ', 'o', 'x'],
                                ]
                            )

        self.assertFalse(self.test_grid.detect_win('o'))
        self.assertFalse(self.test_grid.detect_win('x'))

    def test_grid_has_empty_cells(self):
        self.test_grid_one = Grid(
                                [
                                    [' ', ' ', ' '],
                                    [' ', ' ', ' '],
                                    [' ', ' ', ' '],
                                ]
                            )
        
        self.test_grid_two = Grid(
                                [
                                    ['x', 'x', 'x'],
                                    ['x', 'x', 'x'],
                                    ['y', 'y', 'x'],
                                ]
                            )

        self.assertTrue(self.test_grid_one.grid_has_empty_cells())
        self.assertFalse(self.test_grid_two.grid_has_empty_cells())

if __name__ == '__main__':
    unittest.main()
