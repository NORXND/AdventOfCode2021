"""
Day 4 - Part 2
https://adventofcode.com/2021/day/4#part2

By NORXND @ 04.12.2021
(C) NORXND 2021 - Under The MIT License
"""
import typing

input_file = open('Day4/input.txt', 'r')

input_data = input_file.read().split("\n\n")
numbers = input_data[0].split(",")
raw_boards = input_data[1:]


class Num:
    def __init__(self, value: int, isMarked: bool = False):
        self.number: int = value
        self.isMarked: bool = isMarked
    
    def __str__(self):
        return str(self.number)
    
    def __repr__(self):
        return f"<Number {self.number}, isMarked: {self.isMarked}>"

class Board():
    collumns_range = 5
    
    def split_rows(self):
        rows = self.raw_text.splitlines()
    
        tmp_rows = []
        for row in rows:
            tmp_rows.append(row.split(" "))

        return tmp_rows

    def prepare_row(self, rows):
        result = []

        for row in rows:
            tmp = []
            for element in row:
                    if element != "" and element != " ":
                        tmp.append(Num(int(element)))
            result.append(tmp)

        return result

    def setup_collumns(self):
        rows = self.rows or self.prepare_row(self.split_rows())

        collumns = []
        for i in range(0, self.collumns_range):
            collumn = []
            for row in rows:
                collumn.append(row[i])
            collumns.append(collumn)
        
        return collumns

    def __init__(self, index: int, board: str):
        self.index = index
        self.raw_text: str = board
        self.rows = self.prepare_row(self.split_rows())
        self.collumns = self.setup_collumns()
    
    def __repr__(self):
        return f"Board {self.index}"

    def get_all(self) -> typing.List[Num]:
        returns = []

        for row in self.rows:
            for col in row:
                returns.append(col)

        return returns

    def mark(self, num: int):
        all = self.get_all()

        for x in all:
            if x.number == num:
                x.isMarked = True

    def is_row_full(self):
        for row in self.rows:
            foundNotMarked = False
            for num in row:
                if num.isMarked == False:
                    foundNotMarked = True
            if foundNotMarked:
                continue
            else:
                return True
        return False

    def is_collumn_full(self):
        for col in self.collumns:
            foundNotMarked = False
            for num in col:
                if num.isMarked == False:
                    foundNotMarked = True
            if foundNotMarked:
                continue
            else:
                return True
        return False

    def get_unmarked(self):
        umarked_numbers = []
        for row in self.rows:
            for num in row:
                if num.isMarked == False:
                    umarked_numbers.append(num.number)
        
        return umarked_numbers

boards: typing.List[Board] = []


# Get board
for i, raw_board in enumerate(raw_boards):
    boards.append(Board(i+1, raw_board))

"""def finish(last, num):
    print(last.index)
    print(sum(last.get_unmarked()))
    print(current_num)

    print(sum(last.get_unmarked()) * int(num))
    exit()"""

scores = []
current_num = 0
allowed = boards.copy()
for num in numbers:
    current_num = num
    debris = []

    for board in boards:
        if board not in allowed:
            continue
        
        board.mark(int(num))

        if board.is_collumn_full() or board.is_row_full():
            last_win = {
                "Board": board,
                "Sum": sum(board.get_unmarked()),
                "CurrentNum": int(current_num),
            }

            scores.append(last_win)
            debris.append(last_win)

    for b in debris:
        allowed.remove(b["Board"])

print(scores[-1])
