from common import read_lines


class Command:
    def __init__(self, count: int, src: int, dst: int):
        self.count = count
        self.src = src
        self.dst = dst

    def apply(self, stacks: list[list[str]]):
        for i in range(0, self.count):
            stacks[self.dst-1].append(stacks[self.src-1].pop())

    def apply_9001(self, stacks: list[list[str]]):
        tmp = []
        for i in range(0, self.count):
            tmp.append(stacks[self.src-1].pop())

        for i in range(0, self.count):
            stacks[self.dst-1].append(tmp.pop())
        

def parse_command(line: str) -> Command:
    parts = line.split(" ")
    count = int(parts[1])
    src= int(parts[3])
    dst= int(parts[5])
    return Command(count, src, dst)

def parse_inputs(lines: list[str]):
    stacks: list[list[str]] = []
    stack_count = len(lines[0])//4+1
    stack_count = 9
    for i in range(0,stack_count):
        stacks.append([])

    idx = 0
    # Part 1
    while lines[idx].strip()[0] == "[":
        for i in range(0, stack_count):
            try:
                elem = lines[idx][1+i*4]
                if elem != " ":
                    stacks[i].append(elem)
            except:
                pass

        idx += 1

    for i in range(0,stack_count):
        stacks[i].reverse()

    # Part 2
    cmds = [parse_command(line) for line in lines[idx+2:]]

    return (stacks, cmds)


sample_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".split("\n")

input = sample_input
input = read_lines("input05.txt")

stacks, cmds = parse_inputs(input)
for cmd in cmds:
    cmd.apply(stacks)

print("".join([stack[-1] for stack in stacks]))

stacks, cmds = parse_inputs(input)
for cmd in cmds:
    cmd.apply_9001(stacks)

print("".join([stack[-1] for stack in stacks]))
