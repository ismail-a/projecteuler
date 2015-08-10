#!/usr/bin/env python3
# __author__ = 'ismail'


def countCollatz(n):
    count = 1
    while n is not 1:
        if n % 2 is 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count

n = 1000000
max = 1
index = 1

for i in range(1, n, 3):
    count = countCollatz(i)
    if count > max:
        max = count
        index = i
    # print(str(i) + ': ' + str(count) + ', max: ' + str(max) + ' at ' + str(index))

print(index)