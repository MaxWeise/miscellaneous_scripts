""" This interface defines the functionality
    of an AI opponent

Created 28.08.2021
@author Max Weise
"""

from abc import abstractmethod

from player import Player
from card import Card


class Bot(Player):
    """ This is a type definition of an AI opponent.
        This is a parent interface for several
        child bots. Every child defines a
        specific strategie.
    """

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
