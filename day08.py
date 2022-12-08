from common import read_lines


class Matrix:
    def __init__(self, rows: int, cols: int, data: list):
        self.rows = rows
        self.cols = cols
        self.data = data

    def get(self, col, row):
        return data[col + row*self.cols]
    
    def set(self, col, row, value):
        self.data[col + row*self.cols] = value

    def row(self, idx):
        return self.data[idx*self.cols:(idx+1)*self.cols]
    
    def column(self, idx):
        return self.data[idx::self.cols]

    def __repr__(self):
        tmp = "\n".join([str(self.data[i*self.cols:(i+1)*self.cols]) for i in range(0,self.rows)])
        return f"Matrix\n[{tmp}]"

lines = read_lines("input08.txt")

data: list[int] = []
row_count = 0

for row in lines:
    row_count += 1
    for cell in row:
        data.append(int(cell))

matrix = Matrix(row_count, len(data)//row_count, data)
visible = Matrix(matrix.rows, matrix.cols, [False]*matrix.cols*matrix.rows)

for i in range(0, visible.cols):
    visible.set(i, 0, True)
    visible.set(i, visible.rows-1, True)

for i in range(0, visible.rows):
    visible.set(0, i, True)
    visible.set(visible.cols-1, i, True)

for x in range(0, matrix.cols):
    for y in range(0, matrix.rows):
        col = matrix.column(x)
        row = matrix.row(y)
        current = matrix.get(x,y)
        above = all([v<current for v in col[0:y]])
        below = all([v<current for v in col[y+1:]])
        left = all([v<current for v in row[:x]])
        right = all([v<current for v in row[x+1:]])
        if above or below or left or right:
            visible.set(x, y, True)

def scenic_score(matrix: Matrix, x, y):
    col = matrix.column(x)
    row = matrix.row(y)
    current = matrix.get(x,y)

    def find_first(where: list[int]):
        for i in range(0, len(where)):
            if where[i]>=current: 
                return i+1
        return len(where)

    def find_last(where: list[int]):
        l = len(where)
        for i in range(0, len(where)):
            if where[l-1-i]>=current: 
                return i+1
        return len(where)

    above = col[:y]
    below = col[y+1:]
    left = row[:x]
    right = row[x+1:]

    return find_last(above) * find_first(below) * find_last(left) * find_first(right)

print(visible.data.count(True))

scores = [scenic_score(matrix, x, y) for x in range(0, matrix.cols) for y in range(0, matrix.rows)]
print(max(scores))