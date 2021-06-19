#!/usr/bin/env python
""" Test for the caesar cipher

Created 08.06.2021
Last Revision 19.06.2021
@author Max Weise
"""

import os, unittest, sys

from unittest import TestCase

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.caesar_cipher import Caesar_Cipher


class Test_Caesar_Cipher(TestCase):

    __TEST_WORD = 'CAESAR'
    __TEST_WORD_ENCR = 'FDHVDU'     # Plaintext: caesar, Offset: 3
    __TEST_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    __TEST_ALPHABET_ENCR = 'DEFGHIJKLMNOPQRSTUVWXYZABC'

    def test_encript(self):
        encoded_text = Caesar_Cipher.encript(self.__TEST_WORD, 3)

        self.assertEqual(self.__TEST_WORD_ENCR, encoded_text)

    def test_encript_alphabet(self):
        encoded_text = Caesar_Cipher.encript(self.__TEST_ALPHABET, 3)

        self.assertEqual(encoded_text, self.__TEST_ALPHABET_ENCR)

    def test_decript_with_offset(self):
        decoded_text = Caesar_Cipher.decript_with_offset(self.__TEST_WORD_ENCR, 3)

        self.assertEqual(self.__TEST_WORD, decoded_text)

    def test_decript_alphabet(self):
        decoded_text = Caesar_Cipher.decript_with_offset(self.__TEST_ALPHABET_ENCR, 3)

        self.assertEqual(self.__TEST_ALPHABET, decoded_text)


if __name__ == '__main__':
    unittest.main()
