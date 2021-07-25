#!/usr/bin/env python
""" Simple tictactoe application in terminal window

created 24.05.2021
Last update 26.05.2021
@author Max Weise
"""


class Grid(object):
    """ Grid which holds the game."""

    def __init__(self, grid):
        """ Initialize an empty grid."""
        self.__win = False
        self.grid = grid

    def get_win(self) -> bool:
        return self.__win

    def set_win(self, new_value: bool):
        self.__win = new_value

    def __cell_is_empty(self, cell_x: int, cell_y: int) -> bool:
        """ Checks, if a given cell is empty or not."""
        return self.grid[cell_x][cell_y] == ' '

    def grid_has_empty_cells(self) -> bool:
        """ Iterates over grid to find empty cell.
            Return True if an empty cell is found.
        """
        output = False

        for i in range(3):
            for j in range(3):
                if self.__cell_is_empty(i, j):
                    output = True

        return output

    def __validate_player_input(self, player_x: int, player_y: int) -> bool:
        """ Check, if the player inserts into an empty cell, or if the index is out of range"""
        x_is_valid = (0 <= player_x <= 2)
        y_is_valid = (0 <= player_y <= 2)
        cell_is_empty = self.__cell_is_empty(player_x, player_y)

        return x_is_valid and y_is_valid and cell_is_empty

    def set_player_input(self, player: str):
        """ Get coordinates of the form 'x y' from the player
            and insert symbol according to turn.
        """
        def make_input() -> tuple:
            position = input(f'(Turn: {player}) >>> ')
            coordinates = position.split(' ')

            x = int(coordinates[0])
            y = int(coordinates[1])

            return x, y

        x, y = make_input()
        while not self.__validate_player_input(x, y):
            print(f'Sorry, but the cell {x}|{y} is already taken or not in the grid.')
            print('Please chose a different cell')
            x, y = make_input()

        self.grid[x][y] = player

    def detect_win(self, turn: str) -> bool:
        """ Detect if either a row, col or diagonal has 3
            matching symbols. If so, return true (win).
        """
        win_H = self.__detect_win_horizontal(turn)
        win_V = self.__detect_win_vertical(turn)
        win_D_TL = self.__detect_win_diagonal_topLeft(turn)
        win_D_TR = self.__detect_win_diagonal_topRight(turn)

        return win_H or win_V or win_D_TL or win_D_TR

    def __detect_win_horizontal(self, symbol: str) -> bool:
        """ Check, if any of the rows have 3 identical symbols.
            If so return True
            else  return False."""
        for i in range(3):
            count_symbol = 0
            for j in range(3):
                if self.grid[i][j] == symbol:
                    count_symbol += 1
                else:
                    count_symbol = 0

                if count_symbol == 3:
                    return True

        return False

    def __detect_win_vertical(self, symbol: str) -> bool:
        """ Check, if any of the cols have 3 identical symbols.
            If so return True
            else  return False.
        """
        for i in range(3):
            count_symbol = 0
            for j in range(3):
                if self.grid[j][i] == symbol:
                    count_symbol += 1
                else:
                    count_symbol = 0

                if count_symbol == 3:
                    return True

        return False

    def __detect_win_diagonal_topLeft(self, symbol: str) -> bool:
        """ Check, if any of the diagonals have 3 identical
            symbols. If so, return True.
        """
        for i in range(3):
            if self.grid[i][i] != symbol:
                return False

        return True

    def __detect_win_diagonal_topRight(self, symbol: str) -> bool:
        """ Check, if any of the diagonals have 3 identical
            symbols. If so, return True.
        """
        top_right = self.grid[0][2] == symbol
        middle = self.grid[1][1] == symbol
        bot_left = self.grid[2][0] == symbol

        return top_right and middle and bot_left

    # override
    def __str__(self) -> str:
        """ Output to the console."""
        divider = '---+---+---'

        top_row = f'\n {self.grid[0][0]} | {self.grid[0][1]} | {self.grid[0][2]} \n{divider}'
        mid_row = f'\n {self.grid[1][0]} | {self.grid[1][1]} | {self.grid[1][2]} \n{divider}'
        bot_row = f'\n {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]} \n'

        return top_row + mid_row + bot_row


def main():
    g = Grid(
                [
                    [' ', ' ', ' '],
                    [' ', ' ', ' '],
                    [' ', ' ', ' '],
                ]
            )

    turn = 'o'
    while (not g.get_win()) and g.grid_has_empty_cells():

        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'

        g.set_player_input(turn)

        print(g)

        g.set_win(g.detect_win(turn))

    if g.get_win():
        print(f'The winner is {turn}')
    else:
        print("It's a tie")


if __name__ == '__main__':
    main()
    print('=== END ===')
