"""
Day 9 - Part 1
https://adventofcode.com/2021/day/9

By NORXND @ 09.12.2021
(C) NORXND 2021 - Under The MIT License
"""

input_file = open('Day9/input.txt', 'r')

rows = []

for entry in input_file.readlines():
    l = []

    for char in entry.strip():
        l.append(int(char))

    rows.append(l)

lowest = []

for i, row in enumerate(rows):
    def _check(x, y):
        if y > x:
            return True
        else:
            return False
    
    def check_right(vi, v):        
        try:
            nv = row[vi+1]
        except IndexError:
            return True
        return _check(v, nv)

    def check_left(vi, v):
        if vi == 0:
            return True
        
        nv = row[vi-1]
        return _check(v, nv)

    def check_up(vi, v):
        try:
            nv = rows[i+1][vi]
        except IndexError:
            return True
        return _check(v, nv)

    def check_down(vi, v):
        if i == 0:
            return True
        
        nv = rows[i-1][vi]
        return _check(v, nv)

    for coli, col in enumerate(row):
        if check_down(coli, col) and check_up(coli, col) and check_left(coli, col) and check_right(coli, col):
            lowest.append(col+1)

print(lowest)
print(sum(lowest))