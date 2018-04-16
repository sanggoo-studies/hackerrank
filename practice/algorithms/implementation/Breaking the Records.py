def breakingRecords(score):
    lowest = None
    highest = None
    lowestCount = 0
    highestCount = 0

    for i in score:
        if lowest is None:
            lowest = i
        elif i < lowest:
            lowest = i
            lowestCount += 1

    for i in score:
        if highest is None:
            highest = i
        elif i > highest:
            highest = i
            highestCount += 1

    return [highestCount, lowestCount]


test = [
    [10, 5, 20, 20, 4, 5, 2, 25, 1],
    [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
]

for t in test:
    print(breakingRecords(t))