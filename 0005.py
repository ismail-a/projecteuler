#!/usr/bin/env python3
# __author__ = 'ismail'

import math

p = [1, 2, 3, 5, 7, 11, 13, 17, 19]
a = [1] * len(p)
k = 20
N = 1
i = 1
for i in range(1, len(p)):
    if p[i] < math.sqrt(k):
        a[i] = int(math.log(k, 2) / math.log(p[i], 2))
    N *= p[i] ** a[i]

print('The smallest positive number that is evenly divisible ' +
      'by all of the numbers from 1 to ' + k + ': ' + str(N))
