#!/usr/bin/env python
""" Test for the plyer class.

Created 22.08.2021
@author Max Weise
"""

import sys, os
import unittest
import unittest.mock
from unittest import TestCase
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from card import Card
from human_player import Human_Player
from declarations.numbers_and_symboles import Suits, Values
from declarations.exceptions import IndexOutOfBoundsException, NotAnIntegerError


class Test_Human_Player(TestCase):
    """ Test suit for the human player class."""

    __STARTING_POINTS = 20

    def setUp(self) -> None:
        """ Setup an instance of a human player and fill the hand with three cards."""
        self.underTest = Human_Player('Test_Player', self.__STARTING_POINTS)
        hand_of_player = [
            Card(Suits.SPADES, Values.ACE),
            Card(Suits.SPADES, Values.TWO),
            Card(Suits.SPADES, Values.THREE),
        ]
        self.underTest.set_hand(hand_of_player)

    def test_play_card(self) -> None:
        """ Test, if the player can play a card.
            The number of cards in the hand of the player should
            decrease by exactly one.
            The card should not be found in the hand of the player.

            This method is implemented in the parent class
            <Player.py>
        """
        # Setup needed variables
        number_of_cards = len(self.underTest.get_hand())
        player_hand = self.underTest.get_hand()
        ace_of_spades = player_hand[0]

        played_card = self.underTest._play_card(0)

        # Check if the number of cards deacreased by exactly one
        #       if the played card is the correct one
        #       if the played card can't be found in the current hand of the player
        self.assertEqual(len(self.underTest.get_hand()), number_of_cards - 1)
        self.assertEqual(played_card, ace_of_spades)
        self.assertNotIn(ace_of_spades, self.underTest.get_hand())

    @unittest.mock.patch('builtins.input', return_value=1)
    def test_chose_card(self, mock_input) -> None:
        """ Test the method to let the player chose a card."""
        compare_card = self.underTest.get_hand()[0]

        return_value = self.underTest.choose_card()
        self.assertEqual(return_value, compare_card)

    @unittest.mock.patch('builtins.input', return_value='avx')
    def test_chose_card_E_OutOfBoundsException(self, mock_input) -> None:
        """ Test if an OutOfBoundsError is thrown on incorrect input."""

        with self.assertRaises(NotAnIntegerError):
            self.underTest.choose_card()

    @unittest.mock.patch('builtins.input', return_value=10000)
    def test_chose_card_E_IndexOutOfBoundsException(self, mock_input) -> None:
        """ Test if an OutOfBoundsError is thrown on incorrect input."""

        with self.assertRaises(IndexOutOfBoundsException):
            self.underTest.choose_card()

    def tearDown(self) -> None:
        """ Delete the test instance. This is done explicitly for better readability."""
        del self.underTest


if __name__ == '__main__':
    unittest.main()
