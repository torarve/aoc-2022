from pprint import pprint
from common import read_lines
import re


class Map:
    def __init__(self, data: list[str]):
        self.rows = [x for x in data]

    def __getitem__(self, pos):
        try:
            col, row = pos
            return self.rows[row][col]
        except:
            return None
    
    def __setitem__(self, pos, value):
        col, row = pos
        tmp = self.rows[row]
        self.rows[row] = tmp[:col] + value + tmp[col+1:]

    def row_length(self, row):
        return len(self.rows[row])

    def __repr__(self):
        tmp = "\n".join(self.rows)
        return f"Map\n{tmp}"


lines = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5""".split("\n")

with open("input22.txt") as f:
    lines = [x.strip("\n") for x in f.readlines()]

map_lines = []
w = 0
for i in range(0,len(lines)):
    if lines[i] == "":
        break
    map_lines.append(lines[i])
    w = max(w, len(lines[i]))

map_lines = [x.ljust(w) for x in map_lines]

path = [(int(count), direction) for count, direction in  re.findall(r"(\d+)(R|L)?", lines[-1])]

map = Map(map_lines)
x, y = (map.rows[0].index("."), 0)
dx, dy = (1, 0)


def facing(dx, dy):
    match (dx, dy):
        case (1, 0): return ">"
        case (0, 1): return "v"
        case (-1, 0): return "<"
        case (0, -1): return "^"

def facing_score(dx, dy):
    match (dx, dy):
        case (1, 0): # >
            return 0
        case (0, 1): # v
            return 1
        case (-1, 0): # <
            return 2
        case (0, -1): # ^
            return 3

def step(x, y):
    new_y = (y + dy) % len(map.rows)
    new_x = (x + dx) % w
    return new_x, new_y, map[new_x, new_y]

map[x, y] = facing(dx, dy)
for step_count, turn in path:
    for i in range(0, step_count):
        new_x, new_y, next = step(x, y)
        while next == " ": # Wrap around
            new_x, new_y, next = step(new_x, new_y)

        if next != "#":
            map[new_x,new_y] = facing(dx, dy)
            x, y = new_x, new_y

    if turn == "R":
        dx, dy = -dy, dx
    elif turn == "L":
        dx, dy = dy, -dx

    map[x, y] = facing(dx, dy)


print(1000*(y+1) + 4*(x+1) + facing_score(dx, dy))


#
# PART 2
#

#   1 2
#   3
# 4 5
# 6

h = len(map_lines)


map = Map(map_lines)
x, y = (map.rows[0].index("."), 0)
dx, dy = (1, 0)
map[x, y] = facing(dx, dy)
for step_count, turn in path:
    i = 0
    while i < step_count:
        if (x, y, dx, dy) == (49, 180, 1, 0):
            print()
        new_y = (y + dy)
        new_x = (x + dx)
        new_dx = dx
        new_dy = dy

        if new_y<0:
            if 50 <= x and x < 100: # 1
                new_x, new_y = 0, 150+x-50
                new_dx, new_dy = -dy, -dx
            else: # 2
                new_x, new_y = x-100, 199
                new_dx, new_dy = dx, dy
        elif new_y >= h: # 6
            new_x, new_y = x+100, 0
            new_dx, new_dy = dx, dy
        elif new_x < 0: # 4, 6
            if 100 <= y < 150: # 4
                offset_y = (y - 100)
                new_x, new_y = 50, 49 - offset_y
                new_dx, new_dy = -dx, -dy
            else: # 6
                new_x, new_y = (y-150)+50, 0
                new_dx, new_dy = dy, -dx
        elif new_x >= w: # 2
            new_x, new_y = 99, 149-y
            new_dx, new_dy = -dx, -dy 

        val = map[new_x, new_y]
        if val==" ":
            if 50 <= x and x < 100 and 0 <= y and y < 50: # 1
                new_x, new_y = 0, 149-y
                new_dx, new_dy = -dx, -dy
            elif 100 <=x and x < 150: # 2
                new_x, new_y = 99, x - 50
                new_dx, new_dy = -dy, dx
            elif 50 <= x and x < 100 and 50 <= y and y < 100: # 3
                if dx == -1: # left
                    new_x, new_y = y-50, 100
                    new_dx, new_dy = dy, -dx
                elif dx == 1: # right
                    new_x, new_y = y + 50, 49
                    new_dx, new_dy = dy, -dx
            elif 0 <= x and x < 50 and 100 <= y and y < 150: # 4
                new_x, new_y = 50, x + 50
                new_dx, new_dy = -dy, dx
            elif 50 <= x and x < 100 and 100 <= y and y < 150: # 5
                if dx == 1:
                    new_x, new_y = 149, 49 - (y-100)
                    new_dx, new_dy = -dx, -dy
                else:
                    new_x, new_y = 49, x + 100
                    new_dx, new_dy = -dy, dx
            elif 0 <= x and x < 50 and 150 <= y and y < 200: # 6
                new_x, new_y = y - 100, 149
                new_dx, new_dy = dy, -dx

            val = map[new_x, new_y]

        if val != "#":
            map[new_x,new_y] = facing(dx, dy)
            x, y, dx, dy = new_x, new_y, new_dx, new_dy
            i = i + 1
        else:
            i = step_count

    if turn == "R":
        dx, dy = -dy, dx
    elif turn == "L":
        dx, dy = dy, -dx

    map[x, y] = facing(dx, dy)


print(1000*(y+1) + 4*(x+1) + facing_score(dx, dy))
