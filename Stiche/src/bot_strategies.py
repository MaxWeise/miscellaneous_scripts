""" Bots and their strategies get
    defined in this module.

Created 28.08.2021
@author Max Weise
"""

from bot import Bot
from card import Card


class Bot_HighestFirst(Bot):
    """ This Bot plays his highest cards first."""

    __name: str
    __points: int
    __hand: list
    __stiche: int
    __guessed_stiche: int

    def __init__(self, name: str, starting_point: int = 20) -> None:
        """ Instantiate a Bot by giving it a name."""
        self.__name = name
        self.__points = starting_point
        self.__stiche = 0
        self.__guessed_stiche = 0

    # getter | setter
    def get_name(self) -> str:
        return self.__name

    def set_name(self, new_name: str) -> None:
        self.__name = new_name

    def get_points(self) -> int:
        return self.__points

    def set_points(self, new_points: int) -> None:
        self.__points = new_points

    def get_hand(self) -> list:
        return self.__hand

    def set_hand(self, new_hand: list) -> None:
        self.__hand = new_hand

    def get_stiche(self) -> int:
        return self.__stiche

    def set_stiche(self, new_stiche: int) -> None:
        self.__stiche = new_stiche

    def get_guessed_stiche(self) -> int:
        return self.__guessed_stiche

    def set_guessed_stiche(self, new_guessed_stiche: int) -> None:
        self.__guessed_stiche = new_guessed_stiche

    def choose_card(self) -> Card:
        """ Wrapper method for the private __play_cards method.
            In this method, strategies for the different com players
            can be implemented.
        """
        current_hand = self.get_hand()
        current_hand.sort(reverse=True)
        return self._play_card(0)

    def guess_stiche(self) -> None:
        """ Method for the player to guess the number of stiche they are going to make.
            This bot will see a king or a queen as a guaranteed stich.
        """
        current_hand = self.get_hand()
        for card in current_hand:
            if card.value.value > 10:
                self.set_guessed_stiche(self.get_guessed_stiche() + 1)

    def __str__(self) -> str:
        """ Print a representation of the class to the CLI."""
        pass
