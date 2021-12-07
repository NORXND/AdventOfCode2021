"""
Day 7 - Part 1
https://adventofcode.com/2021/day/7

By NORXND @ 07.12.2021
(C) NORXND 2021 - Under The MIT License
"""

input_file = open('Day7/input.txt', 'r')
crab_positions = []

l = input_file.read().split(",")

for x in l:
    crab_positions.append(int(x))


fuel_cost = {}
for dest in range(0, max(crab_positions)+1):
    sum = 0

    for cpos in crab_positions:
        diff = abs(cpos - dest)
        sum = sum + diff
    
    fuel_cost[dest] = sum

index = min(zip(fuel_cost.values(), fuel_cost.keys()))[1]
print(index)
print(fuel_cost[index])