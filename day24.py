from common import read_lines


def direction(c):
    match c:
        case "<": return (-1,0)
        case ">": return (1,0)
        case "v": return (0,1)
        case "^": return (0,-1)

def move_blizzard(blizzard, w, h):
    x, y, dx, dy = blizzard
    return (x+dx)%w, (y+dy)%h, dx, dy


lines = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#""".split("\n")

lines = read_lines("input24.txt")

start, end = lines[0].index(".")-1, lines[-1].index(".")-1
w, h = len(lines[0])-2, len(lines)-2
blizzards = []
for y, line in enumerate(lines[1:-1]):
    for x, t in enumerate(line[1:-1]):
        if t != ".":
            dx, dy = direction(t)
            blizzards.append((x, y, dx, dy))


def round(positions: set[tuple[int,int]], blizzards: list[tuple[int,int,int,int]], size):
    w, h = size
    blizzards = [move_blizzard(blizzard, *size) for blizzard in blizzards]
    blizzard_positions = set([(x,y) for x, y, _, __ in blizzards])
    updated_positions = set()
    for pos in positions:
        x, y = pos
        options = [(x, y+1), (x-1, y), (x+1,y), (x, y-1), (x,y)]
        options = [(xx,yy) for xx,yy in options if xx%w == xx and yy%h == yy]
        options.append((x,y)) # Wait
        options = [(xx,yy) for xx,yy in options if (xx,yy) not in blizzard_positions or yy == -1 or yy == h]
        updated_positions = updated_positions.union(set(options))
        
    return updated_positions, blizzards

positions = set([(start, -1)])
count = 0
while not (end, h-1) in positions:
    positions, blizzards = round(positions, blizzards, (w,h))
    count += 1
    if len(positions)==0:
        print("Not found!!!")
        break

result1 = count+1
print(result1)

blizzards = [move_blizzard(blizzard, w, h) for blizzard in blizzards]
positions = set([(end, h)])
count = 0
while not (start, 0) in positions:
    positions, blizzards = round(positions, blizzards, (w,h))
    count += 1
    if len(positions)==0:
        print("Not found!!!")
        break

result2 = count+1
print(result2)

blizzards = [move_blizzard(blizzard, w, h) for blizzard in blizzards]
positions = set([(start, -1)])
count = 0
while not (end, h-1) in positions:
    positions, blizzards = round(positions, blizzards, (w,h))
    count += 1
    if len(positions)==0:
        print("Not found!!!")
        break

result3 = count+1
print(result3)

print(result1+result2+result3)
