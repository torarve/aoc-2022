from common import read_lines


class Matrix:
    def __init__(self, rows: int, cols: int, data: list):
        self.rows = rows
        self.cols = cols
        self.data = data

    def __getitem__(self, pos):
        col, row = pos
        return self.data[col + row*self.cols]
    
    def __setitem__(self, pos, value):
        col, row = pos
        self.data[col + row*self.cols] = value

    def __repr__(self):
        tmp = "\n".join([str(self.data[i*self.cols:(i+1)*self.cols]) for i in range(0,self.rows)])
        return f"Matrix\n[{tmp}]"

def to_coord(pos, size) -> tuple[int, int]:
    return pos % size, pos // size

def start_pos(data: list[str], size) -> tuple[int, int]:
    return to_coord(data.index("S"), size)

def end_pos(data: list[str], size) -> tuple[int, int]:
    return to_coord(data.index("E"), size)

def next_steps(m, x, y):
    result = []
    current = m[x,y]
    if x > 0 and m[x-1, y] <= current+1:
        result.append((x-1, y))
    if x+1 < m.cols and m[x+1, y] <= current+1:
        result.append((x+1, y))
    if y > 0 and m[x, y-1] <= current+1:
        result.append((x, y-1))
    if y+1 < m.rows and m[x, y+1] <= current+1:
        result.append((x, y+1))

    return result



lines = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".split("\n")

lines = read_lines("input12.txt")

cols = len(lines[0])
rows = len(lines)
print(rows, cols)
data = [0 if x=="S" else 26 if x == "E" else ord(x) - ord("a") for x in list("".join(lines))]
# print(data)
m = Matrix(rows, cols, data)
# print(m)

start = start_pos(list("".join(lines)), cols)
end = end_pos(list("".join(lines)), cols)

print(start, end, m[end])

count = 0
positions = [start]
seen = set()
while end not in positions:
    count += 1
    seen = seen.union(positions)
    tmp = set()
    for position in positions:
        tmp1 = next_steps(m, *position)
        # tmp = tmp.union([x for x in tmp1 if x not in seen])
        tmp = tmp.union(tmp1)

    positions = list(tmp.difference(seen))
    if len(positions) == 0:
        print("Could not find a solution")
        print(len(seen), m.rows*m.cols)
        break

print(count)

# print(ord('z') - ord("a"))