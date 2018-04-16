#!/bin/python3

import sys


def migratoryBirds(n, ar):
    count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    maximum = 1
    for i in range(n):
        count[ar[i]] += 1

        if count[ar[i]] >= count[maximum]:
            maximum = ar[i]

    return maximum


sys.stdin = open('MigratoryBirds.txt')
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
