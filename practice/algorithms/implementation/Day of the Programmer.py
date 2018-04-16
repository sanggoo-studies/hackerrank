#!/bin/python3
import sys
from io import StringIO


def solve(year):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year == 1918:
        months[1] -= 13
    elif (year < 1918 and year % 4 == 0) or \
            (year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))):
        months[1] = 29

    month = 0
    day = None
    days = 256
    while days:
        if days > months[month]:
            days -= months[month]
            month += 1
        else:
            day = days
            days = 0

    return '{:02}.{:02}.{:}'.format(day, month+1, year)


sys.stdin = StringIO('2017\n'
                     '1918\n'
                     '1900\n'
                     '2000\n'
                     '1800\n')
while 1:
    try:
        year = int(input().strip())
        result = solve(year)
        print(result)
    except EOFError:
        break
