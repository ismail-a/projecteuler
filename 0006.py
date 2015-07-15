#!/usr/bin/env python3
# __author__ = 'ismail'

"""
Algorithm
(x1 + x2 + ... xn)^2 = (x1^2 + x2^2 + ... + xn^2) + 2(x1x2 + x1x3 + ... xn-1 * xn) <- all the combination among x1 to xn
So,
(1 + 2 + ... + 100)^2 - (1^2 + 2^2 + ... 100^2) = 2(1*2 + 1*3 + ... + 99*100)
"""

sum = 0
n = 100

for i in range(1, n):
    for j in range(i + 1, n + 1):
        sum += 2 * i * j

print('Answer: ' + str(sum))