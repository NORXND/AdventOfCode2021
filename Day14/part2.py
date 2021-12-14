"""
Day 14 - Part 2
https://adventofcode.com/2021/day/14#part2

By NORXND @ 14.12.2021
(C) NORXND 2021 - Under The MIT License
"""
import math

input_file = open("Day14/input.txt", "r")
input_segments = input_file.read().split("\n\n")

template = input_segments[0]
rules = {}
connections = {}
bases = {}

for raw_rule in input_segments[1].splitlines():
    rule = raw_rule.split(" -> ")
    rules[rule[0]] = rule[1]

# Make base
for i, char in enumerate(template):
        # If last
        if i+1 >= len(template):
                continue
    
        rule = char + template[i+1]
        if rule in rules:
            if rule in bases:
                bases[rule] = bases[rule] + 1
            else:
                bases[rule] = 1

# Make transforms
for rule in rules:
    conns = []
    v = rules[rule]
    result = rule[:1] + v + rule[1:]
    for r2 in rules:
        if r2 in result:
            conns.append(r2)
    connections[rule] = conns


for step in range(40):
    new_bases = {}
    for base in bases:
        for conn in connections[base]:
            if conn in new_bases:
                new_bases[conn] = new_bases[conn] + bases[base]
            else:
                new_bases[conn] = bases[base]
    bases = new_bases

chars = {}
for base in bases:
    for char in base:
        if char in chars:
            chars[char] = chars[char] + bases[base]
        else:
            chars[char] = bases[base]
for char in chars:
    chars[char] = int(math.ceil(chars[char] /2))

print(max(chars.values())-min(chars.values()))