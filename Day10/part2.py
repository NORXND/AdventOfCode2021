"""
Day 10 - Part 2
https://adventofcode.com/2021/day/10#part2

By NORXND @ 10.12.2021
(C) NORXND 2021 - Under The MIT License
"""

input_file = open('Day10/input.txt', 'r')

opening_chars = ["(", "[", "{", "<"]
closing_chars = [")", "]", "}", ">"]

points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

lines = []
for linei, line in enumerate(input_file):
    text = []
    for chari, char in enumerate(line):
        text.append(char)
    lines.append(text)

missing_closings = []

for line in lines:
    def check():
        stack = []
        missing = []
        for char in line:
            if char in opening_chars:
                stack.append(char)
            elif char in closing_chars:
                pos = closing_chars.index(char)
                if opening_chars[pos] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            for x in stack:
                pos = opening_chars.index(x)
                missing.append(closing_chars[pos])
            missing.reverse()
            return missing
    
    results = check()
    if results != True and results != False:
        score = 0
        for result in results:
            score = (score * 5) + points[result]
        missing_closings.append(score)
        
        

missing_closings.sort()
i = int(len(missing_closings) / 2)
print(missing_closings[i])