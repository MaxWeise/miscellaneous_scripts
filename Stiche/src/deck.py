""" Deck for playing cards. It is possible to create
    'big' deck (52 cards) and a small deck (26 cards).

    This game however, uses a big deck.

Created 15.08.2021
@author Max Weise
"""

import random

from card import Card
from declarations.numbers_and_symboles import Suits, Values


class Deck(object):
    """ The deck holds cards."""

    def __init__(self, small_deck: bool = False):
        """ Create a deck. If noting is specified, a big deck will be created.
            It is possible to specify the creation of a smaller deck."""
        self.deck = []
        self.__create_deck()

    def __create_deck(self) -> None:
        """ Create all the cards and fill them into the deck."""
        for suit in Suits:
            for value in Values:
                self.deck.append(self.__create_card(suit, value))

    def __create_card(self, suit: str, value: int) -> Card:
        """ Create the cards for the deck."""
        return Card(suit, value)

    def shuffle(self) -> None:
        """ Shuffle the deck. The deck itself will be modified with this approach."""
        random.shuffle(self.deck)

    def __str__(self) -> str:
        """ Print a readable representation to the console."""
        for c in self.deck:
            print(c)
        return ''
