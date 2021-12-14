"""
Day 13 - Part 2
https://adventofcode.com/2021/day/13#part2

By NORXND @ 14.12.2021
(C) NORXND 2021 - Under The MIT License
"""
import typing

"""

Input prepare

"""

input_file = open("Day13/input.txt", "r")
_input_segments = input_file.read().split("\n\n")

x_fold_template = "fold along x"
y_fold_template = "fold along y"
full_sign_template = "█"
empty_sign_template = " "

positions =  []
folds: typing.List[typing.Dict[typing.Literal["Type", "Value"], typing.Union[int, str]]] = []

for line in _input_segments[0].splitlines():
    pos = line.split(",")
    positions.append({"X": int(pos[0]), "Y": int(pos[1])})

for line in _input_segments[1].splitlines():
    pos = line.split("=")
    if pos[0] == x_fold_template:
        folds.append({"Type": "X", "Value": int(pos[1])})
    else:
        folds.append({"Type": "Y", "Value": int(pos[1])})

maxX = 0
maxY = 0
for position in positions:
    if position["X"] > maxX:
        maxX = position["X"]

    if position["Y"] > maxY:
        maxY = position["Y"]

"""

Parse data and helpers

"""

class Point:
    def __init__(self, value: str, x: int, y: int):
        self.value: str = value
        self.x: int = x
        self.y: int = y
    
    def __repr__(self):
        return f"{self.value}"

    def __str__(self):
        return f"{self.value}"

Table = typing.List[typing.List[Point]]
Row = typing.List[Point]

def create_new_table(x: int, y: int) -> Table:
    new_table = []
    for rowI in range(0, y):
        col = []
        for colI in range(0, x):
            col.append(Point(empty_sign_template, colI, rowI))
        new_table.append(col)
    
    return new_table

def copy_table(table: Table) -> Table:
    lenX = len(table[0]) # It needs to have at least 1 element
    new = create_new_table(lenX, len(table))

    for rowI, row in enumerate(table):
        for colI, col in enumerate(row):
            new[rowI][colI].value = col.value

    return new

def merge_tables(table1: Table, table2: Table) -> Table:
    lenX1 = len(table1[0])
    lenX2 = len(table2[0])

    # X
    if lenX1 > lenX2:
        lenX = lenX1
    else:
        lenX = lenX2

    lenY1 = len(table1)
    lenY2 = len(table2)

    # Y
    if lenY1 > lenY2:
        lenY = lenY1
    else:
        lenY = lenY2
    

    new_table = create_new_table(lenX, lenY)


    # Table 1
    for rowI, row in enumerate(table1):
        for colI, col in enumerate(row):
            if col.value == full_sign_template:
                new_table[rowI][colI].value = col.value

    # Table 2
    for rowI, row in enumerate(table2):
        for colI, col in enumerate(row):
            if col.value == full_sign_template:
                new_table[rowI][colI].value = col.value

    return new_table

def count(table: Table) -> int:
    counter = 0
    for row in table:
        for col in row:
            if col.value == full_sign_template:
                counter += 1
    return counter

"""

Create actual data

"""

original_table = create_new_table(maxX+1, maxY+1)

for pos in positions:
    row = original_table[pos["Y"]]
    col = row[pos["X"]]

    col.value = full_sign_template


def to_str(table):
    to_print = ""
    for row in table:
        collumn = ""
        for col in row:
            collumn = collumn + col.value
        collumn = collumn + "\n"
        to_print = to_print + collumn
    return to_print

"""

Add Y fold

"""
def flipY(table: Table) -> Table:
    lenY = len(table)
    lenX = len(table[0])
    # Create new rows
    new_table = create_new_table(lenX, lenY)

    # Copy values
    for i, v in enumerate(table):
        new_table[(lenY-i)-1] = v

    return new_table

def foldY(foldPos: int, table: Table) -> Table:
    new_table = copy_table(table)

    # Mark
    for col in new_table[foldPos]:
        col.value = "-"

    # Deviding two things
    upTable = new_table[0:foldPos]
    lowTable = new_table[(foldPos+1):]

    flipped_low_table = flipY(lowTable)
    merged_table = merge_tables(upTable, flipped_low_table)

    return merged_table


"""

Add X fold

"""
def flipX(table: Table) -> Table:
    lenY = len(table)
    lenX = len(table[0])
    # Create new rows
    new_table = create_new_table(lenX, lenY)

    # Copy values
    for rowI, row in enumerate(table):
        for i, v in enumerate(row):
            new_table[rowI][(lenX-i)-1] = v

    return new_table


def foldX(foldPos: int, table: Table) -> Table:
    lenx = len(table[0])
    new_table = copy_table(table)

    # Mark them
    for row in new_table:
        for colI, col in enumerate(row):
            if colI == foldPos:
                col.value = "|"

    # Deviding into left
    left_table = create_new_table(foldPos, len(table))
    for rowI, row in enumerate(left_table):
        for colI, col in enumerate(row):
            col.value = new_table[rowI][colI].value

    # Deviding into right
    right_table = create_new_table((lenx-foldPos)-1, len(table))
    for rowI, row in enumerate(right_table):
        for colI, col in enumerate(row):
                col.value = new_table[rowI][(foldPos+colI)+1].value
    
    flipped_left = flipX(left_table)
    merged_table = merge_tables(flipped_left, right_table)
    
    return merged_table


current_table = original_table
for fold in folds:
    if fold["Type"] == "X":
        folded = foldX(fold["Value"], current_table)
    elif fold["Type"] == "Y": 
        folded = foldY(fold["Value"], current_table)
    current_table = folded

result = flipX(current_table)
print(to_str(result), file=open("Day13/output.txt", "w", encoding='utf-8'))
