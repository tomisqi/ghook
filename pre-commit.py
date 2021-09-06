#!/usr/bin/python3
"""  
     Pre-Commit git hook

     TODO:
     [ ] Print error with color
     [ ] Print filename

"""
__version__ = '0.1'

import sys
import subprocess

NO_COMMIT_STR = "@nocommit"

def main():
    print("Pre-Commit hook check...")

    cmd = "git diff --staged"    
    cmdres = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
    stdout = cmdres.stdout
    gitdiff = stdout.decode('UTF-8') # stdout is returned as bytes but we want a string.
    
    findex = gitdiff.find(NO_COMMIT_STR)
    if (findex >= 0):
        # We found something, print the line and exit with error.
        (startIdx, endIdx) = (gitdiff.rfind('\n', 0, findex) + 1, gitdiff.find('\n', findex, -1))
        print(NO_COMMIT_STR + " found: " + gitdiff[startIdx:endIdx])
        sys.exit(1)
    
    
if __name__ == '__main__':
    main()
    sys.exit(0)

