#!/usr/bin/env python3
# __author__ = 'ismail'

import csv


def scoring(name, position):
    score = 0
    for letter in name:
        score += ord(letter)
    score -= len(name) * (ord('A') - 1)
    return score * position

filename = 'p022_names.txt'
score = 0

with open(filename, 'rb') as f:
    reader = csv.reader(f)
    for names in reader:
        names.sort()
        for i in range(len(names)):
            score += scoring(names[i], i + 1)

print(score)
