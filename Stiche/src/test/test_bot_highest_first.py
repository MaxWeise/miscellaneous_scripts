#!/usr/bin/env python
""" Test class for the bot which follows the
    'highest first' strategy

Created 28.08.2021
@author Max Weise
"""

import sys, os
import unittest
from unittest import TestCase
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from card import Card
from bot_strategies import Bot_HighestFirst
from declarations.numbers_and_symboles import Suits, Values


class Test_Card(TestCase):
    """ Test suite for the card class"""

    def setUp(self) -> None:
        """ Instantiate a test object."""
        self.underTest = Bot_HighestFirst('Test Bot Highest First')
        hand_of_player = [
            Card(Suits.SPADES, Values.KING),
            Card(Suits.SPADES, Values.QUEEN),
            Card(Suits.SPADES, Values.TEN),
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

    def test_choose_card(self) -> Card:
        """ Wrapper method for the private __play_cards method.
            In this method, strategies for the different com players
            can be implemented.

            The method will be run twice to see the bahaviour
            of the method.
        """
        # Variable setup
        highest_card = Card(Suits.SPADES, Values.KING)
        second_highest_card = Card(Suits.SPADES, Values.QUEEN)

        returned_card = self.underTest.choose_card()
        self.assertEqual(returned_card, highest_card)

        # ===== Second run =====
        returned_card = self.underTest.choose_card()
        self.assertEqual(returned_card, second_highest_card)

    def test_guess_stiche(self) -> None:
        """ Method for the player to guess the number of stiche they are going to make.
            This bot will see a king or a queen as a guaranteed stich.
        """

        self.underTest.guess_stiche()
        self.assertEqual(self.underTest.get_guessed_stiche(), 2)

    def tearDown(self) -> None:
        """ Explicitly delete the test instance."""
        del self.underTest


if __name__ == '__main__':
    unittest.main()
