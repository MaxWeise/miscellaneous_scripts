""" Class for a human player inderface

Created 28.08.2021
@author Max Weise
"""

from card import Card
from basemodules.player import Player
from declarations.decorators import overrides
from declarations.exceptions import IndexOutOfBoundsException
from declarations.exceptions import NotAnIntegerError


class Human_Player(Player):
    """ Representation of a human player who plays the
        game and interacts with the CLI


    Args:
        Player (Player): Abstract Base Class which defines the used methods
    """

    def __init__(self, name: str, points: int) -> None:
        """ Instantiate a Player by giving him a name.

        Args:
            name (str): A string which helps to identify the player.
        """
        # Public attributes
        self.name = name
        self.points = points
        self.stiche = 0

        # Private attributes
        self.__guessed_stiche = 0
        self.__hand = []

    @overrides
    def choose_card(self) -> Card:
        """ Wrapper method for the private __play_cards method.
            Accepted values on input: r: int => 1 <= r <= len(self.__hand)

            Exceptions:
            - OutOfBoundsException - When r < 0
            - TypeError            - When type(r) is not an integer
        """
        print(self.get_hand())
        print(f'Please chose a number between 1 and {len(self.get_hand())}')

        try:    # Try parsing the input to int
            chosen_input = int(input('>>> '))
        except ValueError:
            raise NotAnIntegerError('The enterd value is not of type integer')

        if type(chosen_input) is not int:
            raise NotAnIntegerError('The enterd value is not of type integer')

        if chosen_input > len(self.get_hand()):
            raise IndexOutOfBoundsException('The Entered index is too large!')

        return self._play_card(chosen_input - 1)

    @overrides
    def guess_stiche(self) -> None:
        """ Let the player input the number of stiche they think they can make."""
        guessed_stiche = int(input('Please input the number of stiche you think you can make:\n>>> '))
        self.set_guessed_stiche(guessed_stiche)

    # getter | setter
    def set_guessed_stiche(self, new_guessed_stiche: int) -> None:
        """ Set the number of guessed_stiche."""
        self.__guessed_stiche = new_guessed_stiche

    def get_guessed_stiche(self) -> int:
        """ Returns the nuber of guessed_stiche."""
        return self.__guessed_stiche

    def set_hand(self, new_hand: list) -> None:
        """ Utility Method to change the hand of the player.
            This method changens the entire hand of a plyer.

        Args:
            new_hand (list): List of cards the player should have in his hand
        """
        self.__hand = new_hand

    def get_hand(self) -> list:
        """ Returns the current hand of a player."""
        return self.__hand

    def get_points(self) -> int:
        return self.points

    def set_points(self, new_points: int) -> None:
        self.points = new_points

    def get_stiche(self) -> int:
        return self.stiche

    def set_stiche(self, new_stiche: int) -> None:
        self.stiche = new_stiche

    @overrides
    def __str__(self) -> str:
        """ Print a representation of the class to the CLI."""
        return f'<{self.name}>\n' + str([str(c) for c in self.get_hand()])
