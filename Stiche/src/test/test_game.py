#!/usr/bin/env python
""" Testmodule for the game class

Created 24.08.2021
@author Max Weise
"""

import sys, os
import unittest
import unittest.mock
from unittest import TestCase
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from game import Game
from basemodules.player import Player
from human_player import Human_Player


class Test_Game(TestCase):
    """ Testsuite for the game class."""

    __starting_points: int = 20
    __list_of_players: list[Player] = [
        Human_Player('Player 1', __starting_points),
        Human_Player('Player 2', __starting_points),
        Human_Player('Player 3', __starting_points),
    ]

    def setUp(self) -> None:
        """ Create an instance of the class to test on."""
        self.underTest = Game(self.__list_of_players)

    def test_deal_cards(self) -> None:
        """ Test the method to deal cards to the players."""
        self.underTest._deal_cards()
        players = self.underTest.players.get_elements()
        cards_dealt = 0

        for p in players:
            cards_dealt += len(p.get_hand())

        self.assertEqual(len(players[0].get_hand()), 1)
        self.assertEqual(len(players[1].get_hand()), 1)
        self.assertEqual(len(self.underTest.deck.deck), 52 - cards_dealt)

    @unittest.mock.patch('builtins.input', return_value=1)
    def test_play_cards(self, mock_input) -> None:
        """ Test the play_cards method."""
        pos = -1
        players = self.underTest.get_players()

        for p in players:
            p.set_hand([self.underTest.deck.deck[pos]])
            pos -= 1

        return_value = self.underTest._play_cards(players)

        self.assertEqual(return_value, 0)

    def test_calculate_points(self) -> None:
        """ Test if the points get decreased by the right amount."""
        players = self.underTest.players.get_elements()

        players[0].set_guessed_stiche(1)     # Guess correct
        players[1].set_guessed_stiche(0)     # Guess to high
        players[2].set_guessed_stiche(2)     # Guess to low

        for p in players:
            p.set_stiche(1)

        self.underTest._calculate_points()

        self.assertEqual(players[0].get_points(), 19)
        self.assertEqual(players[1].get_points(), 25)
        self.assertEqual(players[2].get_points(), 25)

    # ? Der Test schlägt fehl, da die Exception nicht geworfen wird
    # ? Wa mach mr jetzt?
    def test_loop_endGameCondition(self) -> None:
        """ Test if the loop method detects the end of the game (one player can't get enough cards)."""
        self.underTest.set_rounds(20)   # Setup the ending condition

        self.underTest.loop()

    def tearDown(self) -> None:
        """ Explicitly delete the test instance."""
        del self.underTest


if __name__ == '__main__':
    unittest.main()
