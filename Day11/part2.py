"""
Day 11 - Part 2
https://adventofcode.com/2021/day/11#part2

By NORXND @ 12.12.2021
(C) NORXND 2021 - Under The MIT License
"""
input_file = open("Day11/input.txt", "r")

rows = []
col_len = 0

for line in input_file:
    col = []
    for num in line.strip():
        col.append(int(num))
    col_len = len(col)
    rows.append(col)

def get_right(row, col):
    if col != (col_len-1):
        return [row, col+1]

def get_left(row, col):
    if col != 0:
        return [row, col-1]

def get_up(row, col):
    if row != 0:
        return [row-1, col]

def get_down(row, col):
    if row != (len(rows)-1):
        return [row+1, col]

def get_diagonally_up_right(row, col):
    if row != 0 and col != (col_len-1):
        return [row-1, col+1]

def get_diagonally_up_left(row, col):
    if row != 0 and col != 0:
        return [row-1, col-1]

def get_diagonally_down_right(row, col):
    if row != (len(rows)-1) and col != (col_len-1):
        return [row+1, col+1]

def get_diagonally_down_left(row, col):
    if row != (len(rows)-1) and col != 0:
        return [row+1, col-1]

def found0(rows, zero_row, zero_col):
        adjacents = []
        
        if get_right(zero_row, zero_col) is not None: 
            adjacents.append(get_right(zero_row, zero_col))
        if get_left(zero_row, zero_col) is not None: 
            adjacents.append(get_left(zero_row, zero_col))
        if get_up(zero_row, zero_col) is not None: 
            adjacents.append(get_up(zero_row, zero_col))
        if get_down(zero_row, zero_col) is not None: 
            adjacents.append(get_down(zero_row, zero_col))

        if get_diagonally_up_right(zero_row, zero_col) is not None: 
            adjacents.append(get_diagonally_up_right(zero_row, zero_col))
        if get_diagonally_up_left(zero_row, zero_col) is not None: 
            adjacents.append(get_diagonally_up_left(zero_row, zero_col))
        if get_diagonally_down_right(zero_row, zero_col) is not None: 
            adjacents.append(get_diagonally_down_right(zero_row, zero_col))
        if get_diagonally_down_left(zero_row, zero_col) is not None: 
            adjacents.append(get_diagonally_down_left(zero_row, zero_col))

        for adjacent in adjacents:
            if rows[adjacent[0]][adjacent[1]] != 0:
                rows[adjacent[0]][adjacent[1]] = rows[adjacent[0]][adjacent[1]] + 1
                if rows[adjacent[0]][adjacent[1]] > 9:
                    rows[adjacent[0]][adjacent[1]] = 0
                    rows = found0([x[:] for x in rows], adjacent[0], adjacent[1])
        
        return rows

keep_going = True
step = 1
while keep_going:
    # Add 1 to each
    for row_index, row in enumerate(rows):
        for col_index, col in enumerate(row):
                rows[row_index][col_index] = col + 1

    for row_index, row in enumerate(rows):
        for col_index, col in enumerate(row):
                if col > 9:
                    rows[row_index][col_index] = 0

    # Find 0
    for row_index, row in enumerate(rows):
        for col_index, col in enumerate(row):
            if col == 0:
                new_rows = found0([x[:] for x in rows], row_index, col_index)
                rows = new_rows

    # Calculate
    flashes = 0
    for row_index, row in enumerate(rows):
        for col_index, col in enumerate(row):
            if col == 0:
                flashes = flashes + 1
                

    print(f"Step {step} - {flashes}")

    if flashes == 100:
        keep_going = False
        break

    step = step + 1