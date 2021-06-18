#!/usr/bin/env python
""" Casar Cipher to encode UTF-8 Code

Created 08.06.2021
Last Revision 09.06.2021
@author Max Weise
"""


class Caesar_Cipher(object):
    """ Hold functionality to de and encript Caesar cipher

        NOTE: Only the letters from A - Z are currently used.
              There is no error handling if any other char is used.
    """

    __alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'   # For easier lookup

    def __decode_cipher(cipher_text: str, known_offset: int) -> str:
        pass

    @staticmethod
    def encript(plaintext: str, offset: int) -> str:
        """ Shift every char in string by a given offset."""
        ret = ''
        for char in plaintext:
            i = (Caesar_Cipher.__alphabet.index(char) + offset) % 26
            ret += Caesar_Cipher.__alphabet[i]

        return ret

    @staticmethod
    def decript(cipher_text: str, known_offset: int = None) -> str:
        """ Shift every char in string by a given offset (opposite to encript)."""
        ret = ''
        for char in cipher_text:
            i = (Caesar_Cipher.__alphabet.index(char) - known_offset) % 26
            ret += Caesar_Cipher.__alphabet[i]

        return ret
