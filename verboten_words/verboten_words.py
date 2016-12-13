from __future__ import print_function
from __future__ import unicode_literals

import argparse
import os
import sys


def findBad(file_obj):
    badWords = list()

    vFilename = os.environ.get('VERBOTEN_FILE')

    if vFilename is not None:
        try:
            vFile = open(vFilename, 'r')
            for line in vFile:
                line = line.strip()
                if not line.startswith('#'):
                    badWords.append(line)
            vFile.close()
        except:
            pass

    for idx, line in enumerate(file_obj):
        for word in badWords:
            if line.find(word) >= 0:
                msg = 'Line:{0} Word:{1}'.format(idx, word)
                return (1, msg)

    return (0, None)


def verboten_words(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retv = 0

    try:
        if os.environ['F_IT']:
            return retv
    except KeyError:
        pass

    for filename in args.filenames:
        # Read as binary so we can read byte-by-byte
        with open(filename, 'r') as file_obj:
            ret_for_file, word = findBad(file_obj)
            if ret_for_file:
                print('File:{0} {1}'.format(filename, word))
            retv |= ret_for_file

    return retv


if __name__ == '__main__':
    sys.exit(verboten_words())
