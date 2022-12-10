from common import read_lines


lines="""addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".split("\n")

lines = read_lines("input10.txt")

class CPU:
    def __init__(self):  
        self.cycle = 0
        self.x = 1
        self.signals = []
        self.pixels = [" "] * (40*6)

    def screen(self):
        rows = ["".join(self.pixels[y*40:(y+1)*40]) for y in range(0,6)]
        return "\n".join(rows)

    def step(self):
        if self.cycle == 20:
            self.signals.append(self.x*20)
        elif (self.cycle-20) % 40 == 0:
            self.signals.append(self.x*self.cycle)

    def step2(self):
        pos_x = self.cycle % 40
        pos_y = self.cycle // 40
        if abs(pos_x - self.x)<2:
            self.pixels[self.cycle] = "#"

    def run(self, lines):
        for line in lines:
            self.step2()
            self.cycle += 1
            self.step()
            if line.startswith("addx"):
                self.step2()
                value = int(line.split(" ")[1])
                self.cycle += 1
                self.x += value
                self.step()
                # print(cycle, x)



cpu = CPU()
cpu.run(lines)    
print(sum(cpu.signals))

print(cpu.screen())