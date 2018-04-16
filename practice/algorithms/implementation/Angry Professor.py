import sys
from io import StringIO


def angryProfessor(k, a):
    return 'NO' if len(list(filter(lambda x: x <= 0, a))) >= k else 'YES'


sys.stdin = StringIO("""2
4 3
-1 -3 4 2
4 2
0 -1 2 1
""")
while 1:
    try:
        t = int(input().strip())
        for a0 in range(t):
            n, k = input().strip().split(' ')
            n, k = [int(n), int(k)]
            a = list(map(int, input().strip().split(' ')))
            result = angryProfessor(k, a)
            print(result)
    except EOFError:
        break
