#!/bin/python3

import sys
from io import StringIO


def pageCount(n, p):
    left = p // 2
    right = ((n if n % 2 == 1 else n + 1) - p) // 2

    return left if left < right else right


sys.stdin = StringIO('6\n'
                     '2\n'
                     '5\n'
                     '4\n'
                     '7\n'
                     '7\n'
                     '8\n'
                     '7\n')
while 1:
    try:
        n = int(input())
        p = int(input())

        result = pageCount(n, p)
        print(result)
    except EOFError:
        break
