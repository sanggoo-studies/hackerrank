#!/bin/python3

import sys
from io import StringIO


def getMoneySpent(keyboards, drives, b):
    price = -1
    for k in keyboards:
        for d in drives:
            if price < k + d <= b:
                price = k + d
    return price


sys.stdin = StringIO("""10 2 3
3 1
5 2 8
5 1 1
4
5
""")
while 1:
    try:
        bnm = input().split()

        b = int(bnm[0])

        n = int(bnm[1])

        m = int(bnm[2])

        keyboards = list(map(int, input().rstrip().split()))

        drives = list(map(int, input().rstrip().split()))

        #
        # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
        #

        moneySpent = getMoneySpent(keyboards, drives, b)
        print(moneySpent)
    except EOFError:
        break
