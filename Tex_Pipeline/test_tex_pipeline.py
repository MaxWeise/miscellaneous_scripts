#!/usr/bin/env python
""" Test suit for the tex pipeline

Created 07.10.2021
@author Max Weise
"""

import os
import shutil
import sys
import unittest
from unittest import TestCase

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import src.tex_pipeline as tp
from pathlib import Path


class Test_Tex_Pipeline(TestCase):
    """ Test the TeX Pipeline."""

    __TEST_FILE = 'test_file.tex'
    __FILE_NAME = 'test_file'

    def setUp(self) -> None:
        """ Create a simple tex koma-report to be compiled."""
        with open(self.__TEST_FILE, 'w+') as f:
            f.write('\\documentclass[a4paper, draft, 12pt]{scrreprt}\n\n')
            f.write('\\begin{document}\n\n')
            f.write('This is a Tex file \\\\ I hope this is in a new line\n')
            f.write('\\end{document}\n\n')

    def test_copy_file(self) -> None:
        """ This tests the copy_file function."""
        name_output = tp.copy_file(self.__FILE_NAME)
        list_of_files = os.listdir()

        name_parts = name_output.split('.')
        self.assertEqual(len(name_parts), 1)
        self.assertTrue(self.__TEST_FILE in list_of_files)
        self.assertTrue(tp.FILE_PREFIX + self.__TEST_FILE in list_of_files)

    def test_remove_draft_option(self) -> None:
        """ Test the remove draft function."""
        tp.remove_draft_option(self.__FILE_NAME)

        with open(self.__TEST_FILE) as f:
            lines_in_file = f.readlines()

        self.assertFalse('draft' in lines_in_file[0])

    def test_compile_tex_file(self) -> None:
        """ Test the automated compilation of tex files."""
        tp.compile_tex_file(self.__FILE_NAME)

        list_of_files = os.listdir()
        expected_file_name = self.__FILE_NAME + '.pdf'

        self.assertTrue(expected_file_name in list_of_files)
        self.assertTrue(os.path.getsize(expected_file_name) > 0)

    def test_clean_up(self) -> None:
        """ Test the clean up process."""
        new_file_name = tp.copy_file(__file_name=self.__FILE_NAME)
        tp.compile_tex_file(new_file_name)   # This is only for setup
        tp.clean_up(new_file_name)           # Run tested function

        p = Path(os.path.join(tp.WORKING_PATH, tp.DEPLOY_FOLER))

        self.assertTrue(p.exists())
        dir_entries = os.listdir()                              # Get entries in root
        deploy_folder_entries = os.listdir(tp.DEPLOY_FOLER)     # Get entries in DEPOLY
        today = tp._get_date_prefix()

        self.assertTrue(tp.DEPLOY_FOLER in dir_entries)
        self.assertTrue(self.__TEST_FILE in dir_entries)
        self.assertTrue(today + '_' + self.__FILE_NAME + '.pdf' in deploy_folder_entries)

    def tearDown(self) -> None:
        """ Remove the generated files."""
        try:
            shutil.rmtree(tp.DEPLOY_FOLER)
        except WindowsError:
            # * This error gets thrown during all tests except test_cleanup. The reason being the DEPLOY folder is not
            # * created for other tests and therfore # cant be removed from the path. Because it makes the console
            # * output less readable I chose to ignore it with this mechanism despite it being bad practice
            pass
        except Exception as e:
            print(e)
        finally:
            for file in os.listdir():
                if self.__FILE_NAME in file or file is tp.DEPLOY_FOLER:
                    os.remove(file)


if __name__ == '__main__':
    unittest.main()
