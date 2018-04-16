import sys
from io import StringIO
from itertools import permutations


def formingMagicSquare(s):
    cost = 81
    x = []

    for i in s:
        x.extend(i)

    # 매직스퀘어 갯수는 정해져있다
    squares = [
        (2, 7, 6, 9, 5, 1, 4, 3, 8),
        (2, 9, 4, 7, 5, 3, 6, 1, 8),
        (4, 3, 8, 9, 5, 1, 2, 7, 6),
        (4, 9, 2, 3, 5, 7, 8, 1, 6),
        (6, 1, 8, 7, 5, 3, 2, 9, 4),
        (6, 7, 2, 1, 5, 9, 8, 3, 4),
        (8, 1, 6, 3, 5, 7, 4, 9, 2),
        (8, 3, 4, 1, 5, 9, 6, 7, 2)
    ]
    for P in squares: # permutations(range(1, 10)):
        # if sum(P[0:3]) == 15 and sum(P[3:6]) == 15 and sum(P[0::3]) == 15 and sum(P[1::3]) == 15 and sum(P[0::4]) == 15 and sum(P[2:7:2]) == 15:
            cost = min(cost, sum(abs(P[i] - x[i]) for i in range(0, 9)))
    return cost


sys.stdin = StringIO("""4 9 2
3 5 7
8 1 5
4 8 2
4 5 7
6 1 6
1 1 1
1 1 1
1 1 1
""")
while 1:
    try:
        s = []
        for s_i in range(3):
            s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
            s.append(s_t)

        result = formingMagicSquare(s)
        print(result)
    except EOFError:
        break
