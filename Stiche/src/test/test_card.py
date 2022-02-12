#!/usr/bin/env python
""" Testklasse für das <card.py> modul

Created 16.08.2021
@author Max Weise
"""

import sys, os
import unittest
from unittest import TestCase
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from card import Card
from declarations.numbers_and_symboles import Suits, Values


class Test_Card(TestCase):
    """ Test suite for the card class"""

    def setUp(self) -> None:
        """ Create an instance of a card to test on."""
        self.underTest = Card(Suits.SPADES, Values.ACE)

    def test_equality(self) -> None:
        """ Test the __eq__ method of the card class"""
        test_card = Card(Suits.CLUBS, Values.ACE)

        self.assertTrue(self.underTest == test_card)

    def test_lessthan(self) -> None:
        """ Test the __lt__ method of the card class"""
        test_card = Card(Suits.SPADES, Values.TWO)

        self.assertTrue(self.underTest < test_card)

    def tearDown(self) -> None:
        """ Explicitly delete the test instance."""
        del self.underTest


if __name__ == '__main__':
    unittest.main()
