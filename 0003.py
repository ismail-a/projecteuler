#!/usr/bin/env python3

x = 600851475143
prime_list = []
prime = 2

while prime <= x:
    while x % prime is 0:
        prime_list.append(prime)
        x //= prime
    prime += 1

# print(prime_list)
print('The largest prime factor of the number ' +
      x + ': ' + str(prime_list[-1]))
