#!/usr/bin/env python3
# __author__ = 'ismail'

n = 1000

for a in range(3, (n - 3) // 3):
    for b in range(a + 1, (n - 1 - a) // 2):
        c = n - a - b
        if a**2 + b**2 == c**2:
            print('abc: ' + str(a * b * c))
