#!/usr/bin/env python
""" Pipeline for .tex documents.
    The documents get converted from draft mode to
    compile ready documents and then compiled
    using the LaTeX engine

Created: 07.10.2021
@author: Max Weise
"""

import os
import shutil
import logging
import datetime
import argparse
import subprocess


# === DEFINITION OF CONSTANTS ===
WORKING_PATH = './'
FILE_PREFIX = '[piped]_'    # Use this to identify modified files
FILE_PREFIX_SPLIT = '[piped]'
DEPLOY_FOLER = 'DEPLOY'

LOGGING_LEVELS = {
    'DEBUG'     : logging.DEBUG,
    'INFO'      : logging.INFO,
    'WARNING'   : logging.WARNING,
    'ERROR'     : logging.ERROR,
    'CRITICAL'  : logging.CRITICAL,
}


def copy_file(__file_name: str) -> str:
    """ This function copies the wip-tex file to compile it without
        modifying the original file.
    """
    new_name = FILE_PREFIX + __file_name
    logging.info(f'Copying the file {__file_name}.tex -> {new_name}.tex')
    shutil.copy(__file_name + '.tex', new_name + '.tex')

    return new_name


def remove_draft_option(__file_name: str) -> None:  # sourcery skip: extract-method
    """ This function removes the draft option from a tex file."""

    try:
        lines_of_file = []
        logging.info(f'Now reading {__file_name}.tex')
        with open(__file_name + '.tex', 'r') as f:
            lines_of_file = f.readlines()

        parts_of_line = lines_of_file[0].split(',')
        parts_of_line.pop(parts_of_line.index(' draft'))

        lines_of_file[0] = ','.join(parts_of_line)

        logging.info(f'Now writing {__file_name}.tex')
        with open(__file_name + '.tex', 'w') as f:
            f.writelines(lines_of_file)
    except Exception as e:
        logging.error(e)


def compile_tex_file(__file_name: str, verbose: bool = False) -> None:
    """ Call LaTeX.exe and compile the tex document to a PDF file."""

    arg_list = ['pdflatex', __file_name + '.tex']

    if not verbose:
        arg_list.insert(1, '-quiet')

    try:
        logging.info(f'Calling <{arg_list}>')
        subprocess.check_call(arg_list)
    except Exception as e:
        logging.error(e)


def _get_date_prefix() -> str:
    """ Return a string representation of the current date in the format yyyy_mm_dd_HH_MM"""
    year = datetime.date.today().year
    month = datetime.date.today().month
    day = datetime.date.today().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute

    return f'{year}_{month}_{day}_{hour}_{minute}_'


def _move_file_to_folder(__file_name: str) -> None:
    """ Move the compiled file to a specific folder"""
    deploy_path = os.path.join(WORKING_PATH, DEPLOY_FOLER)
    try:
        os.mkdir(deploy_path)
    except FileExistsError as e:
        logging.info(e)
        logging.warning(f'The directory {DEPLOY_FOLER} does allready exist.')
    except Exception as e:
        logging.error(e)

    today = _get_date_prefix()
    file_name = __file_name + '.pdf'

    # Remove the working prefix from the file
    string_list = __file_name.split('_')
    string_list.pop(string_list.index(FILE_PREFIX_SPLIT))
    new_name = '_'.join(string_list) + '.pdf'

    try:
        logging.info('Moving file to deploy directory')
        os.rename(os.path.join(WORKING_PATH, file_name), os.path.join(deploy_path, today + '_' + new_name))
    except Exception as e:
        logging.error(e)


def _clean_working_dir() -> None:
    """ Remove all auxiliary files which have been generated in the process"""
    logging.info('Cleaning up working directory')
    for f in os.listdir('.'):
        if FILE_PREFIX in f:
            os.remove(f)


def clean_up(__file_name: str = None) -> None:
    """ This function cleans the working directory"""
    _move_file_to_folder(__file_name)
    _clean_working_dir()


def _create_parser() -> argparse.ArgumentParser:
    """ Returns an argumentParser object which contains all valid CLI arguments."""
    # == Setup for system objects ==
    parser = argparse.ArgumentParser()      # Parse CLI Arguments

    # == Add Arguments for the parser to recognize ==
    # Positional Arguments
    parser.add_argument(
        'filename',
        help='Name of file which should be processed in the pipeline'
    )

    # Options
    parser.add_argument(
        '-v',
        help='Turn on the console output for LaTeX.exe',
        action='store_true'
    )

    parser.add_argument(
        '-log',
        help='Select the loglevel of this pipeline. Default: ERROR',
        choices=list(LOGGING_LEVELS.keys()),
        default=LOGGING_LEVELS['ERROR']
    )

    return parser


def main() -> None:
    """ Process of Pipeline"""
    parser = _create_parser()

    try:
        args = parser.parse_args()

        logging.basicConfig(format='[%(levelname)s] - %(message)s', level=LOGGING_LEVELS[args.log])

        verbose = bool(args.v)

        new_file_name = copy_file(args.filename)

        remove_draft_option(new_file_name)
        compile_tex_file(new_file_name, verbose=verbose)
        clean_up(new_file_name)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
