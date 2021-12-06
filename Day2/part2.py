"""
Day 2 - Part 2
https://adventofcode.com/2021/day/2#part2

By NORXND @ 02.12.2021
(C) NORXND 2021 - Under The MIT License
"""
# Position vars
pos = 0
depth = 0
aim = 0

cmds = []
input_file = open("Day2/input.txt", "r")

# Get stuff from file
for line in input_file.readlines():
    formatted_str = line.split(" ")
    cmd = {"Command": formatted_str[0], "Multiplier": int(formatted_str[1])}
    cmds.append(cmd)

# Main loop
for cmd in cmds:
    # Forward command
    if cmd["Command"] == "forward":
        pos = pos + cmd["Multiplier"]
        depth = depth + (aim * cmd["Multiplier"])
    # Down command
    elif cmd["Command"] == "down":
        aim = aim + cmd["Multiplier"]
    # Up command
    elif cmd["Command"] == "up":
        aim = aim - cmd["Multiplier"]

print(f"Position {pos}")
print(f"Depth {depth}")

print(f"Result: {pos*depth}")
