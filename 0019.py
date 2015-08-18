#!/usr/bin/env python3
# __author__ = 'ismail'

import datetime

count = 0
start = '1901-01-01'
end = '2000-12-31'

d = datetime.datetime.strptime(start, '%Y-%m-%d')

while d <= datetime.datetime.strptime(end, '%Y-%m-%d'):
    if d.day is 1 and d.weekday() is 6:
        count += 1
    d += datetime.timedelta(days=1)

print(count)