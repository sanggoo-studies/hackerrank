from functools import reduce


def GCD(a, b):
    while a != 0:
        temp = b % a
        b = a
        a = temp
    return abs(b)


def LCM(arr):
    return reduce(lambda x, y: int(x * y / GCD(x, y)), arr)


def getTotalX(a, b):
    current = lcm = LCM(a)
    minimum = min(b)
    count = 0
    while current <= minimum:
        if all([x % current == 0 for x in b]):
            count += 1
        current += lcm
    return count


test = [
    [[2, 4], [16, 32, 96]],
    [[2, 4], [8, 16, 24]],
    [[2, 4, 16], [32, 96]]
]

for t in test:
    print(getTotalX(t[0], t[1]))
