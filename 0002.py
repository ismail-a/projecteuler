#!/usr/bin/env python3

x = 1
y = 1
sum = 0
while y < 4000000:
    #print('Fibonacci value: ' + str(y))
    if y % 2 is 0:
        sum += y
    temp = y
    y += x
    x = temp

print('Sum of even fibonacci value below 4000000: ' + str(sum))
