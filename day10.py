from common import read_lines

class Computer:
    def __init__(self):  
        self.cycle = 0
        self.x = 1
        self.signals = []
        self.pixels = [" "] * (40*6)

    @property
    def screen(self):
        rows = ["".join(self.pixels[y*40:(y+1)*40]) for y in range(0,6)]
        return "\n".join(rows)

    def step(self, arg=None):
        """Perform a single step, updating the screen and remembering signals"""
        pos_x = self.cycle % 40
        if abs(pos_x - self.x)<2:
            self.pixels[self.cycle] = "#"

        self.cycle += 1

        if arg is not None:
            self.x += arg

        if self.cycle == 20:
            self.signals.append(self.x*20)
        elif (self.cycle-20) % 40 == 0:
            self.signals.append(self.x*self.cycle)

    def run(self, lines):
        for line in lines:
            self.step()
            if line.startswith("addx"):
                value = int(line.split(" ")[1])
                self.step(value)


lines = read_lines("input10.txt")
computer = Computer()
computer.run(lines)    
print(f"Answer part 1: {sum(computer.signals)}")
print(f"Answer part 2:\n {computer.screen}")