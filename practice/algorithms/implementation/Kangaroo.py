def kangaroo(x1, v1, x2, v2):
    while v2 < v1 and x1 <= x2:
        if x1 == x2:
            return 'YES'

        if x1 != x2:
            x1 += v1
            x2 += v2

    return 'NO'


test = [
    [0, 3, 4, 2],
    [0, 2, 5, 3]
]

for i in test:
    print(kangaroo(i[0], i[1], i[2], i[3]))
