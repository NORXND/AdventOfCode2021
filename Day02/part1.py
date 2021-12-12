"""
Day 2 - Part 1
https://adventofcode.com/2021/day/2

By NORXND @ 02.12.2021
(C) NORXND 2021 - Under The MIT License
"""
# Position vars
pos = 0
depth = 0

cmds = []
input_file = open("Day2/input.txt", "r")

# Get stuff from file
for line in input_file.readlines():
    formatted_str = line.split(" ")
    cmd = {"Command": formatted_str[0], "Multiplier": int(formatted_str[1])}
    cmds.append(cmd)

# Main loop
for cmd in cmds:
    if cmd["Command"] == "forward":
        pos = pos + cmd["Multiplier"]
    elif cmd["Command"] == "down":
        depth = depth + cmd["Multiplier"]
    elif cmd["Command"] == "up":
        depth = depth - cmd["Multiplier"]

print(f"Position {pos}")
print(f"Depth {depth}")

print(f"Result: {pos*depth}")
