from functools import cmp_to_key
from common import read_lines


lines = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".split("\n")

lines = read_lines("input13.txt")

def packet_length(value):
    if isinstance(value, int): return 0
    return len(value)

def check(left, right):
    if isinstance(left, list) and isinstance(right, list):
        for a, b in zip(left, right):
            res = check(a, b)
            if res is not None:
                return res

        if packet_length(left) == packet_length(right):
            return None

        return packet_length(left) < packet_length(right)
    elif isinstance(left, list):
        return check(left, [right])
    elif isinstance(right, list):
        return check([left], right)
    else:
        if left == right:
            return None
        return left<right


def compare(left, right):
    """Compare function for sorting."""
    val = check(left, right)
    if val ==True: return -1
    elif val==False: return 1
    else: return 0
    
indices = []
packets = []
for i in range(0, len(lines), 3):
    packets.append(eval(lines[i]))
    packets.append(eval(lines[i+1]))
    if check(packets[-2], packets[-1]):
        indices.append(i//3+1)

print(sum(indices))

packets.append([[2]])
packets.append([[6]])

packets = list(sorted(packets, key=cmp_to_key(compare)))
i1 = packets.index([[2]])+1
i2 = packets.index([[6]])+1
print(i1*i2)
