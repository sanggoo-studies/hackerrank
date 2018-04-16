import sys
from io import StringIO


def hurdleRace(k, height):
    top = 0
    for h in height:
        top = max(top, h)
    return 0 if top <= k else top - k


sys.stdin = StringIO("""5 4
1 6 3 5 2
5 7
2 5 4 5 2
""")
while 1:
    try:
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        height = list(map(int, input().strip().split(' ')))
        result = hurdleRace(k, height)
        print(result)
    except EOFError:
        break
