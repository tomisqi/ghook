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

def check(gitdiff, nocommitStr):
    success = True
    
    findex = gitdiff.find(nocommitStr)
    if (findex >= 0):
        # We found something, print the line and return error.
        (startIdx, endIdx) = (gitdiff.rfind('\n', 0, findex) + 1, gitdiff.find('\n', findex, -1))
        print(nocommitStr + " found: " + gitdiff[startIdx:endIdx])
        success = False

    return success

def main():
    cmd = "git diff --staged"    
    cmdres = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
    stdout = cmdres.stdout
    gitdiff = stdout.decode('UTF-8') # stdout is returned as bytes but we want a string.

    success = check(gitdiff, NO_COMMIT_STR)

    resultStr = "Pass" if success else "Fail"
    print("Pre-Commit hook check..." + resultStr + ".")
    if (not success):
        sys.exit(1)
    sys.exit(0)
    
if __name__ == '__main__':
    main()

