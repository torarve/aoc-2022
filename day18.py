from common import read_lines


lines = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""".split("\n")

lines = read_lines("input18.txt")

def parse_line(line: str) -> tuple[int,int,int]:
    x, y, z = tuple(line.split(","))
    return int(x), int(y), int(z)

def adjacent_to(point: tuple[int,int,int]):
    x,y,z = point
    return set([(x-1, y, z), (x+1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)])

cubes: set[tuple[int,int,int]] = set([parse_line(line) for line in lines])

sides = [x for point in cubes for x in adjacent_to(point) if x not in cubes]
print(len(sides))

def calc_bounds(points: tuple[int,int,int]):
    lower_x = min([x for x,y,z in points])
    upper_x = max([x for x,y,z in points])
    lower_y = min([y for x,y,z in points])
    upper_y = max([y for x,y,z in points])
    lower_z = min([z for x,y,z in points])
    upper_z = max([z for x,y,z in points])
    return (lower_x-1, lower_y-1, lower_z-1), (upper_x+1, upper_y+1, upper_z+1)


lower, upper = calc_bounds(cubes)
x1, y1, z1 = lower
x2, y2, z2 = upper
outside = set([(x1, y1, z1)])

def inside_bounds(p: tuple[int,int,int]):
    x,y,z = p
    return x1<=x and x<=x2 and y1<=y and y<=y2 and z1<=z and z<=z2

while True:
    new_points = set([x for p in outside for x in adjacent_to(p) if inside_bounds(x) and x not in cubes])
    old_len = len(outside)
    outside = outside.union(set(new_points))
    if old_len == len(outside):
        break

sides = [x for point in cubes for x in adjacent_to(point) if x not in cubes and x in outside]
print(len(sides))
