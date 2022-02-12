""" Class to represent the player

Created 22.08.2021
@author Max Weise
"""

from card import Card
from abc import ABC, abstractmethod


class Player(ABC):
    """ Typedeclaration for instances of humand and computer player

    Args:
        ABC: Abstract Base Class
    """

    __name: str
    __hand: list
    __stiche: int
    __points: int

    @abstractmethod
    def __init__(self, name: str) -> None:
        """ Initialize a player by giving it a name."""
        pass

    @abstractmethod
    def choose_card(self) -> Card:
        """ Wrapper method for the private __play_cards method.
            In this method, strategies for the different com players
            can be implemented.
        """
        pass

    @abstractmethod
    def guess_stiche(self) -> None:
        """ Method for the player to guess the number of stiche they are going to make."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """ Print a representation of the class to the CLI."""
        pass

    def _play_card(self, index_of_card: int) -> Card:
        """ Let the player play a card. The card must be contained in the hand.
            Raise an exception if the card is not found.

        Returns:
            Card: Card in the deck.
            IndexOutOfBoundsException: When the user tries to access an element
                                       outside of the range of the list, this
                                       exception will be thrown.
        """
        player_hand = self.get_hand()
        played_card = player_hand.pop(index_of_card)
        self.set_hand(player_hand)
        return played_card

    # Define equality of Players
    def __eq__(self, o: object) -> bool:
        """ Define equality of Players."""
        return self.__points == o.__points

    # Define inequality of Players
    def __lt__(self, o: object) -> bool:
        """ Define inequality of Players (Specificly, the less than operator)."""
        return self.__points == o.__points
