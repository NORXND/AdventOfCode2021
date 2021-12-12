"""
Day 7 - Part 2
https://adventofcode.com/2021/day/7#part2

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
    print(dest)
    for cpos in crab_positions:
        diff = abs(cpos - dest)
        cost_fuel = 0
        for i in range(1, diff+1):
            cost_fuel = cost_fuel + i

        sum = sum + cost_fuel
    
    fuel_cost[dest] = sum

index = min(zip(fuel_cost.values(), fuel_cost.keys()))[1]
print(index)
print(fuel_cost[index])