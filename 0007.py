#!/usr/bin/env python3
# __author__ = 'ismail'

import math

def isPrime(num):
    if num is 1:
        return False
    elif num < 4:
        return True
    elif num % 2 is 0:
        return False
    elif num < 9:
        return True
    elif num % 3 is 0:
        return False
    else:
        r = int(math.sqrt(num))
        f = 5
        while f <= r:
            if num % f is 0:
                return False
            if num % (f + 2) is 0:
                return False
            f += 6
        return True

n = 10001
count = 1
candidate = 1

while count < n:
    candidate += 2
    if isPrime(candidate):
        count += 1

print('The 10001st prime number:' + str(candidate))