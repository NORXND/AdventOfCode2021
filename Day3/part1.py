"""
Day 3 - Part 1
https://adventofcode.com/2021/day/3

By NORXND @ 03.12.2021
(C) NORXND 2021 - Under The MIT License
"""
input_file = open('Day3/input.txt', 'r')
binaries = []

# Get stuff from file
for line in input_file.readlines():
    binaries.append(line)

def get_rate(mode):
    number = ""

    # Get each bit (e.g. digit position in number)
    for bits in range(0, 12):
        count0 = 0
        count1 = 0

        for num in binaries:
            bit = num[bits]

            if bit == "0":
                count0 = count0 + 1
            elif bit == "1":
                count1 = count1 + 1

        if count0 > count1:
            # Check if we want gamma or epsilon
            match mode:
                case "gamma":
                    number = number + "0"
                case "epsilon":
                    number = number + "1"
        else:
            # Check if we want gamma or epsilon
            match mode:
                case "gamma":
                    number = number + "1"
                case "epsilon":
                    number = number + "0"

    return int(number, 2)

gamma = get_rate("gamma")
epsilon = get_rate("epsilon")

print(f"Gamma: {gamma}")
print(f"Epsilon: {epsilon}")

print(f"Power consumption: {gamma * epsilon}")