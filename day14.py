from common import read_lines




lines = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".split("\n")

lines = read_lines("input14.txt")

start = (500,0)


def point_range(begin, end):
    x1, y1 = begin
    x2, y2 = end
    if x1==x2:
        for i in range(min(y1,y2), max(y1,y2)+1):
            yield (x1, i)
    else:
        for i in range(min(x1, x2), max(x1,x2)+1):
            yield (i, y1)

def init(lines):
    blocked = set()
    for line in lines:
        print(line)
        points = [eval(x) for x in line.split(" -> ")]
        for i in range(1,len(points)):
            for x in point_range(points[i-1], points[i]):
                blocked.add(x)
    
    return blocked


blocked = init(lines)
count = 0
bottom = max([y for x, y in blocked])
x, y = (500, 0)
while y <= bottom:
    if (x, y+1) not in blocked:
        y += 1
    elif (x-1, y+1) not in blocked:
        x, y = (x-1, y+1)
    elif (x+1, y+1) not in blocked:
        x, y = (x+1, y+1)
    else:
        blocked.add((x,y))
        count +=1 
        x, y = (500, 0)

print(count)

blocked = init(lines)
bottom +=2
count = 0
x, y = (500, 0)
while True:
    if y+1 == bottom:
        blocked.add((x,y))
        count += 1
        x, y = (500, 0)
    if (x, y+1) not in blocked:
        y += 1
    elif (x-1, y+1) not in blocked:
        x, y = (x-1, y+1)
    elif (x+1, y+1) not in blocked:
        x, y = (x+1, y+1)
    elif y == 0:
        break
    else:
        blocked.add((x,y))
        count +=1 
        x, y = (500, 0)

print(count+1)