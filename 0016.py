#!_usr/bin/env python3
# __author__ = 'ismail'

x = str(2**1000)
sum = 0

for i in range(0, len(x)):
    sum += int(x[i])

print(sum)