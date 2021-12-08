"""
Day 8 - Part 2
https://adventofcode.com/2021/day/8#part2

By NORXND @ 07.12.2021
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

numlen = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
}

class Entry:
    # y - source
    def matches(self, x: str, y: str):
        for char in y:
            if char not in x:
                return False
        return True

    # y - source
    def how_many_not_matches(self, x: str, y: str):
        sum = 0
        for char in y:
            if char not in x:
                sum = sum + 1
        return sum

    def check_known(self):
        for i in self.pattern:
            def _check():
                for x in numlen:
                    if len(i) == x:
                        self.decoded[i] = numlen[x]
                        self.numbers[numlen[x]] = i
                        return True
                return False
            found = _check()

            if not found:
                self.not_found.append(i)
    
    def check_6_digit(self):
        for i in self.not_found.copy():
            number = None
            if len(i) == 6:
                # If has 1 then 9/0
                if self.matches(i, self.numbers[1]):
                    if self.matches(i, self.numbers[4]):
                        number = 9
                    else:
                        number = 0
                else:
                    number = 6
            
                self.decoded[i] = number
                self.numbers[number] = i
                self.not_found.remove(i)
                
    def check_5_digit(self):
        for i in self.not_found.copy():
            number = None
            if len(i) == 5:
                # If has 1 then 3
                if self.matches(i, self.numbers[1]):
                    number = 3
                else:
                    if self.how_many_not_matches(i, self.numbers[4]) == 1:
                        number = 5
                    else:
                        number = 2
                self.decoded[i] = number
                self.numbers[number] = i
                self.not_found.remove(i)

    def decode_output(self):
        result = ""
        for o in self.output:
            for num in self.decoded:
                if len(o) == len(num) and self.matches(o, num):
                    result = result + str(self.decoded[num])
        return result


    def __init__(self, pattern, output):
        self.pattern = pattern
        self.output = output
        self.decoded = {}
        self.numbers = {}
        self.not_found = []

        self.check_known()
        self.check_6_digit()
        self.check_5_digit()

sum = 0
for entry in entries:
    entry = Entry(entry["Patterns"], entry["Output"])
    sum = sum + int(entry.decode_output())

print(sum)