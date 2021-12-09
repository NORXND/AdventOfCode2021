"""
Day 9 - Part 2
https://adventofcode.com/2021/day/9#part2

By NORXND @ 09.12.2021
(C) NORXND 2021 - Under The MIT License
"""

input_file = open("Day9/input.txt", "r")

rows = []

for entry in input_file.readlines():
    l = []

    for char in entry.strip():
        l.append(int(char))

    rows.append(l)

highlighted = []
basins = []

# x - our element, y - what should be larger
def check(x, y):
    if x is None or y is None:
        return True
    elif x < y:
        return True
    else:
        return False


def get_right(rowi, coli):
    try:
        return rows[rowi][coli + 1]
    except IndexError:
        return None


def get_left(rowi, coli):
    if coli == 0:
        return None
    else:
        return rows[rowi][coli - 1]


def get_up(rowi, coli):
    try:
        return rows[rowi + 1][coli]
    except IndexError:
        return None


def get_down(rowi, coli):
    if rowi == 0:
        return None
    else:
        return rows[rowi - 1][coli]

def parse_number(ri, ci, cv, scopes=[]):
    if f"{ri}x{ci}x{cv}" in highlighted:
        return

    nums = []
    """
    #print(f"{ri}x{ci}x{cv}")
    # Checks
    if "r" in scopes:
        if not check(cv, get_right(ri, ci)):
            return
    elif "l" in scopes:
        if not check(cv, get_left(ri, ci)):
            return
    elif "u" in scopes:
        if not check(cv, get_up(ri, ci)):
            return
    elif "d" in scopes:
        if not check(cv, get_down(ri, ci)):
            return
    """
    
    if int(cv) == 9:
        return

    #print("Will add!")
    highlighted.append(f"{ri}x{ci}x{cv}")
    nums.append(f"{ri}x{ci}x{cv}")

    numr_raw = get_right(ri, ci)
    if numr_raw is not None:
        add_numr = parse_number(ri, ci+1, numr_raw, ["r", "u", "d"])
        if add_numr is not None:
            for x in add_numr:
                nums.append(x)

    numl_raw = get_left(ri, ci)
    if numl_raw is not None:
        add_numl = parse_number(ri, ci-1, numl_raw, ["l", "u", "d"])
        if add_numl is not None:
            for x in add_numl:
                nums.append(x)

    numu_raw = get_up(ri, ci)
    if numu_raw is not None:
        add_numu = parse_number(ri+1, ci, numu_raw, ["l", "u", "r"])
        if add_numu is not None:
            for x in add_numu:
                nums.append(x)

    numd_raw = get_down(ri, ci)
    if numd_raw is not None:
        add_numd = parse_number(ri-1, ci, numd_raw, ["l", "r", "d"])
        if add_numd is not None:
            for x in add_numd:
                nums.append(x)

    return nums

for ri, rv in enumerate(rows):
    for ci, cv in enumerate(rv):
        if (
            check(cv, get_right(ri, ci))
            and check(cv, get_left(ri, ci))
            and check(cv, get_up(ri, ci))
            and check(cv, get_down(ri, ci))
        ):
            highlighted.append(f"{ri}x{ci}x{cv}")
            basin = []
            basin.append(f"{ri}x{ci}x{cv}")
            #print(f"{ri}x{ci}x{cv}")


            numr_raw = get_right(ri, ci)
            if numr_raw is not None:
                add_numr = parse_number(ri, ci+1, numr_raw, ["r", "u", "d"])
                if add_numr is not None:
                    for x in add_numr:
                        basin.append(x)

            numl_raw = get_left(ri, ci)
            if numl_raw is not None:
                add_numl = parse_number(ri, ci-1, numl_raw, ["l", "u", "d"])
                if add_numl is not None:
                    for x in add_numl:
                        basin.append(x)

            numu_raw = get_up(ri, ci)
            if numu_raw is not None:
                add_numu = parse_number(ri+1, ci, numu_raw, ["l", "u", "r"])
                if add_numu is not None:
                    for x in add_numu:
                        basin.append(x)

            numd_raw = get_down(ri, ci)
            if numd_raw is not None:
                add_numd = parse_number(ri-1, ci, numd_raw, ["l", "r", "d"])
                if add_numd is not None:
                    for x in add_numd:
                        basin.append(x)

            basins.append(basin)

basins_len = []
for basin in basins:
    basins_len.append(len(basin))

highest = sorted(basins_len, reverse=True)[:3]

result = 1
for x in highest:
    result = result * x

print(result)