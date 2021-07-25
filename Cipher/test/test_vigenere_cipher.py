#!/usr/bin/env python
""" Test for the caesar cipher

Created 19.06.2021
Last Revision 20.06.2021
@author Max Weise
"""

import os, unittest, sys

from unittest import TestCase

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.vigenere_cipher import Vigenere_Cipher


class Test_Vigenere_Cipher(TestCase):

    __TEST_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    __PLAIN_TEXT = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'
    __CIPHER_TEXT = 'OPK UHMTO WZUAA JFB ECSTF SMIM BNI YEQC YWM'
    __KEY_WORD = 'VIGENERE'

    def test_encript(self):
        encripted_text = Vigenere_Cipher.encript(self.__PLAIN_TEXT, self.__KEY_WORD)
        self.assertEquals(encripted_text, self.__CIPHER_TEXT)

    @unittest.skip
    def test_decript_with_keyword(self):
        pass


if __name__ == '__main__':
    unittest.main()
