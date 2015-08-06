#!/usr/bin/env python3


def isPalindrome(val):
    num = str(val)
    for i in range(0, len(num) // 2):
        if num[i] is not num[-1 - i]:
            return False
    return True

max = 0

for x in range(100, 1000)[::-1]:
    for y in range(100, 1000)[::-1]:
        product = x * y
        if product < max:
            break
        if isPalindrome(product) and max < product:
            max = product

print(max)
