#!/usr/bin/env python3
# __author__ = 'ismail'

import math


def d(n):
    dn = 1
    t = math.sqrt(n)
    for j in range(2, int(t) + 1):
        if n % j == 0:
            dn += j + n // j
    if t is int(t):
        dn -= t
    return dn

num, sum = 10000, 0

for i in range(2, num):
    da = d(i)
    if da > i and d(da) == i:
        sum += da + i
    # print('i: ' + str(i)+ ', da: ' + str(da) + ', dda: ' + str(d(da)))

print(sum)