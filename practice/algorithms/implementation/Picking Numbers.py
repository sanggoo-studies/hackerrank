import sys
from collections import Counter
from functools import reduce
from io import StringIO


def pickingNumbers(a):
    # ans = 0
    # a.sort()
    # for i in range(len(a)):
    #     for j in range(i + 1, len(a)):
    #         if abs(a[j] - a[i]) <= 1:
    #             ans = max(ans, j - i + 1)

    # A = [0] * 100
    # for i in a:
    #     A[i] += 1
    A = Counter(a)

    # for i in range(99):
    #     ans = max(ans, A[i] + A[i + 1])
    return reduce(lambda y, x: max(A[x] + A[x + 1], y), range(max(A.keys()) - 1), -1)

    # return ans


sys.stdin = StringIO("""6
4 6 5 3 3 1
6
1 2 2 3 1 2
98
7 12 13 19 17 7 3 18 9 18 13 12 3 13 7 9 18 9 18 9 13 18 13 13 18 18 17 17 13 3 12 13 19 17 19 12 18 13 7 3 3 12 7 13 7 3 17 9 13 13 13 12 18 18 9 7 19 17 13 18 19 9 18 18 18 19 17 7 12 3 13 19 12 3 9 17 13 19 12 18 13 18 18 18 17 13 3 18 19 7 12 9 18 3 13 13 9 7
""")
while 1:
    try:
        n = int(input().strip())
        a = list(map(int, input().strip().split(' ')))
        result = pickingNumbers(a)
        print(result)
    except EOFError:
        break
