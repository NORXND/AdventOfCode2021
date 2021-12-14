"""
Day 14 - Part 1
https://adventofcode.com/2021/day/14

By NORXND @ 14.12.2021
(C) NORXND 2021 - Under The MIT License
"""
input_file = open("Day14/input.txt", "r")
input_segments = input_file.read().split("\n\n")

template = input_segments[0]
rules = {}

for raw_rule in input_segments[1].splitlines():
    rule = raw_rule.split(" -> ")
    rules[rule[0]] = rule[1]


new_template = template
for step in range(10):
    for i, char in enumerate(template):
        # If last
        if i+1 >= len(template):
                continue
    
        rule = char + template[i+1]
        if rule in rules:
            to_insert = rules[rule].lower()
            start = new_template.find(rule)
            end = (start + 2)
            new_template = new_template[:start+1] + to_insert + new_template[end-1:]
    template = new_template.upper()
    new_template = template

chars = {}

for char in template:
    if char in chars:
        chars[char] = chars[char] + 1
    else:
        chars[char] = 1

print(max(chars.values())-min(chars.values()))