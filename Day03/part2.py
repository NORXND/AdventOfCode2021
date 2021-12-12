"""
Day 3 - Part 2
https://adventofcode.com/2021/day/3#part2

By NORXND @ 03.12.2021
(C) NORXND 2021 - Under The MIT License
"""
input_file = open('Day3/input.txt', 'r')
o_binaries = []
lenght = 0

# Get stuff from file
for line in input_file.readlines():
    txt = line.strip()
    lenght = len(txt)
    o_binaries.append(txt)

def get_rate(mode):
    binaries = o_binaries

    # Get each bit (e.g. digit position in number)
    for bits in range(0, lenght):
        # Part when we check which number is common
        count0 = 0
        count1 = 0

        for num in binaries:
            bit = num[bits]

            if bit == "0":
                count0 = count0 + 1
            elif bit == "1":
                count1 = count1 + 1

        if count0 > count1:
            match mode:
                case "ogr":
                    key = "0"
                case "csr":
                    key = "1"
        elif count0 == count1:
            match mode:
                case "ogr":
                    key = "1"
                case "csr":
                    key = "0"
        else:
            match mode:
                case "ogr":
                    key = "1"
                case "csr":
                    key = "0"
        
        # Part when we delete stuff
        new_binaries = []
        for num in binaries:
            if num[bits] == key:
                new_binaries.append(num)
        
        binaries = new_binaries

        if len(binaries) == 1:
            return int(binaries[0], 2)
            
    

ogr = get_rate("ogr")
csr = get_rate("csr")
result = ogr * csr

print(f"OGR: {ogr}")
print(f"OGR: {csr}")
print(f"Result: {result}")