import os
import sys
import k2kmdfile

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage : kmake.py [python source]')
        exit()
    k2kmdfile.make(sys.argv[1], True)
    