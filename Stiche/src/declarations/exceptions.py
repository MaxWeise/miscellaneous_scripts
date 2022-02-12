""" Exceptions get defined in this module

Created: 28.08.2021
@auhtor: Max Weise
"""

from decorators import overrides


class CusotmBaseException(Exception):
    """ This class is used as a base class for all custom created exceptions
        in this project.
    """

    def __init__(self, message: str = None) -> None:
        self.__message = message

    def get_message(self) -> str:
        return self.__message

    def __str__(self) -> str:
        return f'{self.__message}'


class IndexOutOfBoundsException(CusotmBaseException):
    """ This gets raised if the index entered is not in the list."""
    pass


class NotAnIntegerError(CusotmBaseException):
    """ This gets raised if the entered value is not an integer."""

    __DEFAULT_MESSAGE = 'The entered value is not an Integer'

    @overrides
    def __init__(self, message: str = None) -> None:
        if message is None:
            self.__message = self.__DEFAULT_MESSAGE
        else:
            self.__message = message


class GameEndException(CusotmBaseException):
    """ This Exception is raised when the game should end."""

    __DEFAULT_MESSAGE = '=== The game has ended ==='

    @overrides
    def __init__(self, message: str = None) -> None:
        if message is None:
            self.__message = self.__DEFAULT_MESSAGE
        else:
            self.__message = message

