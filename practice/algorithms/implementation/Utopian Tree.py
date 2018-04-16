import sys
from io import StringIO


def utopianTree(n):
    height = 1
    for i in range(n):
        if i % 2 == 0:
            height *= 2
        else:
            height += 1

    return height


sys.stdin = StringIO("""3
0
1
4
""")
while 1:
    try:
        t = int(input().strip())
        for a0 in range(t):
            n = int(input().strip())
            result = utopianTree(n)
            print(result)
    except EOFError:
        break
