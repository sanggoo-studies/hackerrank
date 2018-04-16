import sys
from io import StringIO


def climbingLeaderboard(scores, alice):
    S = sorted(list(set(scores)), reverse=True)
    rankings = []
    ranking = len(S) - 1

    for a in range(len(alice)):
        if alice[a] < S[ranking]:
            rankings.append(ranking + 2)
            continue
        elif S[ranking - 1] <= alice[a]:
            while ranking > 0 and S[ranking - 1] <= alice[a]:
                ranking -= 1
        rankings.append(ranking + 1)

    return rankings


sys.stdin = StringIO("""7
100 100 50 40 40 20 10
4
5 25 50 120
""")
while 1:
    try:
        scores_count = int(input())

        scores = list(map(int, input().rstrip().split()))

        alice_count = int(input())

        alice = list(map(int, input().rstrip().split()))

        result = climbingLeaderboard(scores, alice)

        print('\n'.join(map(str, result)))
        print('\n')
    except EOFError:
        break
