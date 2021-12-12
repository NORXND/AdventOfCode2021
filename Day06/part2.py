"""
Day 6 - Part 2
https://adventofcode.com/2021/day/6#part2

By NORXND @ 06.12.2021
(C) NORXND 2021 - Under The MIT License
"""
import time

input_file = open("Day6/input.txt", "r")

fishes_template = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

fishes = fishes_template.copy()

l = input_file.read().split(",")
for x in l:
    fishes[int(x)] = fishes[int(x)] + 1

print(f"Initial -> {fishes}")

start = time.perf_counter()
for day_num in range(1, 257):
    new_fishes = fishes_template.copy()
    for i in fishes:
        if i == 0:
            goto = 6
            add_new = True
        else:
            goto = i - 1
            add_new = False

        num = fishes[i]

        new_fishes[goto] = new_fishes[goto] + num
        if add_new:
            new_fishes[8] = new_fishes[8] + num
    fishes = new_fishes
    print(f"Day {day_num} -> {fishes}")

sum = 0
for x in fishes:
    sum = sum + fishes[x]

print(sum)
print(f"Completed Execution in {time.perf_counter() - start} seconds")
