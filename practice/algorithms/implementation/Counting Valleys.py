#!/bin/python3

import sys
from io import StringIO


def countingValleys(n, s):
    level = 0
    before = 0
    valleys = 0

    for note in s:
        level += 1 if note == 'U' else -1
        if level == 0 and before < 0:
            valleys += 1
        before = level

    return valleys


sys.stdin = StringIO("""8
UDDDUDUU
16
UDDDUDUUUDDDUDUU
""")

while 1:
    try:
        n = int(input().strip())
        s = input().strip()
        result = countingValleys(n, s)
        print(result)
    except EOFError:
        break
