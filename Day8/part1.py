"""
Day 8 - Part 1
https://adventofcode.com/2021/day/8

By NORXND @ 08.12.2021
(C) NORXND 2021 - Under The MIT License
"""

input_file = open('Day8/input.txt', 'r')

entries = []

for entry in input_file.readlines():
    entry = entry.strip().split(" | ")
    patterns = entry[0].split(" ")
    output = entry[1].split(" ")

    entries.append({
        "Patterns": patterns,
        "Output": output,
    })

segments = {
    1: 2,
    4: 4,
    7: 3,
    8: 7,
}

matches = []
for entry in entries:
    for output in entry["Output"]:
        if len(output) in segments.values():
            matches.append(output)

print(len(matches))