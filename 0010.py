#!/usr/bin/env python3
# __author__ = 'ismail'

import math

limit = 2000000
sieveBound = (limit - 1) / 2
sieve = [False] * sieveBound
crossLimit = int((math.sqrt(limit) - 1) / 2)
for i in range(1, crossLimit):
    if not sieve[i]:
        for j in range(2 * i * (i + 1), sieveBound, 2 * i + 1):
            sieve[j] = True
sum = 2
for i in range(1, sieveBound):
    if not sieve[i]:
        sum += 2 * i + 1

print('The sum of all the primes below ' + str(limit) + ': ' + str(sum))