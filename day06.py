from common import read_lines


def sum_chars(line: str) -> dict[str,int]:
    res = {}
    for c in line:
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
    return res

input = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
input = read_lines("input06.txt")[0]


for i in range(0, len(input)-4):
    counts = sum_chars(input[i:i+4])
    if all([x==1 for x in counts.values()]):
        print(i+4)
        break


for i in range(0, len(input)-14):
    counts = sum_chars(input[i:i+14])
    if all([x==1 for x in counts.values()]):
        print(i+14)
        break