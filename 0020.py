#!/usr/bin/env python3
__author__ = 'ismail'

import math

n = 100
sum = 0

fact = math.factorial(n)
while fact > 0:
    sum += fact % 10
    fact //= 10
print (sum)