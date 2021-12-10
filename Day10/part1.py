"""
Day 10 - Part 1
https://adventofcode.com/2021/day/10

By NORXND @ 10.12.2021
(C) NORXND 2021 - Under The MIT License
"""

input_file = open('Day10/input.txt', 'r')

opening_chars = ["(", "[", "{", "<"]
closing_chars = [")", "]", "}", ">"]

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

lines = []
for linei, line in enumerate(input_file):
    text = []
    for chari, char in enumerate(line):
        text.append(char)
    lines.append(text)

illegal_closings = {}

for line in lines:
    def check():
        stack = []
        for char in line:
            if char in opening_chars:
                stack.append(char)
            elif char in closing_chars:
                pos = closing_chars.index(char)
                if opening_chars[pos] == stack[-1]:
                    stack.pop(-1)
                else:
                    print(f"Expected {closing_chars[opening_chars.index(stack[-1])]} but found {char}")
                    return char
        if len(stack) == 0:
            return True
        else:
            return False
    
    result = check()
    print(result)
    if result != True and result != False:
        s = illegal_closings.get(result)
        if s == None:        
            illegal_closings[result] = points[result]
        else:
            illegal_closings[result] = s + points[result]

print(illegal_closings)
print(sum(illegal_closings.values()))