""" pre-commit check; determines if forbidden words are about to be checked into the repo. """

from __future__ import print_function
from __future__ import unicode_literals

import argparse
import os
import sys


def find_bad(bad_words, file_obj):
    """ search a file for any bad_words
    if no bad words found return (0,'')
    if bad words found return (1,'lines locations')

    Attributes:

        bad_words(list): words not to appear in repo
        file_obj(fd): filedescriptor to search

    """
    for idx, line in enumerate(file_obj):
        bad_found = False
        msg = ''
        for word in bad_words:
            if line.find(word) >= 0:
                bad_found = True
                msg += 'Line:{0} Word:{1}\n'.format(idx, word)
    return (bad_found, msg)


def verboten_words(argv=None):
    """ entry point for the module

    ENVIRONEMNT_VARIABLES:

        VERBOTEN_FILE: pointer to file of bad_words
        F_IT: Existance of F_IT negates all checking for bad words

    returnValue of 0 -> all good/ignored, 1 -> problems
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)
    bad_words = list()

    retv = 0

    try:
        if os.environ['F_IT']:
            return retv
    except KeyError:
        pass

    v_filename = os.environ.get('VERBOTEN_FILE')

    if v_filename is not None:
        try:
            v_file = open(v_filename, 'r')
            for line in v_file:
                line = line.strip()
                if not line.startswith('#'):
                    bad_words.append(line)
            v_file.close()

        except:
            pass

    for filename in args.filenames:
        # Read as binary so we can read byte-by-byte
        with open(filename, 'r') as file_obj:
            ret_for_file, word = find_bad(bad_words, file_obj)
            if ret_for_file:
                print('File:{0} {1}'.format(filename, word))
            retv |= ret_for_file

    return retv

if __name__ == '__main__':
    sys.exit(verboten_words())
