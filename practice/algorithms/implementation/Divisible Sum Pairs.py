def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            count += 1 if (ar[i] + ar[j]) % k == 0 else 0
    return count


test = [
    [6, 3, [1, 3, 2, 6, 1, 2]]
]
for t in test:
    print(divisibleSumPairs(t[0], t[1], t[2]))