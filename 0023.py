#!/usr/bin/env python3
# __author__ = 'ismail'

import math


def d(n):
    dn = 1
    t = math.sqrt(n)
    for j in range(2, int(t) + 1):
        if n % j == 0:
            dn += j + n // j
    if t == int(t):
        dn -= t
    return dn

n = 28123
abundant = []
two_abundant = [False] * n
sum = 0

for i in range(1, n):
    if i < d(i):
        abundant.append(i)

for i in abundant:
    for j in abundant:
        if i + j >= n:
            break
        if two_abundant[i + j] is False:
            two_abundant[i + j] = True

for i in range(n):
    if two_abundant[i] is False:
        sum += i

print(sum)