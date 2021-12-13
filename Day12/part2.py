"""
Day 12 - Part 2
https://adventofcode.com/2021/day/12#part2

By NORXND @ 13.12.2021
(C) NORXND 2021 - Under The MIT License
"""
import typing

input_file = open("Day12/input.txt", "r")

routes_segments: typing.List[str] = []
routes_elements: typing.List[str] = []

connections: typing.Dict[str, typing.List[str]] = {}

found_routes: list = []

for line in input_file:
    segments = line.strip().split("-")
    for x in segments: 
        if x not in routes_elements:
            routes_elements.append(x)
    routes_segments.append(segments)

for x in routes_elements:
    connections[x] = []
    for segment in routes_segments:
        if x in segment:
            if segment[0] == x:
                connections[x].append(segment[1])
            else:
                connections[x].append(segment[0])

def copy(original: list) -> list:
    return [x[:] for x in original]

class Route:
    def __init__(self, path: list = [], used_smalls: list = []) -> 'Route':
        self.path: list = path
        self.last: int = path[-1]
        self.used_smalls: list = used_smalls

        self.extend()

    def __repr__(self):
        return f"{self.path}"

    def extend(self):
        for i, conn in enumerate(connections[self.last]):
            if conn == self.last or conn == "start":
                continue
            
            elif conn == "end":
            
                newpath = copy(self.path)
                newpath.append("end")

                found_routes.append(self.path)
            
            else:
                if conn in self.used_smalls:
                    can_use_twice = True
                    for x in self.used_smalls:
                        if self.used_smalls.count(x) >= 2:
                            can_use_twice = False

                    if self.used_smalls.count(conn) >= 1 and (not can_use_twice):
                        continue

                newpath = copy(self.path)
                newused = copy(self.used_smalls)

                newpath.append(conn)
                if conn.islower():
                    newused.append(conn)

                #print(f"{newpath}")

                Route(newpath, newused)

for conn in connections["start"]:
    route_path = ["start", conn]
    used = []
    
    if conn.islower():
        used.append(conn)

    Route(route_path, used)

print(len(found_routes))