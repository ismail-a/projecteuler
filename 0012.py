#!_usr/bin/env python3
# __author__ = 'ismail'

n = 3
dn = 2
cnt = 0
n1 = dn1 = i = exponent = 0
p = 1000
primeArray = range(1,p)

while cnt <= 500:
    n += 1
    n1 = n
    if n1 % 2 is 0:
        n1 //= 2
    dn1 = 1
    for i in range(1, p + 1):
        if primeArray[i] * primeArray[i] > n1:
            dn1 = 2 * dn1
            break
        exponent = 1
        while n1 % primeArray[i] is 0:
            exponent += 1
            n1 //= primeArray[i]
        if exponent > 1:
            dn1 *= exponent
        if n1 is 1:
            break
    cnt = dn * dn1
    dn = dn1

print n * (n - 1) // 2