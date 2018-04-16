

def countApplesAndOranges(s, t, a, b, apples, oranges):
    inApple = 0
    inOrange = 0

    for i in apples:
        if s <= a + i <= t:
            inApple += 1

    for i in oranges:
        if s <= b + i <= t:
            inOrange += 1

    print(inApple, ' ', inOrange)
    # print(inOrange)

countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])

