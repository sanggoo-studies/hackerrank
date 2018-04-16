def solve(n, s, d, m):
    count = 0
    for i in range(n - m + 1):
        if sum(s[i:i+m]) == d:
            count += 1
    return count


test = [
    [5, [1, 2, 1, 3, 2], 3, 2],
    [6, [1, 1, 1, 1, 1, 1], 3, 2],
    [1, [4], 4, 1]
]
for t in test:
    print(solve(t[0], t[1], t[2], t[3]))