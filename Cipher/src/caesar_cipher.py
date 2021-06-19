#!/usr/bin/env python
""" Casar Cipher to encode UTF-8 Code

Created 08.06.2021
Last Revision 19.06.2021
@author Max Weise
"""


class Caesar_Cipher(object):
    """ Hold functionality to de and encript Caesar cipher

        NOTE: Only the letters from A - Z are currently used.
              There is no error handling if any other char is used.
    """

    __alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'   # For easier lookup

    @staticmethod
    def encript(plaintext: str, offset: int) -> str:
        """ Shift every char in string by a given offset."""
        ret = ''
        for char in plaintext:
            i = (Caesar_Cipher.__alphabet.index(char) + offset) % 26        # Get the offset index
            ret += Caesar_Cipher.__alphabet[i]                              # Compute new index

        return ret

    @staticmethod
    def decript_with_offset(cipher_text: str, known_offset: int = None) -> str:
        """ Shift every char in string by a given offset (opposite to encript)."""
        ret = ''
        for char in cipher_text:
            i = (Caesar_Cipher.__alphabet.index(char) - known_offset) % 26  # Get the offset index
            ret += Caesar_Cipher.__alphabet[i]                              # Compute new index

        return ret

    @staticmethod
    def decript_brute_force(cipher_text: str, console_output: bool = False) -> list:
        """ Print the solution for every possible offset. Returns a list of all possibilities."""
        ret_list = [Caesar_Cipher.decript_with_offset(cipher_text, offset) for offset in range(26)]
        if console_output:
            for key, value in enumerate(ret_list):
                print(f'{key} -- {value}')

        return ret_list

