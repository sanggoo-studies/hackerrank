import sys
from io import StringIO
from math import floor


def sockMerchant(n, ar):
    socks = {}
    pairs = 0
    for i in ar:
        if i in socks:
            socks[i] += 0.5
        else:
            socks[i] = 0.5

    for i in socks:
        pairs += floor(socks[i])

    return pairs


sys.stdin = StringIO('9\n'
                     '10 20 20 10 10 30 50 10 20\n')
while 1:
    try:
        n = int(input().strip())
        ar = list(map(int, input().strip().split(' ')))
        result = sockMerchant(n, ar)
        print(result)
    except EOFError:
        break
