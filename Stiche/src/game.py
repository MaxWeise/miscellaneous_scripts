""" This module defines the flow of the game

Created 24.08.2021
@author Max Weise
"""

from deck import Deck
from basemodules.player import Player
from declarations.ringbuffer import Ringbuffer
# from declarations.exceptions import GameEndException


class Game:
    """ The game consists of three phases:
        1. Guess your Stiche
        2. Each player plays a card
        3. Choose the winner of this round

        If the players have cards left, return to step 2.
        Else determine, who will gain points and who looses points
        based on how far off the guess was
    """

    def __init__(self, players: list[Player]) -> None:
        """ Initialize a game by declaring a list of players."""
        self.__size_of_buffer = len(players)
        self.players = Ringbuffer(self.__size_of_buffer)
        for player in players:
            self.players.enqueue(player)

        self.deck = Deck()
        self.deck.shuffle()
        self.__rounds = 1

    # Getters | Setters
    def get_size_of_buffer(self) -> int:
        """ Return the size of the buffer."""
        return self.__size_of_buffer

    def get_length_of_deck(self) -> int:
        """ Return the number of cards in the deck."""
        return len(self.deck.deck)

    def get_players(self) -> list[Player]:
        return self.players.get_elements()

    def get_rounds(self) -> int:
        """ Retunrs the number of rounds played"""
        return self.__rounds

    def set_rounds(self, rounds: int) -> None:
        """ Utility method to set the played rounds to a prefered value."""
        self.__rounds = rounds

    # Methods
    def _deal_cards(self) -> None:
        """ Deal cards to the players according to the number of played rounds."""
        for player in self.players.get_elements():
            player.set_hand([self.deck.deck.pop() for _ in range(self.__rounds)])

    def _guess_stiche(self) -> None:
        """ Let the players input a number to guess their stiche."""
        for player in self.players.get_elements():
            player.guess_stiche()

    def _play_cards(self, sequence_of_players: tuple[Player]) -> int:
        """ All players play their cards to achieve the number
            of stiche they guessed previously.
        """
        list_of_cards = []
        # * Iterate over sequence
        for player in sequence_of_players:
            # * Build sequence of cards
            list_of_cards.append(player.choose_card())

        # * Find index of highest card
        max_value = max(list_of_cards)
        max_index = list_of_cards.index(max_value)

        # * Return index, pointer will be set in self.loop()
        return max_index

    def _calculate_points(self) -> None:
        """ Calculate the points based on wheather or not the players guessed
            their stiche correctly. If the player guessed correctly, they lose the amount of
            stiche in points. For every wrong guess, they gain 5 points.
        """
        for player in self.players.get_elements():
            player_points = player.get_points()
            player_guessed_stiche = player.get_guessed_stiche()
            player_stiche = player.get_stiche()

            if player_guessed_stiche == player_stiche:
                player.set_points(player_points - player_stiche)
            else:
                player.set_points(player_points + abs(player_stiche - player_guessed_stiche) * 5)

    def _end_game(self) -> None:
        """ This method ends the game by printing the list of players in reversed oder.

            Raises: GameEndException: Exception to end the game.
        """
        list_of_players = self.get_players()
        list_of_players.sort()

        for index, p in enumerate(list_of_players):
            print(f'{index} -- {p}')

        quit()

    def loop(self) -> None:
        """ Play the game according to the rules."""
        # * Initial setup for each round
        if (self.get_rounds() * self.get_size_of_buffer()) > self.get_length_of_deck():
            self._end_game()

        self._deal_cards()
        self._guess_stiche()

        # * Actual game where players throw in their cards
        for _ in range(self.__rounds):
            self._play_cards()

        # * In the end the points of the players get calculated
        self._calculate_points()
        self.__rounds += 1
