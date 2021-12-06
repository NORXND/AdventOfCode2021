"""
Day 1 - Part 1
https://adventofcode.com/2021/day/1

By NORXND @ 02.12.2021
(C) NORXND 2021 - Under The MIT License
"""
input_data = []
increase_counter = 0
last = None  # Cache

input_file = open("Day1/input.txt", "r")

# Get stuff from file
for line in input_file.readlines():
    number = int(line)
    input_data.append(number)


# Main loop
for num in input_data:
    # If this is first element
    if last is None:
        print(f"{num} - N/A")
        last = num
        continue

    # Number is larger than previous
    if num > last:
        print(f"{num} - Increased")
        increase_counter += 1
    # Number is smaller
    elif num < last:
        print(f"{num} - Decreased")

    last = num

print(f"Increased {increase_counter} times!")
