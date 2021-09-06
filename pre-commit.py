#!/usr/bin/python
"""  
     Pre-Commit git hook
"""
__version__ = '0.1'

import sys


def main(lines):
    print("Hook running!")
    for line in lines:
        print(line)

if __name__ == '__main__':
    main(sys.stdin)
    sys.exit(0)

