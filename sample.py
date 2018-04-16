import sys
from io import StringIO


def func(n, p):
    return 0


sys.stdin = StringIO("""
""")
while 1:
    try:
        n = int(input())
        p = int(input())

        result = func(n, p)
        print(result)
    except EOFError:
        break
