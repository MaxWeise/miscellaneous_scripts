""" Values from Ace (1) to Jack (11), Queen (12)
    and King (13) are defined in this module.

Created 18.08.2021
@author Max Weise
"""

from enum import Enum


class Values(Enum):
    """ Values for the playing cards."""
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Suits(Enum):
    """ Suits for the playing cards. They have no value per se,
        they are just used to create a real 52 Card deck."""
    CLUBS = 'Clubs'
    SPADES = 'Spades'
    DIAMONDS = 'Diamonds'
    HEARTS = 'Hearts'
