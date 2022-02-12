""" This is a card used in a
    Deck to play games.

Created 15.08.2021
@author Max Weise
"""
from declarations.numbers_and_symboles import Suits, Values


class Card:
    """ Definition for a playing card. The value is
        defined by the values of the 'Value' enumeration
        The Suits don't bare any value.
        The Ace is the lowest card in the deck."""

    def __init__(self, suit: Suits, value: Values):
        """ Create a card by giving it a Value and a Suit."""
        self.value = value
        self.suit = suit

    # Define equality of cards
    def __eq__(self, o: object) -> bool:
        """ Define equality of cards."""
        return self.value.value == o.value.value

    # Define inequality of cards
    def __lt__(self, o: object) -> bool:
        """ Define inequality of cards (Specificly, the less than operator)."""
        return self.value.value < o.value.value

    def __str__(self) -> str:
        """ Print a representation to the console."""
        return f'{self.value.value} of {self.suit.value}'
