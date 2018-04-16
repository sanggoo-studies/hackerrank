import sys
from functools import reduce
from io import StringIO


def Appetit(n, noteat, items, charged):
    anna_price = 0
    for i in range(n):
        if i != noteat:
            anna_price += items[i]

    anna_price /= 2

    return 'Bon Appetit' if charged - anna_price == 0 else int(charged - anna_price)


sys.stdin = StringIO('4 1\n'
                     '3 10 2 9\n'
                     '12\n'
                     '4 1\n'
                     '3 10 2 9\n'
                     '7\n')


while 1:
    try:
        st = input().split()
        n = int(st[0])
        noteat = int(st[1])
        items = list(map(int, input().split()) )
        charged = int(input().strip())
        print(Appetit(n, noteat, items, charged))
    except EOFError:
        break




