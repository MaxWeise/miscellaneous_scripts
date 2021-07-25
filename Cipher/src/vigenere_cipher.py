#!/usr/bin/env python
""" Vigenere Cipher to encode UTF-8 Code

Created 19.06.2021
Last Revision 29.06.2021
@author Max Weise
"""


class Vigenere_Cipher(object):
    """ Hold functionality to decript and encript Vigenere Cipher

        NOTE: Only the letters from A - Z are currently used.
              There is no error handling if any other char is used.
    """

    __alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'   # For easier lookup

    def __offset_alphabet(offset: int) -> str:
        ret = ''
        for c in Vigenere_Cipher.__alphabet:
            ret += Vigenere_Cipher.__alphabet[(Vigenere_Cipher.__alphabet.index(c) + offset) % 26]

        return ret

    @staticmethod
    def encript(plain_text: str, key: str) -> str:
        """ Encript a message using the Vigenere Cipher."""
        # Get rid of spaces
        plaintext = plain_text.strip()
        keyword = key.strip()

        key_length = len(keyword)
        key_as_int = [ord(i) for i in keyword]
        plaintext_int = [ord(i) for i in plaintext]
        ciphertext = ''

        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            ciphertext += chr(value + 65)

        return ciphertext

    @staticmethod
    def decript_with_offset(cipher_text: str, known_keyword: str) -> str:
        """ Decript messages which have been encripted using the Vigenere Cipher
            This method assumes the keyword is known.
        """

        pass

