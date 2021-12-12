"""
Day 4 - Part 2
https://adventofcode.com/2021/day/5#part2

By NORXND @ 06.12.2021
(C) NORXND 2021 - Under The MIT License
"""
import typing

input_file = open('Day5/input.txt', 'r')

input_lines = input_file.readlines()
lines = []

# Get all lines
for line in input_lines:
    formatted_line = line.strip().split(" -> ")
    start = formatted_line[0].split(",")
    end = formatted_line[1].split(",")

    data = {
        "Start": {
            "X": int(start[0]),
            "Y": int(start[1]),
        },
        "End": {
            "X": int(end[0]),
            "Y": int(end[1]),
        }
    }

    lines.append(data)

# Get max X and Y
maxX = 0
maxY = 0
for line in lines:
    if line["Start"]["X"] > maxX:
        maxX = line["Start"]["X"]
    if line["End"]["X"] > maxX:
        maxX = line["End"]["X"]

    if line["Start"]["Y"] > maxY:
        maxY = line["Start"]["Y"]
    if line["End"]["Y"] > maxY:
        maxY = line["End"]["Y"]

class Point:
    def __init__(self, v: typing.Optional[int], i, row):
        self.Value = v
        self.Index = i
        self.Row = row

    def __repr__(self):
        return f"<Point {self.Index} in {self.Row} Value: {str(self.Value)}>"

class Table:
    def setup_cols(self, row):
        cols = []
        for i in range(self.sizeX):
            cols.append(Point(None, i, row))
        
        return cols

    def setup_rows(self):
        rows = []

        for i in range(self.sizeY):
            cols = self.setup_cols(i)
            rows.append(cols)

        return rows

    def __init__(self, sizeX: int, sizeY: int):
        self.sizeX: int = sizeX
        self.sizeY: int = sizeY

        self.rows: typing.List[typing.List[Point]] = self.setup_rows()

    def mark_in_row(self, row: int, start: int, end: typing.Optional[int]):
        row = self.rows[row]

        if end is None:
            point = row[start]
            if point.Value == None:
                point.Value = 1
            else:
                point.Value = point.Value + 1
            return

        for i in range(start, end+1):
            point = row[i]
            if point.Value == None:
                point.Value = 1
            else:
                point.Value = point.Value + 1

    def get_all_points(self) -> typing.List[Point]:
        all = []

        for row in self.rows:
            for col in row:
                all.append(col)
        
        return all

table = Table(maxX+1, maxY+1)

for line in lines:
    if line["Start"]["X"] == line["End"]["X"] or line["Start"]["Y"] == line["End"]["Y"]:
        # Get our Xs
        if line["Start"]["X"] > line["End"]["X"]:
            startX = line["End"]["X"]
            endX = line["Start"]["X"]
        else:
            startX = line["Start"]["X"]
            endX = line["End"]["X"]

        # Get our Ys
        if line["Start"]["Y"] > line["End"]["Y"]:
            startY = line["End"]["Y"]
            endY = line["Start"]["Y"]
        else:
            startY = line["Start"]["Y"]
            endY = line["End"]["Y"]

        # Check how many rows we need to deal with
        rows_num = endY - startY

        # Means we need only deal with one row else multiple ones
        if rows_num == 0:
            table.mark_in_row(startY, startX, endX)
        else:
            for row in range(startY, endY+1):
                table.mark_in_row(row, startX, endX)
    else:
        startX = line["Start"]["X"]
        endX = line["End"]["X"]

        startY = line["Start"]["Y"]
        endY = line["End"]["Y"]

        print(f'X: {startX} -> {endX} Y: {startY} -> {endY}')

        ix = abs(endX - startX)
        iy = abs(endY - startY)

        for ci in range(ix+1):
            if startX > endX:
                cx = startX - ci
            else:
                cx = startX + ci

            if startY > endY:
                cy = startY - ci
            else:
                cy = startY + ci

            table.mark_in_row(cy, cx, None)


all = table.get_all_points()
above2 = 0

for p in all:
    if p.Value is not None and p.Value >= 2:
        above2 = above2 + 1

print(above2)
