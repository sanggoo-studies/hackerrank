#!/bin/python3

import sys
from io import StringIO


def catAndMouse(x, y, z):
    disCatA = abs(x - z)
    disCatB = abs(y - z)

    return 'Mouse C' if disCatA == disCatB else ('Cat A' if disCatA < disCatB else 'Cat B')


sys.stdin = StringIO("""1 2 3
1 3 2
""")
while 1:
    try:
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)
        print(result)
    except EOFError:
        break
