"""
Day 6 - Part 1
https://adventofcode.com/2021/day/6

By NORXND @ 06.12.2021
(C) NORXND 2021 - Under The MIT License
"""
import time

input_file = open('Day6/input.txt', 'r')

l = input_file.read().split(",")
init = []
for x in l:
    fish = int(x)
    init.append(fish)

day_list = init

del init
del l

start = time.perf_counter()
for d in range(1, 81):
    for i, fish in enumerate(day_list.copy()):
        if fish == 0:
            day_list[i] = 6
            day_list.append(8)
        else:
            day_list[i] = fish - 1

    print(f"Day {d} -> {len(day_list)}")

print(len(day_list))
print(f"Completed Execution in {time.perf_counter() - start} seconds")