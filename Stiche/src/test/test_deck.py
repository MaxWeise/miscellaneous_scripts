#!/usr/bin/env python
""" Test for the deck class

Created 16.08.2021
@author Max Weise
"""

import sys, os
import unittest
from unittest import TestCase
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from deck import Deck


class Test_Deck(TestCase):
    """ Test suite for the Deck class."""

    def setUp(self) -> None:
        """ Create an instance of the Dekc class."""
        self.underTest = Deck()

    def test_deck_creation(self) -> None:
        """ Test the creation of the right amount of cards."""
        self.assertEqual(len(self.underTest.deck), 52)

    def test_shuffle_deck(self):
        """ Test the shuffle method."""
        compare_deck = Deck()
        self.underTest.shuffle()
        decks_are_equal = True

        for i in range(len(self.underTest.deck)):
            if self.underTest.deck[i] != compare_deck.deck[i]:
                decks_are_equal = False

        self.assertFalse(decks_are_equal)

    def tearDown(self) -> None:
        """ Explicitly delete the test instance."""
        del self.underTest


if __name__ == '__main__':
    unittest.main()
