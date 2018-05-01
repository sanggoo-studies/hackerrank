import sys
from io import StringIO


def beautifulDays(i, j, k):
    count = 0
    for n in range(i, j + 1):
        if abs(n - int(str(n)[::-1])) % k == 0:
            count += 1

    sum([1 for day in range(i, j + 1) if (day - int(str(day)[::-1])) % k == 0])
    return count


sys.stdin = StringIO("""20 23 6
""")
while 1:
    try:
        i, j, k = input().strip().split(' ')
        i, j, k = [int(i), int(j), int(k)]
        result = beautifulDays(i, j, k)
        print(result)
    except EOFError:
        break
