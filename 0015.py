#!/usr/bin/env python3
# __author__ = 'ismail'

n = 20
grid = [[1] * (n + 1)] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

print(grid[n][n])
