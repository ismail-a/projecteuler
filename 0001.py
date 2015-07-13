#!/usr/bin/env python3

sum = 0
for num in range(1, 1000):
    if num % 3 == 0 or num % 5 == 0:
        sum += num
print('Sum of FizzBuzz from 1 to 999: ' + str(sum))
