from math import lcm
from common import read_lines



rocks_str = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##""".split("\n")

rocks = [
    ["####"],
    [".#.", "###", ".#."],
    ["..#", "..#", "###"],
    ["#", "#", "#", "#"],
    ["##", "##"]
]

pattern = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

with open("input17.txt", "r") as f: 
    pattern = f.readline().strip("\n")

def draw_shaft(shaft: list[str], rock: list[str] = None, left = None, top = 0):
    res = []
    for i in shaft:
        res.append(f"|{i}|")

        
    if rock is not None:
        for i, r in enumerate(rock):
            l = res[top-i]
            tmp = l[left+1:left+1+len(r)]
            tmp = "".join(["@" if x == "#" else tmp[i] for i,x in enumerate(r)])
            res[top-i] = l[:left+1] + tmp + l[left+1+len(r):]
        
        for i in range(top, max(top-rock_height-1,-1), -1):
            print(res[i])
    else:
        for line in res[::-1]:
            print(line)
        print("+-------+")
    print("")


shaft_row = "......."

def is_empty(row: str):
    return row == shaft_row

def part1(count, repeat = None, shaft = None, start = 0):
    states = {}
    steps = start
    if shaft is None:
        shaft = []
    pattern_idx = 0
    repeat = count if repeat is None else repeat
    idx = 0
    extra = 0
    while idx<count:
        rock = rocks[idx%len(rocks)]
        rock_height = len(rock)
        rock_width = len(rock[0])
        while len(shaft)<4 or any([not is_empty(x) for x in shaft[-(3+rock_height):]]):
            shaft.append(shaft_row)
        
        left, top = 2, len(shaft)-1

        while len(shaft)>4 and all([is_empty(x) for x in shaft[top-(3+rock_height):]]):
            top -=1

        # Do three first steps without checking
        for _ in range(0,3):
            direction = pattern[pattern_idx%len(pattern)]
            pattern_idx += 1
            steps += 2
            top -= 1
            if direction=="<" and left>0: left -= 1
            elif direction==">" and left + rock_width<7: left += 1

        stopped = False
        while not stopped:
            direction = pattern[pattern_idx%len(pattern)]
            pattern_idx = (pattern_idx + 1)%len(pattern)
            if direction=="<" and left>0:
                tmp = [x[left-1:left+rock_width-1] for x in shaft[top:top-rock_height:-1]]
                tmp = zip(tmp, rock)
                if not any([x[i]=="#" and y[i]=="#" for x,y in tmp for i in range(0, len(x))]):
                    left -= 1
            elif direction==">" and left + rock_width<7:
                tmp = [x[left+1:left+rock_width+1] for x in shaft[top:top-rock_height:-1]]
                tmp = zip(tmp, rock)
                if not any([x[i]=="#" and y[i]=="#" for x,y in tmp for i in range(0, len(x))]):
                    left += 1
            steps += 1
            tmp = [shaft[top-i-1][left:left+rock_width] for i in range(0, rock_height)]
            tmp = zip(tmp, rock)
            stopped = any([x[i]=="#" and y[i]=="#" for x,y in tmp for i in range(0, len(x))])
            stopped = stopped or top == 0
            steps += 1
            if stopped:
                for l in range(0,rock_height):
                    r = shaft[top-l]
                    tmp = r[left:left+rock_width]
                    tmp = "".join(["#" if x == "#" else tmp[j] for j, x in enumerate(rock[l])])
                    shaft[top-l] = r[:left] + tmp + r[left+rock_width:]
                stopped = True
            else:
                top -= 1

        key = f"{hash(tuple(shaft[top-200:top+1]))}|{pattern_idx}|{idx%len(rocks)}"
        if extra==0 and key in states:
            old_idx, old_top = states[key]
            remaining = count-idx-1
            extra = (remaining // (idx-old_idx))*(top-old_top)
            idx = count - (remaining % (idx-old_idx))
            #break
        else:
            states[key] = (idx, top)
            idx += 1

    while is_empty(shaft[-1]):
        shaft.pop()

    return len(shaft) + extra


shaft = part1(2022)
print(shaft)
print(part1(1000000000000))
